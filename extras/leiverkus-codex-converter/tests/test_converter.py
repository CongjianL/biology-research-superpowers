import json
import os
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import migrate  # noqa: E402
import verify  # noqa: E402


class TestConversion(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.work = Path(self.tmp.name)
        self.source = self.work / "source"
        self.source.mkdir()
        self.output = self.work / "marketplace"
        (self.source / ".claude-plugin").mkdir()
        (self.source / ".claude-plugin/plugin.json").write_text(
            json.dumps({"name": "research-superpowers", "version": "0.47.0"}))
        (self.source / "LICENSE").write_text("MIT License\n\nCopyright 2026 Upstream\n")
        (self.source / "README.md").write_text("Original project\n")
        for folder in ("skills", "agents", "hooks", "templates", "schema", "scripts", "docs", "examples"):
            (self.source / folder).mkdir(exist_ok=True)
        for name in migrate.EXPECTED_SKILLS:
            p = self.source / "skills" / name
            p.mkdir()
            (p / "SKILL.md").write_text(
                "---\nname: " + name + "\ndescription: Use for " + name + " research work.\n"
                "inputs:\n  - name: source\n    required: true\n---\n"
                "# Upstream \nExact words, including \\u1234 and quotes.\n")
        for name in migrate.EXPECTED_AGENTS:
            p = self.source / "agents" / (name + ".md")
            p.write_text("---\nname: " + name + "\ndescription: Worker " + name +
                         "\nimplements: executing-research-plan\n---\n"
                         "Agent instruction with quotes and \"\"\" triple double quotes.\n")
        (self.source / "hooks/session-context.md").write_text("18 skills for research.\n")
        (self.source / "hooks/drift_check.py").write_text("print('dummy drift')\n")
        p = self.source / "templates/research-project-template"
        p.mkdir()
        (p / "CLAUDE.md").write_text("---\nmethodology: mixed\n---\nRules.\n")

    def convert(self):
        status = migrate.main(["--source", str(self.source), "--output", str(self.output)])
        self.assertEqual(status, 0)

    def test_full_inventory_and_provenance(self):
        self.convert()
        verify.verify(self.output)
        root = self.output / "plugins/research-superpowers"
        report = json.loads((root / "migration-report.json").read_text())
        self.assertEqual(report["skill_count"], 18)
        self.assertEqual(report["agent_count"], 7)
        self.assertTrue((root / "templates/research-project-template/AGENTS.md").is_file())
        self.assertTrue((root / "templates/research-project-template/CLAUDE.md").is_file())
        upstream = (root / "skills/ingest-source/upstream-workflow.md").read_text()
        self.assertIn("inputs:\n", upstream)
        self.assertIn("Exact words", upstream)
        native = (root / "skills/ingest-source/SKILL.md").read_text()
        self.assertIn("Codex execution contract", native)
        self.assertNotIn("inputs:\n", native)
        toml = tomllib.loads((root / "codex-agents/rsp-analyst.toml").read_text())
        self.assertEqual(toml["name"], "rsp-analyst")
        self.assertIn('"""', toml["developer_instructions"])

    def test_hook_when_research_project(self):
        self.convert()
        root = self.output / "plugins/research-superpowers"
        outside = self.work / "outside"
        outside.mkdir()
        env = dict(os.environ, PLUGIN_ROOT=str(root))
        cmd = [sys.executable, str(root / "hooks/codex-session-start.py")]
        result = subprocess.run(cmd, cwd=outside, env=env, text=True, capture_output=True)
        self.assertEqual(result.stdout, "")
        (outside / "input").mkdir()
        result = subprocess.run(cmd, cwd=outside, env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        context = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(context["hookEventName"], "SessionStart")
        self.assertIn("18 skills", context["additionalContext"])
        drift = [sys.executable, str(root / "hooks/codex-drift-check.py")]
        result = subprocess.run(drift, cwd=outside, env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_rejects_inventory_change(self):
        (self.source / "skills/wiki-lint/SKILL.md").unlink()
        with self.assertRaises(migrate.MigrationError):
            migrate.main(["--source", str(self.source), "--output", str(self.output)])

    def test_refuses_unmarked_force_replace(self):
        self.output.mkdir()
        (self.output / "important.txt").write_text("Do not remove")
        with self.assertRaises(migrate.MigrationError):
            migrate.main(["--source", str(self.source), "--output", str(self.output), "--force"])
        self.assertTrue((self.output / "important.txt").exists())

    def test_rebuild_only_generated_output(self):
        self.convert()
        status = migrate.main(["--source", str(self.source), "--output", str(self.output), "--force"])
        self.assertEqual(status, 0)
        verify.verify(self.output)


if __name__ == "__main__":
    unittest.main()
