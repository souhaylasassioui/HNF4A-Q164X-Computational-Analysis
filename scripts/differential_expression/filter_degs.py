#!/usr/bin/env python3

import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Filter DESeq2 results using adjusted p-value and log2FC."
)
parser.add_argument("input", help="DESeq2 CSV input file")
parser.add_argument("output", help="Filtered DEG CSV output file")
parser.add_argument("--padj", type=float, default=0.05)
parser.add_argument("--log2fc", type=float, default=1.0)

args = parser.parse_args()

with open(args.input, newline="") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    if not fields or not {"padj", "log2FoldChange"}.issubset(fields):
        parser.error("Input requires padj and log2FoldChange columns")

    selected = []

    for row in reader:
        try:
            padj = float(row["padj"])
            lfc = float(row["log2FoldChange"])
        except (ValueError, TypeError):
            continue

        if padj < args.padj and abs(lfc) > args.log2fc:
            selected.append(row)

Path(args.output).parent.mkdir(parents=True, exist_ok=True)

with open(args.output, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(selected)

print(f"Significant DEGs: {len(selected)}")
print(f"Output: {args.output}")
