import os
import sys

# We warn if key is missing, but don't exit here so app.py can import build_workflow
if not os.environ.get("GOOGLE_API_KEY"):
    print("WARNING: GOOGLE_API_KEY is not set. The Product Summary Agent will fail.")

from langgraph.graph import StateGraph, START, END
from state import ExperimentState
from agents import sql_agent, statistician_agent, rag_context_agent, post_analysis_agent, product_summary_agent


def build_workflow():
    # Initialize the StateGraph
    workflow = StateGraph(ExperimentState)

    # Add the nodes
    workflow.add_node("sql_agent", sql_agent)
    workflow.add_node("statistician_agent", statistician_agent)
    workflow.add_node("rag_context_agent", rag_context_agent)
    workflow.add_node("post_analysis_agent", post_analysis_agent)
    workflow.add_node("product_summary_agent", product_summary_agent)

    # Define the execution flow (edges)
    workflow.add_edge(START, "sql_agent")
    workflow.add_edge("sql_agent", "statistician_agent")
    workflow.add_edge("statistician_agent", "rag_context_agent")
    workflow.add_edge("rag_context_agent", "post_analysis_agent")
    workflow.add_edge("post_analysis_agent", "product_summary_agent")
    workflow.add_edge("product_summary_agent", END)

    # Compile the graph
    app = workflow.compile()
    return app

def run_test_case(app, experiment_id: str, expected_decision: str):
    print("=" * 60)
    print(f"Running Test Case: {experiment_id}")
    print("=" * 60)
    
    # Initial state
    initial_state = {
        "experiment_id": experiment_id,
        "raw_data": None,
        "stats_results": None,
        "historical_context": None,
        "segment_warnings": None,
        "final_report": None
    }
    
    # Execute the workflow
    result = app.invoke(initial_state)
    
    print("\n--- FINAL EXECUTIVE REPORT ---\n")
    print(result["final_report"])
    print("\n" + "=" * 60 + "\n")
    
    # Assertion check for demo safety
    report_lower = result["final_report"].lower()
    assert result["final_report"] is not None and len(result["final_report"]) > 0, "Final report is empty!"
    
    expected_lower = expected_decision.lower()
    assert expected_lower in report_lower, f"Expected decision '{expected_decision}' not found in the report!"
    
    if experiment_id == "EXP_NEW_PRICING":
        assert "simpson" in (result.get("segment_warnings") or "").lower() or "mobile" in (result.get("segment_warnings") or "").lower(), \
            "Post-Analysis Agent failed to catch Simpson's Paradox!"
        print(f"✅ Assertion passed for {experiment_id}: Simpson's Paradox detected.")
    
    print(f"✅ Assertion passed for {experiment_id}: Correct decision keyword present.")

if __name__ == "__main__":
    print("SAFE: Statistical Analysis For Experimentation — Agentic Workflow")
    print("Inspired by production experimentation systems at Fortune 100 retailers\n")
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("WARNING: GOOGLE_API_KEY is not set. The Product Summary Agent will fail.")
        print("Please set your Google API key before running the demo.")
        sys.exit(1)
        
    app = build_workflow()
    
    # Case 1: "EXP_CART_REDESIGN" (Statistically significant, positive result) -> Launch
    run_test_case(app, "EXP_CART_REDESIGN", "Launch")
    
    # Case 2: "EXP_NEW_PRICING" (Not significant, high variance) -> Needs More Data or Hold
    # The prompt allows "Needs More Data" for not significant. We can check for "Needs More Data".
    run_test_case(app, "EXP_NEW_PRICING", "Needs More Data")
    
    print("Demo execution completed successfully.")
