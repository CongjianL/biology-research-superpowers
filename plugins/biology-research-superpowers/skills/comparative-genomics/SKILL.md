---
name: comparative-genomics
description: "Design and validate microbial comparative genomics and phylogenomics analyses: orthogroups, pangenomes, paralogy, HGT, gene gain/loss and genome QC."
---

# comparative-genomics

Connect genomic variation to defensible evolutionary hypotheses.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Freeze assembly and annotation versions, outgroups, taxon sampling and genome QC thresholds.
2. Build gene families/orthogroups with documented similarity and coverage thresholds and inspect paralog edge cases.
3. Record pangenome presence-absence uncertainty due to fragmented genomes, annotation inconsistency, contamination and HGT.
4. Build species tree from appropriate single-copy markers and diagnose conflict, compositional bias and insufficient signal.
5. Analyze gene family changes against species tree while separating duplication, loss and transfer explanations.
6. Benchmark alternative orthology definitions and leave-one-taxon-out sensitivity; record biological conclusions as conditional on sampling.

## Required outputs and acceptance

- [ ] Reproducible genome and orthogroup tables
- [ ] Sensitivity analysis
- [ ] Gene/species tree reconciliation audit

## Gate policy

HARD-STOP: missing genomes or unreliable assembly annotation cannot support an absence-of-gene claim.

## Mistakes to reject

- Equating a missing annotation with true gene loss
- Assuming gene tree incongruence alone proves HGT

## Method references (load as needed)

- [`bioinformatics-and-phylogeny.md`](../../references/bioinformatics-and-phylogeny.md)
- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
