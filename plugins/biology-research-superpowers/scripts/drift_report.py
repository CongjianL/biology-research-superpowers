#!/usr/bin/env python3
"""Read-only drift comparison by default; explicit --record-baseline to update."""
import argparse,hashlib,json,sys
from pathlib import Path

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--project',type=Path,default=Path.cwd())
    ap.add_argument('--record-baseline',action='store_true')
    a=ap.parse_args();root=a.project.resolve()
    selected=[root/'PROJECT.md',root/'input/metadata/datasets.tsv',root/'input/metadata/samples.tsv',root/'input/metadata/sha256.tsv',root/'knowledge/_meta/claims.tsv',root/'output/bibtex/references.bib']
    selected+=sorted((root/'knowledge/synthesis').glob('*.md'))
    current={str(p.relative_to(root)):digest(p) for p in selected if p.is_file()}
    baseline=root/'knowledge/_meta/drift-baseline.json'
    if a.record_baseline:
        baseline.parent.mkdir(parents=True,exist_ok=True)
        baseline.write_text(json.dumps(current,indent=2)+'\n',encoding='utf-8')
        print('RECORDED BASELINE',len(current),'files; check raw bytes via record_inputs.py --check');return 0
    if not baseline.is_file():
        print('NO BASELINE; run --record-baseline only after inspecting project state');return 0
    old=json.loads(baseline.read_text(encoding='utf-8'))
    added=set(current)-set(old);removed=set(old)-set(current)
    changed={x for x in set(old)&set(current) if old[x]!=current[x]}
    for name,items in [('ADDED',added),('REMOVED',removed),('CHANGED',changed)]:
        for x in sorted(items):print(name,x)
    print('NO DRIFT' if not added and not removed and not changed else 'DRIFT DETECTED')
    return 2 if (added or removed or changed) else 0
if __name__=='__main__':raise SystemExit(main())
