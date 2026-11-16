# Biology Research Superpowers for Codex (independent biology adaptation)

**Upstream inspiration:** [Patrick Leiverkus / research-superpowers](https://github.com/leiverkus/research-superpowers), MIT, original v0.47.0 (2026-11-15). The standalone plugin does **not** claim to reproduce the entire original textual workflow. It reimplements the phase architecture, SOFT-GATE provenance conventions and evidence wiki for biology.

## Scope

29 substantive Codex Skills: 18 adaptations of original lifecycle names + 11 dedicated modules for sequence data, comparative genomics, phylogenetics, protein-family evolution, simulation/numerics, omics, structure, functional assays, reproducible computation, figure integrity, deposition.

8 optional Codex agent TOML definitions are under `codex-agents/`; they **must be installed explicitly**. No remote MCP server is bundled or authenticated. Online literature retrieval uses whatever authorized Codex web/network tools the user has.

## Install as local Codex Plugin

The marketplace root is the directory containing `.agents/plugins/marketplace.json` and `plugins/biology-research-superpowers/plugin.json`.

1. Unzip `biology-research-superpowers-codex.zip` to a permanent directory.
2. `codex plugin marketplace add /absolute/path/to/biology-research-superpowers-marketplace`
3. In Codex, run `/plugins`, choose `biology-research-local`, select **Biology Research Superpowers**, and install it. Then restart if needed.
4. Test by asking: “Use Biology Research Superpowers to plan a microbial rhodopsin family evolution project, clearly separating computational predictions from transport assays.”

`marketplace add` registers the source; it is **not** the same as plugin installation. No automatic hooks or MCP servers run during installation.

## Install optional Codex subagents

After installing from the marketplace, locate the plugin's folder and run:

`python3 scripts/install_agents.py --scope user --dry-run`
`python3 scripts/install_agents.py --scope user`

This script never overwrites existing agent files. Codex delegation behavior depends on client configuration; if unsupported, use the skills sequentially and disclose that limitation.

## New project

`python3 scripts/scaffold_project.py --name my-biology-study --destination ~/Research --study-type mixed --discipline Microbiology --taxon Geodermatophilaceae`

After creation, edit `PROJECT.md` and run audit scripts. Raw data rights/approval requirements remain the user's responsibility.

## Reproducibility gates

- `python3 scripts/record_inputs.py --project /path/to/project` (record inputs)
- `python3 scripts/record_inputs.py --project /path/to/project --check` (detect byte drift)
- `python3 scripts/audit_project.py --project /path/to/project` (claim + metadata validation)
- `python3 scripts/wiki_lint.py --project /path/to/project` (wikilink and source page structure)
- `python3 scripts/drift_report.py --project /path/to/project` (read-only drift check)

Do not treat linter success as proof that a biological hypothesis is valid. Scientific qualification requires independent review and real experiments/results.

## Upstream-preserving variant

This package optionally includes the previous `leiverkus-research-superpowers-to-codex` converter under the **download bundle's** `extras/` folder and `scripts/overlay_upstream.py`. First run that converter on a trusted local clone of the pinned original repository; then overlay its generated plugin onto the biology adaptation. The overlay keeps the original skill content under `references/leiverkus-original.md` and archived upstream resources. It does not silently run upstream code.

## Provenance & licensing

This is an independent community biology adaptation inspired by the original MIT-licensed project, not endorsed by the upstream author. All scientific instructions, tests and scripts in the standalone biology plugin are newly authored, not the original upstream code. The optional overlay copies original MIT content with the original license and attribution.

## Actual verification status

Static manifest/frontmatter/TOML and deterministic local tests may pass without Codex installed. A full user-side installation and end-to-end biological research workflow test is still required; no PubMed, SRA, HPC or wet-lab work is performed by packaging alone.
