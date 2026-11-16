---
name: evolutionary-simulation-validation
description: "Qualify sequence evolution and protein-family simulators with independent oracles, random-model tests, calibration, mixing, replay, numerical precision, joint events and HPC evidence."
---

# evolutionary-simulation-validation

Test whether a simulator is both numerically correct and scientifically fit for a hypothesis.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Write a scientific contract: target probability model, substitution/indel/duplication/loss/transfer events, constraints, topology, time scale and truth objects.
2. Separate deterministic unit invariants from stochastic distributional qualification. For tiny cases implement an independent oracle, not the production scoring code.
3. Test finite precision, log-sum-exp/exponential hazards, rare-event tails and fallback paths; compare exact or high-precision references.
4. For random processes, test independent sampling distribution, null calibration, cross-seed stability and joint effects; certify reference mixing/ESS or explain why it cannot be certified.
5. Check replay/cold resume/ordering and output compatibility separately from scientific accuracy.
6. Lock effect size and power analysis before large HPC jobs; use Slurm receipts for full-scale timing, memory and result verification.
7. Require independent review of all load-bearing numerical conclusions and label gates blocked if evidence is incomplete.

## Required outputs and acceptance

- [ ] Simulation scientific contract and oracle fixtures
- [ ] Statistical qualification and power plan
- [ ] HPC receipts and replay evidence

## Gate policy

HARD-STOP: never accept a simulator as qualified from CI alone or substitute insufficient-power pilot results for production evidence.

## Mistakes to reject

- Circular reference oracle
- Insufficient random seeds
- Uncertified mixing time
- Ignoring event interactions

## Method references (load as needed)

- [`simulator-qualification.md`](../../references/simulator-qualification.md)
- [`study-design-and-statistics.md`](../../references/study-design-and-statistics.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
