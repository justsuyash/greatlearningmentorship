import os
import sys
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import markdown
import asyncio
import json

# LangSmith — auto-instruments all LangGraph executions
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = "abc-corp-experimentation"

# Check for API key before any imports
if not os.getenv("GOOGLE_API_KEY"):
    print("ERROR: GOOGLE_API_KEY not set")
    sys.exit(1)

if not os.environ.get("LANGCHAIN_API_KEY"):
    print("⚠️  WARNING: LANGCHAIN_API_KEY not set — tracing disabled")

if not os.path.exists("warehouse.duckdb"):
    print("⚠️  warehouse.duckdb not found — running seed.py automatically...")
    import subprocess
    subprocess.run(["python", "seed.py"])
    print("✅ Database seeded successfully")

from agents import orchestrator, generate_post_analysis_code
from mock_data import MOCK_EXPERIMENTS, MOCK_METRICS, AGENT_CHECKLIST

app = FastAPI(title="ABC Corp. Experimentation Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

base_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

app.mount("/static", StaticFiles(directory=os.path.join(base_dir, "static")), name="static")

class ExperimentRequest(BaseModel):
    experiment_id: str

class PostAnalysisRequest(BaseModel):
    experiment_id: str
    question: str
    context: str

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    """Serves the main dashboard UI."""
    real_metrics = {}
    if os.path.exists("warehouse.duckdb"):
        import duckdb
        conn = duckdb.connect("warehouse.duckdb", read_only=True)
        df = conn.execute("""
            SELECT experiment_id, variant, COUNT(*) as sessions, SUM(converted) as conversions, SUM(revenue) as revenue
            FROM ab_test_events
            GROUP BY experiment_id, variant
        """).df()
        
        for _, row in df.iterrows():
            exp_id = row['experiment_id']
            if exp_id not in real_metrics:
                real_metrics[exp_id] = {}
            var = row['variant']
            sessions = int(row['sessions'])
            conversions = int(row['conversions'])
            revenue = float(row['revenue'])
            real_metrics[exp_id][var] = {
                "sessions": sessions,
                "conversions": conversions,
                "conversion_rate": conversions/sessions if sessions > 0 else 0,
                "revenue": revenue,
                "aov": revenue/conversions if conversions > 0 else 0
            }
        conn.close()
        
    # Merge any missing mock data just so the UI doesn't crash on un-seeded experiments
    for exp in MOCK_METRICS:
        if exp not in real_metrics:
            real_metrics[exp] = MOCK_METRICS[exp]
            
    return templates.TemplateResponse(
        request, 
        "index.html", 
        {"request": request, "experiments": MOCK_EXPERIMENTS, "metrics": real_metrics}
    )

@app.post("/api/post-analysis")
async def post_analysis(req: PostAnalysisRequest):
    """Generates Python code for post-analysis."""
    code = generate_post_analysis_code(req.experiment_id, req.question, req.context)
    return JSONResponse(content={"code": code})

@app.get("/api/run-experiment/stream")
async def run_experiment_stream(experiment_id: str):
    """Runs the workflow and streams node completion events using SSE."""
    
    async def event_stream():
        initial_state = {
            "experiment_id": experiment_id,
            "agent_log": []
        }
        
        try:
            # Keep track of events we've already yielded so we don't repeat them
            yielded_logs = 0
            
            for chunk in orchestrator.stream(initial_state):
                # The state after the node has completed is in chunk[node_name]
                node_name = list(chunk.keys())[0]
                state = chunk[node_name]
                
                # Fetch the latest log entry if it exists
                agent_logs = state.get("agent_log", [])
                if len(agent_logs) > yielded_logs:
                    latest_log = agent_logs[-1]
                    yielded_logs += 1
                    
                    agent_name = latest_log.get("agent", "")
                    checklist = AGENT_CHECKLIST.get(agent_name, {}).get("checklist_items", [])
                    checks = latest_log.get("checks", [])
                    
                    resolved_items = []
                    for i, item in enumerate(checklist):
                        if checks and i < len(checks):
                            resolved_items.append({
                                "item": item,
                                "passed": checks[i].get("passed", True),
                                "detail": checks[i].get("assessment", "")
                            })
                        else:
                            resolved_items.append({"item": item, "passed": True, "detail": ""})
                    
                    event_data = {
                        "agent": agent_name,
                        "type": latest_log.get("type", ""),
                        "description": latest_log.get("description", ""),
                        "input_summary": latest_log.get("input_summary", ""),
                        "output_summary": latest_log.get("output_summary", ""),
                        "checks": checks,
                        "checks_summary": latest_log.get("checks_summary", ""),
                        "checks_all_passed": latest_log.get("checks_all_passed", True),
                        "status": latest_log.get("status", "completed"),
                        "checklist_items": resolved_items,
                        "checklist_summary": f"{sum(1 for x in resolved_items if x['passed'])}/{len(resolved_items)}"
                    }
                    yield f"data: {json.dumps(event_data)}\n\n"
                    
                await asyncio.sleep(0.5) # Simulated execution delay for visual effect
                
            # Final state payload
            final_state = orchestrator.invoke(initial_state)
            if final_state.get("final_report"):
                final_state["final_report_html"] = markdown.markdown(final_state["final_report"])
            yield f"data: {json.dumps({'node': 'complete', 'state': jsonable_encoder(final_state)})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            
    return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.post("/api/run-experiment")
async def run_experiment(req: ExperimentRequest):
    """Triggers the LangGraph workflow synchronously."""
    initial_state = {"experiment_id": req.experiment_id, "agent_log": []}
    try:
        result = orchestrator.invoke(initial_state)
        if result.get("final_report"):
            result["final_report_html"] = markdown.markdown(result["final_report"])
        return JSONResponse(content=jsonable_encoder({"status": "success", "state": result}))
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
