---
name: finishing-a-research-project
description: "Close a biology research project with reproducibility, data-sharing, reporting-guideline, manuscript and archival checks. Use before submission, thesis handoff or release."
---

# finishing-a-research-project

Close research projects with explicit scientific and artifact acceptance criteria.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Check final report, methods, figure tables, bibliography, raw-data provenance and full accession cross-reference for consistency.
2. Verify environment/lockfile, exact code SHA/tag, random seeds, benchmark receipts and rerun instructions are present.
3. Check that ethics, biosafety, privacy and controlled-access restrictions have been respected.
4. Select appropriate deposition targets (e.g., SRA/GenBank, GEO, PRIDE, PDB, Zenodo) and record actual accession identifiers; do not pretend a planned deposition is complete.
5. Run structural audits and license/privacy scans, then prepare release notes and unresolved limitation register.
6. Produce output/FINAL-CHECKLIST.md with each status PASS, FAIL, N/A or OVERRIDDEN and reason; no blanket PASS.

## Required outputs and acceptance

- [ ] Final signed-off checklist with open gaps
- [ ] Reproducibility and data availability statement
- [ ] Actual or pending depositions distinguished

## Gate policy

SOFT-GATE: documented omissions may be accepted by researcher, but ethical and access requirements remain hard stops.

## Mistakes to reject

- Fake DOIs/accessions
- Archived code not matching generated figures
- Unsupported claims presented as conclusions

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
