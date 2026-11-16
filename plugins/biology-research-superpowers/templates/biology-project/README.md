# Biology Research Superpowers — project skeleton

Use `PROJECT.md` for biology/methodology and `AGENTS.md` for Codex behavior. Leave `input/data` unchanged after acquisition; record accessions, sample IDs and checksums in `input/metadata`.

## Start

1. Complete species/organism, study type, unit and ethics fields in PROJECT.md.
2. Add original data under input/data and populate datasets.tsv / samples.tsv.
3. `python3 scripts/record_inputs.py --project .`
4. Plan the study under input/ideas and record claims under knowledge/_meta/claims.tsv.
5. Audit before claims: `python3 scripts/audit_project.py --project .` and `python3 scripts/wiki_lint.py --project .`.
6. Check claims against original evidence (DOIs/accessions, observations vs predictions). Tests cannot substitute scientific review.

Optional: create a drift baseline only after review, using `python3 scripts/drift_report.py --project . --record-baseline`.
