---
name: wiki-lint
description: "Validate a biology research knowledge wiki for missing metadata, broken source links, orphaned pages, and claim-ledger inconsistencies. Use after source ingest or before drafting/release."
---

# wiki-lint

Check that the wiki resolves structurally before relying on it.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Run python3 scripts/wiki_lint.py --project <root> and record its exit code.
2. Run python3 scripts/audit_project.py --project <root> to validate claim ledger references and provenance rows.
3. Repair broken links or missing source IDs only from real evidence, never invent placeholder citations.
4. Annotate orphaned source pages and stale synthesis, check outdated data accession links manually.
5. Save a dated audit receipt and re-run after fixing blockers.

## Required outputs and acceptance

- [ ] Linter output and exit code
- [ ] Unresolved references listed
- [ ] No fictitious repair entries

## Gate policy

HARD-STOP: verified citations cannot reference nonexistent local source files.

## Mistakes to reject

- Auto-repair by fabricating sources

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
