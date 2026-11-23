# HNF4A Q164X: Integrative Computational Analysis of Mouse Liver Transcriptomics

**RNA-seq | Differential Expression | Regulatory Genomics | Structural Bioinformatics**

## Project Overview

This repository contains computational analysis scripts and documentation developed during my Master's research project in Genomics and Bioinformatics at Mohammed V University, Rabat, Morocco.

The project investigates the molecular consequences of the heterozygous **HNF4A Q164X truncating variant** in mouse liver through an integrative computational approach combining transcriptomics, functional enrichment, regulatory genomics, protein structure prediction, and preliminary molecular dynamics analysis.

HNF4A is a transcription factor involved in regulating hepatic gene expression and metabolic functions. Investigating the effects of its truncation can provide insights into changes in transcriptional regulation and liver-associated biological pathways.

## Research Objectives

1. Characterize gene expression changes associated with the HNF4A Q164X variant.
2. Identify differentially expressed genes and affected biological pathways.
3. Explore potential regulatory consequences using genomic prediction tools.
4. Compare predicted wild-type and truncated HNF4A protein structures.
5. Integrate transcriptomic, regulatory, and structural findings.

## Experimental Design

| Parameter | Description |
|---|---|
| Organism | *Mus musculus* |
| Tissue | Liver |
| Experimental condition | HNF4A Q164X heterozygous |
| Control | Wild-type |
| Biological replicates | 3 per condition |
| Sequencing | Paired-end RNA-seq, 150 bp |
| Reference genome | GRCm39 |
| Gene annotation | GENCODE mouse M33 |

## Computational Workflow

### 1. RNA-seq Processing

The RNA-seq analysis used nf-core/rnaseq, with STAR and featureCounts among the principal processing tools.

The repository includes a mouse-specific SLURM submission script for the nf-core workflow.

### 2. Differential Expression Analysis

Differential expression results were evaluated using DESeq2.

The filtering criteria were:

- Adjusted p-value below 0.05
- Absolute log2 fold change greater than 1

Applying these criteria to the available nf-core DESeq2 results identified **203 differentially expressed genes**.

The filtering procedure is provided in `scripts/differential_expression/filter_degs.py`.

The Master's analysis also reported 207 DEGs from an independent workflow, with 163 genes shared between workflows. These additional counts have not yet been independently reproduced in this repository.

### 3. Functional Enrichment Analysis

Gene Ontology and KEGG pathway analyses were used to investigate biological functions associated with transcriptional changes.

The Master's analysis highlighted changes involving:

- Bile acid and lipid metabolism
- Amino acid metabolism
- Inflammatory responses
- Cell-cycle-associated processes

The corresponding enrichment workflow and results require further documentation before they can be reproduced directly from this repository.

### 4. Regulatory Genomics

AlphaGenome-based analyses explored predicted regulatory signals associated with selected candidate genes.

The repository includes scripts for:

- Preparing candidate genomic coordinates
- Constructing regulatory prediction inputs
- Running mouse genomic predictions
- Processing liver-associated regulatory signals
- Statistical summaries
- Generating regulatory analysis figures

The interpretation of these predictions remains computational and requires appropriate experimental validation.

### 5. Structural Bioinformatics

Predicted wild-type and Q164X HNF4A protein structures were investigated using AlphaFold2/ColabFold-based modeling and structural comparisons.

Preliminary molecular dynamics analyses were also explored using GROMACS.

The repository includes selected simulation parameter files and plotting scripts. These should be considered exploratory rather than a validated, complete molecular dynamics workflow.

## Repository Structure

```text
HNF4A-Q164X-Computational-Analysis/
├── README.md
├── .gitignore
├── docs/
│   └── differential_expression.md
└── scripts/
    ├── differential_expression/
    │   └── filter_degs.py
    ├── rnaseq/
    │   └── run_rnaseq_mouse.slurm
    ├── regulatory_analysis/
    │   └── AlphaGenome analysis scripts
    └── structural_analysis/
        ├── WT/
        └── Q164X/
```

## Reproducibility

This repository currently provides selected analysis scripts and documentation. It is not yet a fully executable end-to-end pipeline.

Reproducing the complete analysis requires access to suitable input data, software dependencies, appropriate computing resources, and additional workflow documentation.

Raw sequencing data, unpublished DEG tables, and manuscript-related figures are not included in the Git history.

## Scientific Limitations

- Transcriptomic associations do not independently establish direct causal regulatory mechanisms.
- AlphaGenome regulatory outputs represent computational predictions.
- Predicted protein structures require appropriate experimental interpretation.
- The molecular dynamics work is preliminary.
- Additional experimental validation is required to establish the biological consequences of HNF4A Q164X.

## Author

**Souhayla Sassioui**

Master's in Genomics and Bioinformatics  
Mohammed V University — Faculty of Sciences, Rabat, Morocco

Research interests: Computational Genomics, Transcriptomics, Regulatory Genomics, Bioinformatics, and Genome Biology.

## Acknowledgments

Master's research conducted under the supervision of **Prof. Hiroaki Taniguchi** and **Prof. Bouabid Badaoui**.

## Project Status

**Master's research completed in 2026.**

Code curation, reproducibility documentation, and preparation of shareable research outputs are ongoing.
