#!/usr/bin/env python3
"""Export a transparent wikilink graph; link is NOT biological causality."""
import argparse,json,re
from pathlib import Path
PAT=re.compile(r'\[\[([^\]]+)\]\]')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--project',type=Path,default=Path.cwd())
    ap.add_argument('--output',default='output/data-analysis/wiki-graph.json')
    a=ap.parse_args();root=a.project.resolve();files=list((root/'knowledge').rglob('*.md'))
    index={p.stem:p for p in files}
    nodes=[{'id':p.stem,'type':p.parent.name,'path':str(p.relative_to(root))} for p in files]
    links=[]
    for p in files:
        for x in PAT.findall(p.read_text(encoding='utf-8')):
            t=Path(x.split('|',1)[0].strip()).stem
            links.append({'source':p.stem,'target':t,'unresolved':t not in index,'relation':'wiki-link-not-causality'})
    output=(root/a.output).resolve()
    if not output.is_relative_to(root):ap.error('output path must be inside project')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps({'nodes':nodes,'edges':links},indent=2),encoding='utf-8')
    print('EXPORTED',len(nodes),'nodes',len(links),'links',output)
    return 0
if __name__=='__main__':raise SystemExit(main())
