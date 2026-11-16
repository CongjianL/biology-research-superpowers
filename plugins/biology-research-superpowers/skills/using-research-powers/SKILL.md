---
name: using-research-powers
description: "Route biological science tasks into a reproducible research workflow. Use at the start of a biology, bioinformatics, microbiology, genetics, omics, phylogeny, experimental validation, or manuscript project; distinguish chat-only answers from project-changing work."
---

# using-research-powers

Map the user request to the correct biological research phase. Preserve the original research-superpowers phase discipline without importing its original archaeology/theology assumptions.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Routing inside the biology plugin

| Research goal | Governing domain skill |
|---|---|
| Literature/primary evidence | `literature-review`, `ingest-source` |
| Genome/sample provenance | `sequence-data-curation`, `comparative-genomics` |
| Tree / ancestral reconstruction | `phylogenetic-inference` |
| Protein family / functional divergence | `protein-family-evolution`, `structure-function-analysis` |
| Multi-factor sequence evolution simulator | `evolutionary-simulation-validation` |
| RNA-seq, metagenomics, microbiome, proteomics | `omics-statistics` |
| Functional transport / protein activity | `functional-assay-design` |
| HPC and numerical reproducibility | `reproducible-computation` |
| Paper and thesis | `drafting-manuscript`, `requesting-peer-review` |

## Procedure

1. Determine whether the question only needs a conversational answer. If yes, answer directly without creating a project.
2. Determine whether the task is discovery, a biological research design, acquisition, source ingestion, data curation, analysis, experimental validation, manuscript development, peer review, or deposition.
3. Read project AGENTS.md and PROJECT.md, select one governing phase skill and any domain skill (see routing table below).
4. Before edits, locate existing artifacts, dataset versions, approval history, and previous review results. Never reset a completed stage just to enforce ceremony.
5. If an upstream stage is missing, explain the dependency; record an authorized SOFT-GATE override when proceeding. Do not override hard stops involving missing source material, data permissions, biological safety, or invented evidence.
6. At handoff, cite the decision ledger, outputs, source accessions, and open validation gaps.

## Required outputs and acceptance

- [ ] Governing skill named and invoked
- [ ] Current artifacts and scientific evidence tier enumerated
- [ ] No claims of completed analysis without outputs

## Gate policy

SOFT-GATE: skipping research phases requires an explicit, logged rationale when it affects scientific claims. HARD-STOP: fabricated sources, fake computation, missing data rights, or unsuitable biosafety clearance.

## Mistakes to reject

- Invoking all skills for a simple definition
- Treating simulation as experimental validation
- Assuming a Codex plugin auto-registers custom agents

## Method references (load as needed)

- [`methods-selection.md`](../../references/methods-selection.md)
- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
