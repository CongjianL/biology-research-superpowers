---
name: revising-manuscript
description: "Revise existing biological manuscripts paragraph by paragraph while preserving approved claims, decision history, citation identity and statistical fidelity."
---

# revising-manuscript

Improve a manuscript without changing scientific conclusions accidentally.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Load target manuscript, previous reviewer comments and revision ledger; identify already approved passages.
2. Choose local vs substantive revision and log each author decision with section/paragraph identifier.
3. Check changed assertions against source, data table and figure. Do not strengthen association into causation.
4. Preserve exact statistics, units, accession versions and original meaning unless an explicit correction is supported.
5. For substantive changes re-run bibliography and claim/figure audit; mark unresolved points for the author.
6. Save revised manuscript and adjacent <name>-revision.md with before/after rationale, approval status and freeze markers.

## Required outputs and acceptance

- [ ] Minimally revised manuscript
- [ ] Persistent paragraph revision ledger
- [ ] Scientific claims preserved or explicitly corrected

## Gate policy

HARD-STOP: do not rewrite approved paragraphs or silently reinterpret a failed experiment.

## Mistakes to reject

- Using prose polishing to hide unsupported conclusions
- Changing statistical denominator

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
