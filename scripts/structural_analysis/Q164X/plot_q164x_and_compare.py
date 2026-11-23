import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pathlib import Path
import os

WT_DIR = os.environ.get("WT_MD_DIR", str(Path("../WT").resolve()))

def read_xvg(filename):
    x, y = [], []
    with open(filename) as f:
        for line in f:
            if line.startswith("#") or line.startswith("@"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
    return x, y

# Q164X RMSD
x, y = read_xvg("rmsd_q164x_clean.xvg")
plt.figure()
plt.plot(x, y)
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("Q164X HNF4A homodimer RMSD")
plt.tight_layout()
plt.savefig("rmsd_q164x_clean.png", dpi=300)
plt.close()

# Q164X RMSF
x, y = read_xvg("rmsf_q164x_clean.xvg")
plt.figure()
plt.plot(x, y)
plt.xlabel("Residue")
plt.ylabel("RMSF (nm)")
plt.title("Q164X HNF4A homodimer RMSF")
plt.tight_layout()
plt.savefig("rmsf_q164x_clean.png", dpi=300)
plt.close()

# Q164X radius of gyration
x, y = read_xvg("gyrate_q164x_clean.xvg")
x = [v / 1000 for v in x]
plt.figure()
plt.plot(x, y)
plt.xlabel("Time (ns)")
plt.ylabel("Radius of gyration (nm)")
plt.title("Q164X HNF4A homodimer radius of gyration")
plt.tight_layout()
plt.savefig("gyrate_q164x_clean.png", dpi=300)
plt.close()

# WT vs Q164X RMSD
x_wt, y_wt = read_xvg(f"{WT_DIR}/rmsd_wt_clean2.xvg")
x_q, y_q = read_xvg("rmsd_q164x_clean.xvg")
plt.figure()
plt.plot(x_wt, y_wt, label="WT")
plt.plot(x_q, y_q, label="Q164X")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("WT vs Q164X HNF4A homodimer RMSD")
plt.legend()
plt.tight_layout()
plt.savefig("rmsd_wt_vs_q164x.png", dpi=300)
plt.close()

# WT vs Q164X radius of gyration
x_wt, y_wt = read_xvg(f"{WT_DIR}/gyrate_wt_clean.xvg")
x_q, y_q = read_xvg("gyrate_q164x_clean.xvg")
x_wt = [v / 1000 for v in x_wt]
x_q = [v / 1000 for v in x_q]
plt.figure()
plt.plot(x_wt, y_wt, label="WT")
plt.plot(x_q, y_q, label="Q164X")
plt.xlabel("Time (ns)")
plt.ylabel("Radius of gyration (nm)")
plt.title("WT vs Q164X HNF4A homodimer radius of gyration")
plt.legend()
plt.tight_layout()
plt.savefig("gyrate_wt_vs_q164x.png", dpi=300)
plt.close()

print("Q164X and comparison plots saved successfully.")
