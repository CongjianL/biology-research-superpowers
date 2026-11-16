# Conversion kit test report

Tested: 2026-11-16

## Source inspection (via GitHub repository connector)

- Source: `leiverkus/research-superpowers`
- Commit: `da0effdf162cd96a42009fe2dfe701b352e50ba8`
- Original manifest: version `0.47.0`, MIT
- Repository tree: 340 entries, 18 `skills/*/SKILL.md`, 7 `agents/*.md`
- Original structure includes Claude SessionStart hooks, state-triggered drift check, project templates, wiki schema and scripts.

## Offline tests

Run `python3 -m unittest discover -s tests -v` in the converter folder.

Five tests passed using a representative synthetic checkout with the same expected skill and agent inventory:

1. Creates and validates Codex plugin manifest, local marketplace, 18 normalized skill entrypoints and verbatim original-workflow hashes.
2. Generates 7 syntactically valid Codex custom agent TOML files and preserves original agent instructions.
3. SessionStart hook sends Codex-compatible JSON only when a research project exists; drift hook is inactive by default.
4. Refuses unknown skill inventories (upstream release drift).
5. Refuses deleting an unrelated output path, but supports rebuilding a previously-generated marketplace.

## Not tested

- Actual upstream clone and full source tree build in this environment (outbound GitHub clone unavailable in this container).
- End-to-end Codex CLI or Codex Desktop plugin installation and activation (Codex binary not present here).
- On-host subagent execution, hook trust confirmation, real PDFs, wiki linting, Quarto rendering, network scholarly data or optional MCP authentication.

Therefore this is a **source-preserving conversion toolkit**, not a pre-bundled full upstream plugin and not certified runtime parity.
