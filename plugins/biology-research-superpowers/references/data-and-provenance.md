# Biological data provenance and reproducibility

## Data identity
- Record dataset name, source URL, DOI/PMID or accession with version, archive and retrieval timestamp, checksum, taxon/strain, collection provenance, rights and known embargo.
- Distinguish BioProject (study), BioSample (sample), SRA run (sequencing record), assembly (genome), Gene/Protein accession (specific sequence). Keep explicit mapping tables.
- For structural records capture PDB/EMDB/AlphaFold model ID, chain, version, residue coverage and uncertainty. For UniProt record accession and entry version where available.

## Layout
- `input/data/` stores immutable original inputs. Derived data live at `output/data-analysis/`.
- `input/metadata/datasets.tsv` and `input/metadata/samples.tsv` are curated registers, not verification by themselves.
- Use `scripts/record_inputs.py` to write SHA256 hashes and record exact data revisions; never silently replace files after preregistration.
- For HPC retain job ID, resources, environment, exact commit/conda/container lock, command, exit status and output checksum.

## Archive suggestions (verify each site's current requirement)
- Reads: NCBI SRA / ENA / DDBJ; genomes: GenBank/ENA/DDBJ; expression: GEO/ArrayExpress; proteomics: PRIDE; structures: PDB/EMDB; code/results: Zenodo/OSF/appropriate institutional repository.
- For clinical/human or restricted biodiversity data, consult permission/consent and access restrictions first.
- FAIR principles: findable, accessible under correct terms, interoperable, reusable, with persistent metadata.
