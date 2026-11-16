---
name: sequence-data-curation
description: "Curate biological sequence and sample datasets with NCBI/ENA/DDBJ accession versions, metadata, contamination, duplicates and train/test leakage checks. Use before genomics, alignment or simulation analysis."
---

# sequence-data-curation

Freeze a clean, traceable biological dataset.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Inventory biological units (isolate, genome, contig, gene, protein, metagenomic bin) and distinguish them from technical records.
2. Collect accession plus version, taxonomy, assembly provenance, collection environment, genome completeness and contamination measures appropriate to data type.
3. Check duplicates, plasmids vs chromosomes, length/completeness outliers, translation/frameshift issues, and reference leakage.
4. Document filters and exclusion rationale; keep raw files byte-for-byte immutable.
5. Export input/metadata/datasets.tsv and sample manifest plus checksum inventory (scripts/record_inputs.py).
6. Verify sequence-to-genome mapping and all selection decisions on a small manually inspected subset.

## Required outputs and acceptance

- [ ] Versioned manifest and inclusion/exclusion log
- [ ] Checksums, raw provenance and QC summary
- [ ] No ambiguous biological units

## Gate policy

HARD-STOP: unverified sample identity or accession must not be treated as exact ground truth.

## Mistakes to reject

- Treating 16S hits as species identification without limits
- Training and benchmarking on homologous leakage

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)
- [`bioinformatics-and-phylogeny.md`](../../references/bioinformatics-and-phylogeny.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
