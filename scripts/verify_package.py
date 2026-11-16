#!/usr/bin/env python3
"""Dependency-free structural verification for the Codex biology plugin."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    tomllib = None

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / 'plugins' / 'biology-research-superpowers'


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    assert (ROOT / '.agents/plugins/marketplace.json').is_file()
    marketplace = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    plugin = json.loads((PLUGIN / 'plugin.json').read_text())
    compat = json.loads((PLUGIN / '.codex-plugin/plugin.json').read_text())
    assert plugin['name'] == compat['name'] == 'biology-research-superpowers'
    assert plugin['version'] == compat['version']
    assert marketplace['plugins'][0]['name'] == plugin['name']
    assert len(list((PLUGIN / 'skills').glob('*/SKILL.md'))) == 29
    assert len(list((PLUGIN / 'codex-agents').glob('*.toml'))) == 8
    assert (PLUGIN / 'templates/biology-project/AGENTS.md').is_file()
    assert (PLUGIN / 'SOURCE_AND_SCOPE.md').is_file()
    assert (ROOT / 'LICENSE').is_file()
    for skill in (PLUGIN / 'skills').glob('*/SKILL.md'):
        content = skill.read_text()
        assert content.startswith('---\n'), skill
        assert re.search(r'\nname:\s*[\w-]+\s*\n', content), skill
        assert 'description:' in content.split('---', 2)[1], skill
        name = re.search(r'\nname:\s*([\w-]+)\s*\n', content).group(1)
        assert name == skill.parent.name, skill
    if tomllib:
        for agent in (PLUGIN / 'codex-agents').glob('*.toml'):
            with agent.open('rb') as f:
                assert isinstance(tomllib.load(f), dict), agent
    for s in (PLUGIN / 'scripts').glob('*.py'):
        compile(s.read_text(), str(s), 'exec')
    print('PASS: manifests, 29 skills, 8 agents, template, scripts and license')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (AssertionError, ValueError, OSError) as e:
        print(f'FAIL: {e}', file=sys.stderr)
        sys.exit(1)
