# Research Superpowers -> Codex migration kit

**Correct upstream project:** [leiverkus/research-superpowers](https://github.com/leiverkus/research-superpowers), by Patrick Leiverkus (MIT).

This kit converts the **complete original Claude Code research plugin** to a Codex-friendly local plugin. It does not substitute the unrelated kthorn project. The source pin for this kit is:

- Git commit: `da0effdf162cd96a42009fe2dfe701b352e50ba8`
- Upstream version: `0.47.0` (2026-11-15)
- Expected: 18 original Skills and 7 original subagents

## Two ways to prepare your plugin

### A. Automatically fetch the exact upstream source (macOS / Linux)

Unzip this kit and open Terminal in the extracted folder:

```bash
bash prepare.sh
```

Requires `python3` (3.10+ recommended), `git`, and network access to GitHub. It clones the original code, checks out the pinned commit and generates a *fully populated* Codex marketplace under `dist/leiverkus-codex-marketplace/`.

### B. Use an already-cloned local source

```bash
bash prepare.sh /absolute/path/to/research-superpowers
```

The output is identical apart from the recorded source Git SHA and possible upstream version drift (the conversion checks the exact 18 Skills and 7 Agents inventory). This is useful when your machine or agent cannot access GitHub, or you want to review the upstream code before transforming it.

## Install in Codex

After preparation, run (substitute your own absolute path):

```bash
codex plugin marketplace add /ABSOLUTE/PATH/TO/dist/leiverkus-codex-marketplace
codex plugin marketplace list
```

Open the **Codex / ChatGPT desktop Plugins Directory**, switch to the `leiverkus-codex-local` source and install `research-superpowers`. Marketplace registration alone does not activate the plugin. Restart the desktop app if needed.

**For skills-only use in Codex CLI:** Copy the selected generated `plugins/research-superpowers/skills/<skill-name>/` directory into `~/.agents/skills/`, checking that you will not overwrite an existing skill. This loads skills without the plugin-specific hooks, optional MCP setup or custom agents.

## Converted parts

| Claude Code original | Codex destination / policy |
| --- | --- |
| `skills/*/SKILL.md` (18) | Native `skills/*/SKILL.md` entrypoint with original complete skill in `upstream-workflow.md`; original YAML metadata preserved in `references/upstream-frontmatter.yaml` |
| `agents/*.md` (7) | Prepared `codex-agents/rsp-*.toml` (manual install into `~/.codex/agents/` or trusted `.codex/agents/`; not auto-enabled) |
| `hooks/hooks.json` | Codex `SessionStart` entries and wrapper scripts, subject to `/hooks` trust review |
| `hooks/drift_check.py` | Original copied unchanged; startup drift is opt-in via `RESEARCH_SUPERPOWERS_ENABLE_DRIFT=1` |
| `templates/research-project-template/CLAUDE.md` | Preserved as methodological metadata + new `AGENTS.md` for Codex |
| `schema/`, `scripts/`, templates, docs, examples | Copied intact; no execution during conversion |
| Original optional MCP docs | Preserved; no external MCP auto-installed or authenticated |

## Important behavior and limits

- For Codex project work, preserve original `CLAUDE.md`. The upstream scripts may read its methodological YAML frontmatter; `AGENTS.md` is an additional Codex instruction file, not a substitute.
- `SOFT-GATE` is a research audit convention. It **cannot override Codex tool permissions**. `HARD-STOP` boundaries such as missing original sources must still be enforced.
- Claude Task / Skill / Todo tools are **not** invoked by name in Codex. The new native skill entrypoints tell Codex to follow original skill procedures using available host tools. For context-isolated subagents, install the generated agent TOML files explicitly.
- Plugin hooks require user review/trust (`/hooks`). The state-triggered drift check can modify derived caches and is disabled by default, even after hooks are trusted.
- The optional `dao-paper-search-mcp` is **not bundled**. To enable it, configure that MCP separately in Codex with your own credentials and review the author's docs. Without the MCP, use the original fallback workflow.
- No claim of full behavioral parity is made until the plugin is run inside your Codex client on representative research tasks. This kit includes an offline structure/provenance verifier, not a live end-to-end research certification.

## Verify the converted files

```bash
python3 verify.py --marketplace dist/leiverkus-codex-marketplace
```

You should see `PASS: 18 original skill bodies preserved, 7 TOML agents parse, manifest/marketplace/hooks/template verified`.

## License and attribution

Original code MIT license. The generated plugin bundles the original `LICENSE` with copyright to Patrick Leiverkus and credits the upstream GitHub repository. The migration scripts in this kit are provided for local adaptation. This is an independent community port, **not endorsed by the original author**.
