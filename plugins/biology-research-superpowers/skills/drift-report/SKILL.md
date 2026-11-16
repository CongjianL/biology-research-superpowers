---
name: drift-report
description: "Detect provenance drift between biology project datasets, sample metadata, claims and outputs. Use for maintenance audits or before a scientific release."
---

# drift-report

Find out-of-band changes without automatically mutating the science.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Run python3 scripts/drift_report.py --project <root> in read-only mode to compare against a prior recorded snapshot.
2. Review differences in input manifests, claim counts, source pages, sample IDs, analysis versions and cached results.
3. Do not treat an updated input as equivalent to the frozen pre-analysis version; create a new dataset revision.
4. If the scientist approves, save a snapshot using --record-baseline after reviewing the changes.
5. Report which steps must be rerun and which conclusions are unaffected.

## Required outputs and acceptance

- [ ] Drift findings and affected artifact paths
- [ ] Approved new baseline only after review
- [ ] No silent workflow execution

## Gate policy

HARD-STOP: never auto-accept dataset revisions as prior certified evidence.

## Mistakes to reject

- Updating cached truth labels while hiding simulator seed or parameter drift

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
