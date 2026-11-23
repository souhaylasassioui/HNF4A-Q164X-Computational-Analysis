# Software Environment

## Overview

This document records software versions observed on the
HPC system during repository documentation in November 2026.

These versions are not necessarily identical to those
used during the original Master's research analyses.

## Conda Environments

### Base environment

- Python: 3.13.13

### nfcore environment

- Python: 3.14.4
- Nextflow: 26.04.0

The nf-core/rnaseq workflow uses additional analysis
tools, including STAR, featureCounts, and DESeq2.

Their exact versions from the original workflow
remain to be verified from pipeline execution records.

### mdplot environment

- Python: 3.11.15
- Matplotlib: 3.10.9
- NumPy: 2.4.4

GROMACS was not available on PATH in this environment
during the inspection.

The original GROMACS version remains to be verified.

## Other Scientific Software

The project also involved:

- nf-core/rnaseq
- DESeq2
- AlphaGenome
- AlphaFold2 / ColabFold
- GROMACS

Exact historical versions and runtime dependencies
require further verification.

## Reproducibility Notes

The HPC setup uses Conda environments and
SLURM-based job submission.

The repository does not yet provide complete
environment specification files or an end-to-end
reproducible workflow.

No original experimental data or unpublished
manuscript-related results are included.
