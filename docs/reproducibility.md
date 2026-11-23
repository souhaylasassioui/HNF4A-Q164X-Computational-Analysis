# Reproducibility Guide

## Research Project
HNF4A Q164X computational analysis of mouse liver.

## Experimental Design
- Organism: Mus musculus
- Tissue: Liver
- Samples: 6 (3 heterozygous, 3 wild-type)
- Sequencing: Paired-end 150 bp
- Reference genome: GRCm39
- Annotation: GENCODE mouse M33

## RNA-seq Analysis
The RNA-seq workflow used nf-core/rnaseq with Nextflow.

Processing tools included:
- STAR
- featureCounts
- DESeq2

SLURM script:
scripts/rnaseq/run_rnaseq_mouse.slurm

## Differential Expression
Filtering criteria:
- Adjusted p-value < 0.05
- Absolute log2 fold change > 1

The verified nf-core results identified 203 DEGs.

Filtering script:
scripts/differential_expression/filter_degs.py

## Regulatory Genomics
AlphaGenome was used for regulatory predictions.

Scripts:
scripts/regulatory_analysis/

API credentials are not included in this repository.

## Structural Bioinformatics
Protein structure prediction involved AlphaFold2/ColabFold.

Preliminary molecular dynamics work used GROMACS.

Scripts:
scripts/structural_analysis/

## Reproducibility Limitations
This repository provides selected scripts rather than
a complete executable analysis pipeline.

Raw sequencing data and unpublished research outputs
are excluded.

Exact software versions and complete execution
instructions are not yet documented.
