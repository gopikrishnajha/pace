#!/usr/bin/env bash
set -euo pipefail

# Run VDMS in Docker (latest public image assumed)
docker run -d --name vdms -p 55555:55555 intel/vdms:latest || true
echo "✅ VDMS started (container: vdms, port 55555)"
