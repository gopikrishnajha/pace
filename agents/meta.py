def meta(s: dict) -> dict:
    # Orchestrator: set/validate window, route into data fetch
    win = s.get("window", {})
    return {"window": win, "route": "vdms_client"}
