#!/usr/bin/env python3
"""Offline structure/provenance verifier for a converted Codex marketplace."""
from __future__ import annotations
import argparse
import hashlib
import json
import sys
import tomllib
from pathlib import Path


def verify(marketplace: Path) -> None:
    cat = marketplace / ".agents/plugins/marketplace.json"
    config = json.loads(cat.read_text(encoding="utf-8"))
    if config["name"] != "leiverkus-codex-local":
        raise ValueError("Unexpected marketplace identity")
    entry = config["plugins"][0]
    assert entry["source"]["path"] == "./plugins/research-superpowers"
    root = marketplace / "plugins/research-superpowers"
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    report = json.loads((root / "migration-report.json").read_text(encoding="utf-8"))
    assert manifest["name"] == "research-superpowers"
    assert manifest["$schema"].startswith("https://agent-plugins.org/")
    assert manifest["extensions"]["com.openai"]["hooks"] == "./hooks/hooks.json"
    assert len(report["skills"]) == 18
    assert len(report["agents"]) == 7
    for skill in report["skills"]:
        folder = root / "skills" / skill["name"]
        native = (folder / "SKILL.md").read_text(encoding="utf-8")
        assert native.startswith("---\nname: " + skill["name"] + "\n")
        assert "\ndescription: " in native.split("\n---\n", 1)[0]
        source_ref = folder / "upstream-workflow.md"
        assert hashlib.sha256(source_ref.read_bytes()).hexdigest() == skill["upstream_sha256"]
        assert native.count("upstream-workflow.md") >= 1
    for agent in report["agents"]:
        path = root / "codex-agents" / (agent["name"] + ".toml")
        record = tomllib.loads(path.read_text(encoding="utf-8"))
        assert record["name"] == agent["name"]
        assert record["developer_instructions"]
    assert (root / "templates/research-project-template/CLAUDE.md").exists()
    assert (root / "templates/research-project-template/AGENTS.md").exists()
    hook = json.loads((root / "hooks/hooks.json").read_text(encoding="utf-8"))
    assert len(hook["hooks"]["SessionStart"]) == 2
    for fn in ["codex-session-start.py", "codex-drift-check.py"]:
        assert (root / "hooks" / fn).is_file()
    assert (root / "LICENSE").is_file()
    print("PASS: 18 original skill bodies preserved, 7 TOML agents parse, "
          "manifest/marketplace/hooks/template verified")
    print("Source SHA:", report["source_commit"] or "not available from fixture")
    print("Plugin:", root)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marketplace", type=Path, required=True)
    args = parser.parse_args()
    try:
        verify(args.marketplace.resolve())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
