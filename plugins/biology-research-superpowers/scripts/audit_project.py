#!/usr/bin/env python3
"""Verify provenance tables and claim evidence without external dependencies."""
import argparse, csv, json, re, sys
from pathlib import Path
CLAIM_FIELDS=['claim_id','claim_text','evidence_type','evidence_path','source_id','confidence','status']
DATASET_FIELDS=['dataset_id','source','accession_version','retrieved_utc','checksum_sha256','local_path','license']
SAMPLE_FIELDS=['sample_id','organism','strain','bioproject','biosample','assembly_accession','biological_unit','notes']
STATUS={'hypothesis','computational_prediction','experimental_observation','model_inference','validated','inconclusive','unsupported','withdrawn'}

def read_tsv(path,fields,errors):
    if not path.is_file():
        errors.append(f'Missing required ledger: {path}')
        return []
    with path.open(encoding='utf-8',newline='') as fh:
        reader=csv.DictReader(fh,delimiter='\t')
        if not reader.fieldnames or not set(fields).issubset(reader.fieldnames):
            errors.append(f'Invalid columns in {path}: need {fields}')
            return []
        result=list(reader)
    for i,row in enumerate(result,2):
        if None in row or any(v is None for v in row.values()): errors.append(f'Malformed TSV row {path}:{i}')
    return result

def check_reference(root,s,errors,location):
    if not s: return False
    p=Path(s)
    if p.is_absolute():
        errors.append(f'{location}: evidence path must be project-relative');return False
    target=(root/p).resolve()
    if not target.is_relative_to(root.resolve()):
        errors.append(f'{location}: path escapes project');return False
    if not target.is_file():
        errors.append(f'{location}: missing evidence {s}');return False
    return True

def audit(root,strict=False):
    errors=[];warnings=[];stats={}
    if not (root/'AGENTS.md').exists(): errors.append('Missing AGENTS.md')
    if not (root/'PROJECT.md').exists(): errors.append('Missing PROJECT.md')
    claims=read_tsv(root/'knowledge/_meta/claims.tsv',CLAIM_FIELDS,errors)
    datasets=read_tsv(root/'input/metadata/datasets.tsv',DATASET_FIELDS,errors)
    samples=read_tsv(root/'input/metadata/samples.tsv',SAMPLE_FIELDS,errors)
    ids=set()
    for i,row in enumerate(claims,2):
        identifier=(row.get('claim_id') or '').strip()
        if not identifier or identifier in ids:errors.append(f'claims.tsv:{i}: empty/duplicate claim_id {identifier!r}')
        ids.add(identifier)
        status=(row.get('status') or '').strip()
        if status not in STATUS: errors.append(f'claims.tsv:{i}: unknown status {status!r}')
        evidence=(row.get('evidence_path') or '').strip()
        if status in {'validated','experimental_observation','model_inference'}:
            if not evidence:errors.append(f'claims.tsv:{i}: {status} requires an evidence_path')
            else:check_reference(root,evidence,errors,f'claims.tsv:{i}')
            if not (row.get('source_id') or '').strip():warnings.append(f'claims.tsv:{i}: no DOI/PMID/accession or run identifier')
        elif evidence:
            check_reference(root,evidence,errors,f'claims.tsv:{i}')
        if not (row.get('claim_text') or '').strip():errors.append(f'claims.tsv:{i}: claim_text missing')
    seen=set()
    for i,row in enumerate(datasets,2):
        d=(row.get('dataset_id') or '').strip()
        if not d or d in seen:errors.append(f'datasets.tsv:{i}: empty/duplicate dataset_id')
        seen.add(d)
        path=(row.get('local_path') or '').strip()
        if path:check_reference(root,path,errors,f'datasets.tsv:{i}')
        if not (row.get('source') or '').strip():warnings.append(f'datasets.tsv:{i}: missing source')
        if not (row.get('accession_version') or '').strip():warnings.append(f'datasets.tsv:{i}: no accession/version')
    seen=set()
    for i,row in enumerate(samples,2):
        sid=(row.get('sample_id') or '').strip()
        if not sid or sid in seen:errors.append(f'samples.tsv:{i}: empty/duplicate sample_id')
        seen.add(sid)
        if not (row.get('biological_unit') or '').strip():warnings.append(f'samples.tsv:{i}: biological unit missing')
    if strict and not claims:errors.append('No claims listed in strict mode')
    stats={'claims':len(claims),'datasets':len(datasets),'samples':len(samples)}
    return {'status':'PASS' if not errors else 'FAIL','errors':errors,'warnings':warnings,'counts':stats}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--project',type=Path,default=Path.cwd())
    ap.add_argument('--strict',action='store_true')
    ap.add_argument('--json',action='store_true')
    a=ap.parse_args();result=audit(a.project.expanduser().resolve(),a.strict)
    if a.json:print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print(result['status'],result['counts'])
        for type_ in ['errors','warnings']:
            for x in result[type_]:print(type_[:-1].upper()+': '+x)
    return 0 if result['status']=='PASS' else 2
if __name__=='__main__':raise SystemExit(main())
