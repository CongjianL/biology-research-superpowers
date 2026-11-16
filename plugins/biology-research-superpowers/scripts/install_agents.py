#!/usr/bin/env python3
"""Explicitly install optional Codex custom agents; never overwrite by default."""
import argparse,shutil
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--scope',choices=['user','project'],default='user')
    ap.add_argument('--project',type=Path,default=Path.cwd());ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args()
    root=Path(__file__).resolve().parent.parent
    agents=sorted((root/'codex-agents').glob('*.toml'))
    dest=(Path.home()/'.codex/agents') if a.scope=='user' else (a.project.resolve()/'.codex/agents')
    existing=[p.name for p in agents if (dest/p.name).exists()]
    if existing:ap.error('Refusing to overwrite: '+', '.join(existing))
    if not a.dry_run:dest.mkdir(parents=True,exist_ok=True)
    for p in agents:
        print(('WOULD INSTALL' if a.dry_run else 'INSTALL'),str(dest/p.name))
        if not a.dry_run:shutil.copy2(p,dest/p.name)
    return 0
if __name__=='__main__':raise SystemExit(main())
