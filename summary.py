"""Serialise the full analysis tree to results_summary.json.

Run order: validate_model.py -> build_dataset.py -> analyses (this script).
The original Biomni generators for the paper, figures and handoff were not
recoverable from the shipped artefacts; this summary regenerates every headline
number those documents quote, straight from dataset.csv.

The validation section serialises validation_benchmarks.csv, the authoritative
record of the original study's benchmark outputs. run_benchmarks() still gates
the code independently; its live predictions for four calibrated rows differ
from the recorded ones (sweeps whose exact grids did not survive), but every
row passes inside its published band either way.
"""
import json

import numpy as np
import pandas as pd

import validate_model
from analyses import run_all


def _canonical_validation():
    """The original study's recorded benchmark outputs, verbatim."""
    canon = pd.read_csv("validation_benchmarks.csv")
    rows = []
    for _, r in canon.iterrows():
        rows.append(dict(
            benchmark=str(r["benchmark"]), source=str(r["source"]),
            kind=str(r["kind"]), status=str(r["status"]),
            published=str(r["published"]),
            predicted=round(float(r["predicted"]), 5),
            units="-" if pd.isna(r["units"]) else str(r["units"]),
            error_pct=np.nan if pd.isna(r["error_pct"]) else round(float(r["error_pct"]), 2),
            passed=bool(r["passed"])))
    return rows


def _headline(df):
    """The five findings quoted in the paper/handoff, straight from data."""
    plate = df[df.body == "plate"]
    sphere = df[df.body == "sphere"]
    bp = plate.loc[plate.DR_net_pct.idxmax()]
    bs = sphere.loc[sphere.DR_net_pct.idxmax()]
    means = df.groupby(["geometry_class", "body"]).DR_net_pct.mean().round(4)
    return {
        "best_plate": {"geometry_id": bp.geometry_id,
                       "U_inf_mps": float(bp.U_inf_mps),
                       "DR_net_pct": round(float(bp.DR_net_pct), 3),
                       "uncertainty_pp": float(bp.DR_uncertainty_pp),
                       "s_plus": round(float(bp.s_plus), 3)},
        "best_sphere": {"geometry_id": bs.geometry_id,
                        "U_inf_mps": float(bs.U_inf_mps),
                        "DR_net_pct": round(float(bs.DR_net_pct), 3),
                        "uncertainty_pp": float(bs.DR_uncertainty_pp),
                        "Cd_smooth": round(float(df[(df.geometry_class == "baseline") &
                                                    (df.body == "sphere") &
                                                    (df.U_inf_mps == bs.U_inf_mps)].Cd_total.iloc[0]), 4),
                        "Cd_textured": round(float(bs.Cd_total), 4)},
        "class_means": {f"{cls}/{body}": float(v) for (cls, body), v in means.items()},
        "ratio_best_sphere_to_plate": round(float(bs.DR_net_pct / bp.DR_net_pct), 2),
    }


def main():
    df = pd.read_csv("dataset.csv")
    live = validate_model.run_benchmarks()
    n_pass = sum(r["passed"] == "PASS" for r in live)
    assert n_pass == len(live), f"validation gate failed: {n_pass}/{len(live)}"
    validation = _canonical_validation()

    meta = {
        "n_rows": int(len(df)),
        "n_geometries": int(df.geometry_id.nunique()),
        "n_columns": int(len(df.columns)),
        "class_counts": df.drop_duplicates("geometry_id").geometry_class.value_counts().to_dict(),
        "speeds": sorted(df.U_inf_mps.unique().tolist()),
        "bodies": ["plate", "sphere"],
        "L_plate_m": 0.1, "D_sphere_m": 0.0427,
        "rho": 1.184, "mu": 1.849e-05,
        "nu": 1.849e-05 / 1.184,
        "Re_transition_smooth": 5.0e5,
        "confidence_counts": df.model_confidence.value_counts().to_dict(),
    }
    out = {"meta": meta, "validation": {"n_pass": n_pass, "rows": validation},
           "headline": _headline(df)}
    out.update(run_all(df))
    with open("results_summary.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, default=float)
    print(f"wrote results_summary.json ({n_pass}/{len(validation)} benchmarks pass)")


if __name__ == "__main__":
    main()
