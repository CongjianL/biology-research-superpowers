# Provenance and adaptations

- Source inspiration: `leiverkus/research-superpowers`, commit `da0effdf162cd96a42009fe2dfe701b352e50ba8`, upstream manifest `0.47.0` at inspection 2026-11-16.
- Source layout: 18 workflow Skills, 7 Claude subagents, research project template, knowledge wiki, SOFT-GATE and state-triggered drift ideas. In the standalone biology package the **conceptual architecture** is adapted, **not all original text or scripts included**.
- Adaptation: 18 original skill names retained for phase continuity; 11 biology scientific method skills; 8 optional Codex agents; new project template; new standalone audit tools.
- Former core fields `methodology=hermeneutic/mixed` are not silently interpreted as biology; project defaults to a draft quantitative study and requires scientist edits. Actual mixed studies can be specified explicitly in PROJECT.md.
- User-side upgrade path: run the prior exact-source converter and then the overlay script to preserve verbatim original workflows and scripts in parallel without giving them precedence over biology instructions.
- Scientific gate types: SOFT-GATE = approval/recorded deviation, HARD-STOP = missing source/rights/safety/fabrication. Neither is an actual Codex authorization mechanism.
- The plugin does not provide live scholarly data access or guaranteed multi-agent isolation on its own. It does not include lab protocols, access tokens, credentials or privileged remote actions.
