---
name: brainstorming-research
description: "Develop testable biological research questions and study designs, including microbial ecology, protein evolution, genomics and laboratory functional validation. Use before beginning a new substantial hypothesis-driven study."
---

# brainstorming-research

Convert broad biological ideas into testable questions while separating evolutionary narrative from mechanistic proof.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Specify the biological system, molecular or evolutionary process, unit of inference, and claimed level (association, evolutionary history, mechanism, function, organismal adaptation).
2. Review the field and identify a specific falsifiable gap; label novel hypotheses as proposals rather than established findings.
3. List at least two competing hypotheses and predictions, including a plausible null or model-misspecification explanation.
4. Identify observational, computational and experimental evidence that could discriminate hypotheses.
5. Assess access to genomes, metadata, protein sequences, structures, assays, controls, replicates and computing budget.
6. Write input/ideas/<slug>-design.md with risks, feasibility, claims/measurements map and acceptance criteria; get approval before locking the plan.

## Required outputs and acceptance

- [ ] Design document with competing hypotheses
- [ ] Evidence vs claim strength matrix
- [ ] Documented feasibility/assumptions

## Gate policy

SOFT-GATE: research plan ordinarily follows an approved design. A documented user override is allowed; ethical and safety requirements are never overridable by the plugin.

## Mistakes to reject

- Promising causal claims without perturbation evidence
- Calling a novel parameterization a novel biological mechanism

## Method references (load as needed)

- [`methods-selection.md`](../../references/methods-selection.md)
- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
