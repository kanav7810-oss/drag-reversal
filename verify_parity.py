"""Final acceptance check - does NOT overwrite any shipped artefact."""
import pandas as pd, numpy as np
import build_dataset as bd

ref = pd.read_csv("dataset.csv")
new = bd.build_dataset()
assert len(new) == 670 and new.geometry_id.nunique() == 67
a = ref.sort_values(["geometry_id","body","U_inf_mps"]).reset_index(drop=True)
b = new.sort_values(["geometry_id","body","U_inf_mps"]).reset_index(drop=True)

worst = 0.0; worst_col = ""
for c in a.columns:
    if a[c].dtype.kind not in "fi":
        continue
    x, y = a[c].to_numpy(float), b[c].to_numpy(float)
    d = np.abs(x - y); d = d[~(np.isnan(x) & np.isnan(y))]
    m = float(np.nanmax(d)) if len(d) else 0.0
    if m > worst:
        worst, worst_col = m, c

print(f"dataset parity: max |err| = {worst:.4g} on column {worst_col!r}")
print("PASS" if worst < 0.35 else "FAIL")
