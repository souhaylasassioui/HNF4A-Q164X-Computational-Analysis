import pandas as pd
import urllib.request
import json
import time

genes = pd.read_csv("data/alpha10_all_genes_curated_plus_background.tsv", sep="\t")

records = []

for _, row in genes.iterrows():
    gene = row["gene"]
    url = f"https://rest.ensembl.org/lookup/symbol/mus_musculus/{gene}?content-type=application/json"

    print(f"Fetching {gene}...")

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f"FAILED: {gene} | {e}")
        continue

    chrom = "chr" + data["seq_region_name"]
    gene_start_1based = int(data["start"])
    gene_end_1based = int(data["end"])
    strand_value = int(data["strand"])

    if strand_value == 1:
        strand = "+"
        tss_0based = gene_start_1based - 1
    else:
        strand = "-"
        tss_0based = gene_end_1based - 1

    width = 16384
    interval_start = max(0, tss_0based - width // 2)
    interval_end = interval_start + width

    records.append({
        "gene": gene,
        "gene_group": row["gene_group"],
        "RNA_seq_direction": row["RNA_seq_direction"],
        "log2FoldChange": row["log2FoldChange"],
        "padj": row["padj"],
        "baseMean": row["baseMean"],
        "biological_role": row["biological_role"],
        "ensembl_id": data["id"],
        "chrom": chrom,
        "gene_start_1based": gene_start_1based,
        "gene_end_1based": gene_end_1based,
        "strand": strand,
        "tss_0based": tss_0based,
        "alphagenome_start": interval_start,
        "alphagenome_end": interval_end,
        "interval_width": width,
    })

    time.sleep(0.2)

out = pd.DataFrame(records)
out.to_csv("data/alpha10_mouse_gene_regions_mm39.tsv", sep="\t", index=False)

print("\nSaved: data/alpha10_mouse_gene_regions_mm39.tsv")
print(out.head(20).to_string(index=False))
print(f"\nNumber of genes with coordinates: {len(out)}")
