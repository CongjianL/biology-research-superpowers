#!/usr/bin/env python3
"""Convert a checkout of leiverkus/research-superpowers to a Codex plugin.

Only Python standard library is needed. This tool never executes upstream code.
The complete upstream skill text is retained in per-skill original workflow files, and
upstream project templates, scripts, schema, and documentation are copied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path

SOURCE_URL = "https://github.com/leiverkus/research-superpowers"
REFERENCE_SHA = "da0effdf162cd96a42009fe2dfe701b352e50ba8"
PLUGIN_NAME = "research-superpowers"
EXPECTED_SKILLS = {
    "acquire-sources", "add-to-library", "brainstorming-research",
    "drafting-manuscript", "drift-report", "executing-research-plan",
    "finishing-a-research-project", "grant-finder", "ingest-source",
    "literature-review", "requesting-peer-review", "revising-manuscript",
    "scaffold-research-project", "semantic-wiki-review",
    "using-research-powers", "wiki-graph", "wiki-lint",
    "writing-research-plan",
}
EXPECTED_AGENTS = {
    "analyst", "drafter", "literature-scout", "peer-reviewer",
    "source-acquirer", "source-ingester", "wiki-linter",
}


class MigrationError(RuntimeError):
    pass


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter(text: str, source: Path) -> tuple[dict[str, str], str, str]:
    """Split YAML without requiring PyYAML; scalar name/description only.

    Preserve the complete original header unmodified as a separate reference.
    Complex upstream inputs/outputs/agents remain accessible to the model.
    """
    if not text.startswith("---\n"):
        raise MigrationError(f"Missing YAML frontmatter: {source}")
    close = text.find("\n---\n", 4)
    if close < 0:
        raise MigrationError(f"Unclosed YAML frontmatter: {source}")
    raw = text[4:close]
    body = text[close + 5:]
    metadata: dict[str, str] = {}
    for k in ("name", "description", "implements"):
        match = re.search(rf"(?m)^{k}:\s*(.+)$", raw)
        if match:
            val = match.group(1).strip()
            if val.startswith("\"") and val.endswith("\""):
                try:
                    val = json.loads(val)
                except json.JSONDecodeError:
                    val = val.strip('"')
            metadata[k] = val
    if not metadata.get("name") or not metadata.get("description"):
        raise MigrationError(f"Missing name or description: {source}")
    return metadata, raw, body


def adapt_skill(source_skill: Path, target_skill: Path) -> dict:
    meta, raw, body = frontmatter(source_skill.read_text(encoding="utf-8"), source_skill)
    slug = source_skill.parent.name
    if meta["name"] != slug:
        raise MigrationError(f"Skill name mismatch: {source_skill}: {meta['name']} != {slug}")
    ref = target_skill / "upstream-workflow.md"
    # Store the original text, including its extended YAML metadata, byte-for-byte.
    ref.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_skill, ref)
    write_text(target_skill / "references" / "upstream-frontmatter.yaml", "---\n" + raw + "\n")
    name = meta["name"]
    description = json.dumps(meta["description"], ensure_ascii=False)
    native = f'''---
name: {name}
description: {description}
---

# {name} (Codex adaptation)

**Required before any substantive work:** Read the complete
[original upstream workflow](upstream-workflow.md) before performing
this task. Preserve its phase prerequisites, HARD-STOP / SOFT-GATE decisions,
research-method branching, source verification, write targets, audit records,
and acceptance checklist. The upstream document is the source of truth for the
research method; this short file only adapts the host environment.

## Codex execution contract

1. Use Codex's available file, shell, web, and MCP tools. Do not call tools
   named `Skill`, `Task`, `TaskCreate`, `TaskUpdate`, `TodoWrite`, `WebSearch`,
   `Read`, or `Write` merely because the Claude examples name them. Invoke
   named Codex skills when supported, otherwise open their `SKILL.md` files.
2. Read `AGENTS.md` in the project. Preserve `CLAUDE.md` alongside it, since
   upstream scripts and methodology detection may read its YAML frontmatter.
   If no research project exists, run the scaffold workflow using the template
   in `templates/research-project-template/` at the installed plugin root.
3. For agents, use the available Codex delegation tools only when enabled,
   permitted, and the `rsp-*` custom agent is installed. Otherwise execute the
   same work sequentially with explicit stage boundaries and fresh source reads.
   Never claim that Claude's `agents/*.md` files automatically register agents.
4. Interpret upstream `scripts/...` relative to the research project root,
   unless explicitly stated otherwise. Run deterministic scripts and record
   results; never infer successful execution from a file's presence.
5. The optional `dao-paper-search-mcp` server is not bundled or automatically
   authenticated. Use it only if the user separately installed and authorized
   it. Otherwise follow the upstream documented fallback and verify citations
   from accessible sources. Never invent citations or use inaccessible texts.
6. Respect the user's stated scope and the host's higher-priority safety and
   permission controls. For SOFT-GATEs, document an authorized override; do
   not use the SOFT-GATE mechanism to bypass permission checks or HARD-STOPS.
7. Do not silently overwrite the user's work, execute untrusted scripts,
   initialize Git, download large source sets, or mutate shared libraries.
   Inspect target files and obtain any required authorization first.

**Upstream source:** {SOURCE_URL} (MIT, Patrick Leiverkus).
**Original metadata:** `references/upstream-frontmatter.yaml`.
'''
    write_text(target_skill / "SKILL.md", native)
    if slug == "using-research-powers":
        (target_skill / "agents").mkdir(parents=True, exist_ok=True)
        write_text(target_skill / "agents" / "openai.yaml",
                   'interface:\n  display_name: "Research Superpowers"\n'
                   '  short_description: "Disciplined research from idea to publication"\n')
    return {
        "name": slug,
        "upstream_bytes": source_skill.stat().st_size,
        "upstream_sha256": sha256(source_skill),
        "retained_sha256": sha256(ref),
    }


def adapt_agent(source_agent: Path, dest: Path) -> dict:
    meta, _, body = frontmatter(source_agent.read_text(encoding="utf-8"), source_agent)
    slug = source_agent.stem
    if slug != meta["name"]:
        raise MigrationError(f"Agent name mismatch: {source_agent}")
    role = "rsp-" + slug
    implements = meta.get("implements") or "using-research-powers"
    prefix = (
        "Codex custom agent adapted from the original leiverkus research-superpowers.\n"
        "You are executing one delegated research task; do not recursively delegate.\n"
        "Project CLAUDE.md is maintained as methodology metadata; read AGENTS.md too.\n"
        "The parent must provide a task specification and may provide a skill path.\n"
        "The upstream Claude 'skills:' frontmatter does NOT preload a skill in Codex.\n"
        f"Before work, read the active plugin's skills/{implements}/"
        "upstream-workflow.md or request its full contents from parent.\n"
        "Do not assume Claude tools, permission overrides, or unrestricted write access.\n"
        "Use current Codex tools and parent user-granted permissions.\n\n"
    )
    # json.dump strings are valid TOML basic strings (newlines escaped).
    fields = {
        "name": role,
        "description": "Research Superpowers: " + meta["description"],
        "developer_instructions": prefix + body,
    }
    output = "# Generated from agents/" + slug + ".md; manually install to Codex.\n"
    output += "# Local agent install never happens implicitly.\n"
    for key, val in fields.items():
        output += f"{key} = {json.dumps(val, ensure_ascii=True)}\n"
    write_text(dest / f"{role}.toml", output)
    return {"name": role, "source": source_agent.name, "implements": implements,
            "upstream_sha256": sha256(source_agent)}


def adapt_project_template(root: Path, version: str) -> None:
    project = root / "templates/research-project-template"
    src = project / "CLAUDE.md"
    if not src.is_file():
        raise MigrationError("Project template is missing CLAUDE.md")
    # Preserve CLAUDE.md; upstream linter/sync logic may depend on it.
    guide = '''# Codex instructions for this Research Superpowers project

This project is scaffolded from the leiverkus research-superpowers template.
Read `CLAUDE.md` in full before editing project research artifacts: it is the
**authoritative research schema and methodology metadata**, even in Codex.
Never rename or delete it. In particular honor its `methodology` (`hermeneutic`,
`quantitative`, `mixed`), `discipline`, `languages` and `plugin_version` fields.

Use the installed `research-superpowers` Codex plugin and its phase skills.
Start with `using-research-powers`, then follow the governing phase skill.
The skill's original complete procedures are in its adjacent upstream-workflow.md.
Keep the design approvals, SOFT-GATE override log, source provenance, BibTeX
citekeys, page-numbered quotations, lint gates and reproducible outputs.

Do not assume Claude-specific tools or `.mcp.json` are loaded by Codex.
Optional Codex custom agents are installed separately; if absent, do the
same steps sequentially and be explicit about the difference.

Do not silently perform network downloads, modify the global research library,
or overwrite existing source pages. Show the expected changes and obey the
user's permissions and approvals. The shared library path is machine-local
and never belongs in version control.
'''
    write_text(project / "AGENTS.md", guide)
    # Project local .mcp.json is Claude-specific; don't silently translate it
    # into active Codex configuration with auto-starting commands.
    write_text(project / "CODEX_MCP_SETUP.md", '''# Optional project wiki-graph MCP in Codex

The upstream `.mcp.json` is for Claude Code; Codex does not automatically read
it. If you want the optional local wiki graph MCP, run from the project root:

    codex mcp add wiki-graph -- python3 scripts/graph_mcp.py

Review the local script and its dependencies before enabling. If your Codex
client version uses another MCP registration format, consult its current docs.
Do not add this automatically to a shared config or use it without consent.
''')


def write_hooks(root: Path) -> None:
    hooks = root / "hooks"
    original_index = hooks / "session-context.md"
    if not original_index.is_file():
        raise MigrationError("Missing upstream hook context index")
    shutil.copy2(original_index, hooks / "upstream-session-context.md")
    index_text = original_index.read_text(encoding="utf-8")
    index_text = index_text.replace(
        "load the skill via\nthe `Skill` tool before responding.",
        "invoke the appropriate Codex Skill, or read the named SKILL.md before responding.")
    index_text = index_text.replace(
        "load the skill via\nthe `Skill` tool (e.g. `Skill ingest-source`).",
        "invoke the Codex skill or read its SKILL.md (for example ingest-source).")
    index_text = index_text.replace(
        "auto-runs state-triggered at session start",
        "can run at session start only if RESEARCH_SUPERPOWERS_ENABLE_DRIFT=1")
    index_text = index_text.replace(
        "Skills\ndeclare their inputs/outputs in frontmatter (see `docs/skill-contract.md`).",
        "The complete upstream workflow and its inputs/outputs metadata are in\n"
        "the skill's adjacent upstream-workflow.md; see docs/skill-contract.md.")
    index_text += ("\nCodex bridge: Claude's Task and Todo tools are not Codex tools. "
                   "Use host-native delegation or sequential execution. "
                   "Keep CLAUDE.md for metadata and read AGENTS.md for host guidance.\n")
    write_text(original_index, index_text)
    # Only context injection is active by default. Drift checking is explicit
    # opt-in because the upstream code may write ~/.cache and library indexes.
    write_text(hooks / "codex-session-start.py", '''#!/usr/bin/env python3
"""Codex SessionStart: inject research skill index as additional context."""
import json
import os
from pathlib import Path

root = Path(os.environ.get("PLUGIN_ROOT") or os.environ.get("CLAUDE_PLUGIN_ROOT") or Path(__file__).resolve().parent.parent)
index = root / "hooks" / "session-context.md"
if index.is_file():
    # Restrict injection to research projects, unless explicitly enabled.
    cwd = Path.cwd()
    if (cwd / "knowledge").exists() or (cwd / "input").exists() or os.environ.get("RESEARCH_SUPERPOWERS_ALWAYS") == "1":
        content = index.read_text(encoding="utf-8")
        ctx = "<research-superpowers>\\n" + content + "\\n</research-superpowers>"
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx}}))
''')
    write_text(hooks / "codex-drift-check.py", '''#!/usr/bin/env python3
"""Codex SessionStart opt-in drift runner. No writes unless explicitly opted in."""
import os
import subprocess
import sys
from pathlib import Path

if os.environ.get("RESEARCH_SUPERPOWERS_ENABLE_DRIFT") == "1":
    root = Path(os.environ.get("PLUGIN_ROOT") or os.environ.get("CLAUDE_PLUGIN_ROOT") or Path(__file__).resolve().parent.parent)
    cmd = [sys.executable, str(root / "hooks" / "drift_check.py")]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=False)
        if result.returncode == 0 and result.stdout.strip():
            print(result.stdout.strip())
    except (OSError, subprocess.TimeoutExpired):
        pass
''')
    write_json(hooks / "hooks.json", {
        "description": "Research Superpowers local Codex hooks. Review and trust in Codex /hooks before enabling.",
        "hooks": {
            "SessionStart": [
                {"matcher": "startup|resume|clear|compact", "hooks": [
                    {"type": "command", "command": "python3 \"${PLUGIN_ROOT}/hooks/codex-session-start.py\"",
                     "timeout": 5, "additionalContextLimit": 3500,
                     "statusMessage": "Loading Research Superpowers workflow index"}]},
                {"matcher": "startup", "hooks": [
                    {"type": "command", "command": "python3 \"${PLUGIN_ROOT}/hooks/codex-drift-check.py\"",
                     "timeout": 125, "async": True,
                     "statusMessage": "Checking research drift (opt in)"}]}
            ]
        }
    })


def make_manifest(upstream: dict) -> dict:
    upstream_version = upstream["version"]
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": PLUGIN_NAME,
        "version": upstream_version + "-codex.1",
        "description": (
            "Codex adaptation of Patrick Leiverkus' research-superpowers: "
            "18 skills for methodology-aware and auditable scholarly research, "
            "citation-backed writing, peer review, and research wiki workflows."
        ),
        "author": {"name": "Community Codex adaptation (source: Patrick Leiverkus)"},
        "license": "MIT",
        "homepage": SOURCE_URL,
        "repository": SOURCE_URL,
        "keywords": ["research", "academic-writing", "literature-review", "peer-review", "wiki", "hermeneutics"],
        "extensions": {"com.openai": {
            "onboardingSkill": "./skills/using-research-powers/SKILL.md",
            "hooks": "./hooks/hooks.json",
            "interface": {
                "displayName": "Research Superpowers for Codex",
                "shortDescription": "Reproducible academic research from idea to publication",
                "developerName": "Community adaptation of Patrick Leiverkus (MIT)",
                "category": "Productivity", "capabilities": ["Read", "Write"],
                "websiteURL": SOURCE_URL,
                "defaultPrompt": [
                    "Help me set up an auditable research project using Research Superpowers.",
                    "Review the available research phases and select the right skill."
                ]
            }
        }}
    }


def copy_source(source: Path, dest: Path) -> None:
    for folder in ("skills", "agents", "hooks", "templates", "schema", "scripts", "docs", "examples"):
        if not (source / folder).is_dir():
            raise MigrationError(f"Required source directory is missing: {folder}")
        shutil.copytree(source / folder, dest / folder,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
                        symlinks=False)
    for name in ("LICENSE", "CHANGELOG.md", "requirements-dev.txt"):
        if (source / name).is_file():
            shutil.copy2(source / name, dest / name)
    if (source / "README.md").is_file():
        shutil.copy2(source / "README.md", dest / "UPSTREAM_README.md")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True, help="Local checkout of original GitHub repo")
    ap.add_argument("--output", type=Path, required=True, help="New marketplace directory")
    ap.add_argument("--force", action="store_true", help="Replace existing generated output")
    ns = ap.parse_args(argv)
    source, out = ns.source.expanduser().resolve(), ns.output.expanduser().resolve()
    if not (source / "skills").is_dir() or not (source / ".claude-plugin/plugin.json").is_file():
        raise MigrationError(f"Not a research-superpowers Claude plugin checkout: {source}")
    try:
        upstream = json.loads((source / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise MigrationError("Invalid original Claude manifest") from exc
    if upstream.get("name") != PLUGIN_NAME:
        raise MigrationError("Unexpected plugin identity; refusing to convert")
    if "MIT License" not in (source / "LICENSE").read_text(encoding="utf-8"):
        raise MigrationError("Source license changed; review manually first")
    skill_paths = sorted((source / "skills").glob("*/SKILL.md"))
    skill_names = {p.parent.name for p in skill_paths}
    if skill_names != EXPECTED_SKILLS:
        raise MigrationError(f"Skill inventory changed: missing={sorted(EXPECTED_SKILLS-skill_names)}, unexpected={sorted(skill_names-EXPECTED_SKILLS)}")
    agent_paths = sorted((source / "agents").glob("*.md"))
    agent_names = {p.stem for p in agent_paths}
    if agent_names != EXPECTED_AGENTS:
        raise MigrationError(f"Agent inventory changed: missing={sorted(EXPECTED_AGENTS-agent_names)}, unexpected={sorted(agent_names-EXPECTED_AGENTS)}")
    if out == source or source.is_relative_to(out) or out.is_relative_to(source):
        raise MigrationError("Source and output paths may not contain each other")
    if out.exists():
        if not ns.force:
            raise MigrationError(f"Output already exists (use --force): {out}")
        marker = out / ".agents/plugins/marketplace.json"
        try:
            marker_data = json.loads(marker.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise MigrationError("Refusing to --force replace a non-generated directory")
        if marker_data.get("name") != "leiverkus-codex-local":
            raise MigrationError("Refusing to --force replace an unrelated marketplace")
        shutil.rmtree(out)
    plugin = out / "plugins" / PLUGIN_NAME
    plugin.mkdir(parents=True)
    copy_source(source, plugin)
    skill_report = []
    for src in skill_paths:
        skill_report.append(adapt_skill(src, plugin / "skills" / src.parent.name))
    agents = []
    for agent in agent_paths:
        agents.append(adapt_agent(agent, plugin / "codex-agents"))
    adapt_project_template(plugin, upstream["version"])
    write_hooks(plugin)
    write_json(plugin / "plugin.json", make_manifest(upstream))
    write_json(plugin / ".codex-plugin" / "plugin.json", {
        "name": PLUGIN_NAME,
        "version": upstream["version"] + "-codex.1",
        "description": "Research Superpowers Codex compatibility fallback",
        "skills": "./skills/",
        "hooks": "./hooks/hooks.json"
    })
    write_json(out / ".agents" / "plugins" / "marketplace.json", {
        "name": "leiverkus-codex-local",
        "interface": {"displayName": "Research Superpowers Codex (Local)"},
        "plugins": [{"name": PLUGIN_NAME,
                     "source": {"source": "local", "path": "./plugins/research-superpowers"},
                     "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                     "category": "Productivity"}]
    })
    write_json(plugin / "migration-report.json", {
        "source": SOURCE_URL,
        "source_commit": get_git_head(source),
        "reference_commit": REFERENCE_SHA,
        "upstream_version": upstream["version"],
        "port_version": upstream["version"] + "-codex.1",
        "skill_count": len(skill_report),
        "agent_count": len(agents),
        "skills": skill_report,
        "agents": agents,
        "notes": [
            "All original skill documents were copied intact next to their Codex SKILL.md as upstream-workflow.md.",
            "Codex skill metadata normalized; original extended YAML frontmatter preserved.",
            "Original project template CLAUDE.md retained; AGENTS.md added for Codex.",
            "Codex hook runners are provided; hook trust is required and drift is opt-in.",
            "Optional MCP not auto-enabled; custom agents must be installed separately.",
            "Live Codex execution and remote MCP functionality not verified by this converter."
        ]
    })
    write_text(plugin / "README_CODEX.md", code_readme())
    print(f"Converted upstream v{upstream['version']} to {plugin}")
    print(f"Verified inventory: {len(skill_report)} skills and {len(agents)} agent definitions")
    print("Local Codex marketplace:", out)
    return 0


def get_git_head(source: Path) -> str | None:
    import subprocess
    try:
        r = subprocess.run(["git", "-C", str(source), "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=5)
        return r.stdout.strip() if r.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def code_readme() -> str:
    return '''# Research Superpowers for Codex (community port)

**Upstream:** https://github.com/leiverkus/research-superpowers
**License:** MIT, Copyright (c) 2026 Patrick Leiverkus.

This conversion preserves all 18 original skill workflows (verbatim in each
skill's `upstream-workflow.md`), the 7 agent documents, research
project template, citation/wiki scripts, schema, and documentation. Codex-native
`SKILL.md` entrypoints add a host-compatibility layer.

## Enable as a local Codex plugin

From the enclosing MARKETPLACE directory (the directory containing
`.agents/plugins/marketplace.json`), run:

    codex plugin marketplace add /absolute/path/to/marketplace
    codex plugin marketplace list

Open the Codex / ChatGPT desktop Plugins Directory and install the
`research-superpowers` entry from `leiverkus-codex-local`. Refresh or restart
if the source is not visible. A marketplace *registration* is not installation.

You can alternatively copy individual `skills/<name>/` directories into
`~/.agents/skills/` and use them as standalone Codex Skills (no plugin hooks).
Beware name conflicts with existing skills.

## Enable the optional 7 custom Codex subagents

The `codex-agents/rsp-*.toml` files are generated but not installed by a
plugin manifest. Manually copy the desired ones into `~/.codex/agents/` or a
trusted project's `.codex/agents/` directory. Keep the `rsp-` prefix.
Subagents inherit the current session permissions, and original Claude
`disallowedTools` is NOT a Codex authorization boundary.

## Hooks and drift check

The plugin bundles `hooks/hooks.json` for SessionStart. Codex requires you to
review/trust hook definitions (CLI: `/hooks`). The session index loads only
inside research projects with `knowledge/` or `input/`, or when you set
`RESEARCH_SUPERPOWERS_ALWAYS=1`.

The drift check is **off by default**, since the upstream check writes a
state/cache and may update an existing derived search index. Opt in using
`RESEARCH_SUPERPOWERS_ENABLE_DRIFT=1` and review the upstream code first.

## Projects and MCPs

The original `templates/research-project-template/CLAUDE.md` is preserved as
the methodology metadata source of truth. A Codex `AGENTS.md` is also created.
`templates/research-project-template/CODEX_MCP_SETUP.md` describes optional
wiki graph server setup. No MCP is launched automatically. The optional
`dao-paper-search-mcp` remains an opt-in external dependency.

## Scope and limits

This is a conversion of host glue, NOT a claim that the original workflows
have been functionally validated on a running Codex installation. Verify
routing, scripts, agent dispatch, hooks, citations and SOFT-GATE logs on an
actual sample project before research production use.
'''


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MigrationError as error:
        print("ERROR:", error, file=sys.stderr)
        raise SystemExit(2)
