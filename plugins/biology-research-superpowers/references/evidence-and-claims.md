# Scientific evidence, citations, and claim boundaries

## Claim tiers (use as explicit labels)
1. **Observation**: directly measured from a stated biological unit, instrument or primary raw data; controls and error sources disclosed.
2. **Reanalysis**: reproducible computation on real data, with code, versions and sample IDs.
3. **Model-supported inference**: a conclusion conditional on phylogeny, evolutionary model, simulation assumptions, data filters or statistical criteria.
4. **Computational prediction**: prospective hypothesis without independent biological validation.
5. **Mechanism supported experimentally**: causal model discriminated by relevant controls and perturbation/readout, with caveats.
6. **Organism/ecology adaptation**: stress-fitness or ecological adaptive benefit requires organism-level evidence (and historical inference if claiming evolutionary adaptation).

These form kinds of evidence, NOT an automatic linear ladder; a prediction never silently becomes observed fact.

## Mandatory evidence fields
- Assertion and claim ID, source ID(s) (DOI/PMID/Accession), figure/table/page or dataset path, study type, organism/strain, biological unit, test/assay or model, version, uncertainty and known limitations.
- Record whether cited work was **read in full**, abstract-only, or metadata-only. Do not quote inaccessible text.
- Distinguish reviewed paper vs preprint, model prediction vs wet-lab test, homolog vs ortholog, protein activity vs cellular phenotype.
- If original full text/data are missing, label the claim `unverified` or `hypothesis` and identify the gap rather than filling it from memory.

## claims.tsv schema
`claim_id	claim_text	evidence_type	evidence_path	source_id	confidence	status`
Permitted status: hypothesis, computational_prediction, experimental_observation, model_inference, validated, inconclusive, unsupported, withdrawn.
Confidence is a qualitative assessment with source context, **not** a numeric posterior unless calibrated.

## Specific no-overclaim checks
- H+/Na+/Cl- transport assays establish molecular activity in the tested condition, not stress-response mechanism in a native host or desert fitness.
- Positive selection statistics are model-based evidence for heterogeneity in substitution patterns, not a direct proof of adaptation to a named environmental variable.
- Gene-tree/species-tree discordance supports a family of explanations: HGT, duplication/loss, ILS, recombination, model violation or sampling; do not decree HGT without discrimination.
- Conserved motif/structure suggests a mechanism but cannot alone establish ion selectivity or photochemical performance.
