# Biology Research Superpowers for Codex

> **Repository bootstrap status (2026-11-16):** This GitHub repository currently contains project documentation only. The complete 29-Skill/8-Agent source tree has not yet been pushed. Use the [source archive provided in ChatGPT](https://github.com/CongjianL/biology-research-superpowers) and run `bash publish_to_github.sh` from the extracted folder to complete publication. Do not treat this repository as installable until the `plugins/` directory appears.


An **independent, biology-focused adaptation** of the research lifecycle, audit-trail, and SOFT-GATE approach of [leiverkus/research-superpowers](https://github.com/leiverkus/research-superpowers). This is **not** an official release or a verbatim source port of that repository.

[Chinese documentation](README-zh.md) | [Validation summary](TEST_REPORT.md) | [Scope and provenance](plugins/biology-research-superpowers/SOURCE_AND_SCOPE.md)

## What is included

- **29 Codex skills:** 18 biology adaptations of research-lifecycle phase names plus 11 additional modules (sequence curation, comparative genomics, phylogeny, protein-family evolution, simulation qualification, omics statistics, structure/function, functional assays, reproducible computation, figure evidence, and deposition).
- **8 optional specialist Codex agent configurations** (not installed automatically).
- **Scientific evidence and audit helpers:** provenance and raw-input checksums, claim ledgers, gate overrides, source wiki validation, drift reporting, and knowledge graphs.
- **Project scaffold** for computational and experimental biology research.
- **Optional, pinned upstream-source overlay** for preserving the complete original project in a separate reference area.

## Install from a local checkout

Clone this repository (after it is published) and point Codex at its *repository root*:

```bash
git clone https://github.com/CongjianL/biology-research-superpowers.git
codex plugin marketplace add "$(pwd)/biology-research-superpowers"
```

Alternatively, from inside the cloned repository:

```bash
codex plugin marketplace add "$PWD"
```

In Codex, open `/plugins` and install `biology-research-superpowers` from the `biology-research-local` marketplace. Marketplace registration alone does not install the plugin. If your Codex version does not expose the plugin marketplace, see `plugins/biology-research-superpowers/README_CODEX.md` for skill-level options.

## Quick checks

Requirements for local scripts: Python 3.10+; an appropriate Codex release for marketplace installation. Third-party packages and network/MCP access depend on the particular task and are not bundled automatically.

```bash
python3 -m compileall -q plugins/biology-research-superpowers/scripts
python3 plugins/biology-research-superpowers/scripts/install_agents.py --scope user --dry-run
```

The bundle was structurally tested offline; **live Codex installation, online scholarly APIs, multi-agent delegation, and scientific end-to-end validation have not been independently verified**. See `TEST_REPORT.md`.

## Upstream code and acknowledgements

The upstream project is **Patrick Leiverkus's** MIT-licensed `leiverkus/research-superpowers`, inspected at commit `da0effdf162cd96a42009fe2dfe701b352e50ba8` (v0.47.0). This repository preserves the source credit and license notices. Optional upstream-overlay files are obtained separately and retain the original notices. The biology adaptation is not affiliated with or endorsed by the upstream author.

## Intended research safeguards

Use evidence trails and explicit checks; do not treat simulated events as observed history, model predictions as measurements, or structure-based hypotheses as functional assay results. Approval gates log deviations but **are not a substitute for platform authorization controls**. No lab outcomes, publication claims, or HPC qualification are guaranteed by the plugin alone.

## License

MIT. See [LICENSE](LICENSE), and retain upstream author notices when adding upstream materials.