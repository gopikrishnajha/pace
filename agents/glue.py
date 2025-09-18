# Tiny-LLM glue placeholder: validate a plan, execute simple tools, return enriched state.
# Later: load an OpenVINO-quantized tiny LLM and produce plans; enforce JSON via jsonschema.

from jsonschema import validate

PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "tool": {"type": "string"},
                    "args": {"type": "object"}
                },
                "required": ["tool", "args"]
            }
        }
    },
    "required": ["steps"]
}

def glue(s: dict) -> dict:
    # Dummy "plan"
    plan = {"steps": [{"tool": "geometry_check", "args": {"bbox": [10, 10, 50, 50]}}]}
    validate(plan, PLAN_SCHEMA)

    # Execute a minimal step (mock): just pass through anomalies for now
    enriched = s.get("anoms", [])
    return {"ok": True, "enriched": enriched}
