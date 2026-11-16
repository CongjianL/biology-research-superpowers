# Biology Research Superpowers — local test report

Build target: independent Codex local plugin, v0.1.0.
Upstream conceptual source: `leiverkus/research-superpowers` v0.47.0, MIT, pinned source SHA `da0effdf162cd96a42009fe2dfe701b352e50ba8` in optional converter.

## Offline checks executed

`python3 -m unittest discover -s /mnt/data/biology_research_build/tests -v` — **5 tests passed**.

1. Portable plugin manifest, compatibility manifest and local marketplace paths parse and agree; no automatic session hooks are registered.
2. All 29 Skill entrypoints have syntactically valid frontmatter, correct names and existing reference paths; 18 carry original lifecycle names; each has standalone, substantive biology procedures.
3. Eight optional Codex agent TOML files parse and explicit installer has safe dry-run.
4. New research project creates; claim and metadata TSV audits pass structural checks, intentionally broken evidence fails, wiki unresolved links fail, raw input hash drift fails, gate approval is logged, drift baseline is opt-in.
5. Upstream archival overlay preserves 18 original skill bodies after checksum validation; rejects tampered source and prevents output overwrite.

Additional smoke checks: Python 3.13 compileall of bundled scripts, standalone project scaffold, audited empty ledgers and zero raw files, wiki graph output, raw SHA256 record/check.

## Not executed / not claimed

- Live `codex` CLI or Codex Desktop installation (binary not present here), plugin activation, optional Agent delegation behavior.
- Internet scholarly API / actual PubMed, SRA, UniProt or Crossref retrieval; authorisation and rate-limit performance.
- Real genomes, experimental assay, Slurm jobs, field/ethics approvals or scientific qualification.
- Full original upstream source clone in this container (network DNS restricted); packaged optional converter fetches the pinned source **on a networked user machine**.

## Scientific limitations

Passing a TSV/wiki parser is structural consistency only. It does not prove sources genuine, data authentic, biological claims valid, numerical implementations correct or wet-lab results reproducible. Real scientific review and user-side end-to-end tests are required before production use.
