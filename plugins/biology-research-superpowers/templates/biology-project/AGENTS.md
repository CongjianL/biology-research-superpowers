# Codex instructions — biological research project

Read `PROJECT.md` and this file before material edits. `CLAUDE.md` exists only for upstream research-superpowers compatibility and methodological metadata; `AGENTS.md` governs Codex behavior here.

Use the installed **Biology Research Superpowers** plugin. Select a phase skill, then a domain skill. For chat-only questions, do not initialize tasks automatically.

- `input/data/` is immutable original data; outputs and simulated data belong in `output/data-analysis/`.
- Assert scientific truth only with claims.tsv entries whose evidence_path, source_id and methods are verifiable. Separate observed assay, computational inference and predicted mechanisms.
- Maintain fixed sample identifiers, genome/protein accession versions, software versions, git SHA, seeds, job receipts and audit logs.
- Pre-analysis plans and user-approved changes are stored in `input/ideas/` and `knowledge/_meta/gate-overrides.tsv`.
- Prefer independent methods for decisive numerical results. Delegate narrowly and avoid concurrent writes to the same files.
- Wet-lab activity does not imply organismal fitness or adaptation; a simulation only validates the claims within its specified truth model.
- Do not bypass approvals, access rights, ethics or biosafety requirements. Never invent citations, figures, data or experimental results.
- Run `python3 scripts/audit_project.py --project .` and `python3 scripts/wiki_lint.py --project .` before manuscript claims or release.
