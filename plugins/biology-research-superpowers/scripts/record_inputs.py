#!/usr/bin/env python3
"""Hash raw research data and record a reproducibility receipt, without editing data."""
import argparse, csv, hashlib, sys
from pathlib import Path

def hash_file(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--project',type=Path,default=Path.cwd())
    ap.add_argument('--output',default='input/metadata/sha256.tsv')
    ap.add_argument('--check',action='store_true',help='Compare existing manifest without writing')
    a=ap.parse_args();root=a.project.resolve();raw=root/'input/data';out=(root/a.output).resolve()
    if not out.is_relative_to(root):ap.error('Output must be inside project')
    if not raw.is_dir():ap.error('Missing input/data')
    rows=[]
    for f in sorted(raw.rglob('*')):
        if f.is_symlink():
            print('SKIP symlink:',f,file=sys.stderr);continue
        if f.is_file():rows.append((f.relative_to(root).as_posix(),f.stat().st_size,hash_file(f)))
    if a.check:
        if not out.exists():ap.error('No existing manifest to check')
        with out.open(newline='',encoding='utf-8') as fh:
            actual=[(r['path'],int(r['bytes']),r['sha256']) for r in csv.DictReader(fh,delimiter='\t')]
        print('PASS: raw input checksums unchanged' if actual==rows else 'FAIL: input checksum drift')
        return 0 if actual==rows else 2
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='',encoding='utf-8') as fh:
        wr=csv.writer(fh,delimiter='\t');wr.writerow(['path','bytes','sha256']);wr.writerows(rows)
    print('RECORDED',len(rows),'raw input files in',out)
    return 0
if __name__=='__main__':raise SystemExit(main())
