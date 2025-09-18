#!/usr/bin/env bash
set -euo pipefail

# Create venv and install deps
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Create .env if missing
if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
  else
    echo "VDMS_HOST=localhost" > .env
    echo "VDMS_PORT=55555" >> .env
    echo "OV_DEVICE=NPU,GPU,CPU" >> .env
    echo "MODEL_DIR=./models" >> .env
  fi
fi

echo "✅ Setup complete. Activate venv with: source .venv/bin/activate"
