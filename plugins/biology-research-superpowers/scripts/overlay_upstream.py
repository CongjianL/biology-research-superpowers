#!/usr/bin/env python3
"""Archive a verified original leiverkus Codex conversion inside the biology plugin.

Scientific active skills stay biology-first. Original workflows become reference
material, NOT automatically executed or preferred over biology safety gates.
"""
from __future__ import annotations
import argparse,hashlib,json,re,shutil,sys
from pathlib import Path

ORIG_NAME='research-superpowers'
BIO_NAME='biology-research-superpowers'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--original-marketplace',required=True,type=Path)
    ap.add_argument('--biology-marketplace',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args()
    src=(args.original_marketplace.resolve()/'plugins'/ORIG_NAME)
    bio=args.biology_marketplace.resolve()
    original_manifest=src/'migration-report.json'
    if not original_manifest.is_file():ap.error('Original converter migration-report.json not found')
    origin=json.loads(original_manifest.read_text(encoding='utf-8'))
    if origin.get('upstream_version')!='0.47.0' or origin.get('skill_count')!=18 or origin.get('agent_count')!=7:
        ap.error('Unexpected original inventory/version. Review source before merging.')
    if not (src/'LICENSE').is_file():ap.error('Missing original MIT license')
    if origin.get('source') != 'https://github.com/leiverkus/research-superpowers':
        ap.error('Unexpected original repository')
    if len(origin.get('skills',[]))!=18 or len(origin.get('agents',[]))!=7:
        ap.error('Original verification inventory missing')
    for record in origin['skills']:
        name=record.get('name','')
        if not re.fullmatch(r'[a-z][a-z0-9-]*',name):ap.error('Unexpected source skill name')
        original=src/'skills'/name/'upstream-workflow.md'
        if not original.is_file():ap.error('Missing full upstream skill: '+name)
        digest=hashlib.sha256(original.read_bytes()).hexdigest()
        if digest!=record.get('upstream_sha256'):ap.error('Original skill hash mismatch: '+name)
    if not (bio/'.agents/plugins/marketplace.json').is_file():ap.error('Biology marketplace missing')
    out=args.output.resolve()
    if out.exists():ap.error('Output already exists, refusing to overwrite')
    if out in (bio,src) or out.is_relative_to(bio) or bio.is_relative_to(out):
        ap.error('Output must not contain / be inside source')
    shutil.copytree(bio,out)
    plugin=out/'plugins'/BIO_NAME
    destination=plugin/'upstream-leiverkus'
    shutil.copytree(src,destination)
    for s in sorted((src/'skills').glob('*/upstream-workflow.md')):
        target=plugin/'skills'/s.parent.name/'references'/'leiverkus-original.md'
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(s,target)
    # Original code and scripts are archived for full provenance; never auto-register original hooks or agents.
    (plugin/'UPSTREAM_MERGE.md').write_text('# Full upstream source archived (opt-in)\n\n'
        'All files from the verified original research-superpowers Codex conversion '
        'are under `upstream-leiverkus/`. Original skill bodies for shared skill names '
        'are additionally in `skills/<name>/references/leiverkus-original.md`.\n\n'
        'These original workflows document the upstream method, but this biology '
        'plugin uses its biology SKILL.md as the operative method. Do not execute '
        'original scripts/hook code without reviewing their behavior and adapting '
        'the path to your project. Original MIT license is preserved in that directory.\n',encoding='utf-8')
    (plugin/'upstream-provenance.json').write_text(json.dumps(origin,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('MERGED verified original reference source with biology plugin:',out)
    print('Biology skill bodies active; 18 complete original workflows stored as references.')
    return 0

if __name__=='__main__':raise SystemExit(main())
