# Example 2 — Multi-factor protein family evolution simulator (illustrative)

**Question:** Can the simulator reproduce declared target distributions and scientifically valid ground truth under substitution, indels, gene duplication/loss/HGT and functional-constraint changes?

| Qualification gate | Independent evidence |
|---|---|
| Model contract | Exact event rates/probabilities, tree/time unit, truth ontology, parameter matrix |
| Deterministic scoring | Tiny enumeration independent oracle; precision extremes; known invariants |
| Sampling law | Alternative CDF/inverse transform, independent acceptance test and confidence bounds |
| Reference mixing | Chain diagnostics, ESS, convergence across starts, explicit failure modes |
| Joint events | Combined histories with known event ordering/annotations; replay/restart equivalence |
| Power | Locked effect size, null calibration, multiple testing and specified 80% target (if adopted) |
| Scale/HPC | Frozen candidate SHA, exact Slurm job receipts, results hash, CPU/RSS/time report |

**Acceptance:** keep correctness, statistical calibration, scientific identifiability, compatibility and performance as *separate* gates. Passing CI is not passing qualification. On insufficient evidence, verdict `INCOMPLETE` rather than `PASS`.

Suggested skills: `evolutionary-simulation-validation`, `writing-research-plan`, `reproducible-computation`, `requesting-peer-review`.
