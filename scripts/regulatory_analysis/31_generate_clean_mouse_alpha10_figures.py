import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

os.makedirs("figures_alpha10_paper", exist_ok=True)

# -----------------------------
# Paper-quality color palette
# -----------------------------
DOWN_COLOR = "#0072B2"      # blue
UP_COLOR = "#D55E00"        # vermillion
BACKGROUND_COLOR = "#BDBDBD"
POINT_GRAY = "#4D4D4D"
EDGE_COLOR = "#222222"
HEATMAP_CMAP = "cividis"

# Global style
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
})

# -----------------------------
# Load data
# -----------------------------
scores = pd.read_csv(
    "results_alpha10/mouse_liver_regulatory_activity_scores.tsv",
    sep="\t"
)

candidate_scores = pd.read_csv(
    "results_alpha10/mouse_alpha10_candidate_liver_regulatory_scores.tsv",
    sep="\t"
)

signal_metrics = pd.read_csv(
    "results_alpha10/mouse_candidate_liver_signal_metrics.tsv",
    sep="\t"
)

summary = pd.read_csv(
    "results_alpha10/mouse_alpha10_alphagenome_summary.tsv",
    sep="\t"
)

# ============================================================
# FIGURE 1: Candidate regulatory activity score
# ============================================================
df = candidate_scores.sort_values("liver_regulatory_activity_score", ascending=True).copy()

colors = [
    DOWN_COLOR if x == "downregulated" else UP_COLOR
    for x in df["RNA_seq_direction"]
]

fig, ax = plt.subplots(figsize=(7.0, 4.6))

ax.barh(
    df["gene"],
    df["liver_regulatory_activity_score"],
    color=colors,
    edgecolor=EDGE_COLOR,
    linewidth=0.5
)

ax.set_xlabel("Liver regulatory activity score")
ax.set_ylabel("")
ax.set_title("Predicted liver regulatory activity in candidate genes")
ax.grid(axis="x", alpha=0.18)

legend_elements = [
    Patch(facecolor=DOWN_COLOR, edgecolor=EDGE_COLOR, label="Downregulated"),
    Patch(facecolor=UP_COLOR, edgecolor=EDGE_COLOR, label="Upregulated"),
]
ax.legend(handles=legend_elements, frameon=False, loc="lower right")

plt.tight_layout()
plt.savefig("figures_alpha10_paper/figure1_candidate_regulatory_score.png")
plt.savefig("figures_alpha10_paper/figure1_candidate_regulatory_score.pdf")
plt.close()

# ============================================================
# FIGURE 2: Candidate DEGs vs non-DE background
# ============================================================
candidate = scores.loc[
    scores["gene_group"] == "candidate_DEG",
    "liver_regulatory_activity_score"
].dropna()

background = scores.loc[
    scores["gene_group"] == "background_nonDE",
    "liver_regulatory_activity_score"
].dropna()

fig, ax = plt.subplots(figsize=(5.4, 4.4))

bp = ax.boxplot(
    [candidate, background],
    labels=["Candidate DEGs", "Non-DE background"],
    patch_artist=True,
    widths=0.5,
    showfliers=False
)

for patch, color in zip(bp["boxes"], [DOWN_COLOR, BACKGROUND_COLOR]):
    patch.set_facecolor(color)
    patch.set_alpha(0.65)
    patch.set_edgecolor(EDGE_COLOR)
    patch.set_linewidth(1)

for median in bp["medians"]:
    median.set_color("black")
    median.set_linewidth(1.4)

for whisker in bp["whiskers"]:
    whisker.set_color(EDGE_COLOR)

for cap in bp["caps"]:
    cap.set_color(EDGE_COLOR)

np.random.seed(1)
x1 = np.random.normal(1, 0.035, size=len(candidate))
x2 = np.random.normal(2, 0.035, size=len(background))

ax.scatter(x1, candidate, s=22, color=UP_COLOR, alpha=0.70, zorder=3)
ax.scatter(x2, background, s=18, color=POINT_GRAY, alpha=0.40, zorder=3)

ax.set_ylabel("Liver regulatory activity score")
ax.set_title("Candidate genes versus non-DE background")
ax.grid(axis="y", alpha=0.18)

plt.tight_layout()
plt.savefig("figures_alpha10_paper/figure2_candidate_vs_background.png")
plt.savefig("figures_alpha10_paper/figure2_candidate_vs_background.pdf")
plt.close()

# ============================================================
# FIGURE 3: Signal metrics heatmap
# ============================================================
df = signal_metrics[["gene", "Mean signal", "Max signal", "Total signal"]].copy()
df = df.sort_values("Max signal", ascending=False)

heat = df.set_index("gene")[["Mean signal", "Max signal", "Total signal"]]
heat_log = np.log10(heat + 1)

fig, ax = plt.subplots(figsize=(6.0, 4.6))

im = ax.imshow(
    heat_log.values,
    aspect="auto",
    cmap=HEATMAP_CMAP
)

ax.set_xticks(range(len(heat_log.columns)))
ax.set_xticklabels(["Mean", "Maximum", "Total"], rotation=0)

ax.set_yticks(range(len(heat_log.index)))
ax.set_yticklabels(heat_log.index)

ax.set_title("Summary of predicted liver regulatory signals")

cbar = plt.colorbar(im, ax=ax, fraction=0.045, pad=0.04)
cbar.set_label("log10(signal + 1)")

plt.tight_layout()
plt.savefig("figures_alpha10_paper/figure3_signal_metrics_heatmap.png")
plt.savefig("figures_alpha10_paper/figure3_signal_metrics_heatmap.pdf")
plt.close()

# ============================================================
# FIGURE 4: Multi-track heatmap
# ============================================================
df = summary.copy()
df = df[df["track_found"] == True]
df = df[df["gene_group"] == "candidate_DEG"]

heat = (
    df.groupby(["gene", "track_name"], as_index=False)["max_signal"]
    .max()
)

short_names = {
    "UBERON:0002107 ATAC-seq": "ATAC",
    "UBERON:0002107 DNase-seq": "DNase",
    "UBERON:0002107 Histone ChIP-seq H3K27ac": "H3K27ac",
    "UBERON:0002107 Histone ChIP-seq H3K4me1": "H3K4me1",
    "UBERON:0002107 Histone ChIP-seq H3K4me3": "H3K4me3",
    "UBERON:0002107 TF ChIP-seq CTCF": "CTCF",
    "UBERON:0002107 TF ChIP-seq EP300": "EP300",
    "UBERON:0002107 polyA plus RNA-seq": "polyA RNA",
    "UBERON:0002107 total RNA-seq": "total RNA",
    "hCAGE UBERON:0002107": "Liver CAGE",
    "hCAGE CL:0000182": "Hepatocyte CAGE",
}

heat["track_short"] = heat["track_name"].map(short_names)
heat = heat.dropna(subset=["track_short"])

matrix = heat.pivot(
    index="gene",
    columns="track_short",
    values="max_signal"
).fillna(0)

track_order = [
    "ATAC",
    "DNase",
    "H3K27ac",
    "H3K4me1",
    "H3K4me3",
    "EP300",
    "CTCF",
    "polyA RNA",
    "total RNA",
    "Liver CAGE",
    "Hepatocyte CAGE",
]

matrix = matrix[[c for c in track_order if c in matrix.columns]]
matrix_log = np.log10(matrix + 1)

gene_order = candidate_scores.sort_values(
    "liver_regulatory_activity_score",
    ascending=False
)["gene"].tolist()

gene_order = [g for g in gene_order if g in matrix_log.index]
matrix_log = matrix_log.loc[gene_order]

fig, ax = plt.subplots(figsize=(8.0, 4.6))

im = ax.imshow(
    matrix_log.values,
    aspect="auto",
    cmap=HEATMAP_CMAP
)

ax.set_xticks(range(len(matrix_log.columns)))
ax.set_xticklabels(matrix_log.columns, rotation=45, ha="right")

ax.set_yticks(range(len(matrix_log.index)))
ax.set_yticklabels(matrix_log.index)

ax.set_title("Multi-track mouse liver regulatory profile")

cbar = plt.colorbar(im, ax=ax, fraction=0.035, pad=0.03)
cbar.set_label("log10(max signal + 1)")

plt.tight_layout()
plt.savefig("figures_alpha10_paper/figure4_multitrack_heatmap.png")
plt.savefig("figures_alpha10_paper/figure4_multitrack_heatmap.pdf")
plt.close()

print("Saved paper-quality figures in: figures_alpha10_paper/")
for f in sorted(os.listdir("figures_alpha10_paper")):
    print(" -", f)
