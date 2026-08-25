"""The nine analyses (a1-a9) over the dataset.

Reconstructed from handoff.md sections 2-3 and results_summary.json structure.
Every headline number quoted in the paper regenerates from here.
"""
import numpy as np
import pandas as pd


def a1_overall_ranking(df, n=20):
    d = df[df.model_confidence != "low"].copy()
    d["lo"] = d.DR_net_pct - d.DR_uncertainty_pp
    top = df.nlargest(n, "DR_net_pct")[
        ["geometry_id", "geometry_class", "body", "U_inf_mps", "DR_net_pct",
         "DR_uncertainty_pp"]].to_dict("records")
    return {"top": top}


def _class_stats(df):
    g = df.groupby(["geometry_class", "body"]).DR_net_pct.agg(
        mean="mean", sd="std", min="min", max="max", n="count").round(4)
    return g.reset_index().to_dict("records")


def a2_regime_ranking(df):
    out = {}
    for body in ["plate", "sphere"]:
        d = df[df.body == body]
        means = d.groupby("geometry_class").DR_net_pct.mean().round(4)
        out[body] = means.sort_values(ascending=False).to_dict()
    return out


def a3_riblet(df):
    rib = df[df.geometry_class == "riblet"].copy()
    plate = rib[rib.body == "plate"]
    best = plate.loc[plate.DR_net_pct.idxmax()]
    # s+ band value: all plate riblet rows, inside s+=10..20 vs outside
    # (matches the shipped worker-0 trace: 16 rows in band, 2.70 pp)
    inside = plate[(plate.s_plus >= 10) & (plate.s_plus <= 20)].DR_net_pct
    outside = plate[(plate.s_plus < 10) | (plate.s_plus > 20)].DR_net_pct
    optima = {}
    for shape, grp in rib.groupby("shape"):
        b = grp.loc[grp.DR_net_pct.idxmax()]
        optima[shape] = {"peak_DR_pct": round(float(b.DR_net_pct), 3),
                         "at_U": float(b.U_inf_mps),
                         "s_plus": round(float(b.s_plus), 3),
                         "lg_plus": round(float(b.lg_plus), 4)}
    return {"best_plate": {"geometry_id": best.geometry_id,
                           "U_inf_mps": float(best.U_inf_mps),
                           "DR_net_pct": round(float(best.DR_net_pct), 3),
                           "s_plus": round(float(best.s_plus), 3)},
            "shape_optima": optima,
            "band_value_pp": round(float(inside.mean() - outside.mean()), 4),
            "n_inside_band": int(len(inside)),
            "mean_inside": round(float(inside.mean()), 4),
            "mean_outside": round(float(outside.mean()), 4)}


def a4_dimple(df):
    d = df[df.geometry_class == "dimple"]
    plate_best = d[d.body == "plate"].loc[
        lambda x: x.DR_net_pct.idxmax()]
    sphere_best = d[d.body == "sphere"].loc[
        lambda x: x.DR_net_pct.idxmax()]
    smooth = df[(df.geometry_class == "baseline") & (df.body == "sphere")]
    return {"best_plate": {"geometry_id": plate_best.geometry_id,
                           "DR_net_pct": round(float(plate_best.DR_net_pct), 3)},
            "best_sphere": {"geometry_id": sphere_best.geometry_id,
                            "U_inf_mps": float(sphere_best.U_inf_mps),
                            "DR_net_pct": round(float(sphere_best.DR_net_pct), 3),
                            "Cd_smooth": round(float(
                                smooth[smooth.U_inf_mps == sphere_best.U_inf_mps].Cd_total.iloc[0]), 4),
                            "Cd_textured": round(float(sphere_best.Cd_total), 4)},
            "plate_class_mean": round(float(d[d.body == "plate"].DR_net_pct.mean()), 4),
            "sphere_class_mean": round(float(d[d.body == "sphere"].DR_net_pct.mean()), 4)}


def a5_shark(df):
    sh = df[df.geometry_class == "shark"]
    best = sh.loc[sh.DR_net_pct.idxmax()]
    ideal_riblet_same = df[(df.body == best.body) &
                           (df.U_inf_mps == best.U_inf_mps) &
                           (df.geometry_class == "riblet")].DR_net_pct.max()
    return {"best": {"geometry_id": best.geometry_id,
                     "U_inf_mps": float(best.U_inf_mps),
                     "body": best.body,
                     "DR_net_pct": round(float(best.DR_net_pct), 3)},
            "shortfall_vs_ideal_riblet_pp": round(float(ideal_riblet_same - best.DR_net_pct), 3),
            "fraction_of_riblet_benefit": round(float(best.DR_net_pct / ideal_riblet_same), 3)}


def a6_hybrid(df):
    hy = df[df.geometry_class == "hybrid"]
    return {"cases": int(len(hy)),
            "mean_hybrid_DR": round(float(hy.DR_net_pct.mean()), 4),
            "interference_model": "strong + 0.3*weak - 1.5*coverage - dimple penalty",
            "confidence": "extrapolation - no peer-reviewed calibration data"}


def a7_speed(df):
    out = {}
    for U, grp in df[df.geometry_class != "baseline"].groupby("U_inf_mps"):
        best = grp.loc[grp.DR_net_pct.idxmax()]
        out[float(U)] = {"best_geometry": best.geometry_id, "body": best.body,
                         "DR_net_pct": round(float(best.DR_net_pct), 3)}
    return out


def a8_pareto(df):
    d = df[df.body == "plate"].drop_duplicates("geometry_id")
    pts = d[["geometry_id", "DR_net_pct_max", "min_feature_um"]] if \
        "DR_net_pct_max" in d else None
    per_geom = df[df.body == "plate"].groupby("geometry_id").agg(
        DR_max=("DR_net_pct", "max"), min_feature=("min_feature_um", "first"),
        manu=("manufacturability_index", "first")).reset_index()
    front = []
    for _, r in per_geom.sort_values("min_feature").iterrows():
        if not front or r.DR_max > front[-1]["DR_max_pct"]:
            front.append({"geometry_id": r.geometry_id,
                          "DR_max_pct": round(float(r.DR_max), 3),
                          "min_feature_um": float(r.min_feature)})
    return {"pareto_front_drag_vs_feature_size": front}


def a9_class_stats(df):
    return _class_stats(df)


def derived(df):
    d = df.copy()
    d["pos"] = d.DR_net_pct > 0
    g = d.groupby("body").agg(rows=("pos", "size"), positive=("pos", "sum"),
                              dr_min=("DR_net_pct", "min"),
                              dr_max=("DR_net_pct", "max"))
    g["fraction_positive"] = (g.positive / g.rows).round(4)
    return {k: {kk: (float(vv) if isinstance(vv, (int, float, np.floating)) else vv)
                for kk, vv in row.items()}
            for k, row in g.to_dict("index").items()}


def run_all(df):
    return {
        "a1_ranking": a1_overall_ranking(df),
        "a2_regime": a2_regime_ranking(df),
        "a3_riblet": a3_riblet(df),
        "a4_dimple": a4_dimple(df),
        "a5_shark": a5_shark(df),
        "a6_hybrid": a6_hybrid(df),
        "a7_speed": a7_speed(df),
        "a8_pareto": a8_pareto(df),
        "a9_stats": a9_class_stats(df),
        "derived": derived(df),
    }
