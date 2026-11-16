# Genomics and phylogeny review checks

## Dataset and taxonomy
- Preserve accession.version, assembly generation/annotation versions, strain/organism names and orthology definitions. Distinguish complete chromosome/plasmid vs MAGs or fragmented assemblies.
- Report genome completeness, contamination, taxon sampling, outgroups, exclusion criteria and environmental metadata accuracy.

## Phylogenetic analysis
- Gene trees and species trees answer different questions; inspect paralogy, HGT, duplication/loss, recombination and gene-tree estimation error.
- MSA reliability must be measured or diagnosed; indel-proximal regions, low-complexity and composition can bias inference. Removing columns is a modeling choice requiring sensitivity checks.
- Save original and trimmed MSAs, selected substitutions model, tree-search settings/seeds, branch support, topology test hypotheses and software versions.
- Use reconciliation tools as model-specific evidence. A transfer count is not a literal count of witnessed transfers.
- Ancestral reconstructions need uncertainty, rooting, residue numbering, and explicit conditional status if topology gate fails.

## Reproducibility receipts
- Alignment/taxa checksums; ordered sequence IDs; tool versions (MAFFT, IQ-TREE, GeneRax, etc where used); code commit; job receipts and independent benchmark checks.
- No default scientific preference is implied by a tool's availability. Choose models appropriate to the data and test adequacy.
