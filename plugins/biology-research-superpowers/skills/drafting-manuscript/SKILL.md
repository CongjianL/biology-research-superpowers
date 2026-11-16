---
name: drafting-manuscript
description: "Draft biology manuscripts and dissertation chapters from verified analyses and source-backed synthesis, including methods, limitations, evidence figures and accession reporting."
---

# drafting-manuscript

Write claims proportional to evidence rather than the most compelling narrative.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Confirm stable synthesis page(s), frozen data tables, result provenance and source citations exist before drafting claim-bearing text.
2. Build an argument map: research question → method → observation → interpretation → limitation → permitted conclusion.
3. Use exact sample counts, effect sizes, confidence intervals, software versions, sequence identifiers and figure anchors from reproducible outputs.
4. Distinguish observed protein transport from physiological stress-response or ecological desert adaptation; do not infer the latter from the former alone.
5. Cite primary papers or data accession for every load-bearing claim and create output/article/*.qmd or markdown with a bibliography.
6. Perform a claim-ledger audit, citation verification, figure-table checks and a manuscript peer-review pass before declaring submission-ready.

## Required outputs and acceptance

- [ ] Source-backed manuscript draft
- [ ] Accurate results and limitations
- [ ] Figure/table/citation traceability

## Gate policy

SOFT-GATE: stable evidence synthesis and audit needed before drafting; user may request a clearly labeled exploratory draft.

## Mistakes to reject

- Inventing precise p values
- Concluding ecological adaptation from in vitro molecular function
- Uncited structure-function claims

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
