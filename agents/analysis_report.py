def analysis_report(s: dict) -> dict:
    n_anoms = len(s.get("enriched", []))
    n_actions = len(s.get("actions", []))
    md = f"""## Summary
Anomalies: {n_anoms}
Actions: {n_actions}
"""
    return {"report_md": md}
