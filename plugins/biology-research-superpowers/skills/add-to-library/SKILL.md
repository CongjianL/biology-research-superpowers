---
name: add-to-library
description: "Register a biology research PDF, dataset, structure or sequence record in a master source library with validated bibliographic and accession metadata. Use when adding one source outside an active review."
---

# add-to-library

Safely register a single reference and avoid duplicate or untraceable copies.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Identify DOI/PMID or accession/version from the source and verify against primary metadata services.
2. Check for an existing entry by persistent identifier and checksum, including preprint-to-publication lineage.
3. Copy rather than mutate the original and record downloaded/ingested timestamp plus license or access restrictions.
4. Update bibliography or metadata registry atomically; present conflicts rather than silently replacing an entry.
5. For data archives, record assembly/sample cross-links and dataset version.

## Required outputs and acceptance

- [ ] One verified library record
- [ ] Checksum and provenance recorded
- [ ] No duplicate identity

## Gate policy

HARD-STOP: do not register uncertain bibliographic identity as verified.

## Mistakes to reject

- Merging preprint and version of record without keeping version history

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
