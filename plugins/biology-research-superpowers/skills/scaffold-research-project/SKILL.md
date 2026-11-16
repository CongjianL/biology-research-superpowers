---
name: scaffold-research-project
description: "Create a versioned biology research project with reproducible metadata, raw-data provenance, claim and gate ledgers, analysis, knowledge wiki and manuscript directories. Use for new projects in biology or bioinformatics."
---

# scaffold-research-project

Initialize the research project with explicit biological unit, study type and data provenance.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Ask for a project slug and destination only if absent and essential; choose sensible scientific defaults otherwise.
2. Run scripts/scaffold_project.py with --name and --destination. The script refuses overwriting any existing directory.
3. Set PROJECT.md fields: discipline, organism/taxon, study_type (computational, experimental, mixed), primary_unit, data availability and ethics/biosafety applicability.
4. Keep input/data immutable; place processed and simulated outputs in output/data-analysis, never in the raw-data folder.
5. Initialize claims.tsv, datasets.tsv, samples.tsv, pre-analysis plan, and gate override ledger.
6. Inspect new AGENTS.md and PROJECT.md; report choices needing researcher confirmation.

## Required outputs and acceptance

- [ ] New project with expected directories
- [ ] Data/claim provenance ledgers
- [ ] No overwritten existing work

## Gate policy

HARD-STOP: never overwrite an existing workspace; never invent ethics or permits.

## Mistakes to reject

- Raw data modified by setup
- Using project defaults as confirmed facts

## Method references (load as needed)

- [`data-and-provenance.md`](../../references/data-and-provenance.md)
- [`study-design-and-statistics.md`](../../references/study-design-and-statistics.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
