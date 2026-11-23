import os
import pandas as pd
import numpy as np

from alphagenome.models import dna_client
from alphagenome.models import dna_model
from alphagenome.models import dna_output
from alphagenome.data import genome

api_key = os.environ.get("ALPHA_GENOME_API_KEY")
if not api_key:
    raise ValueError("ALPHA_GENOME_API_KEY is not set")

regions = pd.read_csv("data/alpha10_mouse_gene_regions_mm39_noMT.tsv", sep="\t")
selected_tracks = pd.read_csv("data/selected_mouse_liver_tracks.tsv", sep="\t")

model = dna_client.create(api_key)

output_type_map = {
    "atac": dna_output.OutputType.ATAC,
    "dnase": dna_output.OutputType.DNASE,
    "cage": dna_output.OutputType.CAGE,
    "rna_seq": dna_output.OutputType.RNA_SEQ,
    "chip_histone": dna_output.OutputType.CHIP_HISTONE,
    "chip_tf": dna_output.OutputType.CHIP_TF,
}

requested_outputs = []
for output_type in selected_tracks["output_type"].unique():
    requested_outputs.append(output_type_map[output_type])

intervals = []
for _, row in regions.iterrows():
    intervals.append(
        genome.Interval(
            chromosome=row["chrom"],
            start=int(row["alphagenome_start"]),
            end=int(row["alphagenome_end"]),
            strand=row["strand"],
            name=row["gene"],
        )
    )

print("Running mouse AlphaGenome predictions for intervals:")
for interval in intervals:
    print(interval)

outputs = model.predict_intervals(
    intervals=intervals,
    organism=dna_model.Organism.MUS_MUSCULUS,
    requested_outputs=requested_outputs,
    ontology_terms=None,
    progress_bar=True,
    max_workers=1,
)

summary_rows = []

for region_row, output in zip(regions.to_dict("records"), outputs):
    gene = region_row["gene"]

    for _, track_row in selected_tracks.iterrows():
        output_type = track_row["output_type"]
        track_name = track_row["track_name"]

        track_data = getattr(output, output_type)

        if track_data is None:
            continue

        metadata = track_data.metadata.reset_index(drop=True)
        values = track_data.values

        matches = metadata.index[metadata["name"] == track_name].tolist()

        if not matches:
            summary_rows.append({
                "gene": gene,
                "gene_group": region_row["gene_group"],
                "RNA_seq_direction": region_row["RNA_seq_direction"],
                "biological_role": region_row["biological_role"],
                "log2FoldChange": region_row["log2FoldChange"],
                "padj": region_row["padj"],
                "baseMean": region_row["baseMean"],
                "chrom": region_row["chrom"],
                "alphagenome_start": region_row["alphagenome_start"],
                "alphagenome_end": region_row["alphagenome_end"],
                "output_type": output_type,
                "track_name": track_name,
                "track_found": False,
                "strand": "",
                "mean_signal": np.nan,
                "max_signal": np.nan,
                "sum_signal": np.nan,
                "reason": track_row["reason"],
            })
            continue

        for idx in matches:
            signal = values[:, idx]

            summary_rows.append({
                "gene": gene,
                "gene_group": region_row["gene_group"],
                "RNA_seq_direction": region_row["RNA_seq_direction"],
                "biological_role": region_row["biological_role"],
                "log2FoldChange": region_row["log2FoldChange"],
                "padj": region_row["padj"],
                "baseMean": region_row["baseMean"],
                "chrom": region_row["chrom"],
                "alphagenome_start": region_row["alphagenome_start"],
                "alphagenome_end": region_row["alphagenome_end"],
                "output_type": output_type,
                "track_name": track_name,
                "track_found": True,
                "strand": metadata.loc[idx, "strand"] if "strand" in metadata.columns else "",
                "mean_signal": float(np.mean(signal)),
                "max_signal": float(np.max(signal)),
                "sum_signal": float(np.sum(signal)),
                "reason": track_row["reason"],
            })

summary = pd.DataFrame(summary_rows)

os.makedirs("results_alpha10", exist_ok=True)
summary.to_csv("results_alpha10/mouse_alpha10_alphagenome_summary.tsv", sep="\t", index=False)

print("\nSaved: results_alpha10/mouse_alpha10_alphagenome_summary.tsv")
print(summary.head(40).to_string(index=False))
