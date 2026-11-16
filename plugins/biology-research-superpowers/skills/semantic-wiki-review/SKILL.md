---
name: semantic-wiki-review
description: "Semantically audit biology knowledge pages for contradictory claims, mismatched organisms/conditions, stale evidence and unsupported mechanistic inferences."
---

# semantic-wiki-review

Read the science behind structurally valid wiki pages.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Sample or exhaustively review source, synthesis and entity pages based on the project risk and size.
2. For each major synthesis claim, trace to the original study, assay/computation type, sample unit, uncertainty and limitation.
3. Spot cross-species extrapolation, gene vs species tree confusion, inconsistent residues/numbering and incompatible conditions.
4. Distinguish confirmed conflict from alternate models or differences in methods.
5. Write a non-destructive audit table of claim IDs, discrepancy, sources and corrective action, without silently rewriting history.

## Required outputs and acceptance

- [ ] Claim contradiction audit
- [ ] Source-backed correction proposals
- [ ] Uncertain conflicts marked as such

## Gate policy

HARD-STOP: cannot resolve contradictory literature by choosing a preferred narrative without evidence.

## Mistakes to reject

- Equating related orthologs with identical function
- Losing historical version context

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`protein-evolution-and-structure.md`](../../references/protein-evolution-and-structure.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
