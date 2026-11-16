#!/usr/bin/env python3
"""Create a biology research project safely from the bundled template."""
import argparse, shutil, sys, re
from pathlib import Path

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--name',required=True)
    p.add_argument('--destination',required=True,help='Parent directory for a new project')
    p.add_argument('--discipline',default='Microbiology')
    p.add_argument('--study-type',choices=['computational','experimental','mixed'],default='computational')
    p.add_argument('--taxon',default='to-be-confirmed')
    ns=p.parse_args(argv)
    if not re.fullmatch(r'[a-z][a-z0-9-]{1,63}',ns.name): p.error('Project name must be kebab-case, 2-64 chars')
    project=(Path(ns.destination).expanduser().resolve()/ns.name)
    if project.exists(): p.error('Project exists; refusing overwrite: '+str(project))
    template=Path(__file__).resolve().parent.parent/'templates'/'biology-project'
    if not template.is_dir(): p.error('Bundled template not found: '+str(template))
    shutil.copytree(template,project)
    (project/'input/data').mkdir(parents=True,exist_ok=True)
    for filename in ['PROJECT.md','CLAUDE.md']:
        f=project/filename
        text=f.read_text(encoding='utf-8')
        text=(text.replace('REPLACE_SLUG',ns.name).replace('REPLACE_DISCIPLINE',ns.discipline)
                  .replace('REPLACE_STUDY_TYPE',ns.study_type).replace('REPLACE_TAXON',ns.taxon))
        f.write_text(text,encoding='utf-8')
    # Copy only deterministic project-audit tools, not scaffolding/installers.
    for name in ['audit_project.py','record_inputs.py','gate_ledger.py','wiki_lint.py','wiki_graph.py','drift_report.py']:
        source=Path(__file__).resolve().parent/name
        shutil.copy2(source,project/'scripts'/name)
    print('CREATED',project)
    print('Review PROJECT.md (study type, biological unit, ethics and taxon are unconfirmed).')
    return 0
if __name__=='__main__': raise SystemExit(main())
