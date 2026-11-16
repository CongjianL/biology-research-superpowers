---
name: grant-finder
description: "Find and assess legitimate biology research funding opportunities using verified current program criteria, eligibility, deadlines and scientific aims."
---

# grant-finder

Map biology study needs to suitable funding schemes.

## Scientific operating rules

- Read the project's `AGENTS.md`, `PROJECT.md`, current plan and evidence ledger before making material changes. For one-off chat questions, do not force a new project.
- Verify external references, data accessions, file existence, tool outputs and actual execution. Never invent experiments, data, job receipts, citations, accession IDs, experimental results or approvals.
- Treat original raw data as immutable. Prefer an explicit candidate/seed/version and compare against a frozen baseline.
- Separate **biological observation**, **computational inference**, **prediction** and **mechanistic validation**. Label conditional results; preserve limitations.
- User-authorized phase overrides go into `knowledge/_meta/gate-overrides.tsv`; HARD-STOPs (missing primary material, data rights, safety, fabricated evidence) are not overridable.
- If Codex custom agents are unavailable, complete steps sequentially and disclose loss of independent context. Do not invoke Claude-only `Task`, `Skill`, or `TodoWrite` tool names.
- Use project `scripts/` relative to the project root and plugin tools under the installed plugin root. Do not run scripts merely because they exist; inspect them first.

## Procedure

1. Gather jurisdiction, career stage and funder preferences only when required by eligibility.
2. Search authoritative funder program pages such as NIH, NSF, ERC, EMBO and relevant national agencies using current rules.
3. Compare deadlines, eligible applicants, budget and allowed expenses using source links and access dates.
4. Match project methods, milestones and preliminary data honestly; distinguish completed evidence from proposed work.
5. Draft a grant fit matrix and a concise specific aims page; report unknown or unverified deadlines explicitly.

## Required outputs and acceptance

- [ ] Verified funding shortlist with links and dates
- [ ] Scientific fit vs eligibility analysis
- [ ] No invented award terms

## Gate policy

HARD-STOP: never rely on stale funding deadlines or imply grant approval.

## Mistakes to reject

- Submitting claims from unvalidated preliminary data as established

## Method references (load as needed)

- [`writing-and-reporting.md`](../../references/writing-and-reporting.md)

**Attribution:** Biology adaptation of the research lifecycle and audit-gate ideas in Patrick Leiverkus’s [research-superpowers](https://github.com/leiverkus/research-superpowers), MIT. This is an independent domain adaptation, not the original skill text.
