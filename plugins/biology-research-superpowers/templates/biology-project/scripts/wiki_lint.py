#!/usr/bin/env python3
"""Validate biology research wiki wikilinks and source page metadata."""
import argparse,re,sys
from pathlib import Path
PAT=re.compile(r'\[\[([^\]]+)\]\]')

def run(root):
    src=root/'knowledge'
    errors=[];warnings=[];paths=list(src.rglob('*.md')) if src.exists() else []
    indexed={}
    for p in paths:indexed.setdefault(p.stem,[]).append(p)
    for p in paths:
        data=p.read_text(encoding='utf-8')
        if p.parent.name=='sources' and not (data.startswith('---\n') and '\n---\n' in data[4:]):
            errors.append(f'{p.relative_to(root)}: source page needs YAML metadata')
        for m in PAT.finditer(data):
            target=m.group(1).split('|',1)[0].strip()
            key=Path(target).stem
            if key not in indexed: errors.append(f'{p.relative_to(root)}: unresolved wikilink {target}')
            elif len(indexed[key])>1: warnings.append(f'{p.relative_to(root)}: ambiguous wikilink {target}')
    return errors,warnings,len(paths)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--project',type=Path,default=Path.cwd())
    a=ap.parse_args();root=a.project.resolve();errors,warnings,n=run(root)
    print('PASS' if not errors else 'FAIL',f'({n} wiki pages)')
    for e in errors:print('ERROR:',e)
    for w in warnings:print('WARN:',w)
    return 0 if not errors else 2
if __name__=='__main__':raise SystemExit(main())
