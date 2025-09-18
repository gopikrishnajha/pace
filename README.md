# PACE  - PdM using Agents for Critical infrastructure on the Edge

Minimal agent + data units scaffold, optimized for Intel Edge (Arrow Lake). Uses **LangGraph** for orchestration and Intel-friendly libs (OpenVINO, OpenCV, NumPy, Shapely). VDMS is optional (dummy fallback included).

## Quick Start (Linux/macOS)

### 0) Prereqs
- Python 3.10+
- (Optional) Docker (for VDMS)
- Intel GPU/NPU drivers if you plan to use acceleration

### 1) Clone & Setup
```bash
git clone https://github.com/gopikrishnajha/pace.git
cd pace
bash scripts/setup.sh
```

### 2) (Optional) Start VDMS in Docker
```bash
bash scripts/run_vdms_docker.sh
```
> Or skip this: the app uses a dummy in-memory source if VDMS isn't available.

### 3) Run a tick
```bash
bash scripts/run_tick.sh
```
You should see a short Markdown summary printed.

---

## What’s inside
```
app/                # LangGraph graph + runner
agents/             # meta, glue, policy_metrics, analysis_report, evidence_audit
data/               # vdms_client stub (uses dummy data if VDMS not running)
tools/              # jsonl parsing, geometry, image ops
schemas/            # JSON Schemas for plans/outputs
scripts/            # setup, run vdms, run tick
models/             # put your quantized tiny-LLM here (OpenVINO IR)
```

## Next Steps
- Wire real VDMS client and queries in `data/vdms_client.py`
- Drop an INT4 tiny-LLM (3–4B) into `models/` and call via OpenVINO in `agents/glue.py`
- Add inference nodes (det/seg/cls) later as `ov_infer_*` nodes in the graph
