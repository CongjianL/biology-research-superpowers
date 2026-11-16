---
name: writing-research-plan
description: "Write auditable preregistered or analysis-ready plans for computational and experimental biology. Use after a design exists and before statistical testing, simulations, phylogenomics or wet-lab validation."
---

# writing-research-plan

Freeze scientific decisions that could otherwise drift after inspecting outcomes.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Define primary and secondary research questions, biological vs technical replicates and independence assumptions.
2. Specify inclusion/exclusion criteria, missing-data strategy, reference databases, accession and software version policies.
3. Choose endpoints, negative and positive controls, sampling design, null model, primary estimand, multiplicity correction and uncertainty intervals.
4. Predeclare analysis settings where practical: aligner, tree/model choices, simulation factors, stopping rules, benchmark metrics, assay readouts.
5. Distinguish exploratory from confirmatory analyses; identify blinding/randomization and ethics/biosafety requirements as applicable.
6. Write input/ideas/<slug>-plan.md with machine-runnable tasks, owners, acceptance gates and resource budget; mark changes as dated amendments, not silent edits.

## Required outputs and acceptance

- [ ] Ready plan with testable task blocks
- [ ] Statistical analysis plan
- [ ] Amendment and gate records

## Gate policy

SOFT-GATE: confirmatory analysis requires a frozen plan (or disclosed post-hoc status); experimental safety approvals remain mandatory where applicable.

## Mistakes to reject

- Pseudoreplication
- After-the-fact sample size rationalization
- Unrecorded exploratory model search

## Method references (load as needed)

- [`study-design-and-statistics.md`](../../references/study-design-and-statistics.md)
- [`simulator-qualification.md`](../../references/simulator-qualification.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
