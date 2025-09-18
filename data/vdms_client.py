import os

def _dummy_anoms():
    return [
        {"frame_id": "f1", "type": "crack", "severity": 3, "score": 0.82, "ts": 1, "source_id": "cam-01"},
        {"frame_id": "f2", "type": "soiling", "severity": 2, "score": 0.65, "ts": 1, "source_id": "cam-01"},
    ]

def vdms_client(s: dict) -> dict:
    # Placeholder: if VDMS env present, you would connect and query here.
    host = os.getenv("VDMS_HOST")
    port = os.getenv("VDMS_PORT")
    # For now, always return dummy until real client is wired.
    anoms = _dummy_anoms()
    return {"anoms": anoms}
