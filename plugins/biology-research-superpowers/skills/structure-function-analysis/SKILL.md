---
name: structure-function-analysis
description: "Analyze sequence–structure–function relationships using PDB/AlphaFold structures, residue mappings, protein motifs, uncertainty and testable mechanistic predictions."
---

# structure-function-analysis

Connect residues and protein structure to bounded mechanism hypotheses.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Verify source structure and protein construct/sequence identity, chain, numbering, missing regions and model confidence.
2. Produce explicit sequence-to-structure position map with insertions/deletions and ambiguous residues flagged.
3. Check membrane context, protonation/ligands and coordinate quality before interpreting active sites.
4. Evaluate proposed electrostatic or pathway effects with alternative explanations and sensitivity to structural model.
5. Separate structure-predicted function, conservation and direct biochemical measurement.
6. Define discriminating mutants or readouts without claiming experimental confirmation before data exist.

## Required outputs and acceptance

- [ ] Residue mapping with unresolved positions
- [ ] Structural observation vs prediction table
- [ ] Specific testable hypotheses

## Gate policy

HARD-STOP: missing structural coordinates or residue mapping blocks site-specific claims.

## Mistakes to reject

- Incorrect reference numbering
- Treating AlphaFold confidence as empirical functional evidence

## Method references (load as needed)

- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
