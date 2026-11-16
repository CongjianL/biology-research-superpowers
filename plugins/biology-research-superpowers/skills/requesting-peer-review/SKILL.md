---
name: requesting-peer-review
description: "Conduct two-pass constructive and adversarial scientific peer review of biology, bioinformatics, evolutionary genomics and experimental manuscripts, with data/code/claims audits."
---

# requesting-peer-review

Expose both conceptual and implementation weaknesses before publication or merging a method paper.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Read research question, plan amendments, methods, results, code/environment and available raw data; map each major claim to supporting artifact.
2. Constructive pass: evaluate biological plausibility, novelty, controls, methods reporting, statistical power, reproducibility and interpretation.
3. Adversarial pass: attempt alternative explanations, selection bias, data leakage, sample non-independence, tree/alignment artifacts, overfitting, numerical instability and missing experimental controls.
4. Use relevant reporting checklists only where appropriate (e.g. PRISMA for a systematic review, STROBE for observational studies, ARRIVE for animal studies).
5. Classify issues as blocking, major, minor and scope extension, and identify concrete falsification tests and independent validators.
6. Deliver review/report.md and a claim×evidence table; never call an internal agent audit journal peer review.

## Required outputs and acceptance

- [ ] Constructive and adversarial reports
- [ ] Blocking issue list and required tests
- [ ] Claim-to-evidence traceability

## Gate policy

HARD-STOP: no acceptance recommendation when a decisive result lacks verifiable input/analysis evidence.

## Mistakes to reject

- Calling a code review a scientific validation
- Inventing reviewer access to hidden files

## Method references (load as needed)

- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)
- [`simulator-qualification.md`](../../references/simulator-qualification.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
