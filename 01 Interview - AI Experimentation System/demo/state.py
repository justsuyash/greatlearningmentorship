from typing import TypedDict, List, Dict, Any

class ExperimentState(TypedDict):
    experiment_id: str
    raw_data: dict
    srm_result: dict
    cuped_result: dict
    guardrail_warnings: list
    
    # Detailed Checks
    srm_checks: list
    stats_checks: list
    guardrail_checks: list
    
    rag_context: str
    segment_warnings: str
    final_report: str
    confidence: str  # "High" | "Medium" | "Low"
    agent_log: list  # list of {agent, type, input_summary, output_summary, description}
