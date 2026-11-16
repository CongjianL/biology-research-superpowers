# Study design and quantitative inference

## Design
- Unit of inference must match sampling design (e.g. genome, biological isolate, replicate culture, individual, clade); technical replicates improve measurement precision but do not increase n of independent organisms.
- Pre-specify primary estimand, effect size, interval method, sample-size/power target, null model, random seeds and stopping rule before outcome-driven model selection.
- Distinguish exploratory and confirmatory claims. Record amendments and alternative tested hypotheses.
- Randomization, blocking, blinding, negative/positive controls and calibration are selected where applicable.

## Analysis
- Verify distributional assumptions (independence, normalization, autocorrelation, heteroscedasticity, censoring, repeated measures).
- Handle missingness, contamination, batch effects and compositionality (microbiome count data are often compositional).
- Present uncertainty (confidence/credible intervals or bootstrap variability), multiple testing method (FDR or FWER when relevant), and sensitivity to alternative preprocessing.
- For hierarchical/evolutionary data, consider phylogenetic non-independence and species/strain pseudoreplication.
- Give empirical p-value resolution when using permutation or empirical reference sets: a finite set of B controls limits attainable tail probability to at least 1/(B+1) with the plus-one rule.

## Power and simulation calibration
- Separate null Type I error calibration from power under declared alternative effect sizes.
- Lock effect sizes and analysis rules before production-scale power evaluation. Report numerator/denominator, CI and thresholds.
- Never turn an underpowered negative result into absence of effect.
