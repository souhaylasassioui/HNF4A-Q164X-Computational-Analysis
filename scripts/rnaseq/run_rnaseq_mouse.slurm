#!/bin/bash
#SBATCH --job-name=rnaseq_mouse
#SBATCH --output=rnaseq_mouse_%j.out
#SBATCH --error=rnaseq_mouse_%j.err
#SBATCH --cpus-per-task=12
#SBATCH --mem=80G
#SBATCH --time=12:00:00

source ~/.bashrc
conda activate nfcore

cd "${PROJECT_DIR:?Set PROJECT_DIR to your RNA-seq working directory}"

nextflow run nf-core/rnaseq \
  --input samplesheet.csv \
  --outdir rnaseq_results_mouse \
  --fasta "https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M33/GRCm39.primary_assembly.genome.fa.gz" \
  --gtf "https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M33/gencode.vM33.primary_assembly.annotation.gtf.gz" \
  --featurecounts_group_type gene_type \
  -profile singularity \
  -resume
