---
name: data-deposition
description: "Prepare biology datasets, code, metadata and manuscript data-availability records for submission to appropriate repositories such as SRA, GenBank, GEO, PRIDE, PDB or Zenodo."
---

# data-deposition

Release reusable data with accurate accessions and legal permissions.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Choose repositories matching record type and data access constraints, verifying current requirements on official sites.
2. Connect BioProject/BioSample and reads/assemblies where applicable, with distinct identifiers for biological samples.
3. Remove or protect sensitive personally identifying or controlled-access data, following institutional and jurisdictional policy.
4. Validate checksums, metadata consistency, reproducible code and public license before submission.
5. Record upload status, embargo, curator feedback and accession exactly as received; generate data availability statement reflecting actual state.
6. Archive final source version and include release verification checklist.

## Required outputs and acceptance

- [ ] Repository-specific submission manifest
- [ ] Consistent accession mapping
- [ ] Truthful deposited/pending status

## Gate policy

HARD-STOP: do not submit protected human/clinical or third-party data without authorization; do not invent accessions.

## Mistakes to reject

- Invented BioSample IDs
- Mismatched read/assembly BioProject
- Missing consent restrictions

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)
- [`bio-safety.md`](../../references/bio-safety.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
