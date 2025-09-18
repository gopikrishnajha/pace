def policy_metrics(s: dict) -> dict:
    acts = []
    for a in s.get("enriched", []):
        if a.get("type") == "crack" and a.get("severity", 0) >= 3 and a.get("score", 0) > 0.7:
            acts.append({"action": "notify_ops", "ref": a})
    metrics = {
        "count_anoms": len(s.get("enriched", [])),
        "count_actions": len(acts),
    }
    return {"actions": acts, "metrics": metrics}
