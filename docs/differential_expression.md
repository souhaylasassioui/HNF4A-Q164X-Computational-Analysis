# Differential Expression Analysis

## Experimental Design
- Organism: Mus musculus
- Tissue: Liver
- Comparison: HNF4A Q164X heterozygous vs wild-type
- Biological replicates: 3 per condition

## DEG Filtering
- Adjusted p-value < 0.05
- Absolute log2 fold change > 1
- Total genes: 16,897
- Significant DEGs: 203

## Reproducibility
Run scripts/differential_expression/filter_degs.py to reproduce the filtering.

## Interpretation
The original DESeq2 contrast direction should be verified.

## Contrast Direction and Provenance

The available DESeq2 results table contains 16,897 genes.

Filtering with adjusted p-value < 0.05 and absolute
log2 fold change > 1 identifies 203 significant DEGs.

The original differential expression script and its
contrast definition have not been recovered.

The nf-core DESeq2 quality-control dataset uses
a design of ~1, without a group comparison.

Therefore, the direction of positive and negative
log2 fold changes remains unverified.

Condition-specific upregulation and downregulation
should not be inferred until the original contrast
has been established.
