#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
TARGET="${1:-https://github.com/CongjianL/biology-research-superpowers.git}"
if [[ ! "$TARGET" =~ ^https://github.com/CongjianL/[A-Za-z0-9._-]+\.git$ ]]; then
  echo 'Refusing target outside expected GitHub owner' >&2
  exit 2
fi
if [ -d .git ]; then
  echo 'This importer expects the clean, extracted source archive, not an existing Git working tree.' >&2
  exit 2
fi
if [ -z "$(git config --global user.name || true)" ] || [ -z "$(git config --global user.email || true)" ]; then
  echo 'Please configure git user.name and user.email first.' >&2
  exit 2
fi
printf 'Publish all source files to %s? [y/N] ' "$TARGET"
read -r confirm
[[ "$confirm" == 'y' || "$confirm" == 'Y' ]] || exit 1
git init -b main
git remote add origin "$TARGET"
git add -A
git commit -m 'feat: add complete Biology Research Superpowers Codex plugin'
git fetch origin main
# The remote already contains an initial README and docs created through the connector.
# Preserve every source file in this archive, while making the push a fast-forward.
git merge --allow-unrelated-histories -s ours -m 'chore: reconcile pre-existing repository bootstrap' origin/main
git push -u origin main
printf '\nPublished complete source to %s\n' "$TARGET"
