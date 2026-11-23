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
