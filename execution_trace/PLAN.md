# Computational Ranking of Surface Micro-Texture Geometries for Aerodynamic Drag Reduction

**Author context:** Kanav Thonda, Rouse High School (Class of 2028) , targeting ISEF / AIAA student paper.
**Deliverables:** dataset.csv, research_paper.md, 8 SVG figures, index.html, handoff.md.

---

## 1. Summary

A semi-empirical reduced-order model evaluates **67 surface micro-texture geometries** across
**5 flow speeds** on **2 test bodies** (flat plate + sphere) = **670 dataset rows**. Full CFD is
infeasible here and is not attempted: resolving 50 µm riblets over a 0.1 m plate requires
wall-resolved DNS/LES at ~10^9 cells per case, ×670 cases. Instead the study composes **published,
peer-reviewed drag correlations** into a unified framework and validates them against specific
published data points.

**What is genuinely new** is the systematic cross-class, cross-Reynolds, cross-body ranking under
one consistent framework with propagated uncertainty, *not* new physics. The paper will state this
explicitly. Predictions inside the calibration envelope are interpolation; outside it (hybrids) they
are labeled extrapolation.

### Four decisions resolved with the user

| Issue | Resolution |
|---|---|
| **All 5 speeds are laminar** (Re_L = 6.4×10³ to 3.2×10⁵ vs ~5×10⁵ transition; would need 78 m/s) | Assume **leading-edge trip → turbulent BL**, standard wind-tunnel practice. Keeps L=0.1 m and all 5 speeds. A `natural_regime` column records what would happen untripped. |
| **Dimples judged only where they fail** | Add a **sphere** (D = 42.7 mm) alongside the plate. Riblets should win on the plate, dimples on the sphere. |
| **Contested literature** (dimples +4% [9] vs −2% [10] vs skeptical review [12]; shark-skin 10% [6] vs 20 to 31% [1,2,5]) | **Conservative consensus** calibration. Consequence: shark-skin will *not* reach the brief's 12% ceiling. This deviation is deliberate and defended in the Discussion. |
| **"How do you know it's right?"** | **Validation table + uncertainty bands** propagated into every ranking. |

### Four decisions delegated to me (recorded as assumptions)

- **Geometry set → grid-filling design** (below) totalling exactly **67**, resolving the brief's 66-vs-67 arithmetic error and its over-specified riblet grid (h/s is not free once h and s are fixed).
- **Hybrids → sub-additive with interference penalty**, widest uncertainty band, labeled extrapolation.
- **Pareto axis → two panels**: feature size exactly as briefed, plus a composite manufacturability index (rolling < stamping < micro-milling < laser < lithography).
- **Web build → fully self-contained** single file (inlined SVGs, embedded data, working downloads).

---

## 2. Physics model (the core interface every downstream number depends on)

**Fluid:** air at 25 °C, ρ = 1.184 kg/m³, µ = 1.849×10⁻⁵ Pa·s, ν = 1.5617×10⁻⁵ m²/s.
**Speeds:** 1, 5, 10, 20, 50 m/s. **Plate:** L = 0.1 m (Re_L 6.4×10³ to 3.2×10⁵). **Sphere:** D = 42.7 mm (Re_D 2.7×10³ to 1.4×10⁵).

**Baseline.** Plate: Schlichting C_F = 0.455/(log₁₀Re_L)^2.58, local Cf_x = (2log₁₀Re_x − 0.65)^−2.3;
u_τ = U√(Cf/2); δ_v = 5ν/u_τ. Sphere: standard Cd(Re_D) drag curve, drag crisis ~3.5×10⁵.

**Riblets.** Drag reduction driven by the groove length scale ℓ_g⁺ = √(A_g)·u_τ/ν, which is the
parameter García-Mayoral & Jiménez showed collapses riblet data [24, 25]. Linear viscous regime for
ℓ_g⁺ ≤ ℓ_g⁺_opt ≈ 10.7, then Kelvin-Helmholtz breakdown [26] rolling over to drag *increase*.
Per-shape ceilings anchored to Bechert et al. 1997 [22]: blade 9.9%, scalloped ~6.5%, V-groove ~6.2%,
U-groove ~5.5%; h/s efficiency peaks at 0.5 per the same source. **The optimal s⁺ ≈ 10 to 20 band
requested in Graph 4 emerges from this physics rather than being hard-coded.**

**Dimples on the plate.** Shallow-dimple friction benefit peaking ~+2% near d/D ≈ 0.05, minus a form-drag
penalty ∝ coverage·(d/D)², reproducing van Campenhout's finding that pressure drag drives the net
*increase* for deeper dimples [10]. Most deep/dense variants land net-negative. Widest single-class
uncertainty (spans the −2% to +4% literature range).

**Dimples on the sphere.** The payoff case. Roughness lowers the critical Re per Achenbach [33],
calibrated so a golf-ball-like relative depth yields Re_crit ≈ 5×10⁴ and post-crisis Cd ≈ 0.25,
with Beratlis' local drag penalty [27] included. Riblets/denticles get only a weak friction credit
on the sphere, where friction is a small share of total drag, the honest cross-body contrast.

**Shark-skin.** Denticles treated as riblet-like with an equivalent spacing from scale and ridge
count, an overlap-dependent alignment efficiency, and a 3D-roughness penalty (denticles are not
spanwise-uniform, so they underperform ideal riblets). Ceiling ~3 to 8% per conservative calibration.

**Hybrids.** DR = DR_strong + 0.3·DR_weak − interference(coverage), where dimples disrupt the
streamwise coherence riblets rely on. No peer-reviewed calibration data exists; flagged accordingly.

**Transition shift.** Roughness Reynolds number k⁺ = k·u_τ/ν; hydraulically smooth below k⁺ ≈ 5.
Above that the texture trips, and ΔRe_tr is reported (negative = earlier transition).

**Uncertainty.** Per-class σ from calibration-source spread (riblets ±1.5 pp, plate dimples ±2.5 pp,
shark-skin ±2 pp, hybrids ±4 pp). Rankings flag overlapping intervals as **statistically tied**, so
the paper never claims a winner the evidence can't support.

---

## 3. Geometry set (exactly 67) and dataset schema

| Class | Construction | n |
|---|---|---|
| A Riblets | full 4-spacing × 4-height grid (V-groove) = 16, + 5 shape variants (U, blade, scalloped) | **21** |
| B Dimples | full 4-diameter × 4-depth-ratio grid = 16, + 4 pattern/coverage variants | **20** |
| C Shark-skin | 4 scale × 3 overlap = 12, + 3 aspect-ratio variants | **15** |
| D Hybrid | riblet+dimple combinations | **10** |
| E Baseline | smooth | **1** |

The full grids in A and B exist specifically so Graph 3 and Graph 5 heatmaps have **zero empty cells**.

**dataset.csv**: 670 rows (67 × 5 speeds × 2 bodies), one row per geometry-speed-body:
`geometry_id, class, shape, body, spacing_um, height_um, h_over_s, diameter_mm, depth_ratio, pattern,
coverage_pct, denticle_scale_um, overlap_pct, U_inf_mps, Re_L, Re_D, u_tau, delta_v_um, s_plus, lg_plus,
k_plus, Cf_smooth, Cf_textured, Cd_pressure, Cd_total, DR_friction_pct, DR_net_pct, DR_uncertainty_pp,
delta_Re_transition, natural_regime, min_feature_um, manufacturability_index, model_confidence`

**Validation table** (`validation_benchmarks.csv`, reproduced in the paper) with % error against:
smooth-plate C_F (Schlichting), Bechert blade-riblet 9.9% peak [22], GM&J breakdown at s⁺ 10 to 20 [24],
smooth-sphere subcritical Cd ≈ 0.5, golf-ball post-crisis Cd ≈ 0.25, van Nesselrooij dimple +4% [9].

---

## 4. Analysis, figures, and written deliverables

All 9 requested analyses run, with ties flagged where uncertainty intervals overlap. Eight figures as
**SVG + PNG** (PNG for the mandatory rendering check), Liberation Sans, colorblind-safe palette:
top-20 bar, DR-vs-speed lines, riblet s×h heatmap, s⁺ scatter with the optimal band highlighted,
dimple heatmap, flow visualization, Pareto (two panels), class box plots.

**Graph 6** is built from *computed* Blasius and log-law velocity profiles rather than drawn as
decorative art, so the laminar-vs-turbulent contrast is quantitatively correct and drawn to scale.

**research_paper.md**: ≥5000 words, all 11 requested sections. **Every citation will be a real,
verifiable paper**: the brief allows "plausible" references, but fabricated citations would end an
ISEF or AIAA submission, so I will not produce any. 20+ real sources are already identified.
Every number in the paper is generated from dataset.csv programmatically, never retyped.

**index.html**: self-contained, aerospace palette (#f0f4f8 / #003087 / #e8931a), Chart.js + Inter,
all 11 sections including the live drag explorer with a parametric SVG cross-section renderer,
multi-select comparison chart, and the sortable/searchable 670-row table.

**handoff.md**: all 8 sections, naming real labs (UT Austin, MIT AeroAstro, Georgia Tech), real
journals (AIAA Journal, Experiments in Fluids, JFM), and real competitions with realistic timing for
a 2028 graduate.

---

## 5. Compute, risks, acceptance criteria

**Compute:** negligible. 670 rows of closed-form algebra, sub-second on the default `worker-0`
(1 CPU / 16 GB, numpy 2.1 / pandas 2.3 / matplotlib 3.10 / scipy 1.15 all present, Liberation Sans
installed). **No HPC, no extra machines, no background jobs.** Wall time is dominated by writing the
paper and HTML, not by computation.

**Principal risk, and the honest framing of it:** the model is *calibrated to* published experiments,
so it interpolates the literature rather than independently predicting it. Riblet and sphere-dimple
predictions are well-anchored; plate-dimple values inherit a genuine unresolved controversy in the
field; hybrids are extrapolation. The paper's Limitations section will say exactly this, and
`model_confidence` in the dataset carries it per-row.

**Acceptance criteria**
1. dataset.csv has exactly 670 rows, 67 unique geometries, class counts 21/20/15/10/1.
2. Riblet optimum falls in s⁺ ≈ 10 to 20 **as a model output**, matching [24] independently.
3. Dimpled sphere shows a clear drag-crisis shift at high speed; smooth sphere does not.
4. All validation benchmarks reproduce within 15%; any that don't are reported, not hidden.
5. Paper ≥5000 words, ≥18 real citations, every quoted number traceable to dataset.csv.
6. All 8 SVGs render correctly (verified visually), heatmaps have no empty cells.
7. index.html opens standalone with all interactive controls working and downloads functional.
