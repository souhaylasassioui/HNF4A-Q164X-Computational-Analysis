import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def read_xvg(filename):
    x = []
    y = []
    with open(filename) as f:
        for line in f:
            if line.startswith("#") or line.startswith("@"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
    return x, y

# Clean RMSD
x, y = read_xvg("rmsd_wt_clean2.xvg")
plt.figure()
plt.plot(x, y)
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("WT HNF4A homodimer RMSD")
plt.tight_layout()
plt.savefig("rmsd_wt_clean.png", dpi=300)
plt.close()

# Clean RMSF
x, y = read_xvg("rmsf_wt_clean.xvg")
plt.figure()
plt.plot(x, y)
plt.xlabel("Residue")
plt.ylabel("RMSF (nm)")
plt.title("WT HNF4A homodimer RMSF")
plt.tight_layout()
plt.savefig("rmsf_wt_clean.png", dpi=300)
plt.close()

# Clean radius of gyration
x, y = read_xvg("gyrate_wt_clean.xvg")
x = [v / 1000 for v in x]  # ps to ns
plt.figure()
plt.plot(x, y)
plt.xlabel("Time (ns)")
plt.ylabel("Radius of gyration (nm)")
plt.title("WT HNF4A homodimer radius of gyration")
plt.tight_layout()
plt.savefig("gyrate_wt_clean.png", dpi=300)
plt.close()

print("Clean WT plots saved successfully.")
