---
name: ingest-source
description: "Ingest a biological paper, biological database entry, genome assembly, protein structure or dataset into an evidence-backed research wiki with source identifiers and page/figure/table anchors."
---

# ingest-source

Structure primary source evidence for claim-level traceability.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Confirm the original file or accessible primary record exists. Abort if missing rather than summarizing from hearsay.
2. Extract DOI/PMID/PMCID or accession/version, authors, year, study type, biological material, experimental design and controls.
3. Separate observed results, authors interpretations, reviewer inferences and limitations; capture numeric results and sample sizes with precise section/figure/table/page anchors.
4. Record organism/strain, conditions, sequence or structural identifiers and deviations; create knowledge/sources/<source-id>.md with a study-specific focus block.
5. Update entities and output/bibtex/references.bib, including stable citation keys.
6. Link claims in knowledge/_meta/claims.tsv to source page/figure or dataset record; run wiki_lint.py and audit_project.py.

## Required outputs and acceptance

- [ ] Source page with verifiable anchors
- [ ] Claims and citations linked
- [ ] Original source identity preserved

## Gate policy

HARD-STOP: missing primary text/data; no invented quotes, residue positions or numeric results.

## Mistakes to reject

- Treating citation abstracts as full-text methods
- Confusing strain and species
- Mixing author interpretation with direct observation

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
