#!/usr/bin/env bash
# Optional: installs Scrapling (BSD-3, github.com/D4Vinci/Scrapling) in its own environment
# so scripts/shop_fetch.py can read shops that block simple fetching.
set -euo pipefail
VENV="${HOME}/.venvs/scrapling"
python3 -m venv "$VENV"
"$VENV/bin/pip" install -q "scrapling[rag]==0.5.1"
"$VENV/bin/python" -m patchright install chromium
"$VENV/bin/python" -m playwright install chromium
echo "Ready: $VENV/bin/python -I $(dirname "$0")/shop_fetch.py OUT_DIR URL ..."
