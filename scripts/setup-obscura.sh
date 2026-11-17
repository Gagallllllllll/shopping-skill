#!/usr/bin/env bash
# Optional: installs Obscura (Apache-2.0, github.com/h4ckf0r0day/obscura), a fast headless browser,
# pinned to v0.2.7, NON-stealth Linux x86_64 build, after checking the published SHA-256.
# Used by shop_fetch.py (fast first pass) and marketplace_search.py (Facebook Marketplace pages).
set -euo pipefail
VER=v0.2.7
ASSET=obscura-x86_64-linux.tar.gz
SHA=11b53d27cd743e00e196e216920e7f3f794cf378e3f1792b8d25d3beabaf9cad
DEST="${HOME}/.local/opt/obscura"
TMP=$(mktemp -d)
curl -fsSL -o "$TMP/$ASSET" "https://github.com/h4ckf0r0day/obscura/releases/download/$VER/$ASSET"
echo "$SHA  $TMP/$ASSET" | sha256sum -c -
mkdir -p "$DEST" && tar xzf "$TMP/$ASSET" -C "$DEST" && rm -rf "$TMP"
"$DEST/obscura" --version
