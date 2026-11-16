---
name: literature-review
description: "Conduct systematic, biology-focused literature reviews using PubMed, Europe PMC, Crossref, OpenAlex, bioRxiv and primary journals. Use for microbial genomics, evolution, biochemistry, omics, methods and current evidence syntheses."
---

# literature-review

Search and triage biological literature without inventing references.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Translate the biological question into organism names, ortholog identifiers, process synonyms, gene/protein aliases and search facets.
2. Search at least two complementary scholarly indexes when available. Record exact query strings, dates, databases and hit counts; specify coverage limits.
3. Deduplicate by DOI/PMID and separate peer-reviewed articles, preprints, reviews, protocols and data records.
4. Screen by pre-specified relevance criteria; identify primary experiments or analyses for load-bearing claims.
5. Verify bibliographic metadata, versions, corrections and retractions, DOI/PMID links and whether full text was actually read.
6. Create input/bibliography/literature-search.md, screening.csv, source table, and output/bibtex/references.bib; label inaccessible and unresolved records.

## Required outputs and acceptance

- [ ] Reproducible search strategy and dates
- [ ] Verified bibliography and evidence table
- [ ] Explicit search limitations

## Gate policy

HARD-STOP: no invented abstracts or DOI; no claims that an inaccessible paper was fully evaluated.

## Mistakes to reject

- Preprint presented as peer-reviewed
- Ignoring negative studies
- Searching only one keyword or only reviews

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
