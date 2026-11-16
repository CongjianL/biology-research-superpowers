---
name: executing-research-plan
description: "Execute a registered computational or laboratory-analysis biology plan with traceable provenance, independent scientific checks and explicit acceptance gates. Use for multi-step studies rather than one-off calculations."
---

# executing-research-plan

Run declared tasks reproducibly without silently changing the hypothesis or accepting an unverified result.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Load the approved plan and compare each task against prerequisites, versions, raw data, permissions, safety and resource availability.
2. Create a task/evidence matrix with input paths, environment, code commit, random seeds and expected artifacts.
3. Delegate independent bounded tasks to available Codex agents where supported; otherwise use sequential independent reviews. Prevent agents from editing the same files concurrently.
4. Run checks for input integrity and software behavior before production-scale analysis; test small known-answer fixtures.
5. Capture exact commands, stdout/stderr, exit code, workload/job ID, runtime, CPU and peak memory when available.
6. Reconcile outputs with plan and independent reviewers; document amendments and report inconclusive or failed tasks as such.

## Required outputs and acceptance

- [ ] Task execution ledger
- [ ] Reproducible environment and result receipts
- [ ] Pass/fail/inconclusive gate decisions

## Gate policy

HARD-STOP: do not claim a Slurm job completed before confirmed completion or fabricate numerical artifacts.

## Mistakes to reject

- Conflating CI passing with scientific validity
- Ignoring seed or candidate SHA
- Merging code under review without qualification

## Method references (load as needed)

- [`simulator-qualification.md`](../../references/simulator-qualification.md)
- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
