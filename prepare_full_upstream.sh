#!/usr/bin/env bash
# Optional: fetch the exact leiverkus source, convert, and merge it with biology workflows.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIO="$ROOT"
CONVERTER="$ROOT/extras/leiverkus-codex-converter"
SOURCE="${1:-}"
if [[ -n "$SOURCE" ]]; then
  bash "$CONVERTER/prepare.sh" "$SOURCE"
else
  bash "$CONVERTER/prepare.sh"
fi
OUT="$(cd "$ROOT/.." && pwd)/biology-with-full-upstream"
python3 "$ROOT/plugins/biology-research-superpowers/scripts/overlay_upstream.py" \
  --original-marketplace "$CONVERTER/dist/leiverkus-codex-marketplace" \
  --biology-marketplace "$BIO" --output "$OUT"
echo "Full upstream-preserving merged marketplace: $OUT"
echo "Install: codex plugin marketplace add \"$OUT\""
