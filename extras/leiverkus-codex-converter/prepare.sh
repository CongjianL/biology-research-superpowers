#!/usr/bin/env bash
# Build a complete, source-preserving Codex plugin from the pinned upstream.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="https://github.com/leiverkus/research-superpowers.git"
PIN="da0effdf162cd96a42009fe2dfe701b352e50ba8"
SOURCE="${1:-}"
if [[ -z "$SOURCE" ]]; then
  SOURCE="$ROOT/work/upstream"
  mkdir -p "$ROOT/work"
  if [[ ! -d "$SOURCE/.git" ]]; then
    echo "Cloning leiverkus/research-superpowers into $SOURCE"
    git clone --quiet "$REPO" "$SOURCE"
  fi
  CURRENT="$(git -C "$SOURCE" rev-parse HEAD)"
  if [[ "$CURRENT" != "$PIN" ]]; then
    git -C "$SOURCE" fetch --quiet origin "$PIN"
    git -C "$SOURCE" -c advice.detachedHead=false checkout --quiet --detach "$PIN"
  fi
  echo "Pinned source to $PIN"
else
  echo "Using supplied local source: $SOURCE"
fi
OUT="$ROOT/dist/leiverkus-codex-marketplace"
python3 "$ROOT/migrate.py" --source "$SOURCE" --output "$OUT" --force
python3 "$ROOT/verify.py" --marketplace "$OUT"
cat <<EOF

Build complete: $OUT

Next: register the local marketplace:
  codex plugin marketplace add "$OUT"
  codex plugin marketplace list

Then open the Codex / ChatGPT desktop Plugins Directory and install
research-superpowers from leiverkus-codex-local.
Review /hooks before trusting optional lifecycle scripts.
EOF
