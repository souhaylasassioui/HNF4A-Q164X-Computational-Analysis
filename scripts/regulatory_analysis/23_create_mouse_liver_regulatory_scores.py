import pandas as pd
import numpy as np
import os

df = pd.read_csv("results_alpha10/mouse_alpha10_alphagenome_summary.tsv", sep="\t")

# Keep only found tracks
df = df[df["track_found"] == True].copy()

# For tracks with multiple strands, keep the maximum value per gene/track
max_df = (
    df.groupby([
        "gene",
        "gene_group",
        "RNA_seq_direction",
        "biological_role",
        "log2FoldChange",
        "padj",
        "baseMean",
        "track_name"
    ], as_index=False)["max_signal"]
    .max()
)

# Pivot to genes x tracks
wide = max_df.pivot_table(
    index=[
        "gene",
        "gene_group",
        "RNA_seq_direction",
        "biological_role",
        "log2FoldChange",
        "padj",
        "baseMean"
    ],
    columns="track_name",
    values="max_signal",
    fill_value=0
).reset_index()

# Clean column names
wide.columns.name = None

track_cols = [
    c for c in wide.columns
    if c not in ["gene", "gene_group", "RNA_seq_direction", "biological_role", "log2FoldChange", "padj", "baseMean"]
]

# Log-transform signals
for c in track_cols:
    wide[c + "_log10"] = np.log10(wide[c] + 1)

# Normalize each track between 0 and 1
norm_cols = []
for c in track_cols:
    log_col = c + "_log10"
    norm_col = c + "_norm"
    min_val = wide[log_col].min()
    max_val = wide[log_col].max()

    if max_val > min_val:
        wide[norm_col] = (wide[log_col] - min_val) / (max_val - min_val)
    else:
        wide[norm_col] = 0

    norm_cols.append(norm_col)

# Integrated liver regulatory activity score
wide["liver_regulatory_activity_score"] = wide[norm_cols].mean(axis=1)

# Rank genes by liver regulatory activity
wide["regulatory_activity_rank"] = wide["liver_regulatory_activity_score"].rank(
    ascending=False,
    method="dense"
).astype(int)

wide = wide.sort_values("liver_regulatory_activity_score", ascending=False)

os.makedirs("results_alpha10", exist_ok=True)

wide.to_csv("results_alpha10/mouse_liver_regulatory_activity_scores.tsv", sep="\t", index=False)

# Save a candidate-only table
candidate = wide[wide["gene_group"] == "candidate_DEG"].copy()
candidate.to_csv("results_alpha10/mouse_alpha10_candidate_liver_regulatory_scores.tsv", sep="\t", index=False)

print("Saved:")
print("results_alpha10/mouse_liver_regulatory_activity_scores.tsv")
print("results_alpha10/mouse_alpha10_candidate_liver_regulatory_scores.tsv")

print("\nTop candidate DEGs by predicted liver regulatory activity:")
cols = [
    "gene",
    "RNA_seq_direction",
    "biological_role",
    "log2FoldChange",
    "padj",
    "liver_regulatory_activity_score",
    "regulatory_activity_rank"
]
print(candidate[cols].to_string(index=False))
