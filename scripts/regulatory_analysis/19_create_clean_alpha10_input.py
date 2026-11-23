import csv

# Curated 10 candidate genes
candidates = [
    ["Cyp8b1", "candidate_DEG", "downregulated", "-2.06699604054807", "4.21232160921752e-05", "1661.03710189795", "bile acid metabolism"],
    ["Fasn", "candidate_DEG", "downregulated", "-1.46643206460199", "2.40162171552017e-06", "11433.5488045835", "fatty acid synthesis"],
    ["Bhmt", "candidate_DEG", "downregulated", "-1.65250933437848", "0.000939343367935862", "18674.9284829266", "one-carbon metabolism"],
    ["Akr1d1", "candidate_DEG", "downregulated", "-1.15903356202302", "0.0024238126348581", "1075.55478327435", "bile acid/steroid metabolism"],
    ["Slc22a7", "candidate_DEG", "downregulated", "-3.11220959831948", "0.0453037751364111", "196.822566771437", "hepatic organic anion transport"],
    ["Cyp4a14", "candidate_DEG", "upregulated", "4.84863708819319", "0.000165480237312936", "1623.68764111184", "fatty acid omega-hydroxylation/xenobiotic response"],
    ["Onecut1", "candidate_DEG", "upregulated", "2.58699734053854", "7.01686664322557e-08", "451.418807498167", "hepatic transcriptional regulation"],
    ["E2f8", "candidate_DEG", "upregulated", "3.38810218462681", "2.63100833524678e-12", "178.931364281625", "cell-cycle/proliferation regulation"],
    ["Cish", "candidate_DEG", "upregulated", "3.28146839579474", "0.0082546095635499", "526.894980011072", "cytokine/JAK-STAT signaling"],
    ["Socs2", "candidate_DEG", "upregulated", "2.94161110749598", "0.00519646874103462", "680.458313938693", "growth hormone/JAK-STAT signaling"],
]

header = ["gene", "gene_group", "RNA_seq_direction", "log2FoldChange", "padj", "baseMean", "biological_role"]

# Write clean curated candidate file
with open("data/alpha10_candidate_DEGs_curated.tsv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)
    writer.writerows(candidates)

# Read background file and add biological_role column
background_rows = []
with open("data/alpha10_background_nonDE_genes.tsv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        background_rows.append([
            row["gene"],
            row["gene_group"],
            row["RNA_seq_direction"],
            row["log2FoldChange"],
            row["padj"],
            row["baseMean"],
            "background non-differentially expressed gene"
        ])

# Write combined file
with open("data/alpha10_all_genes_curated_plus_background.tsv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)
    writer.writerows(candidates)
    writer.writerows(background_rows)

print("Saved:")
print("data/alpha10_candidate_DEGs_curated.tsv")
print("data/alpha10_all_genes_curated_plus_background.tsv")
print("Number of candidate genes:", len(candidates))
print("Number of background genes:", len(background_rows))
print("Total genes:", len(candidates) + len(background_rows))
