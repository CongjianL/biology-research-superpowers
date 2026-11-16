---
name: wiki-graph
description: "Build and inspect a biological knowledge graph linking source articles, genes, proteins, species, mechanisms, hypotheses and claims."
---

# wiki-graph

Expose missing biological and bibliographic connections in the research wiki.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Run python3 scripts/wiki_graph.py --project <root> --output output/data-analysis/wiki-graph.json.
2. Validate that each node references a real wiki source/entity/synthesis file, retaining unresolved outgoing links as flagged edges.
3. Identify hub claims supported by a single source, missing organism or accession mappings, disconnected data and conflicting study conditions.
4. Use graph structure as navigation, never as evidence of a causal biological interaction.
5. Write knowledge/synthesis/graph-audit.md with hypotheses for verification, not automatic conclusions.

## Required outputs and acceptance

- [ ] Graph JSON
- [ ] Flagged unsupported edges and high-dependency nodes
- [ ] Explicit inferential limitations

## Gate policy

SOFT-GATE: interpretation requires inspection of primary evidence.

## Mistakes to reject

- Inferring regulatory causality from co-citation edges

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
