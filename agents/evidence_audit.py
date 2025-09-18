def evidence_audit(s: dict) -> dict:
    log = {"event": "tick_done", "ts": 0}
    logs = s.get("logs", [])
    logs.append(log)
    return {"logs": logs}
