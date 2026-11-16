# Scientific qualification of evolutionary simulators

## Distinct gates (do not merge)
1. **Contract**: sample space, instantaneous rates, parameterization, tree/time units, indel, duplication, loss, HGT, functional regime transition rules and observation/truth labels.
2. **Deterministic correctness**: independently implemented exact small-state oracle and invariants, property tests, perturbation and finite-precision boundaries.
3. **Random-model correctness**: independent CDF/inverse transforms or probability calculations for substitution/hazards, acceptance-rejection and compound event sampling. Distinguish unit uniform PRNG validation from actual transition law.
4. **Mixing and calibration**: initial condition, burn-in, ESS, autocorrelation, replicate chains, null behavior, reference mixing-time certification; report when reference not credible.
5. **Joint process**: compare interactions among substitution, indel, duplication/loss/transfer and shifted functional constraints. E01–E04-style joint cases should have known invariants and adversarial edge cases.
6. **Replay compatibility**: seed stream, event ledger, cold resume, output format, stable identity and backward compatibility are separate from statistical validity.
7. **Power/scale**: lock coordinates, tests, effect sizes, replicates, resource budget; run independent large-scale job, record exit codes, inputs and full uncertainty.

## What a qualification report needs
- Candidate commit SHA, frozen reference, exact test seeds, software/toolchain versions, scope of independent oracle, all tested parameter strata.
- Numerical error summaries (absolute, relative, tail log-probability, finite-precision expectations) and scientific impact.
- Monte Carlo counts, confidence intervals, nominal null rate, achieved power, failed cases, reason codes and untested coordinates.
- Workload timing/memory measured under same conditions, with separation of coordinator/process/file system artifacts.
- Exact conclusion PASS, FAIL, INCOMPLETE, or PASS_WITH_LIMITATION; no default PASS on missing evidence.
