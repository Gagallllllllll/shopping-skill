#!/usr/bin/env bash
# Optional: installs the unofficial Leboncoin client lbc (MIT, github.com/etienne-hd/lbc), pinned,
# in its own environment, for scripts/leboncoin_search.py.
# lbc imitates the Leboncoin mobile app to get past its robot protection: against Leboncoin's
# terms, and your connection can be blocked for a while. Install only if you accept that.
set -euo pipefail
VENV="${HOME}/.venvs/lbc"
python3 -m venv "$VENV"
"$VENV/bin/pip" install -q "lbc==1.1.9"
echo "Ready: $VENV/bin/python -I $(dirname "$0")/leboncoin_search.py \"query\" [--max-price N]"
