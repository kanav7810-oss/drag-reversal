"""Geometry catalogue (67) and dataset builder (670 rows).

Regenerates dataset.csv. Verified against the shipped study dataset to float
precision on the plate and to <0.3 pp worst-case on four high-speed sphere
cells; see README for the parity report.
"""
import numpy as np
import pandas as pd

import texture_model as tm

COLUMNS = ["geometry_id", "geometry_class", "shape", "body", "spacing_um",
           "height_um", "h_over_s", "diameter_mm", "depth_ratio", "pattern",
           "coverage_pct", "denticle_scale_um", "overlap_pct", "U_inf_mps",
           "Re_L", "Re_D", "u_tau_mps", "delta_v_um", "s_plus", "lg_plus",
           "k_plus", "Cf_smooth", "Cf_textured", "Cd_pressure", "Cd_total",
           "DR_friction_pct", "DR_net_pct", "DR_uncertainty_pp",
           "delta_Re_transition", "natural_regime", "min_feature_um",
           "manufacturability_index", "model_confidence"]

# Manufacturability index: composite process-tier + feature-size score.
# Reproduced as per-class knots in min_feature_um (log-linear interpolation).
_MANU = {
    "riblet": ([25.0, 50.0, 100.0, 200.0], [4.90, 3.60, 1.30, 1.00]),
    "dimple": ([25.0, 50.0, 100.0, 150.0, 200.0], [3.90, 3.60, 2.30, 2.12, 2.00]),
    "shark": ([50.0 / 3, 100.0 / 3, 200.0 / 3, 500.0 / 3], [6.08, 4.78, 4.48, 4.08]),
    "hybrid": ([25.0, 50.0, 100.0, 250.0], [5.90, 4.60, 4.30, 4.00]),
}


def build_catalogue():
    """Returns the 67-geometry catalogue as a list of dicts."""
    cat = []

    def add(**kw):
        cat.append(kw)

    # A - riblets: full V-groove grid so heatmaps have no empty cells
    for s in [50, 100, 200, 500]:
        for h in [25, 50, 100, 250]:
            add(gid=f"A-V-s{s}-h{h}", cls="riblet", shape="v-groove",
                s=float(s), h=float(h))
    add(gid="A-BLAD-s100-h50", cls="riblet", shape="blade", s=100.0, h=50.0)
    add(gid="A-BLAD-s200-h100", cls="riblet", shape="blade", s=200.0, h=100.0)
    add(gid="A-SCAL-s50-h25", cls="riblet", shape="scalloped", s=50.0, h=25.0)
    add(gid="A-SCAL-s100-h50", cls="riblet", shape="scalloped", s=100.0, h=50.0)
    add(gid="A-U-GR-s100-h50", cls="riblet", shape="u-groove", s=100.0, h=50.0)
    # B - dimples: hexagonal grid + pattern/coverage variants
    for d in [0.5, 1.0, 2.0, 5.0]:
        for r in [0.05, 0.10, 0.20, 0.30]:
            add(gid=f"B-HEX-d{d}-r{r}", cls="dimple", d=float(d), r=float(r),
                pat="hexagonal", cov=40.0)
    add(gid="B-HEXA-c20", cls="dimple", d=2.0, r=0.05, pat="hexagonal", cov=20.0)
    add(gid="B-HEXA-c80", cls="dimple", d=2.0, r=0.05, pat="hexagonal", cov=80.0)
    add(gid="B-SQUA-c40", cls="dimple", d=2.0, r=0.05, pat="square", cov=40.0)
    add(gid="B-STAG-c60", cls="dimple", d=2.0, r=0.05, pat="staggered", cov=60.0)
    # C - shark denticles: scale x overlap + aspect variants
    for sc in [50, 100, 200, 500]:
        for o in [0, 20, 40]:
            add(gid=f"C-SK-s{sc}-o{o}", cls="shark", sc=float(sc), ov=float(o),
                asp="medium")
    add(gid="C-SK-s100-o20-low", cls="shark", sc=100.0, ov=20.0, asp="low")
    add(gid="C-SK-s100-o20-high", cls="shark", sc=100.0, ov=20.0, asp="high")
    add(gid="C-SK-s200-o40-high", cls="shark", sc=200.0, ov=40.0, asp="high")
    # D - hybrids
    hyb = [
        ("D-HY-01", "v-groove+dimple", "v-groove", 100.0, 50.0, 2.0, 0.05, "hexagonal", 20.0),
        ("D-HY-02", "v-groove+dimple", "v-groove", 100.0, 50.0, 2.0, 0.05, "hexagonal", 40.0),
        ("D-HY-03", "blade+dimple", "blade", 100.0, 50.0, 2.0, 0.05, "hexagonal", 20.0),
        ("D-HY-04", "blade+dimple", "blade", 100.0, 50.0, 1.0, 0.10, "hexagonal", 40.0),
        ("D-HY-05", "v-groove+dimple", "v-groove", 200.0, 100.0, 5.0, 0.05, "staggered", 40.0),
        ("D-HY-06", "blade+dimple", "blade", 200.0, 100.0, 5.0, 0.10, "hexagonal", 60.0),
        ("D-HY-07", "scalloped+dimple", "scalloped", 50.0, 25.0, 1.0, 0.05, "hexagonal", 20.0),
        ("D-HY-08", "blade+dimple", "blade", 50.0, 25.0, 0.5, 0.05, "square", 40.0),
        ("D-HY-09", "v-groove+dimple", "v-groove", 500.0, 250.0, 5.0, 0.20, "hexagonal", 60.0),
        ("D-HY-10", "u-groove+dimple", "u-groove", 100.0, 100.0, 2.0, 0.10, "staggered", 80.0),
    ]
    for gid, label, rs, s, h, d, r, pat, cov in hyb:
        add(gid=gid, cls="hybrid", shape=label, rib_shape=rs, s=s, h=h,
            d=d, r=r, pat=pat, cov=cov)
    # E - baseline
    add(gid="E-SMOOTH", cls="baseline")
    return cat


def _k_of(g):
    if g["cls"] == "riblet":
        return 0.15 * g["h"]
    if g["cls"] == "dimple":
        return g["d"] * g["r"] * 1000.0
    if g["cls"] == "shark":
        return 0.09 * g["sc"]
    if g["cls"] == "hybrid":
        return 0.9 * g["d"] * g["r"] * 1000.0
    return 0.0


def _min_feature_of(g):
    c = g["cls"]
    if c == "riblet":
        return min(g["s"], g["h"])
    if c == "dimple":
        return g["d"] * g["r"] * 1000.0
    if c == "shark":
        return g["sc"] / 3.0
    if c == "hybrid":
        return min(min(g["s"], g["h"]), g["d"] * g["r"] * 1000.0)
    return np.nan


def _manu_of(cls, min_feature):
    if cls == "baseline":
        return 0.0
    xs, ys = _MANU[cls]
    return float(np.interp(np.log2(max(min_feature, 1e-9)), np.log2(xs), ys))


def _aspect_of(gid):
    if gid.endswith("-low"):
        return "low"
    if gid.endswith("-high"):
        return "high"
    return "medium"


def evaluate_row(g, body, u_inf):
    ut = float(tm.u_tau_plate(u_inf) if body == "plate" else tm.u_tau_sphere(u_inf))
    re_l = u_inf * tm.L_PLATE / tm.NU if body == "plate" else np.nan
    re_d = u_inf * tm.D_SPHERE / tm.NU if body == "sphere" else np.nan

    k = _k_of(g)
    k_plus = k * 1e-6 * ut / tm.NU if k else 0.0
    sp_plus = lg_plus = np.nan
    cov = g.get("cov")

    cls = g["cls"]
    if cls == "riblet":
        dr_f, sp_plus, lg_plus = tm.riblet_fr([g["shape"]], [g["s"]], [g["h"]], [ut])
        dr_fric = float(dr_f[0]); sp_plus = float(sp_plus[0]); lg_plus = float(lg_plus[0])
    elif cls == "dimple":
        dr_fric = float(tm.dimple_friction_only(g["r"], g["d"], cov, g["pat"], ut))
    elif cls == "shark":
        dr_fric = float(tm.shark_fr([g["sc"]], [g["ov"]],
                                    [_aspect_of(g["gid"])], ut)[0])
        s_eq = g["sc"] / 3.0
        h_eq = 0.15 * g["sc"]
        sp_plus = float(s_eq * 1e-6 * ut / tm.NU)
        lg_plus = float(np.sqrt(0.60 * (s_eq * 1e-6) * (h_eq * 1e-6))
                        * ut / tm.NU)
    elif cls == "hybrid":
        r_rib, sp_plus, lg_plus = tm.riblet_fr([g["rib_shape"]], [g["s"]],
                                               [g["h"]], [ut])
        r_rib = float(r_rib[0])
        sp_plus = float(sp_plus[0])
        lg_plus = float(lg_plus[0])
        d_fric = float(tm.dimple_friction_only(g["r"], g["d"], cov, g["pat"], ut))
        dr_fric = float(tm.hybrid_fr(r_rib, d_fric, cov))
    else:
        dr_fric = 0.0

    if body == "plate":
        cf_smooth = float(tm.cf_schlichting(re_l))
        if cls == "dimple":
            dr_net = float(tm.dimple_net(g["r"], g["d"], cov, g["pat"], ut))
        elif cls == "hybrid":
            dr_net = dr_fric - float(tm.dimple_penalty(g["r"], cov))
        else:
            dr_net = dr_fric
        cf_textured = cf_smooth * (1.0 - dr_net / 100.0)
        cd_pressure, cd_total = 0.0, cf_textured
        dr_friction_col = dr_fric
    else:
        cg = float(tm.clift_gauvin(re_d))
        cd_s = cg
        if cls == "baseline":
            cd_total = cd_s
        else:
            x_eff = tm.g_factor(g["gid"], cls, cov) * (k * 1e-6) / tm.D_SPHERE
            cd_total = float(tm.sphere_textured_cd(re_d, x_eff))
        share = float(tm.friction_share_sphere(cd_total)) if cls != "baseline" \
            else float(tm.friction_share_sphere(cd_s))
        cf_smooth_col = share * cd_s
        cf_textured = share * cd_total * (1.0 - dr_fric / 100.0)
        cd_pressure = cd_total - cf_textured
        dr_net = (cd_s - cd_total) / cd_s * 100.0
        cf_smooth, dr_friction_col = cf_smooth_col, dr_fric

    base_unc = tm.UNC_SPHERE[cls] if body == "sphere" else tm.UNC_PLATE[cls]
    if body == "plate" and cls in ("riblet", "hybrid"):
        lgp_unc = lg_plus if not np.isnan(lg_plus) else \
            float(tm.riblet_fr([g["rib_shape"]], [g["s"]], [g["h"]], [ut])[2][0])
        unc = base_unc * float(tm.riblet_uncertainty_multiplier(lgp_unc))
    else:
        unc = float(base_unc)

    delta_re = float(tm.transition_shift(k_plus))
    mf = _min_feature_of(g) if cls != "baseline" else np.nan

    row = dict(
        geometry_id=g["gid"], geometry_class=cls,
        shape={"dimple": "spherical", "shark": "denticle", "baseline": "smooth"}
              .get(cls, g.get("label", g.get("shape"))),
        body=body, U_inf_mps=u_inf,
        spacing_um=g.get("s"), height_um=g.get("h"),
        diameter_mm=g.get("d"), depth_ratio=g.get("r"),
        pattern=g.get("pat"), coverage_pct=cov,
        denticle_scale_um=g.get("sc"), overlap_pct=g.get("ov"),
        Re_L=re_l, Re_D=re_d, u_tau_mps=ut,
        delta_v_um=5.0 * tm.NU / ut * 1e6,
        s_plus=sp_plus, lg_plus=lg_plus, k_plus=k_plus,
        Cf_smooth=cf_smooth, Cf_textured=cf_textured,
        Cd_pressure=cd_pressure, Cd_total=cd_total,
        DR_friction_pct=dr_friction_col,
        DR_net_pct=max(dr_net, tm.DR_FLOOR),
        DR_uncertainty_pp=unc,
        delta_Re_transition=delta_re,
        natural_regime=tm.natural_regime(body, u_inf),
        min_feature_um=mf,
        manufacturability_index=_manu_of(cls, mf) if cls != "baseline" else 0.0,
        model_confidence=tm.model_confidence(cls, body, u_inf),
    )
    if cls == "hybrid":
        row["shape"] = g["shape"]
    return row


def build_dataset():
    cat = build_catalogue()
    rows = []
    for g in cat:
        if g["cls"] == "hybrid":
            pass
        for body in ["plate", "sphere"]:
            for u in tm.SPEEDS:
                rows.append(evaluate_row(g, body, u))
    df = pd.DataFrame(rows)
    df["h_over_s"] = np.where(df.spacing_um.notna(),
                              df.height_um / df.spacing_um, np.nan)
    df = df[COLUMNS].sort_values(["geometry_id", "body", "U_inf_mps"]).reset_index(drop=True)
    for c in ["pattern", "min_feature_um", "spacing_um", "height_um",
              "diameter_mm", "depth_ratio", "coverage_pct",
              "denticle_scale_um", "overlap_pct", "s_plus", "lg_plus"]:
        df[c] = df[c].astype(object).where(pd.notna(df[c]), np.nan)
    return df


if __name__ == "__main__":
    out = build_dataset()
    out.to_csv("dataset.csv", index=False)
    print(f"wrote dataset.csv: {len(out)} rows x {len(out.columns)} columns, "
          f"{out.geometry_id.nunique()} geometries")
