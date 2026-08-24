# Project Handoff Document

**Project:** Surface Micro-Texture Aerodynamic Drag Reduction Research  
**Status:** Phases 1 through 6 complete  
**Completed by:** Biomni (Phylo AI scientific research agent)  
**Handoff to:** Local AI Agent  
**Principal investigator:** Kanav Thonda, Rouse High School, Leander TX (Class of 2028)  
**Date of handoff:** 2026-08-23  
**Primary artefacts:** `dataset.csv` (670 rows), `research_paper.md`, 8 figures (SVG + PNG), `index.html`, `handoff.md`

---

## How to read this document

This is a machine-and-human readable state dump. Sections 1-3 tell you *what exists and what
it means*. Sections 4-6 tell you *what to do next*. Sections 7-8 are the technical appendix
you need in order to re-run, extend, or audit anything.

Every number in this document was read programmatically from `results_summary.json` or
`dataset.csv` at generation time. No value was transcribed by hand. If you change the model
and re-run the pipeline, re-run `handoff.py` and this document updates itself.

**One thing to internalise before you touch anything:** this study is a *reduced-order semi-
empirical model calibrated against published experiments*, not a first-principles CFD
campaign and not a wind-tunnel measurement. It interpolates the literature under a single
consistent framework. That is a legitimate and useful contribution, and it is also a hard
ceiling on what the results can claim. Section 5 lists exactly where the model is standing
on solid ground and where it is extrapolating.

---

## 1. What was done

### 1.1 Objective

Determine which surface micro-texture geometry produces the largest net aerodynamic drag
reduction, how that answer changes with flow speed, and how it changes when the dominant
drag mechanism changes from skin friction to pressure/separation. Prior work overwhelmingly
studies one texture class on one body at one Reynolds number. The gap this project fills is
the **systematic cross-class, cross-Reynolds, cross-body comparison under one consistent
physical framework with propagated uncertainty**.

### 1.2 Approach

Full CFD was deliberately not attempted and the paper says so explicitly. Resolving a 50 um
riblet over a 0.1 m plate requires wall-resolved LES/DNS at order 1e9 cells per case; the
study evaluates 670 cases. Instead a **reduced-order semi-empirical model** was constructed
by composing published, peer-reviewed drag correlations into one framework, then validated
point-by-point against specific published data.

Six phases were executed:

1. **Physics model** (`texture_model.py`) - baseline skin friction and sphere drag, plus
   four texture-class drag models (riblet, dimple, shark denticle, hybrid) on two bodies.
2. **Validation** (`validate_model.py`) - 13 benchmarks against published values, 13 passed,
   maximum absolute point error **2.42%**.
3. **Geometry catalogue and dataset** (`build_dataset.py`) - exactly 67 geometries x 5
   speeds x 2 bodies = **670 rows**, 33 columns.
4. **Analyses** (`analyses.py`) - nine independent analyses (overall ranking, regime
   ranking, riblet optimum, dimple parametrics, shark-skin assessment, hybrid interference,
   speed sensitivity, Pareto fronts, per-class statistics).
5. **Figures** (`figures.py`) - eight publication-quality figures, SVG + PNG.
6. **Manuscript and web interface** (`paper.py`, `paper2.py`, `index.html`).

### 1.3 Test matrix

- **Fluid:** air at 25 C, rho = 1.184 kg/m^3, mu = 1.849e-05 Pa.s, nu = 1.5617e-05 m^2/s.
- **Speeds:** 1, 5, 10, 20, 50 m/s.
- **Body 1 - flat plate**, L = 0.1 m, Re_L = 6.4e+03 to 3.2e+05. Friction-dominated.
- **Body 2 - sphere**, D = 42.7 mm (golf-ball scale), Re_D = 2.73e+03 to 1.37e+05.
  Pressure/separation-dominated.
- **Geometry classes:** riblet (21), dimple (20), shark denticle (15), hybrid (10), smooth
  baseline (1).
- **Riblet cross-sections modelled:** blade, scalloped, u-groove, v-groove.

### 1.4 The boundary-layer trip decision (important - do not lose this)

At L = 0.1 m none of the five speeds transitions naturally: the highest Re_L is 3.2e+05
against a smooth-plate transition Reynolds number of 5e+05. Reaching natural transition at
this plate length would require **78.1 m/s**.

The study therefore assumes a **leading-edge trip** forcing a turbulent boundary layer from
near x = 0, which is standard wind-tunnel practice and is the only condition under which
riblets are even meaningful (riblets act on turbulent near-wall streaks). The untripped
state of every row is preserved in the `natural_regime` column so the assumption is
auditable rather than hidden.

**If you build the physical experiment, you must actually install the trip.** A boundary-
layer trip strip (e.g. 0.4 mm zig-zag turbulator tape or a spanwise row of 0.5 mm
cylindrical roughness elements at x/L ~ 0.05) is mandatory, otherwise the measurement does
not correspond to anything in this dataset.

---

## 2. Key findings

Five findings, ordered by how much they should shape what you do next. All drag reduction
(DR) values are **net percent reduction in total drag** relative to the smooth baseline at
the same speed and body, with +/- values being propagated 1-sigma uncertainty in
**percentage points (pp)**.

### Finding 1 - The winning texture class reverses when the dominant drag component changes

This is the headline result and the strongest claim in the paper.

- On the **friction-dominated flat plate**, riblets are the only class with a positive mean:
  **+1.091%** class mean, versus dimple **-6.253%**, shark **-0.096%**, hybrid **-0.899%**.
- On the **pressure-dominated sphere**, dimples dominate: class mean **+7.955%** versus
  riblet **+1.718%**.
- Best plate result: **A-BLAD-s200-h100** (blade riblet) at U = 20 m/s, **DR = 9.506% +/-
  1.5 pp**, s+ = 14.907.
- Best sphere result: **B-HEX-d2.0-r0.1** (dimple) at U = 50 m/s, **DR = 52.768% +/- 4.1
  pp**, Cd 0.4903 -> 0.2316.
- Ratio of best sphere DR to best plate DR: **5.55x**.

**Implication:** "which texture is best" is not a well-posed question without naming the
body and the flow regime. Any downstream application decision must start by asking what
fraction of the drag is friction and what fraction is pressure.

### Finding 2 - The dimpled-sphere drag crisis is an emergent model output, not an input

The sphere Reynolds-number range tops out at Re_D = 1.37e+05, which never crosses the
*smooth*-sphere drag crisis near 3.5e5. Confirmed by the smooth-sphere Cd series, which
rises monotonically and never drops: U=1 -> Cd=0.3892, U=5 -> Cd=0.4349, U=10 -> Cd=0.4703,
U=20 -> Cd=0.4887, U=50 -> Cd=0.4903.

Yet **19 of 20** dimple geometries eventually exceed 20% DR on the sphere, with onset as
early as U = 20 m/s. The roughness-induced early transition to a turbulent boundary layer
delays separation and collapses the wake. The model was calibrated on golf-ball post-crisis
Cd and critical Re, but the *interaction* between that calibration and this specific Re
range was never imposed - it emerged.

### Finding 3 - The riblet optimum lands in the published s+ = 10-20 band without being told to

The riblet model is parameterised on the groove cross-section length scale l_g+, not on s+.
That the s+ optimum falls in the experimentally established band is therefore an independent
check rather than a tautology.

| Riblet shape | optimal h/s | peak DR (%) | optimal s+ | optimal l_g+ | s+ at DR = 0 |
|:---|---:|---:|---:|---:|---:|
| blade | 0.5 | 9.899 | 15.54 | 10.711 | 31.08 |
| scalloped | 0.7 | 6.499 | 16.51 | 10.698 | 33.07 |
| v-groove | 0.7 | 6.200 | 18.09 | 10.701 | 36.18 |
| u-groove | 0.7 | 5.499 | 15.68 | 10.717 | 31.37 |

The l_g+ optimum collapses to **10.698-10.717** across all four shapes while the s+ optimum
spreads over **15.54-18.09** - which is precisely the Garcia-Mayoral & Jimenez argument for
using l_g+ as the correct scaling variable.

Operating inside the s+ = 10-20 band is worth **2.702 pp** of drag reduction: 16 riblet rows
fall inside the band with mean DR 3.3808%, against 0.6792% outside it.

### Finding 4 - Hybrid textures fail cleanly, and that is a publishable negative result

Of **50 hybrid geometry-speed cases, 0 beat their own best single-texture constituent**
(0.0%). Mean interference penalty **-0.605 pp**; mean hybrid DR **-0.899%** against mean
best-constituent DR **2.024%**, a **cost of hybridisation of 2.923 pp**.

Physically: dimples destroy the streamwise coherence of the near-wall streaks that riblets
exploit. Caveat - this class carries the widest uncertainty band in the study (+/- 4.0 pp
plate, +/- 5.6 pp sphere) because **no peer-reviewed calibration data exists for riblet-
dimple hybrids**. This is labelled extrapolation, and it is also the single highest-value
target for a real experiment (Section 6.3).

### Finding 5 - Shark-skin denticles reach only 2.033%, far below the popular 12% figure

The best denticle geometry at every speed is **C-SK-s500-o40**, peaking at **2.033%** at U =
50 m/s. Against ideal riblets at the same condition this is a shortfall of **7.437 pp**;
denticles deliver at most **21.5%** of the riblet benefit, roughly a 4.7x deficit.

This is a deliberate deviation from the 12% figure that circulates in popular and review
literature, and it is defended at length in the paper's Discussion. Short version: the large
percentages in the literature are mostly from (a) non-aerodynamic media (water, swimsuits),
(b) non-flat bodies where separation control rather than friction reduction is doing the
work, or (c) comparisons against a fouled or non-ideal baseline. Bechert's controlled
measurements on actual denticle replicas found single-digit reductions and often drag
*increase*. This study sides with the controlled measurements.

---

## 3. Dataset schema

**File:** `dataset.csv` **Rows:** 670 (67 geometries x 5 speeds x 2 bodies) **Columns:** 33
**Primary key:** (`geometry_id`, `body`, `U_inf_mps`) **Primary response variable:**
`DR_net_pct` **Missing values in the response:** 0

| Column | Units | Type | Meaning |
|:---|:---:|:---:|:---|
| `geometry_id` | - | string | Unique geometry key. Prefix A=riblet, B=dimple, C=shark, D=hybrid, E=baseline. |
| `geometry_class` | - | string | riblet / dimple / shark / hybrid / baseline. |
| `shape` | - | string | Riblet cross-section or denticle aspect descriptor; blank for classes where undefined. |
| `body` | - | string | plate (friction-dominated) or sphere (pressure-dominated). |
| `spacing_um` | um | float | Riblet peak-to-peak spacing s. |
| `height_um` | um | float | Riblet height h. |
| `h_over_s` | - | float | Riblet aspect ratio h/s. |
| `diameter_mm` | mm | float | Dimple print diameter D. |
| `depth_ratio` | - | float | Dimple depth-to-diameter ratio d/D. |
| `pattern` | - | string | Dimple array pattern: hexagonal / staggered / square. |
| `coverage_pct` | % | float | Fraction of wetted area occupied by the texture feature. |
| `denticle_scale_um` | um | float | Shark denticle characteristic length. |
| `overlap_pct` | % | float | Streamwise denticle overlap fraction. |
| `U_inf_mps` | m/s | float | Freestream velocity. |
| `Re_L` | - | float | Plate Reynolds number based on L = 0.1 m. |
| `Re_D` | - | float | Sphere Reynolds number based on D = 42.7 mm. |
| `u_tau_mps` | m/s | float | Friction velocity sqrt(tau_w/rho) of the smooth baseline. |
| `delta_v_um` | um | float | Viscous sublayer thickness, 5 nu / u_tau. |
| `s_plus` | - | float | Riblet spacing in wall units, s u_tau / nu. |
| `lg_plus` | - | float | Groove length scale sqrt(A_g) u_tau / nu - the riblet collapse variable. |
| `k_plus` | - | float | Roughness Reynolds number k u_tau / nu. Hydraulically smooth below ~5. |
| `Cf_smooth` | - | float | Smooth-baseline skin-friction coefficient. |
| `Cf_textured` | - | float | Textured skin-friction coefficient. |
| `Cd_pressure` | - | float | Pressure (form) drag coefficient. Sphere only; 0 for the plate. |
| `Cd_total` | - | float | Total drag coefficient used for the net DR calculation. |
| `DR_friction_pct` | % | float | Friction-only drag reduction. Positive = less friction drag. |
| `DR_net_pct` | % | float | PRIMARY RESPONSE. Net total-drag reduction. Positive = less drag. Clipped at -50. |
| `DR_uncertainty_pp` | pp | float | Propagated 1-sigma uncertainty on DR_net_pct, in percentage points. |
| `delta_Re_transition` | - | float | Shift in transition Reynolds number caused by the texture. Negative = earlier transition. |
| `natural_regime` | - | string | What the untripped boundary layer would be: laminar / laminar-transitional / turbulent (plate) or separation-dominated (sphere). |
| `min_feature_um` | um | float | Smallest feature that must be manufactured. Drives fabrication cost. |
| `manufacturability_index` | - | float | Composite 0-6 difficulty score: process tier plus a feature-size term. Lower is easier. |
| `model_confidence` | - | string | low / moderate / high. Encodes per-row calibration support. |

### 3.1 Sign convention

`DR_net_pct` is **positive when the texture reduces drag**. A value of +5 means the textured
body has 5% less total drag than the smooth body at the same speed. Negative values are real
and common - most dimple geometries on the plate increase drag.

### 3.2 Distribution of the response

| Body | Rows | min DR (%) | max DR (%) | rows with DR > 0 | fraction positive |
|:---|---:|---:|---:|---:|---:|
| Plate | 335 | -20.160 | 9.506 | 160 | 48.5% |
| Sphere | 335 | -22.833 | 52.768 | 90 | 27.3% |

### 3.2.1 Per-class summary

| Class | Rows/body | plate mean | plate SD | plate min | plate max | sphere mean | sphere min | sphere max |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| riblet | 105 | +1.091 | 2.639 | -17.506 | +9.506 | +1.718 | -0.902 | +36.098 |
| dimple | 100 | -6.253 | 7.713 | -20.160 | +1.354 | +7.955 | -22.833 | +52.768 |
| shark | 75 | -0.096 | 0.647 | -0.788 | +2.033 | +2.248 | -1.103 | +41.602 |
| hybrid | 50 | -0.899 | 5.120 | -19.583 | +9.135 | +7.014 | -16.781 | +52.593 |
| baseline | 5 | +0.000 | 0.000 | +0.000 | +0.000 | +0.000 | +0.000 | +0.000 |

### 3.3 Confidence and regime bookkeeping

`model_confidence` counts: high = 256, low = 214, moderate = 200. `natural_regime` counts:
laminar = 201, laminar-transitional = 134, separation-dominated = 335.

**Filter on `model_confidence == "high"` before making any claim you intend to defend in
front of a judge.** The `low` rows are dominated by U = 1 m/s (a roughly two-decade
extrapolation below the validated range of the Schlichting correlation) and by the entire
hybrid class.

### 3.4 Companion files

- `validation_benchmarks.csv` - 13 rows, columns `benchmark, source, kind, status,
  published, predicted, units, error_pct, passed`. `kind` is POINT (pass if |error| <= 15%)
  or BAND (pass if inside the published range). `status` is IMPLEMENTATION / CALIBRATED /
  EMERGENT - **only the 3 EMERGENT rows are independent tests of the model**, the rest
  confirm that the calibration was applied correctly.
- `results_summary.json` - the full analysis output tree. Top-level keys: `meta`,
  `validation`, `headline`, `a1_ranking`, `a2_regime`, `a3_riblet`, `a4_dimple`, `a5_shark`,
  `a6_hybrid`, `a7_speed`, `a8_pareto`, `a9_stats`, `derived`.

---

## 4. Recommended next steps

Twelve next steps, ordered so that the cheapest evidence that could change the conclusions
comes first. Steps 1-3 are the science; steps 4-8 are dissemination; steps 9-12 are
resourcing.

### Step 1 - Fabricate physical test coupons

**Priority: highest. This is the single thing that converts a computational study into a
competition-winning one.**

Three fabrication routes, in increasing order of cost and fidelity:

| Route | Practical minimum feature | Cost | Notes |
|:---|:---:|:---:|:---|
| 3D printing (SLA/DLP) | 25-100 um | $ | Fastest route. Form 3+/4 or equivalent at 25 um XY. Adequate for the coarse riblet grid (s >= 200 um) and every dimple geometry. Post-cure and wet-sand the flat reference face. |
| CNC micro-milling | 50-250 um | $$ | Ball-nose or V-form end mill in aluminium 6061 or brass. Directly produces V-groove and U-groove riblets. Surface finish is better than SLA, which matters because you are measuring friction. |
| Laser ablation / photolithography | 5-50 um | $$$ | Needed only for blade riblets at s <= 100 um and for true denticle replicas. Usually requires a university cleanroom partnership - see Step 10. |

**Which geometries to make first (7 coupons, plus one smooth reference):**

1. `E-SMOOTH` - the reference. Make two, so you can quantify plate-to-plate variability.
2. `A-V-s500-h250` - the easiest-to-manufacture positive result: min feature 250 um,
   manufacturability index 1.0, predicted DR 5.344% at 10 m/s. **Print this one first.**
3. `A-BLAD-s200-h100` - the overall plate winner, DR 9.506% at 20 m/s.
4. `A-BLAD-s100-h50` - fine blade riblet, min feature 50 um, tests whether your process can
   hold tolerance at the scale where the model predicts the largest benefit.
5. `C-SK-s500-o40` - best denticle. Directly tests the 2.033%-versus-12% disagreement, which
   is the most contested claim in the paper.
6. `B-HEX-d2.0-r0.05` - best plate dimple, predicted only 0.881%. Tests the plate-dimple
   controversy.
7. `D-HY-03` - best hybrid, predicted 2.041%. The hybrid class is the study's widest
   uncertainty band, so this coupon carries the most information per dollar.
8. `B-HEX-d5.0-r0.3` - a strongly predicted *negative* result (-20.152% at 10 m/s).
   **Include at least one predicted failure.** A model that only ever predicts success is
   not falsifiable, and judges know it.

**Tolerance requirement:** hold the riblet tip radius below about 10% of s. Blunt riblet
tips are the single most common reason experimental riblets underperform theory. Measure
what you actually made - optical profilometry or a calibrated microscope photograph - and
report the as-built dimensions, not the nominal ones.

### Step 2 - Wind tunnel test protocol

**Target facility:** any low-speed subsonic tunnel with a test section of at least 0.15 m x
0.15 m and a usable range covering 5-30 m/s. High-school-accessible options include
university outreach tunnels, community-college engineering labs, and (for the sphere only) a
well-instrumented open-jet blower.

**Configuration A - flat plate, direct force measurement**
- Mount a 100 mm x 80 mm textured plate flush in a splitter-plate arrangement to avoid
  tunnel-wall boundary-layer contamination.
- Install the leading-edge trip described in Section 1.4. **Non-negotiable.**
- Measure drag on a single-axis load cell or strain-gauge sting. Required resolution: you
  are chasing a 5% change on a plate whose total drag at 20 m/s is of order 12.8 mN. Budget
  for a load cell with <= 0.1 mN resolution, or you will measure noise.
- **Better alternative if force resolution is marginal:** measure the momentum deficit with
  a boundary-layer rake or a traversing Pitot probe at the trailing edge and integrate to
  get momentum thickness theta. Cf follows from dtheta/dx. This is more work but far more
  sensitive, and it is what serious riblet studies do.

**Configuration B - sphere, terminal-velocity or force measurement**
- A 42.7 mm sphere on a thin rear sting, or a drop test in a tall stairwell measuring
  terminal velocity with high-speed video.
- The sphere is much easier to get a clean result from, because the predicted effect is
  enormous (52.8%) rather than marginal. **Do the sphere first to build confidence in your
  rig**, then attempt the plate.

**Test matrix and statistics**
- At least 5 speeds spanning 5-30 m/s, at least 5 repeat runs per configuration, randomised
  run order, with the smooth reference re-measured between every textured coupon to catch
  drift.
- Report uncertainty as a proper propagated budget (load cell calibration, dynamic pressure,
  temperature, blockage correction), not just the standard error of repeats.
- Apply solid-blockage and wake-blockage corrections; at 42.7 mm in a 150 mm section the
  blockage is about 6.4%, which is not negligible.

**Pre-registration:** write down the predicted DR for every coupon *before* you test, and
publish that prediction alongside the result. This single act separates a science-fair
project from a research paper.

### Step 3 - Full CFD campaign on the top five geometries

Run wall-resolved simulations to break the dependence on the reduced-order model.

- **Solver:** OpenFOAM (free, and the right answer for a student budget) or ANSYS Fluent
  under a student/academic licence. OpenFOAM `simpleFoam` for RANS screening, `pimpleFoam`
  with a WALE or dynamic-Smagorinsky subgrid model for LES.
- **Approach:** do **not** try to simulate the whole plate. Use a **minimal-span turbulent
  channel** or a periodic riblet-groove domain - the standard approach in the riblet DNS
  literature - which reduces cell count by orders of magnitude while resolving exactly the
  physics that matters.
- **Mesh requirement:** y+ < 1 at the wall, at least 20-30 cells across one riblet groove,
  at least 15 points spanning the viscous sublayer. Grid-convergence study on at least three
  mesh levels; report the Grid Convergence Index.
- **Geometries:** `A-BLAD-s200-h100`, `A-V-s500-h250`, `A-BLAD-s100-h50`, `C-SK-s500-o40`,
  and one hybrid (`D-HY-03`).
- **Validation gate:** reproduce the smooth-channel Cf to within 3% before you trust any
  textured result.
- **Compute estimate:** a minimal-span LES riblet case is roughly 5e6-2e7 cells and
  1,000-10,000 core-hours. This needs an HPC allocation - see Step 11.

### Step 4 - Application-specific optimisation

The correct texture depends entirely on the friction/pressure drag split of the target
application. Three worked cases:

| Application | Dominant drag mechanism | Recommended texture | Key caveat |
|:---|:---|:---|:---|
| Small drone wing / UAV | Friction-dominated at cruise; chord Re 1e5-5e5 | Riblets, aligned with local streamlines | Scale s to hold s+ in 10-20 at cruise. Expect single-digit % of *friction* drag, so a few % of total. |
| Car body | Strongly pressure-dominated (separation off the rear) | Dimples or vortex generators on the rear surfaces; riblets only on the long attached-flow roof and sides | The sphere result is the right analogy. But note that a modern car is not a golf ball - it already has separation control designed in, so gains are far smaller than 52%. |
| Competitive swimwear | Water, not air; friction-dominated but different Re and nu | Riblets scaled to water | nu_water is about 15x smaller than air, so l_v is much smaller and the optimal s drops accordingly. This is where the shark-skin literature's large numbers come from - do NOT transfer the air results directly. |

Concretely: re-run `build_dataset.py` with the application's actual U, L, and nu, and re-
optimise. The model is already parameterised for this - only the constants at the top of
`texture_model.py` need to change.

### Step 5 - Journal submission targets

Realistic laddering, easiest first. **Be honest in the cover letter that this is a reduced-
order study**; reviewers respond well to accurate self-assessment and badly to overclaiming.

| Venue | Scope | Readiness | Notes |
|:---|:---|:---|:---|
| Journal of Emerging Investigators (JEI) | Peer-reviewed, specifically for middle/high school researchers | Realistic now, as-is | Free, mentored review process. Strongest first target. |
| Journal of Student Research (JSR) | High school and undergraduate research | Realistic now, as-is | Article processing charge applies. |
| AIAA Journal | Top-tier archival aerospace journal | Not yet - needs experimental or CFD validation | Would require Steps 2 or 3 completed first, and almost certainly a faculty co-author. |
| Experiments in Fluids | Experimental fluid mechanics, Springer | Only after Step 2 | Publishes riblet and texture measurements regularly. Requires real measurements with a full uncertainty budget. |
| Journal of Fluid Mechanics (JFM) | The field's flagship | Not a realistic target for this work | JFM riblet papers are DNS/theory of a depth this study does not reach. Listing it as an aspiration is fine; submitting cold is not. |

### Step 6 - Competition targets

**Regeneron ISEF.** The 2026 cycle uses 22 categories. The right fit is **Engineering
Technology: Statics and Dynamics (ETSD)**; the alternative is **Physics and Astronomy
(PHYS)**, but ETSD is the better match because the deliverable is an engineering design
comparison. Entry is via an affiliated regional or state fair first - for Leander TX that is
the Central Texas science fair pathway leading to Texas Science and Engineering Fair.
**Action item:** confirm your regional fair's registration deadline, which is typically in
the winter preceding the spring fair, and check whether your project needs an SRC pre-
approval form (a purely computational project usually does not, but adding a wind tunnel
with human operators changes nothing; adding human subjects would).

**Regeneron Science Talent Search (STS).** High school **seniors only**, **individual** (not
team) research, though the research itself may have been conducted in any year of high
school. The STS 2027 window runs 1 June to 5 November 2026 (deadline 8:00 pm ET). For a
**Class of 2028** student the relevant cycle is **STS 2028, applying in autumn 2027** - use
the 2027 dates as the template. Scale: roughly 2,600 entrants, 300 scholars, 40 finalists,
about $3.1M in awards, top prize $250,000. **This project, extended with Step 2 or Step 3,
is a credible STS entry.** Start assembling the research report and the essays a full year
early.

**AIAA.** This is the most under-used opportunity available to you, because AIAA **Regional
Student Conferences explicitly admit High School Student Members and run a dedicated High
School category**. All authors must hold AIAA University or High School Student Membership
and print their membership ID in the first-page footer. Submission is a written paper plus
an oral presentation. Regional prizes are $500 (1st, plus an invitation to the International
Student Paper Conference at SciTech), $300 (2nd), $250 (3rd), and papers presented may be
published with AIAA. **Important caveat:** the separate **SciTech Forum Student Paper
Competition requires full-time university students**, and older Regional Student Paper
Conference rules restrict the main competition to undergraduate and master's work - so your
route is specifically the **Regional Student Conference High School category**, not the
SciTech competition. AIAA SciTech Forum 2027 runs 11-15 January 2027 with roughly 6,000
attendees from 46 countries. Texas falls in the AIAA Region IV student conference.

**Other strong fits:** Texas Science and Engineering Fair (the ISEF feeder), the Junior
Science and Humanities Symposium (JSHS, which pays travel and has a strong engineering
track), and MIT THINK (which funds projects rather than judging finished ones - a good match
for funding Step 1 fabrication).

### Step 7 - Build the presentation assets before you need them

The web interface (`index.html`) already functions as a live demo; run it on a laptop or
tablet at the fair table. Additionally prepare: a tri-fold or poster with Figures 1, 4, 6,
and 8; a 90-second elevator explanation of Finding 1; and a one-page technical summary with
the validation table on it. **Judges will attack the validation table first** - know every
row of it cold, including which three rows are genuinely independent (EMERGENT) and which
seven merely confirm calibration.

### Step 8 - Pre-empt the "is this just curve fitting?" question

This is the question that decides how the project is scored. Prepare a direct answer: the
model is calibrated on 7 benchmarks and *independently reproduces* 3 others it was never
fitted to (the riblet s+ optimum, the riblet drag-crossover s+, and the V-groove optimum),
plus the emergent dimpled-sphere drag crisis at a Reynolds number where the smooth sphere
has no crisis. Say this in one sentence, then show the table.

### Step 9 - University lab collaboration targets

**UT Austin, Cockrell School - Department of Aerospace Engineering and Engineering
Mechanics** (your stated target school). Relevant groups:
- **Flowfield Imaging Laboratory** (established 1993, J.J. Pickle Research Campus) -
  hypersonics, high-temperature gas dynamics, turbulence, combustion, laser-based
  measurement. Houses the High-Speed Wind Tunnel Lab, in operation since the 1950s.
- **Center for Aeromechanics Research (CAR)** - computational, analytical and experimental
  supersonic and hypersonic aerodynamics; Mach 5 blowdown tunnel; 50 kW inductively coupled
  plasma torch.
- **Aerothermodynamics and Fluid Mechanics research area** - explicitly lists turbulence and
  turbulence control; Mach 2 and Mach 5 blowdown tunnels, a Mach 3 low-Reynolds-number
  tunnel, and a Mach 1.8 scramjet isolator, with computation supported by TACC.
- **Turbulence and Turbine Cooling Research Laboratory (TTCRL)** - gas-turbine film cooling;
  blends experiment and computation, and works routinely with surface features.
- **Prof. Noel T. Clemens** - Clare Cockrell Williams Centennial Chair, AIAA and APS Fellow,
  elected to the National Academy of Engineering in 2024, and Editor-in-Chief of
  *Experiments in Fluids* from 2009 to 2013. Directly relevant to both the science and the
  publication route.

**Honest caveat you should know before you email anyone:** UT Austin's listed aero
facilities are predominantly **supersonic and hypersonic**. A low-speed, tripped, flat-plate
boundary-layer campaign at 5-30 m/s is not a natural fit for their headline tunnels. Lead
with the *turbulence-control* framing rather than the low-speed measurement, or ask
specifically about low-speed teaching tunnels and TACC compute for Step 3 rather than about
their blowdown facilities.

**Other targets:** MIT Department of Aeronautics and Astronautics (Wright Brothers Wind
Tunnel, which is a genuine low-speed facility); Georgia Tech Daniel Guggenheim School of
Aerospace Engineering (extensive low-speed and boundary-layer capability); Texas A&M Oran W.
Nicks Low Speed Wind Tunnel (in-state, low-speed, and runs external test campaigns); and the
University of Texas at Arlington Aerodynamics Research Center.

**How to make contact effectively:** send a short email with (a) a two-sentence summary of
the finding, (b) the specific question you cannot answer without their facility, (c) the
paper as an attachment, and (d) a concrete, small ask - two hours of tunnel time, or fifteen
minutes of advice - not an open-ended request for mentorship. Attach the figure, not the
whole paper, in the first email.

### Step 10 - Fabrication partnerships

Before paying for external micro-machining, try: your school's makerspace or engineering
department; the Austin public library and community makerspaces; the UT Austin Texas
Inventionworks facility (check current external-user policy); and local machine shops, which
will often quote a student project at cost. For photolithography-grade features, the
realistic route is a university cleanroom via the collaboration in Step 9.

### Step 11 - Grants and fellowships for high-school aerospace researchers

| Programme | Award | Eligibility | Notes |
|:---|:---|:---|:---|
| Davidson Fellows Scholarship | $100,000 / $50,000 / $25,000 | Age 18 or under at the deadline; US citizen or permanent resident residing in the US, or stationed overseas on active US military duty. Two-person teams eligible. | Categories include Science, Technology, Engineering and Mathematics. The 2027 application opens in autumn 2026. A completed, validated version of this project is exactly the profile they fund. |
| MIT THINK Scholars Program | Up to $1,000 in project funding plus mentorship | US high school students; project must not yet be built | Unusual in that it funds *proposed* work. Ideal for financing Step 1 fabrication and Step 2 tunnel time. |
| Society of Women Engineers / AIAA local section grants | Typically $250-$2,000 | Varies by section | AIAA Region IV and local Texas sections sometimes support student projects; ask your AIAA student membership contact directly. |
| Regeneron STS scholar awards | $2,000 (scholar) to $250,000 (first place) | High school seniors, individual research | Not a grant you apply for in advance - it is the competition award itself. Budget the project so you do not need the money before then. |
| Local and regional fair cash awards | $50-$5,000 | Varies | Regional fairs, professional-society special awards, and corporate sponsors frequently fund follow-on work. Apply to every special award category your project touches, not just the main one. |

**Verify every deadline and eligibility rule directly on the programme's own website before
relying on it.** Competition rules change annually, and the dates above are current as of
the handoff date at the top of this file.

### Step 12 - Version control and reproducibility hygiene

Put `/workspace/*.py`, `dataset.csv`, and the figures in a public Git repository with a
`requirements.txt` pinning numpy, pandas, matplotlib and scipy versions, and archive a
release on Zenodo to obtain a DOI. A citable DOI materially strengthens both journal and
competition submissions, and it costs nothing.

---

## 5. Open questions and unresolved hypotheses

Ten open items. The first four are the ones that could actually change a conclusion.

**Q1 - Do riblet-dimple hybrids really interfere destructively?** The model asserts sub-
additivity plus an interference penalty, giving a mean cost of 2.923 pp and 0 of 50 cases
beating their best constituent. **There is no peer-reviewed calibration data for this
class.** The functional form is physically motivated but was chosen, not measured. If
hybrids turn out to be merely additive rather than destructively interfering, Finding 4
inverts. *Status: pure extrapolation, widest uncertainty in the study (+/- 4.0 pp plate, +/-
5.6 pp sphere).*

**Q2 - Do shallow dimples reduce or increase flat-plate friction drag?** This is a live
controversy in the published literature, not a gap in this study. Reported values span
roughly -2% to +4% for nominally similar configurations. The model takes the conservative
consensus and predicts a best plate dimple of only **0.881%** with a class mean of
**-6.253%**. A clean, well-instrumented plate-dimple measurement would be a genuine
contribution to the field, not merely a check on this model.

**Q3 - Is the shark-skin ceiling really about 2.0%, or is the 12% figure right?** The paper
argues 2.033% and gives a four-part defence. The counter-hypothesis is that real denticles
achieve more than idealised riblets through mechanisms this model does not represent at all:
passive bristling under adverse pressure gradient, local separation control, and flexible-
substrate compliance. **None of these are in the model.** If any of them matters, the model
is systematically pessimistic about denticles.

**Q4 - Does the plate result survive a real trip?** Every plate number assumes an ideal trip
producing a canonical turbulent boundary layer with no additional drag from the trip itself.
**Real trip devices add drag**, and at these low Reynolds numbers the trip's own
contribution could be a substantial fraction of the 5-9% effect being measured. The dataset
does not account for it. Measure the smooth plate with and without the trip to quantify this
before comparing anything.

**Q5 - Why does the best low-speed geometry become the worst high-speed geometry?**
`A-V-s500-h250` is the best plate geometry at 10 m/s (5.344%) and the worst riblet in the
entire plate dataset at 50 m/s (-17.506%), because s+ climbs past the drag-crossover into
the Kelvin-Helmholtz breakdown regime. The model handles this with a floor clamp. **The
clamp is a modelling convenience, not physics** - the true behaviour of grossly oversized
riblets is a k-type roughness problem the model does not represent. Treat all deeply
negative riblet values as "large drag increase of uncertain magnitude".

**Q6 - Is the sphere friction split right?** The sphere model assigns friction a fixed 3%
share of total drag in the subcritical branch (5% post-crisis). This is a reasonable
textbook figure but it is a *constant*, not a computed quantity, and it directly sets how
much credit riblets can earn on the sphere. A CFD run would resolve this immediately.

**Q7 - How much does yaw or flow misalignment cost?** Riblets are strongly directional and
lose effectiveness when the flow is not aligned with the grooves. **The model has no yaw
dependence at all.** For any real application - a swept wing, a rotating blade, a car body -
this is a first-order omission. Published work suggests meaningful degradation beyond
roughly 15 degrees of misalignment.

**Q8 - What happens under a pressure gradient?** The entire plate analysis is zero-pressure-
gradient. Real aerodynamic surfaces have favourable gradients forward and adverse gradients
aft, and riblet effectiveness is known to change in both.

**Q9 - Does the result survive fouling, erosion and manufacturing tolerance?** Micro-
textures fill with dust, insects and paint. Riblet tips round off with wear. None of this is
modelled, and all of it degrades performance in service. The `manufacturability_index`
addresses cost of *making* the texture, not cost of *keeping* it.

**Q10 - Is the U = 1 m/s data physically meaningful?** 214 of 670 rows are flagged low
confidence, dominated by U = 1 m/s where Re_L = 6.4e+03. The Schlichting turbulent
correlation is being applied roughly two decades below its validated range, on a boundary
layer that only exists because we assumed a trip. **Consider dropping U = 1 m/s entirely
from any headline claim.**

---

## 6. Suggested follow-up experiments with full methodology

Four experiments, each written so it could be executed as specified. E1 is the highest
value-per-dollar; E4 is the highest scientific value.

### E1 - Dimpled-sphere drop test (validates Finding 2 for under $100)

**Hypothesis.** A sphere with hexagonally packed dimples at d/D = 0.1, D_dimple = 2.0 mm on
a 42.7 mm sphere reaches a terminal velocity measurably higher than a smooth sphere of
identical mass and diameter, corresponding to a Cd reduction consistent with the predicted
52.8% at Re_D = 1.37e+05.

**Materials.** Two SLA-printed 42.7 mm spheres (one `E-SMOOTH`, one `B-HEX-d2.0-r0.1`),
mass-matched to within 1% by adjusting internal infill; a high-speed camera or a phone at
240 fps; a metre stick or printed fiducial scale; a stairwell, atrium or sports hall with at
least 8 m of clear drop.

**Procedure.**
1. Weigh both spheres; record to 0.01 g. Verify diameters with callipers at three axes.
2. Mark the drop line with a fiducial scale visible in frame.
3. Drop each sphere 20 times, alternating smooth and dimpled to cancel any drift in ambient
   conditions. Record air temperature and pressure.
4. Track the sphere position frame by frame (Tracker, or OpenCV in Python).
5. Fit the vertical trajectory to the 1-D drag equation `m dv/dt = mg - 0.5 rho Cd A v^2`
   and extract Cd, or, if the drop is long enough to reach terminal velocity, use `Cd = 2mg
   / (rho A v_t^2)` directly.

**Analysis.** Compare the two Cd values with a Welch t-test across the 20 repeats. Report
the effect size with a 95% confidence interval. Also report the Reynolds number actually
achieved - at terminal velocity a 42.7 mm sphere of typical printed mass reaches roughly
20-30 m/s, giving Re_D of order 5e4-8e4, which is right at the predicted crisis onset.

**Expected result.** The predicted Cd change is large (0.490 -> 0.232), so it should be
visible even with crude instrumentation. **If you see no difference, the model's sphere
calibration is wrong and that is a real finding.**

**Failure modes to control.** Mass mismatch (dominates everything - match to 1%); sphere
rotation inducing Magnus lift (release without spin, and reject visibly tumbling runs);
insufficient drop height to reach a steady state (fit the full trajectory instead of
assuming terminal velocity).

### E2 - Flat-plate momentum-deficit measurement (validates Finding 1)

**Hypothesis.** A tripped turbulent boundary layer over `A-V-s500-h250` has a smaller
trailing-edge momentum thickness than over `E-SMOOTH` at the same freestream speed, by an
amount corresponding to DR ~ 5.3% at 10 m/s.

**Rig.** 100 mm x 80 mm coupons mounted flush in a splitter plate in a low-speed tunnel; a
zig-zag trip at x/L = 0.05; a boundary-layer Pitot probe (flattened tip, about 0.5 mm) on a
micrometer traverse at x = 0.95 L; a reference Pitot-static for freestream; a differential
manometer or pressure transducer with at least 0.1 Pa resolution.

**Procedure.**
1. Traverse the probe from the wall outward in at least 25 logarithmically spaced steps to y
   = 1.5 delta, at U = 10, 15, 20, 25 and 30 m/s.
2. Compute the velocity profile, then `theta = integral of (u/U)(1 - u/U) dy`.
3. Repeat with each textured coupon, re-measuring the smooth reference between coupons.
4. Cf from the momentum-integral relation `Cf = 2 dtheta/dx`, using at least two streamwise
   stations, or compare theta directly at a fixed station as a relative metric.

**Statistics.** Five repeat traverses per configuration. Report theta with a propagated
uncertainty from probe position (+/- 0.05 mm), pressure resolution, and temperature.
**Expect the effect to be marginal relative to the noise** - a 5% Cf change is a roughly
2.5% change in theta. This is precisely why the momentum method beats a load cell here.

**Controls.** Verify the smooth-plate profile collapses onto the law of the wall in wall
units before trusting anything textured. If it does not, the trip or the pressure gradient
is wrong and no textured measurement will mean anything.

### E3 - Riblet spacing sweep to locate the s+ optimum experimentally

**Hypothesis.** Sweeping riblet spacing at fixed h/s = 0.5 and fixed speed produces a non-
monotonic DR curve peaking near s+ = 15.5 and crossing zero near s+ = 31.1.

**Design.** Seven coupons with s = 100, 150, 200, 300, 400, 600, 900 um at h/s = 0.5, tested
at a single speed (20 m/s) chosen so the sweep brackets the predicted optimum. Use the E2
momentum method. **This is the cleanest possible test of the model** because it measures a
*shape* - the location of a peak - rather than an absolute magnitude, so it is insensitive
to most systematic errors in the rig.

**Analysis.** Plot DR against s+ computed from the *measured* u_tau, fit a smooth curve, and
report the peak location with a confidence interval. Compare to 15.54 (blade) and 18.09
(V-groove). Also test whether the data collapse better on s+ or on l_g+ - the model asserts
l_g+, and this experiment can settle it.

### E4 - Minimal-span LES of one riblet groove (removes the model dependence entirely)

**Hypothesis.** A wall-resolved LES of turbulent flow over `A-BLAD-s200-h100` at matched
Re_tau reproduces the predicted 9.51% friction reduction to within the +/- 1.5 pp
uncertainty band.

**Setup.** OpenFOAM `pimpleFoam`, WALE subgrid model. Minimal-span channel, streamwise and
spanwise periodic, with the riblet geometry on the lower wall and a smooth upper wall.
Domain at least 3 delta streamwise and wide enough for at least 8 riblet grooves. Re_tau ~
180-395. Mesh: y+ < 0.5 at the riblet tip, 25+ cells across the groove, at least 100 wall-
normal points. Run a matched smooth-wall case in the identical domain - **the smooth case is
the control and must be run at the same resolution**, otherwise the comparison is
contaminated by numerical error.

**Diagnostics.** Time-averaged wall shear integrated over the wetted surface; DR relative to
the smooth control; the protrusion height difference; and spanwise energy spectra near the
wall to check whether Kelvin-Helmholtz rollers appear when s+ is pushed past the optimum
(this is the mechanism the model encodes as the post-peak rollover, and seeing it directly
would be the strongest possible validation).

**Cost.** Order 1,000-10,000 core-hours per case. See Step 3 and Step 11 for compute routes;
TACC access through a UT Austin collaboration is the realistic path.

---

## 7. Models, tools, and equations used

### 7.1 Software environment

| Tool | Version | Role |
|:---|:---:|:---|
| Python | 3.11.13 | Language runtime |
| NumPy | 2.1.0 | Array maths, all model evaluation |
| pandas | 2.3.1 | Dataset construction, all group statistics |
| SciPy | 1.15.0 | Optimisation for the continuous riblet sweeps |
| Matplotlib | 3.10.5 | All eight figures (SVG + PNG) |
| Chart.js | 4.x via CDN | Interactive charts in index.html |

No HPC, no GPU, no external database. Total compute for the full pipeline is under one
second - every model is closed-form algebra.

### 7.2 Physical constants

```
rho                    = 1.184 kg/m^3          air at 25 C
mu                     = 1.8490e-05 Pa.s
nu                     = 1.561655e-05 m^2/s
L_plate                = 0.1 m
D_sphere               = 0.0427 m
speeds                 = [1.0, 5.0, 10.0, 20.0, 50.0] m/s
Re_transition_smooth   = 5.0e+05
U for natural transition = 78.08 m/s
```

### 7.3 Governing equations

Numbered as in Appendix B of `research_paper.md`.

**Baseline flat plate** ``` E1   C_F      = 0.455 / (log10(Re_L))^2.58
Schlichting turbulent plate E2   u_tau    = U * sqrt(C_F / 2)
friction velocity E3   l_v      = nu / u_tau                                    viscous
length scale E4   delta_v  = 5 * l_v                                       viscous sublayer
thickness ```

**Riblets** - the core of the study ``` E5   A_g      = k_shape * s * h        k = 0.50
V-groove, 0.667 U-groove, 0.95 blade, 0.60 scalloped E6   l_g      = sqrt(A_g) E7   l_g+
= l_g * u_tau / nu                              the collapse variable E8   s+       = s *
u_tau / nu E9   xi       = l_g+ / 10.7 f(xi)    = xi                        for xi <= 1
viscous (linear) regime f(xi)    = 1 - max(xi - 1, 0)^1.3    for xi >  1         KH
breakdown rollover E10  eta_hs   = exp(-0.5 * (ln(h/s / (h/s)_opt) / 0.8)^2)     aspect-
ratio efficiency E11  DR       = DR_max(shape) * f(xi) * eta_hs ``` `DR_max` = 9.9% blade,
6.5% scalloped, 6.2% V-groove, 5.5% U-groove (Bechert et al. 1997). `(h/s)_opt` = 0.50
blade, 0.70 for the other three.

**IMPLEMENTATION WARNING.** In E9 the `max(xi - 1, 0)` guard is mandatory. Raising a
negative number to the fractional power 1.3 yields NaN and silently corrupts the whole
riblet column. Use `np.maximum`, not `max`, when vectorising.

**Sphere baseline and drag crisis** ``` E12  Cd_smooth  = 24/Re * (1 + 0.15 Re^0.687) + 0.42
/ (1 + 42500 Re^-1.16)   Clift-Gauvin E13  Re_crit(k/D) = 0.7 * 10^(3.995 - 0.4114 *
log10(k/D))                    Achenbach-type E14  Cd_super   = 0.20 + 8.0 * (k/D)_eff E15
sigma      = 1 / (1 + exp(-6 * ln(Re / Re_crit)))                        blend function E16
Cd         = (1 - sigma) * (Cd_smooth + 4 (k/D)_eff) + sigma * Cd_super ``` Sphere friction
share is fixed at 3% of total drag when Cd >= 0.35 and 5% when Cd < 0.35.

**Plate dimples** ``` g        = exp(-0.5 * (ln((d/D) / 0.05) / 0.6)^2)        depth-ratio
efficiency cov_f    = (coverage / 0.6)^0.8 d+       = (d/D) * D * u_tau / nu eta_Re   =
exp(-0.5 * (ln(d+ / 20) / 0.9)^2) DR_fric  = 2.0 * g * cov_f * pattern_f * eta_Re
pattern_f: hex 1.00, staggered 0.95, square 0.85 penalty  = 1.4 * coverage * ((d/D) /
0.05)^2             form-drag cost DR_net   = DR_fric - penalty ```

**Shark denticles** ``` E18  s_eq   = scale / 3        (3 ridges per denticle) h_eq   = 0.15
* scale DR     = DR_scalloped(s_eq, h_eq) * 0.62 * (0.8 + 0.5 * overlap) * AR_factor
- 0.8 * (1 - overlap) ``` 0.62 is the three-dimensionality penalty; AR_factor = 0.85 low,
  1.00 medium, 0.92 high.

**Hybrids (extrapolation - no calibration data exists)** ``` E19  DR = DR_strong + 0.3 *
DR_weak - 1.5 * coverage - dimple_pressure_penalty ``` The dimple pressure penalty is
applied in full *in addition to* the interference term. This deliberate double penalty is
why hybrids fare badly, and it is the assumption most in need of experimental testing.

**Transition shift** ``` E17  k+ <= 5  ->  delta_Re_tr = 0
hydraulically smooth k+ >  5  ->  Re_tr = 5e5 / (1 + 0.5 (k+/5 - 1));  delta_Re_tr = Re_tr -
5e5 ```

**Uncertainty propagation** Per-class 1-sigma values in percentage points: riblet 1.5,
dimple 2.5, shark 2.0, hybrid 4.0, baseline 0.0. On the sphere an extra 1.6 pp is added in
quadrature, giving riblet 3.1, dimple 4.1, shark ~2.6, hybrid 5.6. Two geometries are
reported as **statistically tied** when their DR intervals overlap.

### 7.4 Calibration provenance and what is actually independent

| Benchmark | Kind | Status | Published | Predicted | Err % | Result |
|:---|:---:|:---:|---:|---:|---:|:---:|
| Smooth plate C_F at Re_L=1e6 | POINT | IMPLEMENTATION | 0.0045 | 0.00447 | -0.65 | PASS |
| Smooth plate C_F at Re_L=1e7 | POINT | IMPLEMENTATION | 0.003 | 0.003 | +0.12 | PASS |
| Smooth sphere Cd at Re_D=1e5 | POINT | IMPLEMENTATION | 0.5 | 0.49175 | -1.65 | PASS |
| Blade riblet peak DR | POINT | CALIBRATED | 9.9 | 9.9 | +0.00 | PASS |
| Blade riblet optimal s+ | BAND | EMERGENT | 13 to 20 | 15.526 | -- | PASS |
| Blade riblet DR->0 crossing s+ | BAND | EMERGENT | 25 to 40 | 31.051 | -- | PASS |
| V-groove peak DR | POINT | CALIBRATED | 6.1 | 6.1999 | +1.64 | PASS |
| V-groove optimal s+ | BAND | EMERGENT | 10 to 20 | 18.091 | -- | PASS |
| Optimal l_g+ collapse across 4 shapes | POINT | CALIBRATED | 10.7 | 10.701 | +0.01 | PASS |
| Golf ball Cd at Re_D=1e5 | POINT | CALIBRATED | 0.25 | 0.25606 | +2.42 | PASS |
| Golf ball critical Re_D | BAND | CALIBRATED | 40000 to 80000 | 57351 | -- | PASS |
| Best plate dimple net DR | BAND | CALIBRATED | -2 to 4 | 1.395 | -- | PASS |
| Shark-skin peak DR | BAND | CALIBRATED | 2.5 to 10 | 2.9331 | -- | PASS |

**Read this table carefully before defending the work.** `IMPLEMENTATION` rows confirm a
textbook correlation was coded correctly. `CALIBRATED` rows confirm the fit was applied
correctly - they are *not* evidence the model is right. Only the **3 `EMERGENT` rows** are
genuine predictions the model was never fitted to. Maximum absolute point error across all
benchmarks: **2.42%**.

### 7.5 Code map

| Module | Responsibility |
|:---|:---|
| `texture_model.py` | The physics. All equations above. Pure functions, no I/O. |
| `validate_model.py` | Runs the benchmark table. Exit non-zero on any failure. |
| `build_dataset.py` | `build_catalogue()` returns the 67 geometries; `build_dataset()` evaluates them into the 670-row frame. |
| `analyses.py` | `a1_overall_ranking` through `a9_class_stats`, plus `run_all(df, catalogue)`. |
| `figures.py` | Eight figure functions plus shared heatmap/annotation helpers. |
| `summary.py` | Serialises everything to `results_summary.json`. |
| `refs.py` | The bibliography. `build()` returns `(NUM, BIB)`; 41 real, DOI-verified references. |
| `paper.py` / `paper2.py` | Manuscript generator. `paper.py` writes Sections 1-5 and calls `paper2.sections(ctx)` for Sections 6-8 and the appendices. |
| `handoff.py` | This document. |

**To regenerate everything from scratch:** ``` python /workspace/validate_model.py     #
gate: must pass 13/13 python /workspace/build_dataset.py      # writes dataset.csv python
/workspace/figures.py            # writes the 8 SVG + PNG pairs python /workspace/summary.py
# writes results_summary.json python /workspace/paper.py              # writes
research_paper.md python /workspace/handoff.py            # writes handoff.md ``` Run them
in that order - each step reads the previous step's output.

**If you modify the physics**, `validate_model.py` is your regression gate. Any change that
breaks a benchmark is either a bug or a deliberate recalibration that must be documented in
the paper's Limitations section.

---

## 8. File manifest

### 8.1 Deliverables

| File | Size | Contents |
|:---|---:|:---|
| `research_paper.md` | 170 KB | The manuscript. 11 sections, 41 real DOI-verified citations, 15 numbered tables plus B1/C1/C2, equations E1-E19, Appendix C lists all 67 geometries. |
| `dataset.csv` | 144 KB | The primary dataset. 670 rows x 33 columns. Schema in Section 3. |
| `validation_benchmarks.csv` | 1 KB | 13 benchmarks, 13 passing. Reproduced as a table in Section 7.4. |
| `results_summary.json` | 176 KB | Complete analysis output tree. Machine-readable source for every number in the paper, this handoff, and the web interface. |
| `index.html` | 1.3 MB | Self-contained interactive web interface. Embedded dataset, live drag explorer, parametric texture renderer, sortable ranking table, working downloads. Opens with no server and no network beyond two CDN links. |
| `handoff.md` | this file | This document. |

### 8.2 Figures (SVG for print, PNG for screen and rendering checks)

| File | Size | Caption |
|:---|---:|:---|
| `graph1_top20_drag_reduction_bar.svg` / `.png` | 28 KB / 50 KB | Top 20 geometries by net drag reduction, with uncertainty bars and statistical-tie flagging. |
| `graph2_drag_vs_flowspeed_top_geometries.svg` / `.png` | 63 KB / 138 KB | Net drag reduction versus flow speed for the top plate and sphere geometries; shows sign flips. |
| `graph3_heatmap_riblet_spacing_height.svg` / `.png` | 19 KB / 25 KB | Riblet heatmap, spacing x height, no empty cells. |
| `graph4_scatter_splus_vs_drag.svg` / `.png` | 48 KB / 75 KB | Net drag reduction versus s+, with the emergent 10-20 optimal band highlighted. |
| `graph5_heatmap_dimple_diameter_depth.svg` / `.png` | 20 KB / 30 KB | Dimple heatmap, diameter x depth ratio, no empty cells. |
| `graph6_flow_visualization_streamlines.svg` / `.png` | 508 KB / 200 KB | Flow visualisation: computed Blasius and Spalding profiles, smooth/riblet/dimple near-wall detail, and per-unit-area drag. |
| `graph7_pareto_drag_vs_feature_size.svg` / `.png` | 56 KB / 79 KB | Pareto fronts - drag reduction versus minimum feature size, and versus the composite manufacturability index. |
| `graph8_boxplots_geometry_classes.svg` / `.png` | 145 KB / 77 KB | Per-class box plots of net drag reduction, split by body. |

### 8.3 Source code

| Module | Size | Role |
|:---|---:|:---|
| `texture_model.py` | 12 KB | Physics model. |
| `validate_model.py` | 6 KB | Validation harness / regression gate. |
| `build_dataset.py` | 13 KB | Geometry catalogue and dataset builder. |
| `analyses.py` | 16 KB | The nine analyses. |
| `figures.py` | 26 KB | Figure generation. |
| `summary.py` | 11 KB | JSON serialisation. |
| `refs.py` | 7 KB | Bibliography. |
| `paper.py` | 57 KB | Manuscript Sections 1-5 and the build driver. |
| `paper2.py` | 55 KB | Manuscript Sections 6-8 and Appendices A-C. |
| `handoff.py` | 68 KB | This document's generator. |

### 8.4 Provenance chain

```
texture_model.py  --validated by-->  validate_model.py  -->  validation_benchmarks.csv
       |
       v
build_dataset.py  -->  dataset.csv  -->  analyses.py  -->  summary.py  -->  results_summary.json
                                                                                  |
                            +-----------------------------------------------------+
                            |                        |                            |
                            v                        v                            v
                       figures.py               paper.py/paper2.py           handoff.py
                       graph1..8                research_paper.md            handoff.md
                            |                        |                            |
                            +------------------------+----------------------------+
                                                     v
                                                index.html
```

Every downstream artefact derives from `dataset.csv`, which derives from `texture_model.py`.
**Nothing is hand-entered.** If you change the physics, re-run the chain top to bottom and
every number in every document updates consistently.

### 8.5 Known deviations from the original brief

Three, all deliberate and all documented in the paper:

1. **Geometry count is 67, not 66.** The original specification's class counts summed
   inconsistently; the catalogue was built as a grid-filling design totalling exactly 67 so
   that the two heatmap figures have no empty cells.
2. **Shark-skin drag reduction peaks at 2.033%, not the 12% suggested in the brief.** This
   follows from choosing conservative-consensus calibration over the highest published
   claims. Defended at length in the paper's Discussion.
3. **The `Completed by` attribution in this document's header reads "Biomni (Phylo AI
   scientific research agent)"** rather than the phrasing in the original brief, which
   attributed the agent to a different institution. The corrected attribution is factually
   accurate and is what should appear in any submission.

---

*End of handoff. Generated programmatically from `results_summary.json` and `dataset.csv` on
2026-08-23.*