# Independent multi-agent scientific review

A delegation must name one bounded input set, expected output paths, scientific question, acceptance gates, allowed tools and deadline/budget if relevant. Each reviewer returns exactly what was checked, commands/tests run, artifacts inspected, caveats and verdict.

Agent roles in `codex-agents/`: `bio-literature-scout`, `bio-source-curator`, `bio-evolution-analyst`, `bio-statistician`, `bio-simulation-auditor`, `bio-manuscript-drafter`, `bio-adversarial-reviewer`, `bio-reproducibility-auditor`.

- For reproducible scientific review, independent reviewers should start from raw inputs or a frozen manifest when practical, not a paraphrase of the implementer's result.
- Separate implementer and reviewer contexts for load-bearing numerical results. A different model in the same code path is not an independent algorithmic oracle.
- Never run two agents that write the same files concurrently; give each agent isolated output paths/worktrees and merge after review.
- If Codex agents are not configured, perform sequential checks and report that independence was limited. Do not pretend agent names are automatically registered just because TOML files exist.
- Only human approval can decide a SOFT-GATE bypass; an agent cannot bypass tool permissions or biosafety controls.
