import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu, spearmanr
import os

df = pd.read_csv("results_alpha10/mouse_liver_regulatory_activity_scores.tsv", sep="\t")

candidate = df[df["gene_group"] == "candidate_DEG"].copy()
background = df[df["gene_group"] == "background_nonDE"].copy()

candidate_scores = candidate["liver_regulatory_activity_score"].dropna()
background_scores = background["liver_regulatory_activity_score"].dropna()

# Mann-Whitney U test: candidate DEGs vs background genes
u_stat, p_value = mannwhitneyu(candidate_scores, background_scores, alternative="two-sided")

summary = pd.DataFrame({
    "comparison": ["Candidate DEGs vs non-DE background genes"],
    "n_candidate_DEGs": [len(candidate_scores)],
    "n_background_nonDE": [len(background_scores)],
    "median_candidate_score": [candidate_scores.median()],
    "median_background_score": [background_scores.median()],
    "mean_candidate_score": [candidate_scores.mean()],
    "mean_background_score": [background_scores.mean()],
    "mannwhitney_U": [u_stat],
    "p_value": [p_value],
})

os.makedirs("results_alpha10", exist_ok=True)
summary.to_csv("results_alpha10/mouse_candidate_vs_background_statistical_summary.tsv", sep="\t", index=False)

# Percentile of each candidate compared with background
def background_percentile(score, background_values):
    return 100 * (background_values <= score).mean()

candidate["background_percentile"] = candidate["liver_regulatory_activity_score"].apply(
    lambda x: background_percentile(x, background_scores)
)

candidate_summary = candidate[[
    "gene",
    "RNA_seq_direction",
    "biological_role",
    "log2FoldChange",
    "padj",
    "liver_regulatory_activity_score",
    "regulatory_activity_rank",
    "background_percentile"
]].sort_values("liver_regulatory_activity_score", ascending=False)

candidate_summary.to_csv("results_alpha10/mouse_candidate_gene_regulatory_priority_table.tsv", sep="\t", index=False)

# Spearman correlation between absolute log2FC and liver regulatory score among candidate genes
rho, spearman_p = spearmanr(
    candidate_summary["log2FoldChange"].abs(),
    candidate_summary["liver_regulatory_activity_score"]
)

correlation = pd.DataFrame({
    "analysis": ["Spearman correlation among 10 candidate DEGs"],
    "variable_1": ["absolute log2FoldChange"],
    "variable_2": ["liver regulatory activity score"],
    "spearman_rho": [rho],
    "p_value": [spearman_p],
    "n": [len(candidate_summary)]
})

correlation.to_csv("results_alpha10/mouse_candidate_spearman_correlation.tsv", sep="\t", index=False)

print("\nCandidate vs background statistical summary:")
print(summary.to_string(index=False))

print("\nCandidate priority table:")
print(candidate_summary.to_string(index=False))

print("\nSpearman correlation:")
print(correlation.to_string(index=False))

print("\nSaved:")
print("results_alpha10/mouse_candidate_vs_background_statistical_summary.tsv")
print("results_alpha10/mouse_candidate_gene_regulatory_priority_table.tsv")
print("results_alpha10/mouse_candidate_spearman_correlation.tsv")
