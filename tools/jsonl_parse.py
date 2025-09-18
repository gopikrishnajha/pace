import json

def parse_jsonl(path: str):
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)
