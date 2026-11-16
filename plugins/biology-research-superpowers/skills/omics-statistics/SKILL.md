---
name: omics-statistics
description: "Plan and audit transcriptomic, metagenomic, microbiome, proteomic, metabolomic and other omics data analyses with batch and compositionality controls."
---

# omics-statistics

Use an appropriate statistical model for the true study design.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Establish count/intensity type, missingness, censoring, library depth, batch structure and biological replicates.
2. Check sample-to-metadata joins and contamination, spike-ins or negative controls as applicable.
3. Define normalization, compositionality treatment, contrasts, confounders and independent unit before seeing effects.
4. Choose differential abundance/expression or multivariate methods with assumptions and multiple-testing correction.
5. Assess robustness with leave-one-batch-out, sensitivity analyses and at least one negative control, including pseudoreplication checks.
6. Report effect sizes with intervals, adjusted p values and transparent zero/infinite estimates; archive analysis code and versions.

## Required outputs and acceptance

- [ ] Sample design matrix and QC
- [ ] Statistical model and diagnostics
- [ ] Adjusted inference with sensitivity analyses

## Gate policy

HARD-STOP: technical replicates are not independent biological replicates.

## Mistakes to reject

- Compositional artefacts
- Confounded treatment and batch
- Multiple testing without correction

## Method references (load as needed)

- [`study-design-and-statistics.md`](../../references/study-design-and-statistics.md)
- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
