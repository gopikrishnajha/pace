from langgraph.graph import StateGraph, END
from typing import Dict

# State is kept simple; extend as needed.
State = Dict

# Node imports
from agents.meta import meta
from data.vdms_client import vdms_client
from agents.glue import glue
from agents.policy_metrics import policy_metrics
from agents.analysis_report import analysis_report
from agents.evidence_audit import evidence_audit

g = StateGraph(State)
g.add_node("meta", meta)
g.add_node("vdms_client", vdms_client)
g.add_node("glue", glue)
g.add_node("policy_metrics", policy_metrics)
g.add_node("analysis_report", analysis_report)
g.add_node("evidence_audit", evidence_audit)

g.set_entry_point("meta")
g.add_edge("meta", "vdms_client")
g.add_edge("vdms_client", "glue")
g.add_edge("glue", "policy_metrics")
g.add_edge("policy_metrics", "analysis_report")
g.add_edge("analysis_report", "evidence_audit")
g.add_edge("evidence_audit", END)

app = g.compile()
