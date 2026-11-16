---
name: figure-evidence-audit
description: "Audit figures and tables for biology manuscripts against underlying measurements, analysis scripts and claimed statistical tests."
---

# figure-evidence-audit

Prevent visually persuasive but irreproducible scientific figures.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Map every figure/table panel to source dataset, script/command, version and exact numerical result.
2. Check axes, units, sample sizes, legend definitions, error bars, statistical contrasts, color coding and absence of clipped outliers.
3. Identify reuse of data, multiple hypothesis testing, post-hoc subset choices and misplaced significance marks.
4. Audit structural residue numbering, phylogeny branch support or alignment site interpretation where relevant.
5. Verify revised manuscript references the correct figure IDs and that counts match result files.
6. Write output/figures/figure-audit.tsv with panel-level PASS/FAIL/N/A and evidence pointers.

## Required outputs and acceptance

- [ ] Panel-to-data traceability matrix
- [ ] Correct figures, captions and tests
- [ ] Explicit failing panels

## Gate policy

HARD-STOP: unsupported or fabricated figure content cannot be marked verified.

## Mistakes to reject

- Image-only result without underlying data
- Error bar ambiguities
- Misleading axis clipping

## Method references (load as needed)

- [`evidence-and-claims.md`](../../references/evidence-and-claims.md)
- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
