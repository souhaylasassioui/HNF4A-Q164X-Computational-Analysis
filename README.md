# HNF4A Q164X: Integrative Computational Analysis

## Project Overview

This project investigates the molecular consequences of the
heterozygous HNF4A Q164X truncating variant in mouse liver.

The study integrates transcriptomics, functional enrichment,
regulatory genomics and structural bioinformatics.

## Research Objectives

1. Characterize transcriptional changes associated with HNF4A Q164X.
2. Identify differentially expressed genes and affected pathways.
3. Investigate potential regulatory consequences.
4. Compare wild-type and mutant protein structures.

## Experimental Design

- Organism: Mus musculus
- Tissue: Liver
- Conditions: HNF4A Q164X heterozygous vs wild-type
- Biological replicates: 3 per condition
- Sequencing: Paired-end RNA-seq (150 bp)

## Computational Methods

### RNA-seq and Differential Expression
- nf-core/rnaseq
- STAR
- featureCounts
- DESeq2

### Functional Analysis
- Gene Ontology
- KEGG pathway enrichment

### Regulatory Genomics
- AlphaGenome predictions

### Structural Bioinformatics
- AlphaFold2 / ColabFold
- Protein structure comparison
- Preliminary molecular dynamics investigation

## Main Findings

- 203 DEGs reported using the nf-core-based workflow
- 207 DEGs reported using the independent workflow
- 163 differentially expressed genes shared between analyses
- Alterations in metabolic and inflammatory pathways
- Structural differences predicted between WT and Q164X HNF4A

These findings are computational and require appropriate
experimental validation.

## Repository Organization

- scripts/: Analysis scripts and workflows
- results/: Selected, shareable analysis outputs
- figures/: Scientific visualizations
- docs/: Methodology and supplementary documentation
- environment/: Software dependencies and versions

## Author

Souhayla Sassioui
Master's in Genomics and Bioinformatics
Mohammed V University, Rabat, Morocco

## Status

Completed Master's research project (2026).
Repository documentation and code curation in progress.
