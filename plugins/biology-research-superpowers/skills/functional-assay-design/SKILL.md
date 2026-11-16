---
name: functional-assay-design
description: "Plan and evaluate non-clinical biological functional experiments such as protein transport, ion specificity, protein activity and stress association with adequate controls and replication."
---

# functional-assay-design

Distinguish molecular function, cellular phenotype and ecological adaptation.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. State the exact mechanistic question and assay readout, e.g. light-driven H+, Na+ or Cl- transport, and the evidence tier it can support.
2. Select conceptual positive/negative controls, expression controls, orthogonal measurements and biological replicate units; document feasibility and biosafety approval requirements.
3. Identify confounders: expression level, membrane localization, light response artifacts, ionic strength, pH, sample handling and background cellular transport.
4. Plan randomization, calibration, power/precision, blinding if practical, and analyses before results are available.
5. Define when data would refute the preferred mechanism and how ambiguous assay readouts would be interpreted.
6. Document how organism-level stress fitness or desert adaptation claims would need additional independent phenotypic/ecological evidence.

## Required outputs and acceptance

- [ ] Assay question and expected evidence tier
- [ ] Control/replicate plan
- [ ] Predeclared analysis and interpretation thresholds

## Gate policy

HARD-STOP: follow institutional biosafety/ethics rules; no claim of organismal adaptation from transport activity alone.

## Mistakes to reject

- Missing biological replicates
- Directly interpreting expression artifact as ion transport

## Method references (load as needed)

- [`study-design-and-statistics.md`](../../references/study-design-and-statistics.md)
- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)
- [`bio-safety.md`](../../references/bio-safety.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
