---
name: reproducible-computation
description: "Create or audit reproducible bioinformatics computing workflows across local macOS and Slurm HPC, including code commit, environments, seeds, containers, provenance and resource receipts."
---

# reproducible-computation

Ensure that another researcher can reproduce results and detect changes.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Inventory local and HPC environments, tool versions, reference database snapshots and exact code SHA.
2. Separate immutable inputs, cache and results; prefer per-run output directories and deterministic filenames.
3. Record shell commands, Slurm scripts/IDs, exit status, random seeds, CPU/RAM/time, and any relevant filesystem performance assumptions.
4. Create small deterministic fixtures and scientific invariants, then scale with quantitative memory/duration budgets.
5. Use checksums for input and output manifests; distinguish algorithm changes from data and configuration changes.
6. Provide reproducibility instructions with explicit known limitations and no fabricated execution receipts.

## Required outputs and acceptance

- [ ] Run manifest and executable reproduction script
- [ ] Environment and input hashes
- [ ] Verified job status and resource measurements

## Gate policy

HARD-STOP: a job submission is not a completed experiment; no false timing or memory results.

## Mistakes to reject

- Running network fetches on isolated compute nodes
- Treating high-water RSS of coordinator as worker peak

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)
- [`simulator-qualification.md`](../../references/simulator-qualification.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
