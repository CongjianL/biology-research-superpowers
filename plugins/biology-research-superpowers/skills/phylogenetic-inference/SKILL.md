---
name: phylogenetic-inference
description: "Perform defensible phylogenetic inference for genes, proteins, genomes and evolutionary simulations with alignment/model/topology uncertainty."
---

# phylogenetic-inference

Reconstruct evolutionary history without overclaiming uncertain branches.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Define homolog/ortholog set, rooting/outgroups and the tested phylogenetic question.
2. Generate and assess MSA; track unstable columns, paralogy, recombination, indels and composition/heterotachy.
3. Predeclare alignment filtering and model selection; save original and trimmed alignments.
4. Infer tree and branch support with full software versions, seeds, model fit and convergence data.
5. Compare gene vs species tree, alternative topology tests and reconciliation; separate weak bootstrap from outright model rejection.
6. Report uncertainty in ancestral state inference and map functional substitutions using correct numbering and sequence lineage.

## Required outputs and acceptance

- [ ] MSA and tree provenance
- [ ] Support and topology uncertainty
- [ ] Alternative histories explicitly evaluated

## Gate policy

HARD-STOP: missing rooting/mapping prevents direction-of-change claims; do not infer HGT solely from incongruence.

## Mistakes to reject

- Relying on one best tree as guaranteed truth
- Confusing alignment confidence with biological selection

## Method references (load as needed)

- [`bioinformatics-and-phylogeny.md`](../../references/bioinformatics-and-phylogeny.md)
- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
