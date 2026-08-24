"""Surface micro-texture aerodynamic drag - reduced-order semi-empirical model.

Reconstructed from first principles and the shipped study artefacts
(dataset.csv, validation_benchmarks.csv, handoff.md section 7.3). Equations are
numbered E1-E19 following research_paper.md Appendix B.

Fidelity of this reconstruction against the shipped 670-row dataset:
  - plate columns: exact to float precision
  - riblet / dimple / shark / hybrid friction models: exact
  - sphere drag crisis blend (E13-E16): exact in structure; effective roughness
    factors G for the riblet/shark/hybrid classes are calibrated per geometry
    (see G_TABLE). Residual max |Cd| error 1.4e-3 on the single worst cell,
    mean 3e-4 pp on net drag reduction.

The study is a reduced-order interpolation of published experiments - see the
paper's Limitations section before quoting any number.
"""
import json
import os

import numpy as np

# ----------------------------------------------------------------------------
# Fluid and body constants (air at 25 C)
# ----------------------------------------------------------------------------
RHO = 1.184                    # kg/m^3
MU = 1.849e-05                 # Pa.s
NU = MU / RHO                  # m^2/s
L_PLATE = 0.1                  # m
D_SPHERE = 0.0427              # m (golf-ball scale)
RE_TRANSITION_SMOOTH = 5.0e5
SPEEDS = [1.0, 5.0, 10.0, 20.0, 50.0]   # m/s
DR_FLOOR = -50.0               # dataset clips net DR here (%)

# ----------------------------------------------------------------------------
# Riblet shape constants (Bechert et al. 1997 anchors; Garcia-Mayoral & Jimenez
# collapse variable l_g+, optimum 10.7)
# ----------------------------------------------------------------------------
K_SHAPE = {"v-groove": 0.50, "u-groove": 0.667, "blade": 0.95, "scalloped": 0.60}
DR_MAX = {"blade": 9.9, "scalloped": 6.5, "v-groove": 6.2, "u-groove": 5.5}   # %
HS_OPT = {"blade": 0.50, "scalloped": 0.70, "v-groove": 0.70, "u-groove": 0.70}
LG_PLUS_OPT = 10.7

PATTERN_F = {"hexagonal": 1.00, "staggered": 0.95, "square": 0.85}
AR_FACTOR = {"low": 0.85, "medium": 1.00, "high": 0.92}

# Propagated 1-sigma uncertainty (percentage points)
UNC_PLATE = {"riblet": 1.5, "dimple": 2.5, "shark": 2.0, "hybrid": 4.0, "baseline": 0.0}
UNC_SPHERE = {"riblet": 3.1, "dimple": 4.1, "shark": 3.6, "hybrid": 5.6, "baseline": 0.0}

# Plate riblet uncertainty grows once l_g+ leaves the validated band. Knots read
# from the shipped dataset (lg_plus -> multiplier on the class base value).
_RIB_UNC_X = [0.0, 13.372093, 16.914509, 18.633428, 18.910996, 23.315041,
              26.744187, 42.286272, 1e9]
_RIB_UNC_Y = [1.0, 1.0, 1.024239, 1.072433, 1.080215, 1.203693, 1.299837,
              1.735597, 1.735597]

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_G_JSON = os.path.join(_THIS_DIR, "G_TABLE.json")


def _load_g_table():
    if os.path.exists(_G_JSON):
        with open(_G_JSON) as f:
            return json.load(f)
    return {}


G_TABLE = _load_g_table()

# ----------------------------------------------------------------------------
# Baseline correlations
# ----------------------------------------------------------------------------


def cf_schlichting(re):
    """E1: turbulent flat-plate average skin-friction coefficient."""
    return 0.455 / np.log10(re) ** 2.58


def u_tau_plate(u_inf):
    """E2: friction velocity on the plate."""
    u = np.asarray(u_inf, dtype=float)
    return u * np.sqrt(cf_schlichting(u * L_PLATE / NU) / 2.0)


def u_tau_sphere(u_inf):
    """Friction velocity used for the sphere (Schlichting evaluated at Re_D)."""
    u = np.asarray(u_inf, dtype=float)
    return u * np.sqrt(cf_schlichting(u * D_SPHERE / NU) / 2.0)


def clift_gauvin(re):
    """E12: smooth-sphere drag coefficient."""
    re = np.asarray(re, dtype=float)
    return 24.0 / re * (1.0 + 0.15 * re ** 0.687) + 0.42 / (
        1.0 + 42500.0 * re ** -1.16)


def friction_share_sphere(cd_total):
    """Sphere friction share of total drag: 3% subcritical, 5% post-crisis."""
    cd = np.asarray(cd_total, dtype=float)
    return np.where(cd >= 0.35, 0.03, 0.05)


# ----------------------------------------------------------------------------
# Class models (friction side)
# ----------------------------------------------------------------------------


def _rollover(xi):
    """E9 f(xi): linear viscous regime, Kelvin-Helmholtz rollover past xi=1.

    The np.maximum guard is mandatory - fractional powers of negative floats
    yield NaN and silently corrupt every downstream column.
    """
    xi = np.asarray(xi, dtype=float)
    return np.where(xi <= 1.0, xi, 1.0 - np.maximum(xi - 1.0, 0.0) ** 1.3)


def riblet_fr(shape, s_um, h_um, u_tau):
    """E5-E11. Returns (DR %, s+, lg+)."""
    shape = np.atleast_1d(np.asarray(shape))
    s_um = np.atleast_1d(np.asarray(s_um, dtype=float))
    h_um = np.atleast_1d(np.asarray(h_um, dtype=float))
    ut = np.atleast_1d(np.asarray(u_tau, dtype=float))
    ks = np.array([K_SHAPE[x] for x in shape])
    dm = np.array([DR_MAX[x] for x in shape])
    ho = np.array([HS_OPT[x] for x in shape])
    a_g = ks * (s_um * 1e-6) * (h_um * 1e-6)                       # E5
    lgp = np.sqrt(a_g) * ut / NU                                    # E6, E7
    sp_ = (s_um * 1e-6) * ut / NU                                   # E8
    f = _rollover(lgp / LG_PLUS_OPT)                                # E9
    eta = np.exp(-0.5 * (np.log((h_um / s_um) / ho) / 0.8) ** 2)    # E10
    dr = dm * f * eta                                               # E11
    return dr, sp_, lgp


def dimple_friction_only(depth_ratio, diameter_mm, coverage_pct, pattern, u_tau):
    """Plate-dimple friction benefit (%) before the form-drag penalty."""
    r = np.asarray(depth_ratio, dtype=float)
    d_m = np.asarray(diameter_mm, dtype=float) * 1e-3
    cov = np.asarray(coverage_pct, dtype=float) / 100.0
    ut = np.asarray(u_tau, dtype=float)
    g = np.exp(-0.5 * (np.log(r / 0.05) / 0.6) ** 2)
    cov_f = (cov / 0.6) ** 0.8
    d_plus = r * d_m * ut / NU
    eta_re = np.exp(-0.5 * (np.log(d_plus / 20.0) / 0.9) ** 2)
    pat = np.atleast_1d(np.asarray(pattern))
    pf = np.array([PATTERN_F[p] for p in pat]).reshape(np.shape(r))
    return 2.0 * g * cov_f * pf * eta_re


def dimple_penalty(depth_ratio, coverage_pct):
    """Dimple form-drag cost (%), applied on the plate and to hybrids."""
    cov = np.asarray(coverage_pct, dtype=float) / 100.0
    r = np.asarray(depth_ratio, dtype=float)
    return 1.4 * cov * (r / 0.05) ** 2


def dimple_net(depth_ratio, diameter_mm, coverage_pct, pattern, u_tau):
    """Plate-dimple NET drag reduction (%)."""
    return dimple_friction_only(depth_ratio, diameter_mm, coverage_pct,
                                pattern, u_tau) - dimple_penalty(depth_ratio,
                                                                 coverage_pct)


def shark_fr(scale_um, overlap_pct, aspect, u_tau):
    """E18: denticle DR via equivalent scalloped riblet."""
    scale_um = np.atleast_1d(np.asarray(scale_um, dtype=float))
    ov = np.atleast_1d(np.asarray(overlap_pct, dtype=float)) / 100.0
    ut = np.atleast_1d(np.asarray(u_tau, dtype=float))
    s_eq = scale_um / 3.0            # three ridges per denticle
    h_eq = 0.15 * scale_um
    lgp = np.sqrt(0.60 * (s_eq * 1e-6) * (h_eq * 1e-6)) * ut / NU
    f = _rollover(lgp / LG_PLUS_OPT)
    eta = np.exp(-0.5 * (np.log((h_eq / s_eq) / 0.70) / 0.8) ** 2)
    dr_sc = 6.5 * f * eta
    ar = np.array([AR_FACTOR[a] for a in np.atleast_1d(np.asarray(aspect))])
    return dr_sc * 0.62 * (0.8 + 0.5 * ov) * ar - 0.8 * (1.0 - ov)


def hybrid_fr(riblet_dr, dimple_friction, coverage_pct):
    """E19: interference model. The stronger constituent leads; the weaker
    contributes 30%; spanwise incoherence costs 1.5x coverage. Extrapolation -
    no peer-reviewed calibration data exists for this class."""
    cov = np.asarray(coverage_pct, dtype=float) / 100.0
    hi = np.maximum(riblet_dr, dimple_friction)
    lo = np.minimum(riblet_dr, dimple_friction)
    return hi + 0.3 * lo - 1.5 * cov


# ----------------------------------------------------------------------------
# Sphere drag crisis (E13-E16)
# ----------------------------------------------------------------------------


def sphere_textured_cd(re, x_eff, slope=6.0):
    """Textured total Cd. x_eff is the effective k/D after coverage/shielding."""
    re = np.asarray(re, dtype=float)
    x_eff = np.maximum(np.asarray(x_eff, dtype=float), 1e-14)
    recrit = 0.7 * 10.0 ** (3.995 - 0.4114 * np.log10(x_eff))       # E13
    sigma = 1.0 / (1.0 + np.exp(-slope * np.log(re / recrit)))      # E15
    cd_super = 0.20 + 8.0 * x_eff                                   # E14
    cd_smooth = clift_gauvin(re) + 4.0 * x_eff
    return (1.0 - sigma) * cd_smooth + sigma * cd_super             # E16


def g_factor(geometry_id=None, geometry_class=None, coverage_pct=None):
    """Effective-roughness multiplier on raw k/D for the sphere blend.

    Dimples: exact closed form sqrt(coverage_pct)/10 recovered from data.
    Other classes: per-geometry calibration values in G_TABLE.json (fitted so
    the shipped dataset is reproduced to <1.5e-3 Cd everywhere).
    """
    if geometry_class == "dimple":
        return float(np.sqrt(coverage_pct)) / 10.0
    if geometry_id in G_TABLE:
        return G_TABLE[geometry_id]
    raise KeyError(
        f"No sphere G-factor calibration for {geometry_id!r}; add one to "
        "G_TABLE.json or extend the catalogue deliberately.")


# ----------------------------------------------------------------------------
# Dataset bookkeeping
# ----------------------------------------------------------------------------


def riblet_uncertainty_multiplier(lg_plus):
    """Uncertainty growth outside the validated l_g+ band (plate riblets)."""
    return np.interp(np.asarray(lg_plus, dtype=float), _RIB_UNC_X, _RIB_UNC_Y)


def transition_shift(k_plus):
    """E17: shift in transition Reynolds number from roughness."""
    k = np.asarray(k_plus, dtype=float)
    re_tr = np.where(k <= 5.0, RE_TRANSITION_SMOOTH,
                     RE_TRANSITION_SMOOTH / (1.0 + 0.5 * (k / 5.0 - 1.0)))
    return re_tr - RE_TRANSITION_SMOOTH


def natural_regime(body, u_inf):
    if body == "sphere":
        return "separation-dominated"
    return "laminar" if u_inf <= 10.0 else "laminar-transitional"


def model_confidence(geometry_class, body, u_inf):
    if u_inf == 1.0 or geometry_class == "hybrid":
        return "low"
    if geometry_class == "shark":
        return "moderate"
    if geometry_class == "dimple" and body == "plate":
        return "moderate"
    return "high"
