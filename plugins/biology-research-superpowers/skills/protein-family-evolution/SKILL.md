---
name: protein-family-evolution
description: "Analyze protein family evolution: motifs, domain architecture, profiles, Potts/DCA, phylogeny, duplication/HGT, selection and functional divergence with sequence-to-function limits."
---

# protein-family-evolution

Build an evidence-supported history of protein-family diversification.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Curate family membership and distinguish orthology, paralogy and convergent similarity; record HMM/sequence thresholds.
2. Choose appropriate models for sequence sampling and family heterogeneity; document profile vs Potts vs other likelihood or energy semantics.
3. Test MSA robustness and site-specific effects around historical indels, transmembrane helices and functionally important motifs.
4. Combine gene-tree, reconciliation, domain, selection and ancestral reconstruction with uncertainty rather than forcing one narrative.
5. When comparing functional types (e.g. proton/Na+/Cl- transport), explicitly analyze class imbalance and non-identifiability.
6. Design informative structural/experimental validation and rank claims by evidence tier.

## Required outputs and acceptance

- [ ] Family membership and model audit
- [ ] Explicit evolutionary scenarios and uncertainty
- [ ] Function claims bounded by evidence

## Gate policy

HARD-STOP: motif or statistical profile alone does not establish transport specificity or organismal adaptation.

## Mistakes to reject

- Treating Potts score as fitness without calibration
- Confusing transfer predictions with experimentally observed transfer

## Method references (load as needed)

- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)
- [`bioinformatics-and-phylogeny.md`](../../references/bioinformatics-and-phylogeny.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
