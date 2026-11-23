import csv

tracks = [
    ["atac", "UBERON:0002107 ATAC-seq", "liver chromatin accessibility"],
    ["dnase", "UBERON:0002107 DNase-seq", "liver chromatin accessibility"],
    ["chip_histone", "UBERON:0002107 Histone ChIP-seq H3K27ac", "liver active enhancer/regulatory mark"],
    ["chip_histone", "UBERON:0002107 Histone ChIP-seq H3K4me3", "liver promoter mark"],
    ["chip_histone", "UBERON:0002107 Histone ChIP-seq H3K4me1", "liver enhancer-associated mark"],
    ["cage", "hCAGE UBERON:0002107", "liver promoter activity"],
    ["cage", "hCAGE CL:0000182", "hepatocyte promoter activity"],
    ["rna_seq", "UBERON:0002107 polyA plus RNA-seq", "liver transcription signal"],
    ["rna_seq", "UBERON:0002107 total RNA-seq", "liver transcription signal"],
    ["chip_tf", "UBERON:0002107 TF ChIP-seq EP300", "liver enhancer co-activator"],
    ["chip_tf", "UBERON:0002107 TF ChIP-seq CTCF", "liver chromatin architecture factor"],
]

with open("data/selected_mouse_liver_tracks.tsv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["output_type", "track_name", "reason"])
    writer.writerows(tracks)

print("Saved clean file: data/selected_mouse_liver_tracks.tsv")
