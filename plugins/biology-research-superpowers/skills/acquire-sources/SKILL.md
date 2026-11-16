---
name: acquire-sources
description: "Acquire and track legally accessible research PDFs, datasets, FASTA, FASTQ, metadata, structures and supplementary materials for a biology review or analysis. Use after source discovery and before ingestion or computation."
---

# acquire-sources

Create a permission-aware, versioned acquisition ledger.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Read the literature worklist or dataset manifest and list source identifiers: DOI, PMID, accession, archive revision and provider.
2. Prefer original publisher, PubMed Central, institutional repositories or documented public biological archives; preserve original licensing and embargo restrictions.
3. Fetch only permitted material and record access time, file size, hash, accession version and source URL; no auto-fetch of large datasets without authorization.
4. Place original inputs under the explicitly selected read-only library or input/data, and derivative files in output.
5. For paywalled or blocked records create input/bibliography/acquisition-todo.md with a legitimate manual access path.
6. Validate downloaded content types, checksums and FASTA/FASTQ basic formats; never label missing original text as acquired.

## Required outputs and acceptance

- [ ] Acquisition ledger with identity, version and checksums
- [ ] Worklist for inaccessible originals
- [ ] Original inputs protected from modification

## Gate policy

HARD-STOP: do not bypass paywalls, fetch restricted controlled-access data, or substitute an unrelated preprint without disclosure.

## Mistakes to reject

- Unversioned accession
- PDF accidentally saved as HTML
- Missing license/consent checks

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
