#!/usr/bin/env python3
"""Log human-approved SOFT-GATE overrides; never override a HARD-STOP."""
import argparse,csv,datetime,json,sys
from pathlib import Path
STAGES=['design','plan','acquisition','ingest','analysis','manuscript','review','release']

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--project',type=Path,default=Path.cwd())
    sub=p.add_subparsers(dest='command',required=True)
    o=sub.add_parser('override')
    o.add_argument('--stage',choices=STAGES,required=True)
    o.add_argument('--reason',required=True)
    o.add_argument('--approved-by',required=True,help='Actual authorizer; do not invent')
    l=sub.add_parser('list')
    a=p.parse_args();log=a.project.resolve()/'knowledge/_meta/gate-overrides.tsv'
    if a.command=='list':
        print(log.read_text(encoding='utf-8') if log.exists() else 'No override ledger found.')
        return 0
    if len(a.reason.strip())<12 or len(a.approved_by.strip())<2:
        p.error('Specify a substantive reason and actual human approver')
    if any(x in a.reason.lower() for x in ['biosafety bypass','invent citation','fake data','ethics exemption']):
        p.error('HARD-STOP is not overridable')
    log.parent.mkdir(parents=True,exist_ok=True)
    first=not log.exists() or log.stat().st_size==0
    with log.open('a',encoding='utf-8',newline='') as fh:
        wr=csv.writer(fh,delimiter='\t')
        if first:wr.writerow(['timestamp_utc','stage','reason','approved_by'])
        wr.writerow([datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),a.stage,a.reason,a.approved_by])
    print('RECORDED OVERRIDE',a.stage,'(audit only, not a permissions grant)')
    return 0
if __name__=='__main__':raise SystemExit(main())
