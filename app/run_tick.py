import sys, pathlib, os
root = pathlib.Path(__file__).resolve().parents[1]
sys.path.append(str(root))

from app.graph import app

if __name__ == "__main__":
    # Example window; replace with real timestamps
    state = app.invoke({"window": {"start": 0, "end": 1, "source_id": "cam-01"}})
    print(state.get("report_md", "(no report)"))
