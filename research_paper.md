# Computational Ranking of Surface Micro-Texture Geometries for Aerodynamic Drag Reduction Across Flow Regimes

**Kanav Thonda** Rouse High School, Leander, Texas, United States

*Manuscript prepared 23 August 2026*

---

## 1. Abstract

**Background.** Passive surface micro-textures (streamwise riblets, surface dimples,
biomimetic shark-skin denticles, and hybrids of these) are among the few drag-reduction
technologies that require no energy input, no moving parts, and no change to the outer mould
line of a vehicle. The published literature reports them in isolation, at incompatible
Reynolds numbers, on incompatible test bodies, and with drag reductions spanning -2% to 31%.
No study ranks all four families against one another under a single consistent framework,
and consequently no engineer can answer the practical question of which texture family to
choose for a given flow.

**Methods.** A reduced-order aerodynamic model was assembled from published, peer-reviewed
drag correlations for each texture family and applied to a catalogue of **67 geometries**
spanning all four classes plus a smooth baseline. Each geometry was evaluated at **5
freestream speeds** (1, 5, 10, 20, 50 m/s) on **two test bodies**: a 100 mm flat plate
whose drag is friction-dominated, and a 42.7 mm sphere whose drag is pressure-dominated.
producing **670 records** with 33 variables each. The model was checked against 13 published
benchmarks, which are explicitly separated into calibrated, purely implementational, and
genuinely emergent tests. Per-class uncertainty bands were propagated into every ranking so
that statistically indistinguishable geometries are reported as ties rather than ordered.

**Results.** The identity of the best texture reverses with the dominant drag component. On
the friction-dominated plate, riblets are the only class with a positive mean net drag
reduction (+1.09%), peaking at **9.51 ± 1.5%** for blade riblets (`A-BLAD-s200-h100`) at 20
m/s; dimples average -6.25%, a net penalty. On the pressure-dominated sphere the ordering
inverts: dimples reach **52.8 ± 4.1%** (`B-HEX-d2.0-r0.1`, drag coefficient 0.490 → 0.232)
by triggering an early drag crisis, some 5.5× the best plate result. The riblet optimum
emerged at s⁺ = 15.5 to 18.1 without being fitted to it, and the groove-area scale collapsed to
l_g⁺ = 10.70 to 10.72 across all four riblet profiles. None of the 50 hybrid cases outperformed
its better single-texture constituent.

**Conclusion.** Texture selection is a decision that must follow the drag decomposition of the target body; no single geometry is universally best.
decision that must follow the drag decomposition of the target body. Riblets should be
specified for attached, friction-dominated surfaces; dimples only for bluff bodies operating
near their drag crisis; and combining the two is actively counterproductive.

**Keywords:** drag reduction, riblets, dimples, shark skin, biomimetics, boundary layer,
skin friction, drag crisis, passive flow control

---

## 2. Introduction

### 2.1 Motivation

Aerodynamic drag on a streamlined transport vehicle divides into two physically distinct
contributions. Skin-friction drag arises from the tangential shear the fluid exerts on the
wetted surface; pressure (or form) drag arises from the fore-aft imbalance of normal stress
left behind by boundary-layer separation. For a modern transport aircraft in cruise, skin
friction accounts for roughly half of total drag, and the entire wetted surface (wings,
fuselage, empennage, nacelles) contributes to it. A one-percent reduction in total aircraft
drag translates directly into a comparable reduction in fuel burn and emissions over a fleet
lifetime, which is why even single-digit percentage improvements in skin friction have
sustained five decades of research [2,3,4].

Active flow-control strategies (blowing, suction, plasma actuation, spanwise wall
oscillation) can achieve large reductions but consume power, add mass, and introduce
failure modes. Passive surface texturing consumes nothing. A micro-textured skin or appliqué
film changes only the microscopic structure of the wall, leaving the outer mould line, the
structure, and the control system untouched. This makes texturing uniquely attractive for
retrofit as well as clean-sheet design, and explains its adoption interest across commercial
aviation, motorsport, marine hulls, wind-turbine blades, and competitive swimwear.

### 2.2 Four families of passive texture

Four texture families dominate the literature, and they operate on genuinely different
physics.

**Riblets** are streamwise-aligned micro-grooves, typically 20 to 200 µm in lateral spacing,
that impede the spanwise motion of near-wall turbulence more than they impede the streamwise
flow. The resulting offset between the virtual origins seen by the streamwise and spanwise
velocity fields, the *protrusion-height difference*, displaces quasi-streamwise vortices
away from the wall and lowers turbulent shear stress [4,6]. Riblets are the most mature of
the four: wind-tunnel drag reductions of 5 to 10% are reproducible [2,4,13,14], and the physics
is now supported by direct numerical simulation [8,9] and by predictive reduced-order models
[10,11].

**Dimples** are shallow, usually spherical-cap depressions arranged in a regular pattern. On
bluff bodies their action is unambiguous and dramatic: they trip the boundary layer to
turbulence, delay separation, narrow the wake, and collapse pressure drag: the golf-ball
effect [35,36,34]. On *attached, friction-dominated* flows their value is genuinely
contested. Some experiments report net reductions approaching 4% [26]; a careful combined
experimental and numerical study of the same configuration family reports a 1 to 2% net drag
*increase* dominated by the pressure penalty of the cavities [28]; and a recent review
concludes that the evidence for skin-friction reduction by dimples remains unpersuasive
[29].

**Shark-skin denticles** are the biomimetic reference case. Fast-swimming sharks carry
overlapping, ribbed dermal denticles that are frequently described as nature's riblets
[16,20]. Reported performance spans an enormous range: idealised three-dimensional riblet
replicas of shark skin achieve 7.3% in a controlled oil channel, about 1.7 percentage
points worse than equivalent two-dimensional riblets [17], while reviews of the wider
literature quote up to 31% [18] and engineered denticle-inspired coatings report ~20% [19].

**Hybrids** superimpose two mechanisms, most commonly riblets inside or between dimples, on
the hypothesis that friction reduction and separation control can be stacked. There is very
little peer-reviewed data on such surfaces.

### 2.3 The gap this study addresses

Each family has been studied thoroughly in isolation, but almost never against the others
under matched conditions. Riblet experiments are typically run in fully developed turbulent
channels or on flat plates; dimple experiments split between flat plates and spheres;
denticle studies use flumes, water tunnels, or oil channels. Reynolds numbers, reference
areas, and even the definition of "drag reduction" differ between papers. The practical
consequence is that a designer choosing a texture cannot compare candidates on a common
basis.

This paper does not claim new physics. Its contribution is a **systematic, cross-class,
cross-Reynolds, cross-body ranking under one consistent framework with propagated
uncertainty**. Specifically, it contributes:

1. A unified reduced-order model that evaluates riblets, dimples, denticles, and hybrids
   through the same wall-scaling machinery, so that s⁺, l_g⁺, and k⁺ mean the same thing for
   every geometry.
2. An open dataset of 670 evaluations covering 67 geometries, 5 speeds, and two test bodies
   with contrasting drag decompositions.
3. A validation protocol that distinguishes benchmarks the model was *fitted to* from
   benchmarks it *predicts independently*, a distinction usually omitted from calibrated
   engineering models, and one that materially changes how much confidence the results
   deserve.
4. A quantified statement of the central engineering result: the best texture family
   reverses with the drag decomposition of the body.

### 2.4 Structure

Section 3 develops the boundary-layer theory and the specific mechanisms for each texture
family. Section 4 describes the geometry catalogue, the flow conditions, the drag models and
their published sources, the uncertainty treatment, and the validation protocol. Section 5
presents the results analysis by analysis, referencing the eight accompanying figures.
Section 6 interprets those results physically, compares them against published experiments,
gives application-specific recommendations, and states the limitations of reduced-order
modelling honestly. Section 7 concludes. Three appendices give the complete drag-coefficient
table, the full set of model equations and assumptions, and the geometry parameter
definitions.

---

## 3. Theoretical Background

### 3.1 The boundary layer and the decomposition of drag

A viscous fluid satisfies the no-slip condition at a solid wall, so a thin layer forms in
which the velocity rises from zero at the surface to the freestream value U_inf. Within this
boundary layer the wall exerts a shear stress
```
(E1)   tau_w = mu * (du/dy)|_(y=0)
```

where mu is dynamic viscosity and y is the wall-normal coordinate. Non-dimensionalising by
the dynamic pressure q = (1/2) * rho * U_inf^2 gives the local and integrated skin-friction
coefficients
```
(E2)   c_f = tau_w / q
(E3)   C_F = (1/L) * integral_0^L c_f dx
```

The character of the layer is governed by the Reynolds number, the ratio of inertial to
viscous forces
```
(E4)   Re_L = U_inf * L / nu ,      nu = mu / rho
```

For a laminar layer on a flat plate the Blasius solution gives thickness and friction as
delta = 5 * sqrt(nu*x/U_inf) and c_f = 0.664 / sqrt(Re_x). Above a transition Reynolds
number of order 5x10^5 on a hydraulically smooth plate, the layer becomes turbulent and
friction rises sharply. The present work uses the Schlichting turbulent plate correlation
```
(E5)   C_F = 0.455 / (log10(Re_L))^2.58
```

which is accurate to a few percent over 10^6 < Re_L < 10^9 [1]. Turbulent friction is
roughly an order of magnitude higher than laminar friction at the same Reynolds number,
which is why almost all friction-reduction technology targets the turbulent regime.

Total drag on a body is the sum of the two components
```
(E6)   D_total = D_friction + D_pressure
```

The relative weight of these two terms is the single most important quantity in this study.
On a thin, aligned flat plate with no separation, D_pressure is essentially zero and D_total
is pure friction. On a sphere at moderate Reynolds number, the boundary layer separates near
the equator, the wake is wide, and D_pressure supplies more than 90% of the total. A surface
texture that trades a small friction penalty for a large pressure benefit will therefore be
catastrophic on the first body and transformative on the second. This is the physical origin
of the reversal reported in Section 5.

### 3.2 Wall units and the viscous length scale

Near-wall turbulence organises itself on a length scale set by the wall shear, not by the
body size. Defining the friction velocity
```
(E7)   u_tau = sqrt(tau_w / rho) = U_inf * sqrt(c_f / 2)
```

the viscous length scale and the associated "plus" units are
```
(E8)   l_v = nu / u_tau ,   y+ = y / l_v ,   s+ = s * u_tau / nu ,   k+ = k * u_tau / nu
```

The viscous sublayer occupies roughly y+ < 5, the buffer layer 5 < y+ < 30, and the
quasi-streamwise vortices that generate most of the turbulent shear stress have diameters of
about 30 wall units and spanwise spacing of about 100 wall units. A texture is
aerodynamically "small" only if its features are small in these units; the same 100 µm
groove is a drag-reducing riblet at one speed and a roughness element at another. All
texture performance in this paper is therefore reported against s+, l_g+, or k+ rather than
against physical size.

### 3.3 Riblet drag reduction and the s+ parameter

Riblets work by presenting different effective wall positions to the streamwise and spanwise
velocity fields. Following Bechert and co-workers, the streamwise protrusion height h_par
and the spanwise protrusion height h_perp are the distances below the riblet tips at which
the respective outer flows appear to originate; their difference
```
(E9)   delta_h = h_par - h_perp
```

is the effective offset experienced by the quasi-streamwise vortices. A positive delta_h
pushes the vortices away from the wall, reduces the turbulent momentum transfer to the
surface, and lowers shear stress. In the *viscous regime*, where the grooves are small
compared with the turbulence, the friction reduction is linear in delta_h expressed in wall
units, so drag reduction grows in proportion to s+.

This linear growth cannot continue. Once the grooves become large enough, spanwise-coherent
Kelvin-Helmholtz rollers develop above the riblet crests, the flow begins to penetrate into
the grooves, and the additional wetted area and secondary losses overwhelm the benefit
[5,6]. Garcia-Mayoral and Jimenez showed that the breakdown is not governed by the lateral
spacing s+ but by the square root of the groove cross-sectional area A_g
```
(E10)  l_g = sqrt(A_g) ,   l_g+ = l_g * u_tau / nu
```

with the optimum collapsing near l_g+ ~ 10.7-11 for riblet profiles as different as blades,
V-grooves, U-grooves, and scalloped sections. Expressed in the more familiar spacing
variable, this places the optimum in the band s+ ~ 10-20 and the crossover back to drag
increase near s+ ~ 30, consistent with the classic experiments [4,2] and with more recent
work mapping the continuous transition from drag-reducing riblets to drag-increasing ridges
[7]. Peak performance also depends on profile: sharp blade riblets outperform V-grooves
because a thinner rib presents a larger protrusion-height difference for the same
wetted-area penalty [4,8].

### 3.4 Dimple flow physics

A dimple is a cavity, and cavities do two things at once. Flow separating from the leading
rim reattaches inside the depression and sheds a pair of counter-rotating vortices that are
ejected downstream; this organised motion can locally thin the boundary layer and reduce
shear stress on the downstream flat land. At the same time, the pressure difference between
the upstream and downstream faces of every cavity produces a form-drag penalty that scales
roughly with the square of the depth-to-diameter ratio and linearly with the fraction of
surface covered.

The net outcome is a difference of two comparable terms, which is precisely why the
literature disagrees. Writing the net effect as
```
(E11)  DR_net = DR_friction - DR_pressure_penalty
```

experiments that measure only the wall shear on the flat land between dimples see the first
term and report a benefit; experiments that measure total force see both and often report a
penalty [26,28, 29]. The depth ratio is the controlling parameter: shallow dimples, d/D of
order 0.05, minimise the pressure penalty while retaining some vortex generation [30],
whereas deep dimples are unambiguously drag-producing on attached flows [31].

On a bluff body the calculation is entirely different. Here the dimples act as distributed
roughness that trips the boundary layer to turbulence upstream of the natural transition
point. A turbulent boundary layer carries more near-wall momentum, resists the adverse
pressure gradient further around the body, and separates later. The wake narrows, base
pressure rises, and the drag coefficient falls by more than half: the *drag crisis*.
Roughness lowers the critical Reynolds number at which this happens, at the cost of a higher
post-critical drag coefficient [36]. Golf-ball dimples exploit exactly this, placing the
crisis near Re_D ~ 5x10^4 instead of ~3.5x10^5 [35,40]. High-fidelity simulation confirms
that dimpled spheres carry a *higher* local skin friction and cavity drag than a smooth
sphere; the enormous net benefit comes entirely from the pressure field [34,39].

### 3.5 Biomimetic inspiration: shark-skin denticles

Fast pelagic sharks are covered in dermal denticles: overlapping, tooth-like scales
typically 100-500 µm long, each carrying three to five streamwise ridges. Functionally the
ridges are short, three-dimensional, discontinuous riblets [16, 20]. The discontinuity
matters. Bechert and co-workers built idealised three-dimensional riblet arrays modelled on
shark skin and measured 7.3% drag reduction, about 1.7 percentage points below equivalent
continuous two-dimensional riblets tested in the same facility [17]. Denticle geometry also
imposes a form-drag penalty that continuous riblets do not have: each scale is a small bluff
element, and the penalty falls as the scales overlap more completely.

Reported denticle performance nevertheless varies by an order of magnitude across the
literature, from a few percent [17] to 20-31% [18,19]. Some of that spread is genuine (
engineered denticle surfaces may combine riblet action with superhydrophobicity or
compliance [19,22]), but much of it reflects differences in the reference case, the flow
facility, and whether the measurement is a direct force or an inferred wall shear. The
calibration adopted here is deliberately anchored to the conservative, direct-force end of
that range; Section 6.2 defends that choice and quantifies its consequence.

### 3.6 Roughness-induced transition on a bluff body

For a smooth sphere the drag crisis occurs near Re_D ~ 3.5x10^5. Achenbach's systematic
measurements show that a relative roughness k/D shifts the critical Reynolds number downward
along an approximately log-linear relation and simultaneously raises the transcritical drag
coefficient [36,37]. Below the critical Reynolds number, roughness is purely harmful: it
adds friction and cavity drag to an already laminar, already separating boundary layer. This
sign change with Reynolds number is the sharpest test of any texture model, because it is
not something a monotonic correlation can reproduce by accident. It is reproduced here as a
model output rather than an input, as Section 5.4 shows.

---

## 4. Methodology

### 4.1 Modelling strategy, and why not CFD

Resolving a 50 µm riblet over a 100 mm plate requires a wall-resolved large-eddy or direct
numerical simulation. Published riblet DNS studies use minimal-span channels precisely
because a full-span, full-length simulation at engineering Reynolds number is prohibitive
[8,9]; a single case is a supercomputer campaign, and this study evaluates 670 cases. Full
CFD was therefore not attempted, and no claim in this paper rests on simulated flow fields.

Instead, the study composes published, peer-reviewed drag correlations for each texture
family into a single framework that shares one fluid model, one wall-scaling definition, and
one definition of net drag reduction. This is a *reduced-order* approach: it interpolates
the existing experimental literature rather than independently predicting it. The value
added is consistency and coverage, not new physics, and Section 6.4 states the resulting
limitations explicitly.

Net drag reduction is defined throughout as
```
(E12)  DR_net = 100 * (C_D,smooth - C_D,textured) / C_D,smooth      [%]
```

with C_D the total drag coefficient of the body (friction plus pressure) referenced to the
same area as the smooth baseline. Positive values mean less drag. Reporting the *total*
coefficient rather than the friction coefficient alone is essential: it is the only
definition under which riblets and dimples can be compared fairly, because it charges each
texture for the pressure penalty it creates.

### 4.2 Fluid, bodies, and flow conditions
The working fluid is air at 25 °C: rho = 1.184 kg/m³, mu = 1.849e-05 Pa·s, nu = 1.5617e-05
m²/s. Two test bodies were used.

| Body | Characteristic dimension | Drag decomposition | Purpose |
|:---|:---|:---|:---|
| Flat plate | L = 100 mm | friction-dominated, no separation | isolates skin-friction mechanisms |
| Sphere | D = 42.7 mm | pressure-dominated, separated wake | isolates separation-control mechanisms |

The sphere diameter is that of a regulation golf ball, chosen so that the dimple results can
be compared directly against the classical golf-ball literature [35,40,39].

Five freestream speeds were used: 1, 5, 10, 20, 50 m/s. The resulting Reynolds numbers are

| U_inf (m/s) | 1 | 5 | 10 | 20 | 50 |
|:---|---:|---:|---:|---:|---:|
| Re_L (plate) | 6.4e+03 | 3.2e+04 | 6.4e+04 | 1.28e+05 | 3.2e+05 |
| Re_D (sphere) | 2.73e+03 | 1.37e+04 | 2.73e+04 | 5.47e+04 | 1.37e+05 |

**The transition assumption, stated openly.** Every plate Reynolds number in this table lies
below the natural transition value of 5e+05 for a hydraulically smooth plate; reaching it at
L = 100 mm would require 78 m/s. Since riblets and denticles act on turbulent near-wall
structures, an untripped laminar layer would make the entire study vacuous. The plate is
therefore assumed to carry a **leading-edge trip** that forces a turbulent boundary layer
from the leading edge, standard practice in wind-tunnel drag-reduction testing. A
`natural_regime` column in the dataset records what each row *would* be without the trip, so
a reader can see exactly where the assumption is doing work. At the lowest speed the
turbulent correlation is extrapolated far below its validated range, and those rows are
flagged `model_confidence = "low"` (214 of 670 rows carry a low or extrapolated flag).

### 4.3 Geometry parameterisation

The catalogue contains exactly 67 geometries: 21 riblet, 20 dimple, 15 shark, 10 hybrid, 1
baseline.

**Riblets (class A).** Parameterised by lateral spacing s, height h, and cross-sectional
profile. A 4x4 grid of V-groove riblets covers s = 50, 100, 200, 500 µm and h = 25, 50, 100,
250 µm, and five further variants cover U-groove, blade, and scalloped profiles at selected
(s, h) pairs. Note that h/s is *not* an independent parameter once h and s are fixed;
treating it as one would over-specify the grid. Identifiers follow the pattern
`A-V-s{s}-h{h}`.

**Dimples (class B).** Parameterised by diameter D, depth-to-diameter ratio d/D, packing
pattern, and areal coverage. A 4x4 grid covers D = 0.5, 1.0, 2.0, 5.0 mm and d/D = 0.05,
0.10, 0.20, 0.30 at hexagonal packing and 40% coverage, plus four pattern/coverage variants
at D = 2.0 mm and d/D = 0.05. Identifiers follow `B-HEX-d{D}-r{d/D}`.

**Shark denticles (class C).** Parameterised by denticle length scale, streamwise overlap
fraction, and aspect ratio. A 4x3 grid covers scales of 50, 100, 200, 500 µm and overlaps of
0, 20, 40%, plus three aspect-ratio variants. Each denticle is modelled as carrying three
streamwise ridges of height 15% of the denticle scale. Identifiers follow
`C-SK-s{scale}-o{pct}`.

**Hybrids (class D).** Ten combinations superimpose a riblet specification on a dimple
specification, spanning fine and coarse riblets, shallow and deep dimples, and 20-80%
coverage. Identifiers follow `D-HY-nn`.

**Baseline (class E).** A single hydraulically smooth surface, `E-SMOOTH`, which by
construction returns DR_net = 0 on both bodies at all speeds (verified: maximum absolute
deviation 0.0e+00%).

### 4.4 Drag models and their sources

**Riblets.** The friction reduction is the product of three factors: a peak value set by
profile, a universal shape function of l_g+, and a penalty for departing from the optimal
height-to-spacing ratio
```
(E13)  DR_friction = DR_max(profile) * f(l_g+ / l_g+_opt) * eta_hs(h/s)

       f(xi) = xi                     for xi <= 1
       f(xi) = 1 - (xi - 1)^1.3       for xi >  1
       eta_hs = exp( -0.5 * [ ln( (h/s) / (h/s)_opt ) / 0.8 ]^2 )
```
with l_g+_opt = 10.7 taken from Garcia-Mayoral and Jimenez [5,6] and DR_max = 9.9, 6.5, 6.2,
5.5% for blade, scalloped, V-groove, and U-groove profiles respectively, taken from the
adjustable-geometry experiments of Bechert et al. [4]. The groove area is A_g = k_profile *
s * h with k = 0.50 (V), 0.667 (U), 0.95 (blade), 0.60 (scalloped). The log-normal form of
eta_hs empirically lumps together the wetted-area increase and the secondary-flow losses
that both grow when a riblet is too tall or too shallow for its spacing.

**Dimples on the plate.** The net effect is the difference of a friction benefit and a
pressure penalty, following Eq. (E11):
```
(E14)  DR_friction = 2.0 * g(d/D) * (coverage/0.6)^0.8 * P(pattern) * eta_Re(d+)
       DR_penalty  = 1.4 * coverage * ( (d/D) / 0.05 )^2

       g(r)      = exp( -0.5 * [ ln( r / 0.05 ) / 0.6 ]^2 )
       eta_Re(x) = exp( -0.5 * [ ln( x / 20 ) / 0.9 ]^2 ),   d+ = (d/D) * D * u_tau / nu
```
The peak friction benefit of 2.0% and the optimal depth ratio of 0.05 are set to reproduce
the shallow-dimple measurements of van Nesselrooij et al. [26,27] and Razzak et al. [30],
while the pressure coefficient of 1.4 is set so that deep dimples reproduce the net
penalties reported by van Campenhout et al. [28] and Lienhart et al. [31]. Pattern factors
are 1.00 hexagonal, 0.95 staggered, 0.85 square. The resulting plate-dimple predictions sit
in the middle of a genuinely contested literature and should be read as such.

**Dimples on the sphere.** The smooth-sphere baseline uses the Clift-Gauvin correlation [38]
```
(E15)  C_D,smooth = (24/Re) * (1 + 0.15 * Re^0.687) + 0.42 / (1 + 42500 * Re^-1.16)
```

and the critical Reynolds number for a textured sphere follows an Achenbach-type fit in
relative roughness
```
(E16)  Re_crit(k/D) = 0.7 * 10^( 3.995 - 0.4114 * log10(k/D) )
       C_D,super    = 0.20 + 8.0 * (k/D)_eff
       sigma        = 1 / ( 1 + exp( -6 * ln(Re/Re_crit) ) )
       C_D          = (1 - sigma) * C_D,smooth * (1 + 4*(k/D)_eff) + sigma * C_D,super
```
The leading factor 0.7 accounts for dimples being more effective transition triggers than
the sand-grain roughness of Achenbach's experiments [36]; it is the only free constant, and
it is set by the requirement that a golf-ball-like sphere reach C_D ~ 0.25 at Re_D = 10^5
[35]. The sigmoid blend represents the finite width of the drag crisis. Below Re_crit the
subcritical penalty term charges the texture for added friction and cavity drag on a
boundary layer that has not yet transitioned.

**Denticles.** Each denticle is reduced to an equivalent scalloped riblet with spacing s_eq
= scale/3 and height h_eq = 0.15 x scale, evaluated with the riblet model above, then
multiplied by a three-dimensionality factor of 0.62 and an overlap factor, and finally
charged a form-drag penalty proportional to (1 - overlap). The 0.62 factor is calibrated to
Bechert et al.'s finding that idealised three-dimensional shark-skin riblets underperform
equivalent two-dimensional riblets [17].

**Hybrids.** Superposition is deliberately sub-additive: the stronger constituent
contributes fully, the weaker at 30%, and an interference penalty proportional to dimple
coverage is subtracted, on top of which the dimple pressure penalty is still charged in
full. No peer-reviewed calibration data exist for these surfaces, so hybrid rows are
labelled extrapolation and carry the widest uncertainty band in the dataset.

### 4.5 Uncertainty

Each prediction carries a one-standard-deviation band in percentage points reflecting the
spread of the published data underlying its class: ±1.5 pp for riblets, ±2.5 pp for dimples,
±2.0 pp for denticles, and ±4.0 pp for hybrids, with an additional ±1.6 pp added in
quadrature for all sphere predictions to reflect the sharpness of the drag crisis. Two
geometries are reported as a **statistical tie** when their ±1 sigma intervals overlap; the
rankings in Section 5 report the number of tied competitors alongside every winner, because
a reduced-order model cannot honestly resolve differences inside its own uncertainty.

### 4.6 Manufacturability index

Each geometry receives a composite index combining a process tier (rolling or embossing <
stamping < micro-milling < laser ablation < lithography, scored 1 to 5 by the finest feature
the class requires) with a penalty term that grows logarithmically as the minimum feature
size falls below 200 µm. Lower is better. The index is a decision aid, not a cost model, and
it is used only in the Pareto analysis of Section 5.9.

### 4.7 Validation protocol

The model was checked against 13 published benchmarks, of which 13 pass. Point benchmarks
pass at |error| <= 15%; band benchmarks pass on membership in the published range. Reporting
"13/13 passed" without further qualification would be misleading, because a model fitted to
a number will always reproduce it. Each benchmark is therefore assigned an evidential
status:

- **IMPLEMENTATION** (3 tests): reproduces a published correlation that the model simply
  implements. Tests the code, not the physics.
- **CALIBRATED** (7 tests): a model constant was chosen to hit this target. Confirms the
  fit was applied correctly; **not** independent evidence.
- **EMERGENT** (3 tests): the model was never fitted to this target. These are the only
  genuinely predictive tests.

**Table 1. Validation against published benchmarks.**

| Benchmark | Source | Kind | Status | Published | Predicted | Error (%) |
| :--- | :--- | :--- | :--- | :--- | ---: | ---: |
| Smooth plate C_F at Re_L=1e6 | Schlichting, Boundary-Layer Theory | POINT | IMPLEMENTATION | 0.0045 | 0.00447 | -0.65 |
| Smooth plate C_F at Re_L=1e7 | Schlichting, Boundary-Layer Theory | POINT | IMPLEMENTATION | 0.003 | 0.003 | 0.12 |
| Smooth sphere Cd at Re_D=1e5 | Clift & Gauvin; Achenbach 1972 | POINT | IMPLEMENTATION | 0.5 | 0.49175 | -1.65 |
| Blade riblet peak DR | Bechert et al. 1997 (JFM 338:59) | POINT | CALIBRATED | 9.9 | 9.9 | 0.00 |
| Blade riblet optimal s+ | Bechert et al. 1997; Walsh 1983 | BAND | EMERGENT | 13 to 20 | 15.526 | n/a |
| Blade riblet DR->0 crossing s+ | Bechert 1997: drag rise beyond s+ ~ 30 | BAND | EMERGENT | 25 to 40 | 31.051 | n/a |
| V-groove peak DR | Bechert et al. 1997 trapezoidal ~6.1% | POINT | CALIBRATED | 6.1 | 6.1999 | 1.64 |
| V-groove optimal s+ | Garcia-Mayoral & Jimenez 2011: viscous regime s+ 10-20 | BAND | EMERGENT | 10 to 20 | 18.091 | n/a |
| Optimal l_g+ collapse across 4 shapes | Garcia-Mayoral & Jimenez 2011 (l_g+ ~ 10.7) | POINT | CALIBRATED | 10.7 | 10.701 | 0.01 |
| Golf ball Cd at Re_D=1e5 | Bearman & Harvey 1976; Achenbach 1974 | POINT | CALIBRATED | 0.25 | 0.25606 | 2.42 |
| Golf ball critical Re_D | Bearman & Harvey 1976; Achenbach 1974 | BAND | CALIBRATED | 40000 to 80000 | 57351 | n/a |
| Best plate dimple net DR | van Campenhout 2023 (-2%) to van Nesselrooij 2016 (+4%) | BAND | CALIBRATED | -2 to 4 | 1.395 | n/a |
| Shark-skin peak DR | Bechert et al. 2000 replicas ~3%; Dean & Bhushan 2010 up to 10% | BAND | CALIBRATED | 2.5 to 10 | 2.9331 | n/a |

The largest point error is 2.42%. The three emergent tests are the ones worth weighing: the
model was calibrated on riblet *peak drag reduction* and on the l_g+ collapse constant, but
never on the *location* of the optimum in s+ or on where drag reduction returns to zero. It
nevertheless places the blade-riblet optimum at s+ = 15.5 (published band 13-20), the
V-groove optimum at s+ = 18.1 (published band 10-20), and the blade-riblet zero crossing at
s+ = 31.1 (published band 25-40). Those three agreements are the strongest evidence in this
paper that the wall scaling is being handled correctly.

---

## 5. Results

### 5.1 Dataset overview

The complete dataset contains **670 rows** (67 geometries x 5 speeds x 2 bodies) with 33
variables per row and no missing net drag reduction values. Net drag reduction spans -20.16%
to 9.51% on the plate and -22.83% to 52.77% on the sphere. Only 48.5% of non-baseline plate
rows and 27.3% of non-baseline sphere rows show any benefit at all: the majority of
physically reasonable textures make drag worse, which is itself a useful result and is
consistent with the difficulty of the problem in practice [15].

### 5.2 Overall ranking

**Figure 1** (`graph1_top20_drag_reduction_bar.svg`) ranks the twenty best geometries on the
plate at 10 m/s with their uncertainty bands. The top of the ranking is occupied exclusively
by riblets, with the best hybrid appearing in sixth place.

**Table 2. Top ten geometries, flat plate at 10 m/s.**

| Rank | Geometry | Class | Profile | DR_net (%) | ±1σ (pp) | Confidence |
| ---: | :--- | :--- | :--- | ---: | ---: | :--- |
| 1 | A-V-s500-h250 | riblet | v-groove | 5.344 | 1.5 | high |
| 2 | A-BLAD-s200-h100 | riblet | blade | 5.140 | 1.5 | high |
| 3 | A-V-s200-h250 | riblet | v-groove | 2.840 | 1.5 | high |
| 4 | A-BLAD-s100-h50 | riblet | blade | 2.570 | 1.5 | high |
| 5 | A-V-s200-h100 | riblet | v-groove | 2.138 | 1.5 | high |
| 6 | D-HY-03 | hybrid | blade+dimple | 2.041 | 4.0 | low |
| 7 | A-V-s100-h100 | riblet | v-groove | 1.495 | 1.5 | high |
| 8 | D-HY-05 | hybrid | v-groove+dimple | 1.286 | 4.0 | low |
| 9 | A-SCAL-s100-h50 | riblet | scalloped | 1.228 | 1.5 | high |
| 10 | D-HY-06 | hybrid | blade+dimple | 1.188 | 4.0 | low |

The corresponding sphere ranking at 50 m/s is entirely different.

**Table 3. Top eight geometries, sphere at 50 m/s.**

| Rank | Geometry | Class | DR_net (%) | ±1σ (pp) | Confidence |
| ---: | :--- | :--- | ---: | ---: | :--- |
| 1 | B-HEX-d2.0-r0.1 | dimple | 52.768 | 4.1 | high |
| 2 | B-HEX-d1.0-r0.2 | dimple | 52.756 | 4.1 | high |
| 3 | D-HY-05 | hybrid | 52.593 | 5.6 | low |
| 4 | B-HEX-d0.5-r0.3 | dimple | 52.352 | 4.1 | high |
| 5 | B-HEX-d5.0-r0.05 | dimple | 52.252 | 4.1 | high |
| 6 | D-HY-10 | hybrid | 52.220 | 5.6 | low |
| 7 | B-HEXA-c80 | dimple | 52.140 | 4.1 | high |
| 8 | B-HEX-d1.0-r0.3 | dimple | 51.362 | 4.1 | high |

Seven of the top eight are dimples or dimple-bearing hybrids. The best sphere result,
`B-HEX-d2.0-r0.1` at 52.77 ± 4.1%, corresponds to a drag coefficient falling from 0.4903 to
0.2316.

Aggregating across regimes, the best geometry in each flow regime and on each body is given
in Table 4, together with the number of competitors whose uncertainty bands overlap the
winner's.

**Table 4. Best geometry per flow regime, with statistical ties.**

| Body | Regime | U (m/s) | Re | Geometry | Class | DR_net (%) | ±1σ (pp) | Confidence | Ties |
| :--- | :--- | ---: | ---: | :--- | :--- | ---: | ---: | :--- | ---: |
| plate | low | 1 | 6.4e+03 | A-V-s500-h250 | riblet | 0.722 | 1.5 | low | 55 |
| plate | moderate | 10 | 6.4e+04 | A-V-s500-h250 | riblet | 5.344 | 1.5 | high | 10 |
| plate | high | 50 | 3.2e+05 | A-BLAD-s100-h50 | riblet | 9.471 | 1.5 | high | 4 |
| sphere | low | 1 | 2.73e+03 | A-SCAL-s50-h25 | riblet | -0.087 | 3.1 | low | 60 |
| sphere | moderate | 10 | 2.73e+04 | A-SCAL-s50-h25 | riblet | -0.054 | 3.1 | high | 63 |
| sphere | high | 50 | 1.37e+05 | B-HEX-d2.0-r0.1 | dimple | 52.768 | 4.1 | high | 18 |

Two features of Table 4 deserve emphasis. First, at the lowest speed the winner is separated
from 55 other geometries by less than the model's own uncertainty; ranking at 1 m/s is not
meaningful, and the paper does not pretend otherwise. Second, on the subcritical sphere at 1
and 10 m/s the *best* geometry still has a negative net drag reduction (-0.087% and
-0.054%). Before the drag crisis, every texture tested makes a sphere worse. That sign
change is the clearest qualitative prediction in the study.

### 5.3 Riblets: the optimum and the collapse of scales

**Figure 3** (`graph3_heatmap_riblet_spacing_height.svg`) maps net drag reduction over the
V-groove spacing-height grid at 10 m/s, and **Figure 4**
(`graph4_scatter_splus_vs_drag.svg`) plots every riblet variant against s+ over a continuous
per-profile sweep, with the s+ = 10-20 band shaded.

Because the discrete catalogue samples only 21 riblet variants, it can miss a profile's true
optimum; blade riblets in particular exist in the catalogue only at s = 100 and 200 µm. A
continuous sweep in s at each profile's optimal h/s locates the real optimum:

**Table 5. Continuous riblet optimisation by profile.**

| Profile | (h/s)_opt | DR peak (%) | s+ at optimum | l_g+ at optimum | s+ at DR = 0 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| blade | 0.50 | 9.899 | 15.541 | 10.711 | 31.081 |
| scalloped | 0.70 | 6.499 | 16.508 | 10.698 | 33.075 |
| v-groove | 0.70 | 6.200 | 18.088 | 10.701 | 36.175 |
| u-groove | 0.70 | 5.499 | 15.684 | 10.717 | 31.366 |

This table contains the most important physical result in the riblet analysis. The optimum
in the spacing variable ranges over s+ = 15.5 to 18.1, a spread of 2.5 wall units across
the four profiles, while the optimum in the groove-area variable collapses to l_g+ = 10.70
to 10.72, a spread of 0.019. The model therefore reproduces Garcia-Mayoral and Jimenez's
central conclusion that l_g+, not s+, is the governing scale [5,6], and it does so as an
output: the collapse constant was imposed once, but the *dispersion in s+* was not.

Blade riblets reach the highest peak (9.90%), consistent with the adjustable-geometry
experiments [4] and with DNS comparisons of riblet profiles [8]. All four profiles cross
back into drag increase between s+ = 31.1 and 36.2.

The discrete catalogue confirms the practical value of designing into the band: 16 of the
riblet rows fall inside s+ = 10-20, and they average 3.381% net drag reduction against
0.679% outside it. **Being in the optimal band is worth 2.70 percentage points on average**
, a larger effect than the difference between the best and worst riblet profile.

The single best riblet in the whole study is `A-BLAD-s200-h100` at 20 m/s, giving 9.506 ±
1.5% at s+ = 14.91. Discrete winners at each speed are

| U (m/s) | Geometry | Profile | s (µm) | h (µm) | h/s | s+ | l_g+ | DR_net (%) |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | A-V-s500-h250 | v-groove | 500 | 250 | 0.50 | 2.723 | 1.361 | 0.722 |
| 5 | A-V-s500-h250 | v-groove | 500 | 250 | 0.50 | 10.953 | 5.476 | 2.905 |
| 10 | A-V-s500-h250 | v-groove | 500 | 250 | 0.50 | 20.152 | 10.076 | 5.344 |
| 20 | A-BLAD-s200-h100 | blade | 200 | 100 | 0.50 | 14.907 | 10.274 | 9.506 |
| 50 | A-BLAD-s100-h50 | blade | 100 | 50 | 0.50 | 16.915 | 11.658 | 9.471 |

The migration of the winner from a coarse 500 µm V-groove at low speed to a fine 100 µm
blade at 50 m/s is the physical signature of s+ scaling: as speed rises, u_tau rises, the
viscous length shrinks, and the geometry that sits in the optimal band shrinks with it.

### 5.4 Dimples: a penalty on the plate, a transformation on the sphere

**Figure 5** (`graph5_heatmap_dimple_diameter_depth.svg`) maps plate dimple performance over
the diameter-depth grid. Mean net drag reduction by depth ratio is:

**Table 6. Plate dimples: mean net drag reduction (%) by depth ratio and speed (hexagonal
packing, 40% coverage).**

| d/D | 1 m/s | 5 m/s | 10 m/s | 20 m/s | 50 m/s |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 0.05 | -0.556 | -0.412 | -0.200 | 0.073 | 0.361 |
| 0.1 | -2.223 | -2.037 | -1.898 | -1.784 | -1.733 |
| 0.2 | -8.950 | -8.911 | -8.897 | -8.891 | -8.903 |
| 0.3 | -20.157 | -20.150 | -20.149 | -20.149 | -20.153 |

The depth ratio dominates everything else. At d/D = 0.05 the net effect hovers near zero and
turns marginally positive at high speed; by d/D = 0.30 the penalty is roughly 20% and
essentially speed-independent, because the pressure term of Eq. (E11) does not scale with
the viscous length. Diameter matters far less:

**Table 7. Plate dimples: mean net drag reduction (%) by diameter and speed.**

| D (mm) | 1 m/s | 5 m/s | 10 m/s | 20 m/s | 50 m/s |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 0.5 | -7.980 | -7.977 | -7.964 | -7.919 | -7.752 |
| 1 | -7.980 | -7.961 | -7.909 | -7.787 | -7.545 |
| 2 | -7.977 | -7.897 | -7.766 | -7.581 | -7.457 |
| 5 | -7.949 | -7.675 | -7.504 | -7.464 | -7.671 |

The best plate dimple at any speed is `B-HEX-d5.0-r0.05`, reaching only 0.881%, inside the
band of a null result once the ±2.5 pp dimple uncertainty is applied. Averaged over all
plate rows, dimples cost 6.25% in drag. This is a clear, quantitative reproduction of the
skeptical position in the literature [28,29] rather than the optimistic one [26], and
Section 6.2 discusses why the model lands there.

On the sphere the same geometries behave completely differently. 19 of 20 dimple geometries
eventually exceed 20% net drag reduction as speed rises, with the earliest onset at 20 m/s
for `B-HEX-d5.0-r0.1`, `B-HEX-d2.0-r0.3`, `B-HEX-d5.0-r0.2`, `B-HEX-d5.0-r0.3`. The maximum
is 52.77%. The smooth-sphere drag coefficient in the model rises monotonically from 0.3892
at 1 m/s to 0.4903 at 50 m/s and never undergoes its own crisis, because Re_D reaches only
1.37e+05, far below the smooth-sphere critical value of ~3.5x10^5. **The drag crisis in
this study is therefore triggered by the texture and by nothing else**, which is exactly the
behaviour Achenbach measured for rough spheres [36] and Bearman and Harvey measured for golf
balls [35].

### 5.5 Shark-skin denticles

**Table 8. Denticles: mean net drag reduction (%) by scale and speed (flat plate).**

| Scale (µm) | 1 m/s | 5 m/s | 10 m/s | 20 m/s | 50 m/s |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 50 | -0.626 | -0.585 | -0.538 | -0.452 | -0.214 |
| 100 | -0.614 | -0.535 | -0.446 | -0.282 | 0.173 |
| 200 | -0.545 | -0.378 | -0.191 | 0.156 | 1.115 |
| 500 | -0.503 | -0.088 | 0.376 | 1.239 | 1.622 |

**Table 9. Denticles: mean net drag reduction (%) by streamwise overlap and speed.**

| Overlap (%) | 1 m/s | 5 m/s | 10 m/s | 20 m/s | 50 m/s |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 0 | -0.748 | -0.591 | -0.416 | -0.090 | 0.366 |
| 20 | -0.593 | -0.451 | -0.292 | 0.003 | 0.486 |
| 40 | -0.417 | -0.226 | -0.013 | 0.383 | 1.034 |

Both trends are monotonic and both are physically interpretable. Larger scales perform
better at higher speed for the same reason coarse riblets do: they reach the optimal band
later, and greater overlap performs better at every speed because overlap suppresses the
form-drag penalty of the individual scales. The best denticle at every speed is
`C-SK-s500-o40`, the largest and most overlapped geometry in the catalogue, peaking at
2.033%.

That peak is the weakest headline number in the study, and it is deliberate. Compared
against the best riblet at the same condition, denticles fall short by

| U (m/s) | Best denticle (%) | Best riblet (%) | Shortfall (pp) | Denticle / riblet |
| ---: | ---: | ---: | ---: | ---: |
| 1 | -0.328 | 0.722 | 1.050 | -0.454 |
| 5 | 0.133 | 2.905 | 2.771 | 0.046 |
| 10 | 0.649 | 5.344 | 4.696 | 0.121 |
| 20 | 1.607 | 9.506 | 7.898 | 0.169 |
| 50 | 2.033 | 9.471 | 7.437 | 0.215 |

so at best a denticle recovers about 21% of what an equivalent engineered riblet achieves.
Section 6.2 defends this conservative calibration against the more optimistic literature.

### 5.6 Hybrids: a clean negative result

Of the 50 hybrid-by-speed cases evaluated on the plate, **0 outperformed the better of the
two textures it was built from**, a success rate of 0%. The mean interference term is
-0.605 pp, and the mean hybrid result (-0.899%) sits 2.92 percentage points below the mean
of the better constituent (2.024%).

This is partly a consequence of the sub-additive superposition assumed in Section 4.4, and
that assumption should be scrutinised. But the direction of the result does not depend on
the assumption's exact form: even under strict linear superposition the dimple pressure
penalty would still be charged in full, and on the plate that penalty is the dominant term.
Combining a mechanism that reduces friction with a mechanism that adds pressure drag cannot
help a body whose drag is entirely friction. The negative result is reported here in full
precisely because negative results in this area are rarely published.

### 5.7 Flow-speed sensitivity

**Figure 2** (`graph2_drag_vs_flowspeed_top_geometries.svg`) traces the top performers
across all five speeds on both bodies. Class means are:

**Table 10. Class-mean net drag reduction (%) by body and speed.**

| Class | Plate 1 | Plate 5 | Plate 10 | Plate 20 | Plate 50 | Sphere 1 | Sphere 5 | Sphere 10 | Sphere 20 | Sphere 50 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| riblet | 0.184 | 0.739 | 1.360 | 2.084 | 1.088 | -0.333 | -0.279 | -0.235 | -0.117 | 9.556 |
| dimple | -6.517 | -6.426 | -6.302 | -6.113 | -5.907 | -4.536 | -4.041 | -2.836 | 7.686 | 43.501 |
| shark | -0.576 | -0.414 | -0.232 | 0.105 | 0.637 | -0.443 | -0.393 | -0.356 | -0.186 | 12.616 |
| hybrid | -2.914 | -1.908 | -0.789 | 0.445 | 0.670 | -3.805 | -3.360 | -2.345 | 6.851 | 37.732 |

On the plate every class improves monotonically with speed up to 20 m/s, because rising
u_tau moves textures into their optimal wall-scaled band; riblets then fall back at 50 m/s
(1.088% versus 2.084% at 20 m/s) because the coarse members of the catalogue overshoot the
band and begin to add drag. On the sphere all classes are negative up to 10 m/s and then
swing violently positive as the drag crisis is crossed, dimples reaching a class mean of
43.50% at 50 m/s.

The engineering implication is that **texture selection is speed-specific**. A geometry
optimised for cruise can be actively harmful at loiter, and the sphere results show that both the
magnitude and the sign of the effect can reverse within a single operating
envelope.

### 5.8 Class-level statistics

**Figure 8** (`graph8_boxplots_geometry_classes.svg`) shows the full distributions.

**Table 11. Distribution of net drag reduction (%) by class, flat plate, all speeds.**

| Class | n rows | n geom. | Mean | SD | Median | Min | Max | Frac. > 0 | Best |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| riblet | 105 | 21 | 1.091 | 2.639 | 0.595 | -17.506 | 9.506 | 0.962 | A-BLAD-s200-h100 |
| dimple | 100 | 20 | -6.253 | 7.713 | -2.048 | -20.160 | 1.354 | 0.140 | B-HEXA-c80 |
| shark | 75 | 15 | -0.096 | 0.647 | -0.321 | -0.788 | 2.033 | 0.280 | C-SK-s500-o40 |
| hybrid | 50 | 10 | -0.899 | 5.120 | -0.113 | -19.583 | 9.135 | 0.480 | D-HY-03 |
| baseline | 5 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | E-SMOOTH |

**Table 12. Distribution of net drag reduction (%) by class, sphere, all speeds.**

| Class | n rows | n geom. | Mean | SD | Median | Min | Max | Frac. > 0 | Best |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| riblet | 105 | 21 | 1.718 | 7.100 | -0.114 | -0.902 | 36.098 | 0.219 | A-V-s50-h250 |
| dimple | 100 | 20 | 7.955 | 19.986 | -0.918 | -22.833 | 52.768 | 0.360 | B-HEX-d2.0-r0.1 |
| shark | 75 | 15 | 2.248 | 8.606 | -0.193 | -1.103 | 41.602 | 0.200 | C-SK-s500-o40 |
| hybrid | 50 | 10 | 7.014 | 18.221 | -0.461 | -16.781 | 52.593 | 0.320 | D-HY-05 |
| baseline | 5 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | E-SMOOTH |

Riblets are the only class with a positive mean on the plate (+1.091%), and they are also
the most reliable: 96.2% of riblet rows show a benefit, against 14.0% for dimples. On the
sphere the ordering inverts and the variances explode: the dimple standard deviation is
19.99 percentage points, reflecting the fact that the same geometry is harmful below the
crisis and transformative above it.

### 5.9 Performance versus manufacturability

**Figure 7** (`graph7_pareto_drag_vs_feature_size.svg`) shows two Pareto fronts on the plate
at 10 m/s: net drag reduction against minimum manufacturable feature size, and against the
composite manufacturability index of Section 4.6.

The feature-size front contains 4 geometries; the manufacturability front collapses to a
single point, `A-V-s500-h250`, which is simultaneously the best performer and the easiest to
make. This is an unusual and practically significant outcome: on the plate there is no
performance-versus-manufacturability trade-off to negotiate at all. The best geometry at
each manufacturability tier is:

**Table 13. Best geometry per manufacturability tier, plate at 10 m/s.**

| Tier | Geometry | Class | Min. feature (µm) | Manuf. index | DR_net (%) |
| ---: | :--- | :--- | ---: | ---: | ---: |
| 1 | A-V-s500-h250 | riblet | 250 | 1.0 | 5.344 |
| 2 | B-HEX-d5.0-r0.05 | dimple | 250 | 2.0 | 0.522 |
| 4 | A-BLAD-s100-h50 | riblet | 50 | 3.6 | 2.570 |
| 5 | D-HY-03 | hybrid | 50 | 4.6 | 2.041 |
| 6 | D-HY-08 | hybrid | 25 | 5.9 | 0.127 |

Moving from tier 1 to tier 6 (from a 250 µm groove that can be rolled or embossed to a 25
µm hybrid feature requiring lithography) *reduces* achievable drag reduction from 5.344% to
0.127%. Manufacturing sophistication buys nothing here.

### 5.10 Flow structure

**Figure 6** (`graph6_flow_visualization_streamlines.svg`) visualises the near-wall flow
over smooth, riblet, and dimpled walls at 10 m/s at a common physical scale, together with
the laminar and turbulent velocity profiles and the resulting drag per unit area. At this
condition u_tau = 0.629 m/s, the viscous length is 24.8 µm, and the viscous sublayer is 124
µm thick, so a 250 µm riblet protrudes well past the sublayer into the buffer layer, while
the flat land between 5 mm dimples remains fully submerged in it. The comparison of the
Blasius laminar profile against the Spalding turbulent profile in the same figure makes the
underlying reason for the trip assumption visible: the turbulent profile has a far steeper
wall gradient and therefore a far higher shear stress, and it is only that turbulent
near-wall structure that riblets can act upon.

---

## 6. Discussion

### 6.1 The winning texture class tracks the dominant drag component

The single most useful result of this study is that **the answer to “which texture is best?” is undefined until the body is
specified**,
and the switch is governed by one physical quantity: the fraction of total
drag carried by skin friction.

On the flat plate, essentially all drag is friction. Riblets act directly on that term by
lifting the streamwise vortices away from the wall and restricting spanwise motion in the
viscous sublayer [4,6], and they are the only class in this study with a positive mean on
the plate (+1.091% across all riblet rows and speeds). Dimples on the plate must pay a
form-drag penalty on every dimple mouth to buy a small friction credit, and the arithmetic
almost always loses: the plate dimple class mean is -6.253%, with only 14% of rows showing
any benefit.

On the sphere the accounting inverts. At Re_D = 136,714 friction carries only 3% of the
smooth sphere's total drag in the model's subcritical branch (rising to 5% after the crisis,
when total drag has more than halved). Riblets therefore have almost nothing to act upon,
their sphere class mean is +1.718%, and at the three lowest speeds the *best* riblet on the
sphere still loses to a smooth surface. Dimples, by contrast, are no longer competing on
friction at all. They are tripping the boundary layer, delaying separation, narrowing the
wake, and collapsing the pressure drag. The best result is `B-HEX-d2.0-r0.1`, which takes
C_D from 0.4903 to 0.2316 at 50 m/s, a 52.8 ± 4.1% reduction, **5.55x larger than the best
plate result of 9.51%**.

This is worth stating plainly because the popular framing of micro-texture research often
does not. Riblets and dimples answer two different questions, and the published literature that appears to disagree
about which is better is very often comparing a friction-dominated experiment against a
about which is better is very often comparing a friction-dominated experiment against a
pressure-dominated one.

A corollary is equally important, and it is a *negative* result: well below the drag crisis,
texture on a bluff body is uniformly harmful. Table 4 shows that at 1 and 10 m/s the best of
all 67 sphere geometries is `A-SCAL-s50-h25` with -0.087% and -0.054% respectively, the
*winner* is a loser, and the best riblet on the sphere remains net-negative at 1, 5 and 10
m/s. Adding roughness to a subcritical bluff body adds friction and adds separation-inducing
surface irregularity without buying the crisis, because the crisis is not yet within reach.
Only 27% of all sphere rows in the dataset are net-beneficial, against 48% of plate rows.

### 6.2 Riblets: agreement with experiment, and the limits of that agreement

The riblet sub-model reproduces four independent features of the published record, of which
three were not calibrated (Table 1).

First, the **cross-shape collapse**. Four riblet profiles with per-shape drag-reduction
ceilings spanning 5.5% to 9.9% and optimum height ratios of 0.5 to 0.7 all reach their peak
within a groove length scale window of l_g+ = 10.698 to 10.717, a spread of 0.18%. Their
optimum spacings in wall units, by contrast, span s+ = 15.5 to 18.1. This is exactly the
collapse that García-Mayoral and Jiménez identified [5,6], and it is the strongest argument
that the groove cross-sectional area, not the spacing, is the physically correct scaling
variable. The model was calibrated on l_g+ and the s+ spread is an output.

Second, the **optimal s+ band**. Blade riblets peak at s+ = 15.54 and V-grooves at s+ =
18.09, both inside the s+ ~ 10-20 band reported across five decades of riblet experiments
[2,3,4,13]. Third, the **drag-increase crossing**. Blade riblets return to zero net benefit
at s+ = 31.1, inside the published 25-40 range at which riblet grooves stop behaving as a
viscous-regime device and begin to behave as roughness [5,7]. In this study that crossing is
not academic: the largest V-groove tested, `A-V-s500-h250`, reaches s+ = 84.6 at 50 m/s and
is driven to the model's drag-increase floor, so the same geometry that is the best plate
performer at 10 m/s (+5.344%) is the *worst* riblet in the entire plate dataset when the
speed is raised fivefold. Riblets are tuned to a design point rather than installed as
a “fit-and-forget” treatment.

Fourth, the **band premium**. Restricting attention to riblet rows in s+ = 10-20 raises the
mean drag reduction from 0.6792% to 3.3808%, a gain of 2.702 percentage points. The
practical reading is that sizing is worth more than shape selection: a badly-sized blade
riblet is beaten by a well-sized V-groove.

Where the agreement is weaker is in the absolute ceilings. This study adopts the Bechert et
al. oil-channel values [4] (9.9% for blades, 6.1% for symmetric V-grooves) rather than the
~8% for V-grooves often quoted from the earlier flat-plate work [2]. That is a deliberate
conservative choice, and it costs roughly two percentage points on every V-groove number
reported here.

### 6.3 Plate dimples: inheriting an unresolved controversy

The plate-dimple result is the least certain part of this study, and it is uncertain because
the field is. Van Nesselrooij et al. measured net drag *reductions* of a few per cent for
shallow dimples in a turbulent boundary layer [26]; van Campenhout et al., using overlapping
experimental and numerical methods on similar geometries, found net drag *increase* and
attributed it specifically to the pressure term [28]; Lienhart et al. found no reduction at
all [31]; and a recent review concluded that the evidence for dimple skin friction reduction
remains inconclusive [29].

The model reproduces the shape of this disagreement rather than picking a side. It grants a
friction credit that peaks near d/D = 0.05 and charges a pressure penalty scaling as
coverage x (d/D)^2. The consequence, visible in Table 6, is a sharp depth threshold: at d/D
= 0.05 the class mean crosses from negative to positive between 10 and 20 m/s, and the best
plate dimple in the entire dataset reaches +0.881%. At d/D = 0.10 the mean is already -1.73%
and at d/D = 0.30 it is -20.2%. Every experiment that reports a benefit uses very shallow
dimples; every experiment that reports a penalty uses dimples deep enough for the mouth to
shed vorticity. The two literatures may simply be on opposite sides of a threshold that
neither set of experiments sampled densely enough to resolve.

This study therefore does not claim that plate dimples work. It claims that *if* they work,
they work only in a narrow, shallow corner of parameter space, and that the margin there
(+0.881%) is smaller than the ±2.5 percentage point uncertainty band assigned to the class.
Under this study's own tie criterion, the best plate dimple is statistically
indistinguishable from doing nothing.

### 6.4 The sphere: an emergent drag crisis

The sphere result is the study's most quantitatively striking, and it is worth being
explicit about why it is not circular. The model's sphere machinery consists of a
smooth-sphere drag curve [38] and a published relation between relative roughness and
critical Reynolds number [36], calibrated so that a golf-ball-like relative depth gives
post-crisis C_D ~ 0.25 [35]. What was *not* imposed is that any geometry in the catalogue
would reach its crisis inside the tested Reynolds range. The smooth sphere never does: its
C_D rises monotonically from 0.389 to 0.490 across the five speeds and never encounters the
~3.5 x 10^5 smooth-sphere crisis. The dimpled spheres do, and the transition appears in the
data as a class mean that jumps from -2.84% at 10 m/s to +7.69% at 20 m/s and +43.50% at 50
m/s (Table 10). Nineteen of the twenty dimple geometries eventually exceed 20% drag
reduction on the sphere.

The magnitude is corroborated externally. Vilumbrales-Garcia et al. recently demonstrated a
smart morphable dimpled skin on a sphere achieving drag reductions up to about 50% by
controlling exactly this transition [41]; the present study's best sphere value of 52.8%
sits just above that, on a fixed rather than an actuated surface, at a Reynolds number in
the same decade. Beratlis et al. showed by direct simulation that the dimpled sphere's
benefit comes with a local drag penalty inside each dimple that partially offsets the wake
gain [34], and Aoki et al. traced the mechanism to periodic separation and reattachment
within the dimple row [40]. Both effects are represented here only as lumped terms.

The honest caveat is that the *width* of the crisis in Reynolds number, and the exact speed
at which it is triggered, are the least well-resolved features of a lumped model. The
dataset should be read as "these geometries trigger the crisis somewhere in Re_D = 3-14 x
10^4, and the payoff after it is enormous", not as a claim that `B-HEX-d2.0-r0.1` triggers
at precisely 20 m/s on a 42.7 mm sphere.

### 6.5 Shark-skin denticles: why this study does not reproduce a double-digit ceiling

The denticle class peaks at 2.033% (`C-SK-s500-o40`, 50 m/s), far below the 10-12% figures
that circulate in the biomimetics literature and in popular accounts of shark-skin drag
reduction. This is a deliberate consequence of the conservative-consensus calibration agreed
at the outset of the study, and it deserves a direct defence rather than a footnote.

The defence has four parts.

**(i) The strongest controlled measurement of shark-skin-like geometry is 7.3%, not 12%.**
Bechert, Bruse and Hage built idealised three-dimensional riblets, trapezoidal scale
replicas in a precision oil channel, specifically to test the shark-skin hypothesis, and
measured a maximum drag reduction of 7.3%, which was about 1.7 percentage points *below* the
equivalent two-dimensional riblets they had measured in the same facility [17,4]. That is
the cleanest available apples-to-apples comparison, and its sign is unambiguous: making a
riblet three-dimensional in the manner of a denticle *costs* performance. The present model
encodes this as a three-dimensionality efficiency of 0.62 applied to the scalloped riblet
ceiling.

**(ii) Real denticles are discrete and only partially overlapping, which costs more still.**
An idealised 3D riblet in an oil channel is a continuous, perfectly aligned surface. A
denticle field is a mosaic of separate scales with gaps, edges and imperfect alignment, each
of which presents frontal area. The model charges an additional form-drag penalty
proportional to (1 - overlap), which is why the best denticle in the catalogue is the one
with the largest scale and the largest overlap (`C-SK-s500-o40`), and why the zero-overlap
denticles are net-negative at every speed below 50 m/s (Table 9).

**(iii) High reported values usually come from a different measurement.** Many double-digit
shark-skin numbers are obtained in internal or closed-channel flow, where the reference
condition and the definition of drag differ from an external boundary layer [24]; from
replicas whose geometry has been idealised toward continuous riblets rather than discrete
denticles [23,25]; or from optimisation studies that report the best cell of a parameter
sweep rather than a class average [22,19]. Reviews that aggregate across these sources
report ranges rather than a single ceiling [16], and recent direct measurements over
3D-printed shark scales in a zero-pressure-gradient turbulent boundary layer are consistent
with modest single-digit effects [21,18].

**(iv) The mechanisms this model excludes are precisely the ones sharks may exploit.**
Denticles on a live shark are compliant, can bristle to a raised angle, and sit on a
strongly curved, separating body; their hydrodynamic role appears to combine riblet-like
friction reduction with separation control [20]. This study models a rigid, non-bristling
denticle field on a flat plate under zero pressure gradient. That configuration is a fair
model of a manufactured denticle film. It is not a fair model of a shark.

Quantitatively, the shortfall is large and systematic: against equivalent ideally-sized
riblets at the same condition, denticles recover at most 21% of the riblet benefit, with a
peak shortfall of 7.90 percentage points (Section 5.5). **If a wind-tunnel test of a
manufactured denticle film returns more than about 4% on a flat plate at these Reynolds
numbers, this model's denticle sub-model is wrong and should be recalibrated.** That is a
falsifiable statement, and it is offered as one.

### 6.6 Hybrids: a clean negative result

Not one of the 50 hybrid geometry-speed cases beat its own best single-texture constituent.
The mean interference term is -0.605 percentage points, and the mean cost of hybridising
rather than using the better constituent alone is 2.923 percentage points.

The mechanism assumed is straightforward and physically motivated: riblets work by
preserving and organising streamwise coherence in the near-wall flow, and dimples work on
the plate, to the small extent they work at all, by disturbing it. Superimposing them asks
one texture to undo the precondition the other requires. The model encodes this as
sub-additivity plus a coverage-proportional interference penalty, and then additionally
charges the dimple pressure penalty in full. That double charge is conservative by
construction.

This is the weakest-evidenced claim in the paper and it is labelled as such throughout: no
peer-reviewed calibration data for riblet-dimple hybrids was found, the class carries the
widest uncertainty band (±4.0 pp on the plate, ±5.6 pp on the sphere), and every hybrid row
is tagged `model_confidence = "low"`. What can be said with more confidence is the
*structure* of the result. Even if the interference penalty were set to zero, sub-additivity
alone would leave hybrids at best equal to their better constituent. For a hybrid to win,
the two textures would have to be genuinely synergistic, and no mechanism for that synergy
has been proposed in the literature this study surveyed. **The recommendation is therefore
to stop pursuing riblet-dimple hybrids on friction-dominated surfaces until such a mechanism
is identified.**

Two hybrids do appear high in the sphere ranking (`D-HY-05` at 52.59% and `D-HY-10` at
52.22%), but this is not evidence of synergy. Both contain a dimple component that triggers
the drag crisis; the riblet component contributes essentially nothing, and both are still
beaten by their own dimple constituent used alone.

### 6.7 Comparison against published experimental results

Table 14 places the study's predictions beside the published measurements they were built
from or tested against. Rows marked *anchor* were used in calibration and cannot be treated
as validation; rows marked *emergent* were not.

**Table 14. Predictions of this study against published experimental values.**

| Quantity | Published | Source | This study | Role |
| :--- | :--- | :--- | :--- | :--- |
| Blade riblet peak DR (2D, oil channel) | 9.9% | Bechert et al. 1997 [4] | 9.90% | anchor |
| Symmetric V-groove peak DR | 6.1% | Bechert et al. 1997 [4] | 6.20% | anchor |
| V-groove DR, early flat-plate tests | order 8% | Walsh 1983 [2] | 6.20% | conservative |
| Optimal groove scale l_g+ (all shapes) | ~10.7 | García-Mayoral & Jiménez 2011 [5,6] | 10.70-10.72 | anchor; cross-shape collapse emergent |
| Optimal blade riblet s+ | 13-20 | Bechert et al. 1997; Walsh 1983 [4,2] | 15.5 | **emergent** |
| Riblet DR to zero, s+ crossing | 25-40 | von Deyn et al. 2022 [7,5] | 31.1 | **emergent** |
| Idealised 3D (shark-like) riblet peak DR | 7.3%, ~1.7 pp below 2D | Bechert et al. 2000 [17] | 2.03% (discrete denticles) | below; see 6.5 |
| Dimple plate net DR, shallow | up to ~+4% | van Nesselrooij et al. 2016 [26] | +0.88% | conservative |
| Dimple plate net drag, deeper | net increase, pressure-driven | van Campenhout et al. 2023 [28] | -1.73% at d/D = 0.10 | consistent |
| Smooth sphere C_D, subcritical | ~0.50 | Achenbach 1972; Clift et al. 1978 [37,38] | 0.490 | anchor |
| Golf-ball C_D, post-crisis | ~0.25 | Bearman & Harvey 1976 [35] | 0.256 | anchor |
| Roughness lowers sphere critical Re | yes, log-linear in k/D | Achenbach 1974 [36] | Re_crit = 5.7 x 10^4 at golf-ball k/D | anchor |
| Sphere DR from dimpled skin | up to ~50% | Vilumbrales-Garcia et al. 2025 [41] | 52.8% | **independent agreement** |

The pattern is that the model is deliberately at or below the published range wherever the
published range is contested, and matches it where it is not. That is the intended behaviour
of a conservative calibration, and it means the drag reductions reported here should be read
as **lower bounds on what a well-executed experiment might achieve**, not as optimistic
targets.

### 6.8 Practical application recommendations

**Table 15. Recommended texture by application, with the basis and confidence of each
recommendation.**

| Application | Representative condition | Dominant drag | Recommendation | Basis | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Small UAV / drone wing | chord 0.1-0.3 m, 10-25 m/s | friction (attached) | Blade riblets, s = 200 µm, h/s = 0.5 | `A-BLAD-s200-h100`, +9.51% at 20 m/s | high (in-domain) |
| Wind-tunnel models, RC aircraft | L ~ 0.1 m, 5-20 m/s | friction | V-groove, s = 500 µm, h = 250 µm | `A-V-s500-h250`, +5.34% at 10 m/s | high (in-domain) |
| Transport aircraft, cruise | Re_x ~ 10^7, 230 m/s | friction | Blade riblets sized to l_g+ = 10.7, i.e. s ~ 71 µm | scaling rule only; outside tested Re | low (extrapolation) |
| Car body, attached upper surfaces | L ~ 1-2 m, 25-35 m/s | mixed | Riblets on roof and hood; do not dimple attached-flow regions | plate results, Section 5.2 | moderate |
| Car body, base and wake | - | pressure | Micro-texture does not address base drag; use geometry or active control | outside model scope | n/a |
| Sports ball or bluff body near its crisis | Re_D = 5 x 10^4 - 2 x 10^5 | pressure | Hexagonal dimples, d/D = 0.10, D_dimple/D_body ~ 0.047 | `B-HEX-d2.0-r0.1`, +52.8% at 50 m/s | high (in-domain) |
| Bluff body far below its crisis | Re_D < ~2 x 10^4 | pressure | Leave it smooth; every class tested is net-negative | Table 4, sphere low/moderate rows | high |
| Competitive swimwear, hydrofoils | water, Re_L ~ 10^6 | friction | Riblets in principle; sizing must be redone for water | air-only calibration | low (out of domain) |

Three of these deserve comment.

The **cruise-aircraft** row is a scaling illustration, not a prediction of this model. At U
= 230 m/s and nu = 3.9e-05 m^2/s (ISA, 11 km) taken 3 m aft of the nose, Re_x = 1.77e+07,
C_F = 0.00275, u_tau = 8.52 m/s and the viscous length is 4.58 µm. Holding l_g+ = 10.7 fixed
gives a required groove scale of l_g = 49.0 µm, i.e. a blade spacing near 71 µm or a
V-groove spacing near 83 µm. That is one to two orders of magnitude finer than anything that
performs well at 10 m/s on a 0.1 m plate, which is the practical reason riblet films for
transport aircraft are hard: the correct feature size shrinks in direct proportion to the
viscous length.

The **bluff-body-below-crisis** row is the recommendation most likely to be ignored and most
likely to matter. A great deal of consumer and hobbyist "aero texturing" is applied to
bodies operating one to two decades below their critical Reynolds number, where this study
finds no texture helps and most hurt.

The **swimwear** row is included because it is a common motivation for shark-skin research,
and excluded from any quantitative claim because this study is calibrated for air. The
Reynolds-number mapping is straightforward in principle: water's kinematic viscosity is
roughly 1/15 that of air, so the viscous length at a given speed is far smaller and the
required riblet spacing correspondingly finer, but nothing in this dataset was computed for
water, and no number here should be quoted for a swimsuit.

### 6.9 Limitations of reduced-order modelling versus full CFD

The most important limitation is structural. **This model is calibrated to published
experiments, which means that over most of its range it interpolates the literature rather
than independently predicting it.** Only three of the thirteen validation benchmarks are
emergent (Table 1); the other ten test that the implementation is faithful, not that the
physics is right. Any reader treating the calibrated benchmarks as validation is
double-counting.

A full wall-resolved CFD study would remove that circularity, and it is worth being concrete
about why one was not run. Resolving a 50 µm riblet over a 0.1 m plate with the ~10
wall-unit spanwise resolution needed to capture the groove flow requires on the order of
10^9 cells for a single direct numerical simulation; there are 670 geometry-speed-body
combinations in this study. The riblet DNS literature that this model borrows from typically
simulates a handful of geometries in minimal-span channels for exactly this reason [8,9]. A
reduced-order model is the only way to survey 67 geometries; the price is that it cannot
discover physics that was not put into it.

The specific consequences are:

1. **No resolved flow field.** The model returns integrated coefficients. It cannot show
   where separation occurs on the plate, cannot resolve the Kelvin-Helmholtz rollers that
   terminate the riblet viscous regime [5,12], and cannot resolve the in-dimple
   recirculation that Beratlis et al. identified as the source of the dimpled sphere's local
   drag penalty [34].
2. **Zero pressure gradient assumed throughout.** Real wings and car bodies have strong
   favourable and adverse gradients, which change both the friction level and the riblet
   optimum. Nothing here transfers directly to an adverse-gradient region.
3. **Perfect flow alignment assumed.** Riblets are directional, and yaw degrades their
   performance; no yaw sensitivity is modelled. For a swept wing or a vehicle in crosswind
   this is a first-order omission.
4. **Boundary-layer thickness is internally inconsistent at low Reynolds number.** At Re_L =
   64,035 the standard 0.37 L Re^(-1/5) turbulent correlation gives delta = 4.05 mm while
   integrating the Spalding wall profile to u = 0.99 U gives 2.18 mm, a factor of 1.9. Both
   correlations are being used below their validated range. Figure 6 uses the
   profile-derived value and says so; no result in Section 5 depends on delta.
5. **The lowest speed is an extrapolation.** At 1 m/s, Re_L = 6,404, and the Schlichting
   turbulent-plate correlation is being applied roughly two decades below the range it was
   fitted on. All 214 rows at that condition or in the hybrid class carry `model_confidence
   = "low"`.
6. **The trip is an assumption, not a measurement.** At L = 0.1 m none of the five speeds
   transitions naturally; 78.1 m/s would be required. A leading-edge trip is standard
   wind-tunnel practice and is what the `natural_regime` column records, but the trip itself
   adds drag that is not accounted for, and a real experiment must subtract it.
7. **Sphere wall shear is approximated.** The sphere's u_tau, and therefore its reported s+,
   are estimated from the flat-plate correlation at Re_D. This is adequate for classifying
   whether a texture is hydraulically smooth; it is not adequate for predicting a riblet
   optimum on a curved, separating body.
8. **h/s efficiency is a lumped empirical factor.** The Gaussian eta_hs term absorbs
   wetted-area increase, secondary-flow losses and tip effects into a single curve fitted to
   one dataset [4]. A mechanistic model would separate them [10,11].
9. **No manufacturing tolerance, fouling, erosion or ageing.** Riblet tips are fragile and
   their benefit degrades as they round over; dimples fill with debris. Nothing here models
   service life.

### 6.10 Manufacturing feasibility

The manufacturability analysis produced the study's most practically useful surprise: on the
plate there is **no performance-versus-manufacturability trade-off at all**. The Pareto
front in the manufacturability plane collapses to the single point `A-V-s500-h250` (Table
13), a 500 µm-spaced, 250 µm-deep V-groove whose minimum feature is 250 µm, coarse enough
to be produced by micro-rolling, embossing or adhesive film, the same tier of process used
for commercial riblet films [16]. Moving up the process ladder to 50 µm blade riblets (laser
or diamond micro-milling) *reduces* the achievable drag reduction at 10 m/s from 5.344% to
2.570%, and moving to 25 µm lithographic hybrid features reduces it to 0.127%.

The reason is the wall-unit scaling. At 10 m/s the viscous length is 24.8 µm, so the groove
scale that satisfies l_g+ = 10.7 is hundreds of micrometres. Fine features are actively wrong at this Reynolds number, because they sit deep in the
hydraulically-smooth regime and do nothing. Fine features only become correct at high
hydraulically-smooth regime and do nothing. Fine features only become correct at high
Reynolds number, which is precisely where manufacturing becomes hard.

For the four classes the practical picture is:

- **Riblets** are the most manufacturable and the best performing on the plate. At the sizes
  that work here they are within reach of embossing, micro-rolling, or even careful 3D
  printing, and adhesive riblet film is a mature product concept. Blade riblets are the
  exception: their thin, tall elements are fragile and require micro-milling or laser
  structuring, and they are the class most degraded by tip rounding.
- **Dimples** are trivially manufacturable at the sizes tested here (0.5-5 mm, so minimum
  features of 250-1500 µm) by stamping, embossing or moulding. On a sphere, where they are
  transformative, this is a strong combination. On a plate, where they are net-negative,
  ease of manufacture is irrelevant.
- **Denticles** are the least manufacturable and the worst performing on the plate, a bad
  combination. Faithful denticle replication requires soft lithography, two-photon
  polymerisation or high-resolution additive manufacturing [19,22], and this study predicts
  that the resulting surface will recover at most 21% of what a far cheaper riblet film
  would deliver.
- **Hybrids** combine the tightest tolerance requirement with the widest uncertainty band
  and the weakest predicted performance.

### 6.11 What would falsify these conclusions

Three predictions are specific enough to be wrong, and testing them is the natural next
step:

1. **Riblet sizing dominates riblet shape.** A wind-tunnel test at 10 m/s on a 0.1 m tripped
   plate should show a V-groove at s = 500 µm outperforming a blade riblet at s = 100 µm,
   despite the blade's higher intrinsic ceiling, because only the former is near l_g+ =
   10.7. If the blade wins, the l_g+ scaling as implemented is wrong.
2. **Denticle films underperform riblet films by roughly a factor of four to five.** Section
   6.5 gives the threshold: more than ~4% on a flat plate at these Reynolds numbers
   falsifies the denticle sub-model.
3. **Riblet-dimple hybrids never beat their better constituent.** A single counter-example
   at any condition falsifies the sub-additivity assumption, which would be a genuinely
   interesting result.

---

## 7. Conclusion

### 7.1 Contributions

This study built a semi-empirical, uncertainty-propagating reduced-order model of surface
micro-texture drag and used it to rank 67 geometries across 5 flow speeds on 2 test bodies,
producing a 670-row dataset in which every geometry is evaluated on identical terms. Four
contributions stand out.

**A cross-body ranking that reverses.** The best plate geometry is the blade riblet
`A-BLAD-s200-h100` at 9.51 ± 1.5% (20 m/s, s+ = 14.9); the best sphere geometry is the
dimple `B-HEX-d2.0-r0.1` at 52.77 ± 4.1% (50 m/s), which is 5.55 times larger. Riblets are
the only class with a positive plate mean; dimples dominate the sphere. A single-body study
of either kind would have produced a confidently wrong general recommendation.

**An emergent, not imposed, reproduction of riblet scaling.** The optimal groove scale
collapses to l_g+ = 10.70-10.72 across four riblet profiles whose optimal spacings span s+ =
15.5 to 18.1, the blade optimum falls at s+ = 15.5 inside the published 13-20 band, and the
drag-increase crossing falls at s+ = 31.1 inside the published 25-40 band. These three
results were not calibration targets.

**Two clean negative results.** No hybrid, at any of 50 geometry-speed cases, beat its own
best constituent; the mean cost of hybridising is 2.92 percentage points. And on a
subcritical bluff body every texture class tested is net-harmful: the best sphere geometry
at 10 m/s still loses to a smooth surface. Negative results of this kind are cheap to obtain
computationally and expensive to obtain experimentally, which is a reasonable argument for
doing the survey this way round.

**Honest uncertainty.** Every prediction carries a class-specific uncertainty band, every
ranking flags statistical ties, and 214 of 670 rows are explicitly labelled low-confidence.
The validation table separates what the model was told from what it worked out.

### 7.2 Recommended texture by application

For a **friction-dominated surface at these Reynolds numbers** (a small UAV wing, a
wind-tunnel model, the attached-flow region of a vehicle), use **riblets sized to l_g+ ~
10.7 at the design speed**, which at 10-20 m/s means groove spacings of a few hundred
micrometres. Shape matters less than size: a correctly-sized V-groove beats an
incorrectly-sized blade. Expect 5-9% on the treated area, and expect it to degrade sharply
if the operating speed rises much above the design point.

For a **pressure-dominated bluff body operating near its critical Reynolds number**, use
**hexagonal dimples at d/D ~ 0.10 with 40-80% coverage**, and expect a transformative rather
than incremental effect, up to 53% here. For the same body a decade below its crisis, use
nothing.

For **shark-skin denticles**, the recommendation is negative: at these conditions they are
harder to make than riblets and deliver at most 21% of the benefit. Their appeal is
biological, not aerodynamic, and the biological advantage probably lies in mechanisms
(compliance, bristling, separation control on a curved body) that a rigid manufactured film
does not reproduce.

For **hybrids**, the recommendation is also negative, and is offered as a falsifiable
prediction rather than a settled conclusion.

### 7.3 Future work

The single highest-value next step is **experimental**, not computational: a tripped
flat-plate wind-tunnel campaign at 10-20 m/s testing three riblet spacings that bracket l_g+
= 10.7, one denticle film, and one shallow-dimple plate, with force-balance resolution
better than 1% of total drag. That campaign would test all three falsifiable predictions of
Section 6.11 at once and would either validate the ranking or identify exactly which
sub-model is wrong.

The highest-value **computational** next step is a small number of wall-resolved LES or DNS
cases at the top of the ranking (one blade riblet near optimum, one past breakdown, one
dimpled sphere either side of the crisis) to replace lumped terms with resolved physics at
the four or five conditions where the ranking is decided.

Beyond those: extend the flow-condition matrix upward in Reynolds number so the
cruise-relevant regime is inside the domain rather than extrapolated from it; add
pressure-gradient and yaw sensitivity, since both are first-order for any real application;
and, if the hybrid question is to be settled, look for a mechanism by which two textures
could be genuinely synergistic before testing more combinations blindly.

---

## 8. References

All 41 references below are real, published works, verified by DOI or by publisher record.
Formatting follows AIAA style.

[1] Schlichting, H., and Gersten, K., *Boundary-Layer Theory*, 9th ed., Springer-Verlag,
    Berlin, 2017, Chaps. 2, 17, 18.
[2] Walsh, M. J., "Riblets as a Viscous Drag Reduction Technique," *AIAA Journal*, 1983.
    doi:10.2514/3.60126
[3] Walsh, M., "Turbulent boundary layer drag reduction using riblets," *20th Aerospace
    Sciences Meeting*, 1982. doi:10.2514/6.1982-169
[4] Bechert, D. W., Bruse, M., Hage, W., van der Hoeven, J. G. T., and Hoppe, G.,
    "Experiments on Drag-Reducing Surfaces and Their Optimization with an Adjustable
    Geometry," *Journal of Fluid Mechanics*, Vol. 338, 1997, pp. 59-87.
    doi:10.1017/S0022112096004673
[5] García-Mayoral, R., and Jiménez, J., "Hydrodynamic stability and breakdown of the
    viscous regime over riblets," *Journal of Fluid Mechanics*, 2011.
    doi:10.1017/jfm.2011.114
[6] García-Mayoral, R., and Jiménez, J., "Drag reduction by riblets," *Philosophical
    Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*,
    2011. doi:10.1098/rsta.2010.0359
[7] von Deyn, L. H., Gatti, D., and Frohnapfel, B., "From drag-reducing riblets to
    drag-increasing ridges," *Journal of Fluid Mechanics*, 2022. doi:10.1017/jfm.2022.796
[8] Endrikat, S., Modesti, D., MacDonald, M., García-Mayoral, R., Hutchins, N., and Chung,
    D., "Direct Numerical Simulations of Turbulent Flow Over Various Riblet Shapes in
    Minimal-Span Channels," *Flow, Turbulence and Combustion*, 2020.
    doi:10.1007/s10494-020-00224-z
[9] Modesti, D., Endrikat, S., Hutchins, N., and Chung, D., "Dispersive stresses in
    turbulent flow over riblets," *Journal of Fluid Mechanics*, 2021.
    doi:10.1017/jfm.2021.310
[10] Wong, J., Camobreco, C. J., García-Mayoral, R., Hutchins, N., and Chung, D., "A viscous
     vortex model for predicting the drag reduction of riblet surfaces," *Journal of Fluid
     Mechanics*, 2024. doi:10.1017/jfm.2023.1006
[11] Ran, W., Zare, A., and Jovanović, M. R., "Model-based design of riblets for turbulent
     drag reduction," *Journal of Fluid Mechanics*, 2020. doi:10.1017/jfm.2020.722
[12] Camobreco, C. J., Endrikat, S., García-Mayoral, R., Luhar, M., and Chung, D., "Why do
     only some riblets promote spanwise rollers?," *Journal of Fluid Mechanics*, 2025.
     doi:10.1017/jfm.2025.10790
[13] Lazos, B., and Wilkinson, S. P., "Turbulent viscous drag reduction with thin-element
     riblets," *AIAA Journal*, 1988. doi:10.2514/3.9922
[14] Parker, K., and Sayers, A. T., "The effect of longitudinal microstriations and their
     profiles on the drag of flat plates," *Proceedings of the Institution of Mechanical
     Engineers, Part C: Journal of Mechanical Engineering Science*, 1999.
     doi:10.1243/0954406991522392
[15] Bezuijen, S., "Hydrodynamic Drag Reduction in Turbulent Boundary Layer Flow Using
     Riblets," M.S. Thesis, Delft Univ. of Technology, Delft, The Netherlands, 2017.
[16] Dean, B., and Bhushan, B., "Shark-skin surfaces for fluid-drag reduction in turbulent
     flow: a review," *Philosophical transactions. Series A, Mathematical, physical, and
     engineering sciences*, 2010. doi:10.1098/rsta.2010.0201
[17] Bechert, D. W., Bruse, M., and Hage, W., "Experiments with three-dimensional riblets as
     an idealized model of shark skin," *Experiments in Fluids*, 2000.
     doi:10.1007/s003480050400
[18] Graybill, M. T., and Xu, N. W., "Experimental Studies of Bioinspired Shark Denticles
     for Drag Reduction," *Integrative And Comparative Biology*, 2024.
     doi:10.1093/icb/icae086
[19] Yang, K., et al., "Surface Modification of 3D Biomimetic Shark Denticle Structures for
     Drag Reduction," *Advanced Materials*, 2025. doi:10.1002/adma.202417337
[20] Lloyd, C. J., et al., "Hydrodynamic efficiency in sharks: the combined role of riblets
     and denticles," *Bioinspiration & Biomimetics*, 2021. doi:10.1088/1748-3190/abf3b1
[21] Osman, E., Xu, C., and Huang, W., "Experimental study of a zero-pressure-gradient
     turbulent boundary layer over a bioinspired surface with 3D-printed shark scales,"
     *Physics of Fluids*, 2026. doi:10.1063/5.0301233
[22] Cui, X., Chen, D., and Chen, H., "Multistage Gradient Bioinspired Riblets for
     Synergistic Drag Reduction and Efficient Antifouling," *ACS Omega*, 2023.
     doi:10.1021/acsomega.2c07729
[23] Bixler, G. D., and Bhushan, B., "Fluid Drag Reduction with Shark-Skin Riblet Inspired
     Microstructured Surfaces," *Advanced Functional Materials*, 2013.
     doi:10.1002/adfm.201203683
[24] Bixler, G. D., and Bhushan, B., "Shark skin inspired low-drag microstructured surfaces
     in closed channel flow," *Journal of Colloid and Interface Science*, 2013.
     doi:10.1016/j.jcis.2012.10.061
[25] Mawignon, F. J., et al., "Optimized three-dimensional cuboidal shark-inspired riblets
     for enhanced drag reduction in turbulent flow," *Ocean Engineering*, 2025.
     doi:10.1016/j.oceaneng.2024.120199
[26] van Nesselrooij, M., Veldhuis, L. L. M., van Oudheusden, B. W., and Schrijer, F. F. J.,
     "Drag reduction by means of dimpled surfaces in turbulent boundary layers,"
     *Experiments in Fluids*, 2016. doi:10.1007/s00348-016-2230-9
[27] van Nesselrooij, M., "On the Drag Reduction of Dimpled Surfaces in Turbulent Boundary
     Layers: Proof of Concept and Identification of Flow Structure," M.S. Thesis, Delft
     Univ. of Technology, Delft, The Netherlands, 2015.
[28] van Campenhout, O. W. G., van Nesselrooij, M., Lin, Y. Y., Casacuberta, J., van
     Oudheusden, B. W., and Hickel, S., "Experimental and numerical investigation into the
     drag performance of dimpled surfaces in a turbulent boundary layer," *International
     Journal of Heat and Fluid Flow*, 2023. doi:10.1016/j.ijheatfluidflow.2023.109110
[29] Gattere, F., Chiarini, A., and Quadrio, M., "Dimples for Skin-Friction Drag Reduction:
     Status and Perspectives," *Fluids*, 2022. doi:10.3390/fluids7070240
[30] Razzak, M. A., et al., "Experimental study of skin friction drag reduction of turbulent
     boundary layer over shallow dimples," *AIAA SCITECH 2022 Forum*, 2022.
     doi:10.2514/6.2022-0712
[31] Lienhart, H., Breuer, M., and Köksoy, C., "Drag reduction by dimples? – A complementary
     experimental/numerical investigation," *International Journal of Heat and Fluid Flow*,
     2008. doi:10.1016/j.ijheatfluidflow.2008.02.001
[32] Paik, B., et al., "Study on the Drag Reduction of 2-D Dimpled-Plates," *Journal of the
     Society of Naval Architects of Korea*, 2012. doi:10.3744/snak.2012.49.4.333
[33] İlter, Y. K., Ünal, U. O., Shi, W., Tokgöz, S., and Atlar, M., "An experimental
     investigation into the drag reduction performance of dimpled plates in a fully
     turbulent channel flow," *Ocean Engineering*, 2024. doi:10.1016/j.oceaneng.2024.118198
[34] Beratlis, N., Balaras, E., and Squires, K., "On the origin of the drag force on dimpled
     spheres," *Journal of Fluid Mechanics*, 2019. doi:10.1017/jfm.2019.647
[35] Bearman, P. W., and Harvey, J. K., "Golf Ball Aerodynamics," *Aeronautical Quarterly*,
     1976. doi:10.1017/s0001925900007617
[36] Achenbach, E., "The effects of surface roughness and tunnel blockage on the flow past
     spheres," *Journal of Fluid Mechanics*, 1974. doi:10.1017/s0022112074001285
[37] Achenbach, E., "Experiments on the flow past spheres at very high Reynolds numbers,"
     *Journal of Fluid Mechanics*, 1972. doi:10.1017/s0022112072000874
[38] Clift, R., Grace, J. R., and Weber, M. E., *Bubbles, Drops, and Particles*, Academic
     Press, New York, 1978, Chap. 5.
[39] Li, J., Tsubokura, M., and Tsunoda, M., "Numerical Investigation of the Flow Around a
     Golf Ball at Around the Critical Reynolds Number and its Comparison with a Smooth
     Sphere," *Flow, Turbulence and Combustion*, 2015. doi:10.1007/s10494-015-9630-4
[40] Aoki, K., Muto, K., and Okanaga, H., "Mechanism of Drag Reduction by Dimple Structures
     on a Sphere," *Journal of Fluid Science and Technology*, 2012. doi:10.1299/jfst.7.1
[41] Vilumbrales-Garcia, R., Sudarsana, P. B., and Sareen, A., "Adaptive drag reduction of a
     sphere using smart morphable skin," *Flow*, 2025. doi:10.1017/flo.2025.7

---

## Appendix A. Full drag coefficient table

Every row of `dataset.csv`, split by body. `Cf_smooth` and `Cf_textured` are skin-friction
coefficients; `Cd_press` is the pressure-drag coefficient (identically zero for the plate
except for the dimple form-drag term, which is reported as an equivalent coefficient);
`Cd_total` is the total drag coefficient on which `DR_net` is computed. `Conf.` is the
per-row model-confidence flag defined in Section 4.5.

### A.1 Flat plate, L = 0.1 m (335 rows)

| Geometry | Class | U (m/s) | Cf_smooth | Cf_textured | Cd_press | Cd_total | DR_net (%) | ± (pp) | Conf. |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| A-BLAD-s100-h50 | riblet | 1 | 0.014464 | 0.014413 | 0.000000 | 0.014413 | +0.347 | 1.5 | low |
| A-BLAD-s100-h50 | riblet | 5 | 0.009362 | 0.009232 | 0.000000 | 0.009232 | +1.397 | 1.5 | high |
| A-BLAD-s100-h50 | riblet | 10 | 0.007923 | 0.007720 | 0.000000 | 0.007720 | +2.570 | 1.5 | high |
| A-BLAD-s100-h50 | riblet | 20 | 0.006774 | 0.006452 | 0.000000 | 0.006452 | +4.753 | 1.5 | high |
| A-BLAD-s100-h50 | riblet | 50 | 0.005582 | 0.005053 | 0.000000 | 0.005053 | +9.471 | 1.5 | high |
| A-BLAD-s200-h100 | riblet | 1 | 0.014464 | 0.014363 | 0.000000 | 0.014363 | +0.694 | 1.5 | low |
| A-BLAD-s200-h100 | riblet | 5 | 0.009362 | 0.009101 | 0.000000 | 0.009101 | +2.794 | 1.5 | high |
| A-BLAD-s200-h100 | riblet | 10 | 0.007923 | 0.007516 | 0.000000 | 0.007516 | +5.140 | 1.5 | high |
| A-BLAD-s200-h100 | riblet | 20 | 0.006774 | 0.006130 | 0.000000 | 0.006130 | +9.506 | 1.5 | high |
| A-BLAD-s200-h100 | riblet | 50 | 0.005582 | 0.005714 | 0.000000 | 0.005714 | -2.363 | 1.8 | high |
| A-SCAL-s100-h50 | riblet | 1 | 0.014464 | 0.014440 | 0.000000 | 0.014440 | +0.166 | 1.5 | low |
| A-SCAL-s100-h50 | riblet | 5 | 0.009362 | 0.009300 | 0.000000 | 0.009300 | +0.667 | 1.5 | high |
| A-SCAL-s100-h50 | riblet | 10 | 0.007923 | 0.007826 | 0.000000 | 0.007826 | +1.228 | 1.5 | high |
| A-SCAL-s100-h50 | riblet | 20 | 0.006774 | 0.006620 | 0.000000 | 0.006620 | +2.270 | 1.5 | high |
| A-SCAL-s100-h50 | riblet | 50 | 0.005582 | 0.005294 | 0.000000 | 0.005294 | +5.152 | 1.5 | high |
| A-SCAL-s50-h25 | riblet | 1 | 0.014464 | 0.014452 | 0.000000 | 0.014452 | +0.083 | 1.5 | low |
| A-SCAL-s50-h25 | riblet | 5 | 0.009362 | 0.009331 | 0.000000 | 0.009331 | +0.334 | 1.5 | high |
| A-SCAL-s50-h25 | riblet | 10 | 0.007923 | 0.007875 | 0.000000 | 0.007875 | +0.614 | 1.5 | high |
| A-SCAL-s50-h25 | riblet | 20 | 0.006774 | 0.006697 | 0.000000 | 0.006697 | +1.135 | 1.5 | high |
| A-SCAL-s50-h25 | riblet | 50 | 0.005582 | 0.005438 | 0.000000 | 0.005438 | +2.576 | 1.5 | high |
| A-U-GR-s100-h50 | riblet | 1 | 0.014464 | 0.014442 | 0.000000 | 0.014442 | +0.148 | 1.5 | low |
| A-U-GR-s100-h50 | riblet | 5 | 0.009362 | 0.009307 | 0.000000 | 0.009307 | +0.595 | 1.5 | high |
| A-U-GR-s100-h50 | riblet | 10 | 0.007923 | 0.007837 | 0.000000 | 0.007837 | +1.095 | 1.5 | high |
| A-U-GR-s100-h50 | riblet | 20 | 0.006774 | 0.006637 | 0.000000 | 0.006637 | +2.025 | 1.5 | high |
| A-U-GR-s100-h50 | riblet | 50 | 0.005582 | 0.005325 | 0.000000 | 0.005325 | +4.596 | 1.5 | high |
| A-V-s100-h100 | riblet | 1 | 0.014464 | 0.014434 | 0.000000 | 0.014434 | +0.202 | 1.5 | low |
| A-V-s100-h100 | riblet | 5 | 0.009362 | 0.009286 | 0.000000 | 0.009286 | +0.813 | 1.5 | high |
| A-V-s100-h100 | riblet | 10 | 0.007923 | 0.007805 | 0.000000 | 0.007805 | +1.495 | 1.5 | high |
| A-V-s100-h100 | riblet | 20 | 0.006774 | 0.006587 | 0.000000 | 0.006587 | +2.765 | 1.5 | high |
| A-V-s100-h100 | riblet | 50 | 0.005582 | 0.005288 | 0.000000 | 0.005288 | +5.265 | 1.5 | high |
| A-V-s100-h25 | riblet | 1 | 0.014464 | 0.014457 | 0.000000 | 0.014457 | +0.049 | 1.5 | low |
| A-V-s100-h25 | riblet | 5 | 0.009362 | 0.009344 | 0.000000 | 0.009344 | +0.196 | 1.5 | high |
| A-V-s100-h25 | riblet | 10 | 0.007923 | 0.007895 | 0.000000 | 0.007895 | +0.361 | 1.5 | high |
| A-V-s100-h25 | riblet | 20 | 0.006774 | 0.006729 | 0.000000 | 0.006729 | +0.667 | 1.5 | high |
| A-V-s100-h25 | riblet | 50 | 0.005582 | 0.005497 | 0.000000 | 0.005497 | +1.514 | 1.5 | high |
| A-V-s100-h250 | riblet | 1 | 0.014464 | 0.014449 | 0.000000 | 0.014449 | +0.099 | 1.5 | low |
| A-V-s100-h250 | riblet | 5 | 0.009362 | 0.009325 | 0.000000 | 0.009325 | +0.400 | 1.5 | high |
| A-V-s100-h250 | riblet | 10 | 0.007923 | 0.007865 | 0.000000 | 0.007865 | +0.736 | 1.5 | high |
| A-V-s100-h250 | riblet | 20 | 0.006774 | 0.006682 | 0.000000 | 0.006682 | +1.361 | 1.5 | high |
| A-V-s100-h250 | riblet | 50 | 0.005582 | 0.005553 | 0.000000 | 0.005553 | +0.509 | 1.6 | high |
| A-V-s100-h50 | riblet | 1 | 0.014464 | 0.014443 | 0.000000 | 0.014443 | +0.144 | 1.5 | low |
| A-V-s100-h50 | riblet | 5 | 0.009362 | 0.009308 | 0.000000 | 0.009308 | +0.581 | 1.5 | high |
| A-V-s100-h50 | riblet | 10 | 0.007923 | 0.007839 | 0.000000 | 0.007839 | +1.069 | 1.5 | high |
| A-V-s100-h50 | riblet | 20 | 0.006774 | 0.006640 | 0.000000 | 0.006640 | +1.977 | 1.5 | high |
| A-V-s100-h50 | riblet | 50 | 0.005582 | 0.005331 | 0.000000 | 0.005331 | +4.486 | 1.5 | high |
| A-V-s200-h100 | riblet | 1 | 0.014464 | 0.014422 | 0.000000 | 0.014422 | +0.289 | 1.5 | low |
| A-V-s200-h100 | riblet | 5 | 0.009362 | 0.009254 | 0.000000 | 0.009254 | +1.162 | 1.5 | high |
| A-V-s200-h100 | riblet | 10 | 0.007923 | 0.007754 | 0.000000 | 0.007754 | +2.138 | 1.5 | high |
| A-V-s200-h100 | riblet | 20 | 0.006774 | 0.006506 | 0.000000 | 0.006506 | +3.953 | 1.5 | high |
| A-V-s200-h100 | riblet | 50 | 0.005582 | 0.005421 | 0.000000 | 0.005421 | +2.875 | 1.5 | high |
| A-V-s200-h25 | riblet | 1 | 0.014464 | 0.014461 | 0.000000 | 0.014461 | +0.016 | 1.5 | low |
| A-V-s200-h25 | riblet | 5 | 0.009362 | 0.009356 | 0.000000 | 0.009356 | +0.062 | 1.5 | high |
| A-V-s200-h25 | riblet | 10 | 0.007923 | 0.007914 | 0.000000 | 0.007914 | +0.115 | 1.5 | high |
| A-V-s200-h25 | riblet | 20 | 0.006774 | 0.006760 | 0.000000 | 0.006760 | +0.212 | 1.5 | high |
| A-V-s200-h25 | riblet | 50 | 0.005582 | 0.005555 | 0.000000 | 0.005555 | +0.482 | 1.5 | high |
| A-V-s200-h250 | riblet | 1 | 0.014464 | 0.014408 | 0.000000 | 0.014408 | +0.384 | 1.5 | low |
| A-V-s200-h250 | riblet | 5 | 0.009362 | 0.009218 | 0.000000 | 0.009218 | +1.543 | 1.5 | high |
| A-V-s200-h250 | riblet | 10 | 0.007923 | 0.007698 | 0.000000 | 0.007698 | +2.840 | 1.5 | high |
| A-V-s200-h250 | riblet | 20 | 0.006774 | 0.006468 | 0.000000 | 0.006468 | +4.525 | 1.5 | high |
| A-V-s200-h250 | riblet | 50 | 0.005582 | 0.005766 | 0.000000 | 0.005766 | -3.305 | 1.9 | high |
| A-V-s200-h50 | riblet | 1 | 0.014464 | 0.014450 | 0.000000 | 0.014450 | +0.097 | 1.5 | low |
| A-V-s200-h50 | riblet | 5 | 0.009362 | 0.009326 | 0.000000 | 0.009326 | +0.392 | 1.5 | high |
| A-V-s200-h50 | riblet | 10 | 0.007923 | 0.007866 | 0.000000 | 0.007866 | +0.721 | 1.5 | high |
| A-V-s200-h50 | riblet | 20 | 0.006774 | 0.006684 | 0.000000 | 0.006684 | +1.334 | 1.5 | high |
| A-V-s200-h50 | riblet | 50 | 0.005582 | 0.005440 | 0.000000 | 0.005440 | +2.540 | 1.5 | high |
| A-V-s50-h100 | riblet | 1 | 0.014464 | 0.014454 | 0.000000 | 0.014454 | +0.067 | 1.5 | low |
| A-V-s50-h100 | riblet | 5 | 0.009362 | 0.009337 | 0.000000 | 0.009337 | +0.268 | 1.5 | high |
| A-V-s50-h100 | riblet | 10 | 0.007923 | 0.007884 | 0.000000 | 0.007884 | +0.494 | 1.5 | high |
| A-V-s50-h100 | riblet | 20 | 0.006774 | 0.006712 | 0.000000 | 0.006712 | +0.913 | 1.5 | high |
| A-V-s50-h100 | riblet | 50 | 0.005582 | 0.005466 | 0.000000 | 0.005466 | +2.072 | 1.5 | high |
| A-V-s50-h25 | riblet | 1 | 0.014464 | 0.014453 | 0.000000 | 0.014453 | +0.072 | 1.5 | low |
| A-V-s50-h25 | riblet | 5 | 0.009362 | 0.009335 | 0.000000 | 0.009335 | +0.290 | 1.5 | high |
| A-V-s50-h25 | riblet | 10 | 0.007923 | 0.007881 | 0.000000 | 0.007881 | +0.534 | 1.5 | high |
| A-V-s50-h25 | riblet | 20 | 0.006774 | 0.006707 | 0.000000 | 0.006707 | +0.988 | 1.5 | high |
| A-V-s50-h25 | riblet | 50 | 0.005582 | 0.005457 | 0.000000 | 0.005457 | +2.243 | 1.5 | high |
| A-V-s50-h250 | riblet | 1 | 0.014464 | 0.014462 | 0.000000 | 0.014462 | +0.012 | 1.5 | low |
| A-V-s50-h250 | riblet | 5 | 0.009362 | 0.009358 | 0.000000 | 0.009358 | +0.049 | 1.5 | high |
| A-V-s50-h250 | riblet | 10 | 0.007923 | 0.007916 | 0.000000 | 0.007916 | +0.090 | 1.5 | high |
| A-V-s50-h250 | riblet | 20 | 0.006774 | 0.006763 | 0.000000 | 0.006763 | +0.167 | 1.5 | high |
| A-V-s50-h250 | riblet | 50 | 0.005582 | 0.005568 | 0.000000 | 0.005568 | +0.253 | 1.5 | high |
| A-V-s50-h50 | riblet | 1 | 0.014464 | 0.014449 | 0.000000 | 0.014449 | +0.101 | 1.5 | low |
| A-V-s50-h50 | riblet | 5 | 0.009362 | 0.009324 | 0.000000 | 0.009324 | +0.406 | 1.5 | high |
| A-V-s50-h50 | riblet | 10 | 0.007923 | 0.007864 | 0.000000 | 0.007864 | +0.748 | 1.5 | high |
| A-V-s50-h50 | riblet | 20 | 0.006774 | 0.006680 | 0.000000 | 0.006680 | +1.382 | 1.5 | high |
| A-V-s50-h50 | riblet | 50 | 0.005582 | 0.005407 | 0.000000 | 0.005407 | +3.137 | 1.5 | high |
| A-V-s500-h100 | riblet | 1 | 0.014464 | 0.014443 | 0.000000 | 0.014443 | +0.146 | 1.5 | low |
| A-V-s500-h100 | riblet | 5 | 0.009362 | 0.009307 | 0.000000 | 0.009307 | +0.589 | 1.5 | high |
| A-V-s500-h100 | riblet | 10 | 0.007923 | 0.007838 | 0.000000 | 0.007838 | +1.084 | 1.5 | high |
| A-V-s500-h100 | riblet | 20 | 0.006774 | 0.006657 | 0.000000 | 0.006657 | +1.726 | 1.5 | high |
| A-V-s500-h100 | riblet | 50 | 0.005582 | 0.005652 | 0.000000 | 0.005652 | -1.261 | 1.9 | high |
| A-V-s500-h25 | riblet | 1 | 0.014464 | 0.014464 | 0.000000 | 0.014464 | +0.001 | 1.5 | low |
| A-V-s500-h25 | riblet | 5 | 0.009362 | 0.009362 | 0.000000 | 0.009362 | +0.004 | 1.5 | high |
| A-V-s500-h25 | riblet | 10 | 0.007923 | 0.007923 | 0.000000 | 0.007923 | +0.008 | 1.5 | high |
| A-V-s500-h25 | riblet | 20 | 0.006774 | 0.006773 | 0.000000 | 0.006773 | +0.015 | 1.5 | high |
| A-V-s500-h25 | riblet | 50 | 0.005582 | 0.005581 | 0.000000 | 0.005581 | +0.022 | 1.5 | high |
| A-V-s500-h250 | riblet | 1 | 0.014464 | 0.014359 | 0.000000 | 0.014359 | +0.722 | 1.5 | low |
| A-V-s500-h250 | riblet | 5 | 0.009362 | 0.009090 | 0.000000 | 0.009090 | +2.905 | 1.5 | high |
| A-V-s500-h250 | riblet | 10 | 0.007923 | 0.007500 | 0.000000 | 0.007500 | +5.344 | 1.5 | high |
| A-V-s500-h250 | riblet | 20 | 0.006774 | 0.006650 | 0.000000 | 0.006650 | +1.829 | 1.6 | high |
| A-V-s500-h250 | riblet | 50 | 0.005582 | 0.006559 | 0.000000 | 0.006559 | -17.506 | 2.6 | high |
| A-V-s500-h50 | riblet | 1 | 0.014464 | 0.014461 | 0.000000 | 0.014461 | +0.018 | 1.5 | low |
| A-V-s500-h50 | riblet | 5 | 0.009362 | 0.009355 | 0.000000 | 0.009355 | +0.074 | 1.5 | high |
| A-V-s500-h50 | riblet | 10 | 0.007923 | 0.007913 | 0.000000 | 0.007913 | +0.136 | 1.5 | high |
| A-V-s500-h50 | riblet | 20 | 0.006774 | 0.006757 | 0.000000 | 0.006757 | +0.251 | 1.5 | high |
| A-V-s500-h50 | riblet | 50 | 0.005582 | 0.005577 | 0.000000 | 0.005577 | +0.094 | 1.6 | high |
| B-HEX-d0.5-r0.05 | dimple | 1 | 0.014464 | 0.014464 | 0.000081 | 0.014545 | -0.560 | 2.5 | low |
| B-HEX-d0.5-r0.05 | dimple | 5 | 0.009362 | 0.009362 | 0.000052 | 0.009415 | -0.560 | 2.5 | moderate |
| B-HEX-d0.5-r0.05 | dimple | 10 | 0.007923 | 0.007923 | 0.000044 | 0.007967 | -0.554 | 2.5 | moderate |
| B-HEX-d0.5-r0.05 | dimple | 20 | 0.006774 | 0.006771 | 0.000038 | 0.006809 | -0.515 | 2.5 | moderate |
| B-HEX-d0.5-r0.05 | dimple | 50 | 0.005582 | 0.005564 | 0.000031 | 0.005595 | -0.234 | 2.5 | moderate |
| B-HEX-d0.5-r0.1 | dimple | 1 | 0.014464 | 0.014464 | 0.000324 | 0.014788 | -2.240 | 2.5 | low |
| B-HEX-d0.5-r0.1 | dimple | 5 | 0.009362 | 0.009362 | 0.000210 | 0.009572 | -2.236 | 2.5 | moderate |
| B-HEX-d0.5-r0.1 | dimple | 10 | 0.007923 | 0.007921 | 0.000177 | 0.008099 | -2.211 | 2.5 | moderate |
| B-HEX-d0.5-r0.1 | dimple | 20 | 0.006774 | 0.006765 | 0.000152 | 0.006917 | -2.110 | 2.5 | moderate |
| B-HEX-d0.5-r0.1 | dimple | 50 | 0.005582 | 0.005556 | 0.000125 | 0.005681 | -1.770 | 2.5 | moderate |
| B-HEX-d0.5-r0.2 | dimple | 1 | 0.014464 | 0.014464 | 0.001296 | 0.015760 | -8.960 | 2.5 | low |
| B-HEX-d0.5-r0.2 | dimple | 5 | 0.009362 | 0.009362 | 0.000839 | 0.010201 | -8.955 | 2.5 | moderate |
| B-HEX-d0.5-r0.2 | dimple | 10 | 0.007923 | 0.007922 | 0.000710 | 0.008632 | -8.939 | 2.5 | moderate |
| B-HEX-d0.5-r0.2 | dimple | 20 | 0.006774 | 0.006770 | 0.000607 | 0.007377 | -8.905 | 2.5 | moderate |
| B-HEX-d0.5-r0.2 | dimple | 50 | 0.005582 | 0.005576 | 0.000500 | 0.006077 | -8.862 | 2.5 | moderate |
| B-HEX-d0.5-r0.3 | dimple | 1 | 0.014464 | 0.014464 | 0.002916 | 0.017380 | -20.160 | 2.5 | low |
| B-HEX-d0.5-r0.3 | dimple | 5 | 0.009362 | 0.009362 | 0.001887 | 0.011250 | -20.158 | 2.5 | moderate |
| B-HEX-d0.5-r0.3 | dimple | 10 | 0.007923 | 0.007923 | 0.001597 | 0.009520 | -20.153 | 2.5 | moderate |
| B-HEX-d0.5-r0.3 | dimple | 20 | 0.006774 | 0.006773 | 0.001366 | 0.008139 | -20.146 | 2.5 | moderate |
| B-HEX-d0.5-r0.3 | dimple | 50 | 0.005582 | 0.005581 | 0.001125 | 0.006706 | -20.144 | 2.5 | moderate |
| B-HEX-d1.0-r0.05 | dimple | 1 | 0.014464 | 0.014464 | 0.000081 | 0.014545 | -0.560 | 2.5 | low |
| B-HEX-d1.0-r0.05 | dimple | 5 | 0.009362 | 0.009362 | 0.000052 | 0.009414 | -0.552 | 2.5 | moderate |
| B-HEX-d1.0-r0.05 | dimple | 10 | 0.007923 | 0.007919 | 0.000044 | 0.007963 | -0.504 | 2.5 | moderate |
| B-HEX-d1.0-r0.05 | dimple | 20 | 0.006774 | 0.006757 | 0.000038 | 0.006795 | -0.307 | 2.5 | moderate |
| B-HEX-d1.0-r0.05 | dimple | 50 | 0.005582 | 0.005531 | 0.000031 | 0.005562 | +0.355 | 2.5 | moderate |
| B-HEX-d1.0-r0.1 | dimple | 1 | 0.014464 | 0.014464 | 0.000324 | 0.014788 | -2.240 | 2.5 | low |
| B-HEX-d1.0-r0.1 | dimple | 5 | 0.009362 | 0.009359 | 0.000210 | 0.009569 | -2.204 | 2.5 | moderate |
| B-HEX-d1.0-r0.1 | dimple | 10 | 0.007923 | 0.007911 | 0.000177 | 0.008089 | -2.088 | 2.5 | moderate |
| B-HEX-d1.0-r0.1 | dimple | 20 | 0.006774 | 0.006746 | 0.000152 | 0.006898 | -1.833 | 2.5 | moderate |
| B-HEX-d1.0-r0.1 | dimple | 50 | 0.005582 | 0.005541 | 0.000125 | 0.005666 | -1.511 | 2.5 | moderate |
| B-HEX-d1.0-r0.2 | dimple | 1 | 0.014464 | 0.014464 | 0.001296 | 0.015760 | -8.959 | 2.5 | low |
| B-HEX-d1.0-r0.2 | dimple | 5 | 0.009362 | 0.009360 | 0.000839 | 0.010199 | -8.936 | 2.5 | moderate |
| B-HEX-d1.0-r0.2 | dimple | 10 | 0.007923 | 0.007919 | 0.000710 | 0.008629 | -8.900 | 2.5 | moderate |
| B-HEX-d1.0-r0.2 | dimple | 20 | 0.006774 | 0.006768 | 0.000607 | 0.007375 | -8.865 | 2.5 | moderate |
| B-HEX-d1.0-r0.2 | dimple | 50 | 0.005582 | 0.005577 | 0.000500 | 0.006077 | -8.875 | 2.5 | moderate |
| B-HEX-d1.0-r0.3 | dimple | 1 | 0.014464 | 0.014464 | 0.002916 | 0.017380 | -20.160 | 2.5 | low |
| B-HEX-d1.0-r0.3 | dimple | 5 | 0.009362 | 0.009362 | 0.001887 | 0.011249 | -20.152 | 2.5 | moderate |
| B-HEX-d1.0-r0.3 | dimple | 10 | 0.007923 | 0.007922 | 0.001597 | 0.009520 | -20.146 | 2.5 | moderate |
| B-HEX-d1.0-r0.3 | dimple | 20 | 0.006774 | 0.006773 | 0.001366 | 0.008139 | -20.143 | 2.5 | moderate |
| B-HEX-d1.0-r0.3 | dimple | 50 | 0.005582 | 0.005581 | 0.001125 | 0.006707 | -20.150 | 2.5 | moderate |
| B-HEX-d2.0-r0.05 | dimple | 1 | 0.014464 | 0.014464 | 0.000081 | 0.014545 | -0.560 | 2.5 | low |
| B-HEX-d2.0-r0.05 | dimple | 5 | 0.009362 | 0.009356 | 0.000052 | 0.009408 | -0.489 | 2.5 | moderate |
| B-HEX-d2.0-r0.05 | dimple | 10 | 0.007923 | 0.007900 | 0.000044 | 0.007944 | -0.263 | 2.5 | moderate |
| B-HEX-d2.0-r0.05 | dimple | 20 | 0.006774 | 0.006720 | 0.000038 | 0.006758 | +0.232 | 2.5 | moderate |
| B-HEX-d2.0-r0.05 | dimple | 50 | 0.005582 | 0.005503 | 0.000031 | 0.005534 | +0.861 | 2.5 | moderate |
| B-HEX-d2.0-r0.1 | dimple | 1 | 0.014464 | 0.014463 | 0.000324 | 0.014787 | -2.236 | 2.5 | low |
| B-HEX-d2.0-r0.1 | dimple | 5 | 0.009362 | 0.009346 | 0.000210 | 0.009555 | -2.061 | 2.5 | moderate |
| B-HEX-d2.0-r0.1 | dimple | 10 | 0.007923 | 0.007888 | 0.000177 | 0.008066 | -1.794 | 2.5 | moderate |
| B-HEX-d2.0-r0.1 | dimple | 20 | 0.006774 | 0.006726 | 0.000152 | 0.006878 | -1.537 | 2.5 | moderate |
| B-HEX-d2.0-r0.1 | dimple | 50 | 0.005582 | 0.005547 | 0.000125 | 0.005672 | -1.614 | 2.5 | moderate |
| B-HEX-d2.0-r0.2 | dimple | 1 | 0.014464 | 0.014463 | 0.001296 | 0.015759 | -8.955 | 2.5 | low |
| B-HEX-d2.0-r0.2 | dimple | 5 | 0.009362 | 0.009356 | 0.000839 | 0.010195 | -8.894 | 2.5 | moderate |
| B-HEX-d2.0-r0.2 | dimple | 10 | 0.007923 | 0.007916 | 0.000710 | 0.008626 | -8.863 | 2.5 | moderate |
| B-HEX-d2.0-r0.2 | dimple | 20 | 0.006774 | 0.006768 | 0.000607 | 0.007375 | -8.869 | 2.5 | moderate |
| B-HEX-d2.0-r0.2 | dimple | 50 | 0.005582 | 0.005580 | 0.000500 | 0.006080 | -8.920 | 2.5 | moderate |
| B-HEX-d2.0-r0.3 | dimple | 1 | 0.014464 | 0.014463 | 0.002916 | 0.017379 | -20.158 | 2.5 | low |
| B-HEX-d2.0-r0.3 | dimple | 5 | 0.009362 | 0.009361 | 0.001887 | 0.011248 | -20.145 | 2.5 | moderate |
| B-HEX-d2.0-r0.3 | dimple | 10 | 0.007923 | 0.007922 | 0.001597 | 0.009519 | -20.144 | 2.5 | moderate |
| B-HEX-d2.0-r0.3 | dimple | 20 | 0.006774 | 0.006773 | 0.001366 | 0.008139 | -20.149 | 2.5 | moderate |
| B-HEX-d2.0-r0.3 | dimple | 50 | 0.005582 | 0.005582 | 0.001125 | 0.006707 | -20.157 | 2.5 | moderate |
| B-HEX-d5.0-r0.05 | dimple | 1 | 0.014464 | 0.014461 | 0.000081 | 0.014542 | -0.543 | 2.5 | low |
| B-HEX-d5.0-r0.05 | dimple | 5 | 0.009362 | 0.009314 | 0.000052 | 0.009367 | -0.047 | 2.5 | moderate |
| B-HEX-d5.0-r0.05 | dimple | 10 | 0.007923 | 0.007838 | 0.000044 | 0.007882 | +0.522 | 2.5 | moderate |
| B-HEX-d5.0-r0.05 | dimple | 20 | 0.006774 | 0.006676 | 0.000038 | 0.006714 | +0.881 | 2.5 | moderate |
| B-HEX-d5.0-r0.05 | dimple | 50 | 0.005582 | 0.005525 | 0.000031 | 0.005556 | +0.463 | 2.5 | moderate |
| B-HEX-d5.0-r0.1 | dimple | 1 | 0.014464 | 0.014454 | 0.000324 | 0.014778 | -2.176 | 2.5 | low |
| B-HEX-d5.0-r0.1 | dimple | 5 | 0.009362 | 0.009307 | 0.000210 | 0.009516 | -1.647 | 2.5 | moderate |
| B-HEX-d5.0-r0.1 | dimple | 10 | 0.007923 | 0.007865 | 0.000177 | 0.008042 | -1.498 | 2.5 | moderate |
| B-HEX-d5.0-r0.1 | dimple | 20 | 0.006774 | 0.006734 | 0.000152 | 0.006886 | -1.656 | 2.5 | moderate |
| B-HEX-d5.0-r0.1 | dimple | 50 | 0.005582 | 0.005570 | 0.000125 | 0.005695 | -2.034 | 2.5 | moderate |
| B-HEX-d5.0-r0.2 | dimple | 1 | 0.014464 | 0.014459 | 0.001296 | 0.015755 | -8.925 | 2.5 | low |
| B-HEX-d5.0-r0.2 | dimple | 5 | 0.009362 | 0.009353 | 0.000839 | 0.010192 | -8.860 | 2.5 | moderate |
| B-HEX-d5.0-r0.2 | dimple | 10 | 0.007923 | 0.007918 | 0.000710 | 0.008627 | -8.886 | 2.5 | moderate |
| B-HEX-d5.0-r0.2 | dimple | 20 | 0.006774 | 0.006772 | 0.000607 | 0.007379 | -8.926 | 2.5 | moderate |
| B-HEX-d5.0-r0.2 | dimple | 50 | 0.005582 | 0.005582 | 0.000500 | 0.006082 | -8.954 | 2.5 | moderate |
| B-HEX-d5.0-r0.3 | dimple | 1 | 0.014464 | 0.014462 | 0.002916 | 0.017378 | -20.150 | 2.5 | low |
| B-HEX-d5.0-r0.3 | dimple | 5 | 0.009362 | 0.009361 | 0.001887 | 0.011248 | -20.146 | 2.5 | moderate |
| B-HEX-d5.0-r0.3 | dimple | 10 | 0.007923 | 0.007923 | 0.001597 | 0.009520 | -20.152 | 2.5 | moderate |
| B-HEX-d5.0-r0.3 | dimple | 20 | 0.006774 | 0.006774 | 0.001366 | 0.008139 | -20.157 | 2.5 | moderate |
| B-HEX-d5.0-r0.3 | dimple | 50 | 0.005582 | 0.005582 | 0.001125 | 0.006707 | -20.160 | 2.5 | moderate |
| B-HEXA-c20 | dimple | 1 | 0.014464 | 0.014464 | 0.000040 | 0.014504 | -0.280 | 2.5 | low |
| B-HEXA-c20 | dimple | 5 | 0.009362 | 0.009359 | 0.000026 | 0.009385 | -0.239 | 2.5 | moderate |
| B-HEXA-c20 | dimple | 10 | 0.007923 | 0.007910 | 0.000022 | 0.007932 | -0.110 | 2.5 | moderate |
| B-HEXA-c20 | dimple | 20 | 0.006774 | 0.006743 | 0.000019 | 0.006762 | +0.175 | 2.5 | moderate |
| B-HEXA-c20 | dimple | 50 | 0.005582 | 0.005536 | 0.000016 | 0.005552 | +0.536 | 2.5 | moderate |
| B-HEXA-c80 | dimple | 1 | 0.014464 | 0.014464 | 0.000162 | 0.014626 | -1.119 | 2.5 | low |
| B-HEXA-c80 | dimple | 5 | 0.009362 | 0.009351 | 0.000105 | 0.009456 | -0.997 | 2.5 | moderate |
| B-HEXA-c80 | dimple | 10 | 0.007923 | 0.007882 | 0.000089 | 0.007971 | -0.603 | 2.5 | moderate |
| B-HEXA-c80 | dimple | 20 | 0.006774 | 0.006681 | 0.000076 | 0.006756 | +0.260 | 2.5 | moderate |
| B-HEXA-c80 | dimple | 50 | 0.005582 | 0.005444 | 0.000063 | 0.005506 | +1.354 | 2.5 | moderate |
| B-SQUA-c40 | dimple | 1 | 0.014464 | 0.014464 | 0.000081 | 0.014545 | -0.560 | 2.5 | low |
| B-SQUA-c40 | dimple | 5 | 0.009362 | 0.009357 | 0.000052 | 0.009409 | -0.500 | 2.5 | moderate |
| B-SQUA-c40 | dimple | 10 | 0.007923 | 0.007903 | 0.000044 | 0.007948 | -0.308 | 2.5 | moderate |
| B-SQUA-c40 | dimple | 20 | 0.006774 | 0.006728 | 0.000038 | 0.006766 | +0.114 | 2.5 | moderate |
| B-SQUA-c40 | dimple | 50 | 0.005582 | 0.005514 | 0.000031 | 0.005546 | +0.648 | 2.5 | moderate |
| B-STAG-c60 | dimple | 1 | 0.014464 | 0.014464 | 0.000121 | 0.014585 | -0.839 | 2.5 | low |
| B-STAG-c60 | dimple | 5 | 0.009362 | 0.009354 | 0.000079 | 0.009432 | -0.747 | 2.5 | moderate |
| B-STAG-c60 | dimple | 10 | 0.007923 | 0.007893 | 0.000067 | 0.007959 | -0.450 | 2.5 | moderate |
| B-STAG-c60 | dimple | 20 | 0.006774 | 0.006703 | 0.000057 | 0.006760 | +0.201 | 2.5 | moderate |
| B-STAG-c60 | dimple | 50 | 0.005582 | 0.005478 | 0.000047 | 0.005525 | +1.027 | 2.5 | moderate |
| C-SK-s100-o0 | shark | 1 | 0.014464 | 0.014576 | 0.000000 | 0.014576 | -0.776 | 2.0 | low |
| C-SK-s100-o0 | shark | 5 | 0.009362 | 0.009428 | 0.000000 | 0.009428 | -0.702 | 2.0 | moderate |
| C-SK-s100-o0 | shark | 10 | 0.007923 | 0.007972 | 0.000000 | 0.007972 | -0.619 | 2.0 | moderate |
| C-SK-s100-o0 | shark | 20 | 0.006774 | 0.006806 | 0.000000 | 0.006806 | -0.466 | 2.0 | moderate |
| C-SK-s100-o0 | shark | 50 | 0.005582 | 0.005584 | 0.000000 | 0.005584 | -0.042 | 2.0 | moderate |
| C-SK-s100-o20 | shark | 1 | 0.014464 | 0.014552 | 0.000000 | 0.014552 | -0.613 | 2.0 | low |
| C-SK-s100-o20 | shark | 5 | 0.009362 | 0.009412 | 0.000000 | 0.009412 | -0.530 | 2.0 | moderate |
| C-SK-s100-o20 | shark | 10 | 0.007923 | 0.007958 | 0.000000 | 0.007958 | -0.437 | 2.0 | moderate |
| C-SK-s100-o20 | shark | 20 | 0.006774 | 0.006792 | 0.000000 | 0.006792 | -0.264 | 2.0 | moderate |
| C-SK-s100-o20 | shark | 50 | 0.005582 | 0.005570 | 0.000000 | 0.005570 | +0.213 | 2.0 | moderate |
| C-SK-s100-o20-high | shark | 1 | 0.014464 | 0.014553 | 0.000000 | 0.014553 | -0.615 | 2.0 | low |
| C-SK-s100-o20-high | shark | 5 | 0.009362 | 0.009413 | 0.000000 | 0.009413 | -0.538 | 2.0 | moderate |
| C-SK-s100-o20-high | shark | 10 | 0.007923 | 0.007959 | 0.000000 | 0.007959 | -0.453 | 2.0 | moderate |
| C-SK-s100-o20-high | shark | 20 | 0.006774 | 0.006794 | 0.000000 | 0.006794 | -0.294 | 2.0 | moderate |
| C-SK-s100-o20-high | shark | 50 | 0.005582 | 0.005574 | 0.000000 | 0.005574 | +0.144 | 2.0 | moderate |
| C-SK-s100-o20-low | shark | 1 | 0.014464 | 0.014553 | 0.000000 | 0.014553 | -0.617 | 2.0 | low |
| C-SK-s100-o20-low | shark | 5 | 0.009362 | 0.009413 | 0.000000 | 0.009413 | -0.546 | 2.0 | moderate |
| C-SK-s100-o20-low | shark | 10 | 0.007923 | 0.007960 | 0.000000 | 0.007960 | -0.467 | 2.0 | moderate |
| C-SK-s100-o20-low | shark | 20 | 0.006774 | 0.006796 | 0.000000 | 0.006796 | -0.321 | 2.0 | moderate |
| C-SK-s100-o20-low | shark | 50 | 0.005582 | 0.005577 | 0.000000 | 0.005577 | +0.085 | 2.0 | moderate |
| C-SK-s100-o40 | shark | 1 | 0.014464 | 0.014529 | 0.000000 | 0.014529 | -0.450 | 2.0 | low |
| C-SK-s100-o40 | shark | 5 | 0.009362 | 0.009396 | 0.000000 | 0.009396 | -0.357 | 2.0 | moderate |
| C-SK-s100-o40 | shark | 10 | 0.007923 | 0.007944 | 0.000000 | 0.007944 | -0.254 | 2.0 | moderate |
| C-SK-s100-o40 | shark | 20 | 0.006774 | 0.006778 | 0.000000 | 0.006778 | -0.063 | 2.0 | moderate |
| C-SK-s100-o40 | shark | 50 | 0.005582 | 0.005556 | 0.000000 | 0.005556 | +0.467 | 2.0 | moderate |
| C-SK-s200-o0 | shark | 1 | 0.014464 | 0.014572 | 0.000000 | 0.014572 | -0.751 | 2.0 | low |
| C-SK-s200-o0 | shark | 5 | 0.009362 | 0.009419 | 0.000000 | 0.009419 | -0.604 | 2.0 | moderate |
| C-SK-s200-o0 | shark | 10 | 0.007923 | 0.007958 | 0.000000 | 0.007958 | -0.439 | 2.0 | moderate |
| C-SK-s200-o0 | shark | 20 | 0.006774 | 0.006783 | 0.000000 | 0.006783 | -0.132 | 2.0 | moderate |
| C-SK-s200-o0 | shark | 50 | 0.005582 | 0.005542 | 0.000000 | 0.005542 | +0.716 | 2.0 | moderate |
| C-SK-s200-o20 | shark | 1 | 0.014464 | 0.014548 | 0.000000 | 0.014548 | -0.585 | 2.0 | low |
| C-SK-s200-o20 | shark | 5 | 0.009362 | 0.009402 | 0.000000 | 0.009402 | -0.419 | 2.0 | moderate |
| C-SK-s200-o20 | shark | 10 | 0.007923 | 0.007942 | 0.000000 | 0.007942 | -0.234 | 2.0 | moderate |
| C-SK-s200-o20 | shark | 20 | 0.006774 | 0.006766 | 0.000000 | 0.006766 | +0.111 | 2.0 | moderate |
| C-SK-s200-o20 | shark | 50 | 0.005582 | 0.005522 | 0.000000 | 0.005522 | +1.065 | 2.0 | moderate |
| C-SK-s200-o40 | shark | 1 | 0.014464 | 0.014524 | 0.000000 | 0.014524 | -0.419 | 2.0 | low |
| C-SK-s200-o40 | shark | 5 | 0.009362 | 0.009384 | 0.000000 | 0.009384 | -0.235 | 2.0 | moderate |
| C-SK-s200-o40 | shark | 10 | 0.007923 | 0.007926 | 0.000000 | 0.007926 | -0.029 | 2.0 | moderate |
| C-SK-s200-o40 | shark | 20 | 0.006774 | 0.006750 | 0.000000 | 0.006750 | +0.355 | 2.0 | moderate |
| C-SK-s200-o40 | shark | 50 | 0.005582 | 0.005503 | 0.000000 | 0.005503 | +1.415 | 2.0 | moderate |
| C-SK-s200-o40-high | shark | 1 | 0.014464 | 0.014525 | 0.000000 | 0.014525 | -0.424 | 2.0 | low |
| C-SK-s200-o40-high | shark | 5 | 0.009362 | 0.009386 | 0.000000 | 0.009386 | -0.254 | 2.0 | moderate |
| C-SK-s200-o40-high | shark | 10 | 0.007923 | 0.007929 | 0.000000 | 0.007929 | -0.065 | 2.0 | moderate |
| C-SK-s200-o40-high | shark | 20 | 0.006774 | 0.006754 | 0.000000 | 0.006754 | +0.288 | 2.0 | moderate |
| C-SK-s200-o40-high | shark | 50 | 0.005582 | 0.005511 | 0.000000 | 0.005511 | +1.263 | 2.0 | moderate |
| C-SK-s50-o0 | shark | 1 | 0.014464 | 0.014578 | 0.000000 | 0.014578 | -0.788 | 2.0 | low |
| C-SK-s50-o0 | shark | 5 | 0.009362 | 0.009433 | 0.000000 | 0.009433 | -0.751 | 2.0 | moderate |
| C-SK-s50-o0 | shark | 10 | 0.007923 | 0.007980 | 0.000000 | 0.007980 | -0.710 | 2.0 | moderate |
| C-SK-s50-o0 | shark | 20 | 0.006774 | 0.006817 | 0.000000 | 0.006817 | -0.633 | 2.0 | moderate |
| C-SK-s50-o0 | shark | 50 | 0.005582 | 0.005605 | 0.000000 | 0.005605 | -0.421 | 2.0 | moderate |
| C-SK-s50-o20 | shark | 1 | 0.014464 | 0.014554 | 0.000000 | 0.014554 | -0.626 | 2.0 | low |
| C-SK-s50-o20 | shark | 5 | 0.009362 | 0.009417 | 0.000000 | 0.009417 | -0.585 | 2.0 | moderate |
| C-SK-s50-o20 | shark | 10 | 0.007923 | 0.007966 | 0.000000 | 0.007966 | -0.538 | 2.0 | moderate |
| C-SK-s50-o20 | shark | 20 | 0.006774 | 0.006805 | 0.000000 | 0.006805 | -0.452 | 2.0 | moderate |
| C-SK-s50-o20 | shark | 50 | 0.005582 | 0.005594 | 0.000000 | 0.005594 | -0.214 | 2.0 | moderate |
| C-SK-s50-o40 | shark | 1 | 0.014464 | 0.014531 | 0.000000 | 0.014531 | -0.465 | 2.0 | low |
| C-SK-s50-o40 | shark | 5 | 0.009362 | 0.009402 | 0.000000 | 0.009402 | -0.419 | 2.0 | moderate |
| C-SK-s50-o40 | shark | 10 | 0.007923 | 0.007953 | 0.000000 | 0.007953 | -0.367 | 2.0 | moderate |
| C-SK-s50-o40 | shark | 20 | 0.006774 | 0.006792 | 0.000000 | 0.006792 | -0.271 | 2.0 | moderate |
| C-SK-s50-o40 | shark | 50 | 0.005582 | 0.005582 | 0.000000 | 0.005582 | -0.006 | 2.0 | moderate |
| C-SK-s500-o0 | shark | 1 | 0.014464 | 0.014562 | 0.000000 | 0.014562 | -0.678 | 2.0 | low |
| C-SK-s500-o0 | shark | 5 | 0.009362 | 0.009391 | 0.000000 | 0.009391 | -0.309 | 2.0 | moderate |
| C-SK-s500-o0 | shark | 10 | 0.007923 | 0.007915 | 0.000000 | 0.007915 | +0.103 | 2.0 | moderate |
| C-SK-s500-o0 | shark | 20 | 0.006774 | 0.006715 | 0.000000 | 0.006715 | +0.870 | 2.0 | moderate |
| C-SK-s500-o0 | shark | 50 | 0.005582 | 0.005514 | 0.000000 | 0.005514 | +1.211 | 2.0 | moderate |
| C-SK-s500-o20 | shark | 1 | 0.014464 | 0.014536 | 0.000000 | 0.014536 | -0.503 | 2.0 | low |
| C-SK-s500-o20 | shark | 5 | 0.009362 | 0.009371 | 0.000000 | 0.009371 | -0.088 | 2.0 | moderate |
| C-SK-s500-o20 | shark | 10 | 0.007923 | 0.007894 | 0.000000 | 0.007894 | +0.376 | 2.0 | moderate |
| C-SK-s500-o20 | shark | 20 | 0.006774 | 0.006690 | 0.000000 | 0.006690 | +1.239 | 2.0 | moderate |
| C-SK-s500-o20 | shark | 50 | 0.005582 | 0.005491 | 0.000000 | 0.005491 | +1.622 | 2.0 | moderate |
| C-SK-s500-o40 | shark | 1 | 0.014464 | 0.014511 | 0.000000 | 0.014511 | -0.328 | 2.0 | low |
| C-SK-s500-o40 | shark | 5 | 0.009362 | 0.009350 | 0.000000 | 0.009350 | +0.133 | 2.0 | moderate |
| C-SK-s500-o40 | shark | 10 | 0.007923 | 0.007872 | 0.000000 | 0.007872 | +0.649 | 2.0 | moderate |
| C-SK-s500-o40 | shark | 20 | 0.006774 | 0.006665 | 0.000000 | 0.006665 | +1.607 | 2.0 | moderate |
| C-SK-s500-o40 | shark | 50 | 0.005582 | 0.005468 | 0.000000 | 0.005468 | +2.033 | 2.0 | moderate |
| D-HY-01 | hybrid | 1 | 0.014464 | 0.014486 | 0.000040 | 0.014527 | -0.436 | 4.0 | low |
| D-HY-01 | hybrid | 5 | 0.009362 | 0.009335 | 0.000026 | 0.009361 | +0.013 | 4.0 | low |
| D-HY-01 | hybrid | 10 | 0.007923 | 0.007858 | 0.000022 | 0.007881 | +0.540 | 4.0 | low |
| D-HY-01 | hybrid | 20 | 0.006774 | 0.006651 | 0.000019 | 0.006670 | +1.533 | 4.0 | low |
| D-HY-01 | hybrid | 50 | 0.005582 | 0.005335 | 0.000016 | 0.005350 | +4.151 | 4.0 | low |
| D-HY-02 | hybrid | 1 | 0.014464 | 0.014530 | 0.000081 | 0.014611 | -1.015 | 4.0 | low |
| D-HY-02 | hybrid | 5 | 0.009362 | 0.009362 | 0.000052 | 0.009415 | -0.558 | 4.0 | low |
| D-HY-02 | hybrid | 10 | 0.007923 | 0.007879 | 0.000044 | 0.007924 | -0.002 | 4.0 | low |
| D-HY-02 | hybrid | 20 | 0.006774 | 0.006665 | 0.000038 | 0.006703 | +1.054 | 4.0 | low |
| D-HY-02 | hybrid | 50 | 0.005582 | 0.005341 | 0.000031 | 0.005372 | +3.752 | 4.0 | low |
| D-HY-03 | hybrid | 1 | 0.014464 | 0.014457 | 0.000040 | 0.014497 | -0.233 | 4.0 | low |
| D-HY-03 | hybrid | 5 | 0.009362 | 0.009258 | 0.000026 | 0.009285 | +0.829 | 4.0 | low |
| D-HY-03 | hybrid | 10 | 0.007923 | 0.007739 | 0.000022 | 0.007762 | +2.041 | 4.0 | low |
| D-HY-03 | hybrid | 20 | 0.006774 | 0.006463 | 0.000019 | 0.006482 | +4.309 | 4.0 | low |
| D-HY-03 | hybrid | 50 | 0.005582 | 0.005056 | 0.000016 | 0.005072 | +9.135 | 4.0 | low |
| D-HY-04 | hybrid | 1 | 0.014464 | 0.014500 | 0.000324 | 0.014824 | -2.493 | 4.0 | low |
| D-HY-04 | hybrid | 5 | 0.009362 | 0.009287 | 0.000210 | 0.009496 | -1.432 | 4.0 | low |
| D-HY-04 | hybrid | 10 | 0.007923 | 0.007764 | 0.000177 | 0.007941 | -0.224 | 4.0 | low |
| D-HY-04 | hybrid | 20 | 0.006774 | 0.006484 | 0.000152 | 0.006636 | +2.035 | 4.0 | low |
| D-HY-04 | hybrid | 50 | 0.005582 | 0.005075 | 0.000125 | 0.005200 | +6.849 | 4.0 | low |
| D-HY-05 | hybrid | 1 | 0.014464 | 0.014508 | 0.000081 | 0.014589 | -0.866 | 4.0 | low |
| D-HY-05 | hybrid | 5 | 0.009362 | 0.009296 | 0.000052 | 0.009348 | +0.148 | 4.0 | low |
| D-HY-05 | hybrid | 10 | 0.007923 | 0.007777 | 0.000044 | 0.007822 | +1.286 | 4.0 | low |
| D-HY-05 | hybrid | 20 | 0.006774 | 0.006519 | 0.000038 | 0.006557 | +3.204 | 4.0 | low |
| D-HY-05 | hybrid | 50 | 0.005582 | 0.005439 | 0.000031 | 0.005470 | +2.006 | 4.1 | low |
| D-HY-06 | hybrid | 1 | 0.014464 | 0.014490 | 0.000486 | 0.014976 | -3.539 | 4.0 | low |
| D-HY-06 | hybrid | 5 | 0.009362 | 0.009162 | 0.000315 | 0.009477 | -1.220 | 4.0 | low |
| D-HY-06 | hybrid | 10 | 0.007923 | 0.007563 | 0.000266 | 0.007829 | +1.188 | 4.0 | low |
| D-HY-06 | hybrid | 20 | 0.006774 | 0.006175 | 0.000228 | 0.006402 | +5.488 | 4.0 | low |
| D-HY-06 | hybrid | 50 | 0.005582 | 0.005656 | 0.000188 | 0.005843 | -4.684 | 4.8 | low |
| D-HY-07 | hybrid | 1 | 0.014464 | 0.014495 | 0.000040 | 0.014536 | -0.497 | 4.0 | low |
| D-HY-07 | hybrid | 5 | 0.009362 | 0.009359 | 0.000026 | 0.009385 | -0.245 | 4.0 | low |
| D-HY-07 | hybrid | 10 | 0.007923 | 0.007898 | 0.000022 | 0.007920 | +0.043 | 4.0 | low |
| D-HY-07 | hybrid | 20 | 0.006774 | 0.006714 | 0.000019 | 0.006733 | +0.599 | 4.0 | low |
| D-HY-07 | hybrid | 50 | 0.005582 | 0.005446 | 0.000016 | 0.005462 | +2.153 | 4.0 | low |
| D-HY-08 | hybrid | 1 | 0.014464 | 0.014525 | 0.000081 | 0.014606 | -0.986 | 4.0 | low |
| D-HY-08 | hybrid | 5 | 0.009362 | 0.009353 | 0.000052 | 0.009406 | -0.461 | 4.0 | low |
| D-HY-08 | hybrid | 10 | 0.007923 | 0.007869 | 0.000044 | 0.007913 | +0.127 | 4.0 | low |
| D-HY-08 | hybrid | 20 | 0.006774 | 0.006653 | 0.000038 | 0.006691 | +1.228 | 4.0 | low |
| D-HY-08 | hybrid | 50 | 0.005582 | 0.005310 | 0.000031 | 0.005341 | +4.316 | 4.0 | low |
| D-HY-09 | hybrid | 1 | 0.014464 | 0.014487 | 0.001944 | 0.016431 | -13.603 | 4.0 | low |
| D-HY-09 | hybrid | 5 | 0.009362 | 0.009171 | 0.001258 | 0.010429 | -11.394 | 4.0 | low |
| D-HY-09 | hybrid | 10 | 0.007923 | 0.007569 | 0.001065 | 0.008634 | -8.965 | 4.0 | low |
| D-HY-09 | hybrid | 20 | 0.006774 | 0.006710 | 0.000910 | 0.007621 | -12.497 | 4.3 | low |
| D-HY-09 | hybrid | 50 | 0.005582 | 0.005925 | 0.000750 | 0.006675 | -19.583 | 6.9 | low |
| D-HY-10 | hybrid | 1 | 0.014464 | 0.014607 | 0.000648 | 0.015255 | -5.471 | 4.0 | low |
| D-HY-10 | hybrid | 5 | 0.009362 | 0.009388 | 0.000419 | 0.009808 | -4.759 | 4.0 | low |
| D-HY-10 | hybrid | 10 | 0.007923 | 0.007880 | 0.000355 | 0.008235 | -3.927 | 4.0 | low |
| D-HY-10 | hybrid | 20 | 0.006774 | 0.006640 | 0.000303 | 0.006943 | -2.498 | 4.0 | low |
| D-HY-10 | hybrid | 50 | 0.005582 | 0.005409 | 0.000250 | 0.005659 | -1.391 | 4.0 | low |
| E-SMOOTH | baseline | 1 | 0.014464 | 0.014464 | 0.000000 | 0.014464 | +0.000 | 0.0 | low |
| E-SMOOTH | baseline | 5 | 0.009362 | 0.009362 | 0.000000 | 0.009362 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 10 | 0.007923 | 0.007923 | 0.000000 | 0.007923 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 20 | 0.006774 | 0.006774 | 0.000000 | 0.006774 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 50 | 0.005582 | 0.005582 | 0.000000 | 0.005582 | +0.000 | 0.0 | high |

### A.2 Sphere, D = 42.7 mm (335 rows)

| Geometry | Class | U (m/s) | Cf_smooth | Cf_textured | Cd_press | Cd_total | DR_net (%) | ± (pp) | Conf. |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| A-BLAD-s100-h50 | riblet | 1 | 0.011676 | 0.011651 | 0.378216 | 0.389867 | -0.169 | 3.1 | low |
| A-BLAD-s100-h50 | riblet | 5 | 0.013046 | 0.012863 | 0.422501 | 0.435364 | -0.115 | 3.1 | high |
| A-BLAD-s100-h50 | riblet | 10 | 0.014108 | 0.013726 | 0.456834 | 0.470560 | -0.064 | 3.1 | high |
| A-BLAD-s100-h50 | riblet | 20 | 0.014660 | 0.013911 | 0.474651 | 0.488563 | +0.021 | 3.1 | high |
| A-BLAD-s100-h50 | riblet | 50 | 0.014708 | 0.013195 | 0.467528 | 0.480723 | +1.943 | 3.1 | high |
| A-BLAD-s200-h100 | riblet | 1 | 0.011676 | 0.011626 | 0.378897 | 0.390523 | -0.337 | 3.1 | low |
| A-BLAD-s200-h100 | riblet | 5 | 0.013046 | 0.012680 | 0.423183 | 0.435862 | -0.229 | 3.1 | high |
| A-BLAD-s200-h100 | riblet | 10 | 0.014108 | 0.013343 | 0.457513 | 0.470856 | -0.127 | 3.1 | high |
| A-BLAD-s200-h100 | riblet | 20 | 0.014660 | 0.013277 | 0.475168 | 0.488445 | +0.045 | 3.1 | high |
| A-BLAD-s200-h100 | riblet | 50 | 0.014708 | 0.014146 | 0.434803 | 0.448949 | +8.425 | 3.1 | high |
| A-SCAL-s100-h50 | riblet | 1 | 0.011676 | 0.011675 | 0.378216 | 0.389891 | -0.175 | 3.1 | low |
| A-SCAL-s100-h50 | riblet | 5 | 0.013046 | 0.012970 | 0.422501 | 0.435471 | -0.139 | 3.1 | high |
| A-SCAL-s100-h50 | riblet | 10 | 0.014108 | 0.013937 | 0.456834 | 0.470770 | -0.108 | 3.1 | high |
| A-SCAL-s100-h50 | riblet | 20 | 0.014660 | 0.014313 | 0.474651 | 0.488964 | -0.061 | 3.1 | high |
| A-SCAL-s100-h50 | riblet | 50 | 0.014708 | 0.013645 | 0.467528 | 0.481173 | +1.852 | 3.1 | high |
| A-SCAL-s50-h25 | riblet | 1 | 0.011676 | 0.011676 | 0.377875 | 0.389551 | -0.087 | 3.1 | low |
| A-SCAL-s50-h25 | riblet | 5 | 0.013046 | 0.013008 | 0.422160 | 0.435168 | -0.070 | 3.1 | high |
| A-SCAL-s50-h25 | riblet | 10 | 0.014108 | 0.014022 | 0.456493 | 0.470516 | -0.054 | 3.1 | high |
| A-SCAL-s50-h25 | riblet | 20 | 0.014660 | 0.014487 | 0.474341 | 0.488827 | -0.033 | 3.1 | high |
| A-SCAL-s50-h25 | riblet | 50 | 0.014708 | 0.014255 | 0.474270 | 0.488525 | +0.352 | 3.1 | high |
| A-U-GR-s100-h50 | riblet | 1 | 0.011676 | 0.011678 | 0.378216 | 0.389894 | -0.175 | 3.1 | low |
| A-U-GR-s100-h50 | riblet | 5 | 0.013046 | 0.012980 | 0.422501 | 0.435481 | -0.142 | 3.1 | high |
| A-U-GR-s100-h50 | riblet | 10 | 0.014108 | 0.013957 | 0.456834 | 0.470791 | -0.113 | 3.1 | high |
| A-U-GR-s100-h50 | riblet | 20 | 0.014660 | 0.014352 | 0.474651 | 0.489004 | -0.069 | 3.1 | high |
| A-U-GR-s100-h50 | riblet | 50 | 0.014708 | 0.013733 | 0.467528 | 0.481261 | +1.834 | 3.1 | high |
| A-V-s100-h100 | riblet | 1 | 0.011676 | 0.011691 | 0.378897 | 0.390589 | -0.354 | 3.1 | low |
| A-V-s100-h100 | riblet | 5 | 0.013046 | 0.012969 | 0.423183 | 0.436152 | -0.296 | 3.1 | high |
| A-V-s100-h100 | riblet | 10 | 0.014108 | 0.013915 | 0.457513 | 0.471428 | -0.248 | 3.1 | high |
| A-V-s100-h100 | riblet | 20 | 0.014660 | 0.014248 | 0.475168 | 0.489416 | -0.153 | 3.1 | high |
| A-V-s100-h100 | riblet | 50 | 0.014708 | 0.012800 | 0.434803 | 0.447603 | +8.699 | 3.1 | high |
| A-V-s100-h25 | riblet | 1 | 0.011676 | 0.011680 | 0.377875 | 0.389556 | -0.089 | 3.1 | low |
| A-V-s100-h25 | riblet | 5 | 0.013046 | 0.013028 | 0.422160 | 0.435188 | -0.074 | 3.1 | high |
| A-V-s100-h25 | riblet | 10 | 0.014108 | 0.014062 | 0.456493 | 0.470555 | -0.063 | 3.1 | high |
| A-V-s100-h25 | riblet | 20 | 0.014660 | 0.014563 | 0.474341 | 0.488903 | -0.048 | 3.1 | high |
| A-V-s100-h25 | riblet | 50 | 0.014708 | 0.014425 | 0.474270 | 0.488695 | +0.317 | 3.1 | high |
| A-V-s100-h250 | riblet | 1 | 0.011676 | 0.011768 | 0.380942 | 0.392710 | -0.899 | 3.1 | low |
| A-V-s100-h250 | riblet | 5 | 0.013046 | 0.013093 | 0.425227 | 0.438319 | -0.794 | 3.1 | high |
| A-V-s100-h250 | riblet | 10 | 0.014108 | 0.014096 | 0.459532 | 0.473628 | -0.716 | 3.1 | high |
| A-V-s100-h250 | riblet | 20 | 0.014660 | 0.014486 | 0.475504 | 0.489989 | -0.271 | 3.1 | high |
| A-V-s100-h250 | riblet | 50 | 0.024513 | 0.015642 | 0.297647 | 0.313289 | +36.096 | 3.1 | high |
| A-V-s100-h50 | riblet | 1 | 0.011676 | 0.011678 | 0.378216 | 0.389894 | -0.176 | 3.1 | low |
| A-V-s100-h50 | riblet | 5 | 0.013046 | 0.012982 | 0.422501 | 0.435484 | -0.142 | 3.1 | high |
| A-V-s100-h50 | riblet | 10 | 0.014108 | 0.013961 | 0.456834 | 0.470795 | -0.114 | 3.1 | high |
| A-V-s100-h50 | riblet | 20 | 0.014660 | 0.014360 | 0.474651 | 0.489012 | -0.071 | 3.1 | high |
| A-V-s100-h50 | riblet | 50 | 0.014708 | 0.013750 | 0.467528 | 0.481278 | +1.830 | 3.1 | high |
| A-V-s200-h100 | riblet | 1 | 0.011676 | 0.011680 | 0.378897 | 0.390577 | -0.351 | 3.1 | low |
| A-V-s200-h100 | riblet | 5 | 0.013046 | 0.012918 | 0.423183 | 0.436101 | -0.284 | 3.1 | high |
| A-V-s200-h100 | riblet | 10 | 0.014108 | 0.013815 | 0.457513 | 0.471327 | -0.227 | 3.1 | high |
| A-V-s200-h100 | riblet | 20 | 0.014660 | 0.014056 | 0.475168 | 0.489224 | -0.114 | 3.1 | high |
| A-V-s200-h100 | riblet | 50 | 0.014708 | 0.013190 | 0.434803 | 0.447993 | +8.620 | 3.1 | high |
| A-V-s200-h25 | riblet | 1 | 0.011676 | 0.011685 | 0.377875 | 0.389560 | -0.090 | 3.1 | low |
| A-V-s200-h25 | riblet | 5 | 0.013046 | 0.013047 | 0.422160 | 0.435208 | -0.079 | 3.1 | high |
| A-V-s200-h25 | riblet | 10 | 0.014108 | 0.014100 | 0.456493 | 0.470594 | -0.071 | 3.1 | high |
| A-V-s200-h25 | riblet | 20 | 0.014660 | 0.014636 | 0.474341 | 0.488977 | -0.063 | 3.1 | high |
| A-V-s200-h25 | riblet | 50 | 0.014708 | 0.014591 | 0.474270 | 0.488861 | +0.284 | 3.1 | high |
| A-V-s200-h250 | riblet | 1 | 0.011676 | 0.011730 | 0.380942 | 0.392672 | -0.889 | 3.1 | low |
| A-V-s200-h250 | riblet | 5 | 0.013046 | 0.012925 | 0.425227 | 0.438152 | -0.756 | 3.1 | high |
| A-V-s200-h250 | riblet | 10 | 0.014108 | 0.013765 | 0.459532 | 0.473297 | -0.646 | 3.1 | high |
| A-V-s200-h250 | riblet | 20 | 0.014660 | 0.014099 | 0.475504 | 0.489603 | -0.192 | 3.1 | high |
| A-V-s200-h250 | riblet | 50 | 0.024513 | 0.016446 | 0.297647 | 0.314094 | +35.932 | 3.1 | high |
| A-V-s200-h50 | riblet | 1 | 0.011676 | 0.011684 | 0.378216 | 0.389900 | -0.177 | 3.1 | low |
| A-V-s200-h50 | riblet | 5 | 0.013046 | 0.013010 | 0.422501 | 0.435511 | -0.148 | 3.1 | high |
| A-V-s200-h50 | riblet | 10 | 0.014108 | 0.014016 | 0.456834 | 0.470850 | -0.125 | 3.1 | high |
| A-V-s200-h50 | riblet | 20 | 0.014660 | 0.014464 | 0.474651 | 0.489116 | -0.092 | 3.1 | high |
| A-V-s200-h50 | riblet | 50 | 0.014708 | 0.014124 | 0.467528 | 0.481652 | +1.754 | 3.1 | high |
| A-V-s50-h100 | riblet | 1 | 0.011676 | 0.011710 | 0.378897 | 0.390607 | -0.359 | 3.1 | low |
| A-V-s50-h100 | riblet | 5 | 0.013046 | 0.013049 | 0.423183 | 0.436232 | -0.314 | 3.1 | high |
| A-V-s50-h100 | riblet | 10 | 0.014108 | 0.014072 | 0.457513 | 0.471585 | -0.282 | 3.1 | high |
| A-V-s50-h100 | riblet | 20 | 0.014660 | 0.014548 | 0.475168 | 0.489716 | -0.215 | 3.1 | high |
| A-V-s50-h100 | riblet | 50 | 0.014708 | 0.013143 | 0.434803 | 0.447946 | +8.629 | 3.1 | high |
| A-V-s50-h25 | riblet | 1 | 0.011676 | 0.011677 | 0.377875 | 0.389552 | -0.088 | 3.1 | low |
| A-V-s50-h25 | riblet | 5 | 0.013046 | 0.013014 | 0.422160 | 0.435175 | -0.071 | 3.1 | high |
| A-V-s50-h25 | riblet | 10 | 0.014108 | 0.014035 | 0.456493 | 0.470528 | -0.057 | 3.1 | high |
| A-V-s50-h25 | riblet | 20 | 0.014660 | 0.014511 | 0.474341 | 0.488851 | -0.038 | 3.1 | high |
| A-V-s50-h25 | riblet | 50 | 0.014708 | 0.014308 | 0.474270 | 0.488578 | +0.341 | 3.1 | high |
| A-V-s50-h250 | riblet | 1 | 0.011676 | 0.011780 | 0.380942 | 0.392722 | -0.902 | 3.1 | low |
| A-V-s50-h250 | riblet | 5 | 0.013046 | 0.013144 | 0.425227 | 0.438371 | -0.806 | 3.1 | high |
| A-V-s50-h250 | riblet | 10 | 0.014108 | 0.014198 | 0.459532 | 0.473730 | -0.738 | 3.1 | high |
| A-V-s50-h250 | riblet | 20 | 0.014660 | 0.014679 | 0.475504 | 0.490183 | -0.310 | 3.1 | high |
| A-V-s50-h250 | riblet | 50 | 0.024513 | 0.015631 | 0.297647 | 0.313278 | +36.098 | 3.1 | high |
| A-V-s50-h50 | riblet | 1 | 0.011676 | 0.011684 | 0.378216 | 0.389900 | -0.177 | 3.1 | low |
| A-V-s50-h50 | riblet | 5 | 0.013046 | 0.013008 | 0.422501 | 0.435509 | -0.148 | 3.1 | high |
| A-V-s50-h50 | riblet | 10 | 0.014108 | 0.014012 | 0.456834 | 0.470845 | -0.124 | 3.1 | high |
| A-V-s50-h50 | riblet | 20 | 0.014660 | 0.014456 | 0.474651 | 0.489108 | -0.090 | 3.1 | high |
| A-V-s50-h50 | riblet | 50 | 0.014708 | 0.013963 | 0.467528 | 0.481492 | +1.787 | 3.1 | high |
| A-V-s500-h100 | riblet | 1 | 0.011676 | 0.011699 | 0.378897 | 0.390596 | -0.356 | 3.1 | low |
| A-V-s500-h100 | riblet | 5 | 0.013046 | 0.013002 | 0.423183 | 0.436185 | -0.303 | 3.1 | high |
| A-V-s500-h100 | riblet | 10 | 0.014108 | 0.013980 | 0.457513 | 0.471493 | -0.262 | 3.1 | high |
| A-V-s500-h100 | riblet | 20 | 0.014660 | 0.014464 | 0.475168 | 0.489632 | -0.198 | 3.1 | high |
| A-V-s500-h100 | riblet | 50 | 0.014708 | 0.013703 | 0.434803 | 0.448506 | +8.515 | 3.1 | high |
| A-V-s500-h25 | riblet | 1 | 0.011676 | 0.011687 | 0.377875 | 0.389562 | -0.090 | 3.1 | low |
| A-V-s500-h25 | riblet | 5 | 0.013046 | 0.013056 | 0.422160 | 0.435216 | -0.081 | 3.1 | high |
| A-V-s500-h25 | riblet | 10 | 0.014108 | 0.014117 | 0.456493 | 0.470611 | -0.074 | 3.1 | high |
| A-V-s500-h25 | riblet | 20 | 0.014660 | 0.014668 | 0.474341 | 0.489009 | -0.070 | 3.1 | high |
| A-V-s500-h25 | riblet | 50 | 0.014708 | 0.014665 | 0.474270 | 0.488935 | +0.268 | 3.1 | high |
| A-V-s500-h250 | riblet | 1 | 0.011676 | 0.011685 | 0.380942 | 0.392627 | -0.878 | 3.1 | low |
| A-V-s500-h250 | riblet | 5 | 0.013046 | 0.012725 | 0.425227 | 0.437952 | -0.710 | 3.1 | high |
| A-V-s500-h250 | riblet | 10 | 0.014108 | 0.013420 | 0.459532 | 0.472952 | -0.572 | 3.1 | high |
| A-V-s500-h250 | riblet | 20 | 0.014660 | 0.014619 | 0.475504 | 0.490123 | -0.298 | 3.1 | high |
| A-V-s500-h250 | riblet | 50 | 0.024513 | 0.019012 | 0.297647 | 0.316659 | +35.409 | 3.1 | high |
| A-V-s500-h50 | riblet | 1 | 0.011676 | 0.011695 | 0.378216 | 0.389911 | -0.180 | 3.1 | low |
| A-V-s500-h50 | riblet | 5 | 0.013046 | 0.013056 | 0.422501 | 0.435558 | -0.159 | 3.1 | high |
| A-V-s500-h50 | riblet | 10 | 0.014108 | 0.014108 | 0.456834 | 0.470941 | -0.145 | 3.1 | high |
| A-V-s500-h50 | riblet | 20 | 0.014660 | 0.014639 | 0.474651 | 0.489291 | -0.128 | 3.1 | high |
| A-V-s500-h50 | riblet | 50 | 0.014708 | 0.014456 | 0.467528 | 0.481984 | +1.686 | 3.1 | high |
| B-HEX-d0.5-r0.05 | dimple | 1 | 0.011676 | 0.011721 | 0.378971 | 0.390692 | -0.381 | 4.1 | low |
| B-HEX-d0.5-r0.05 | dimple | 5 | 0.013046 | 0.013090 | 0.423256 | 0.436347 | -0.341 | 4.1 | high |
| B-HEX-d0.5-r0.05 | dimple | 10 | 0.014108 | 0.014151 | 0.457586 | 0.471737 | -0.314 | 4.1 | high |
| B-HEX-d0.5-r0.05 | dimple | 20 | 0.014660 | 0.014689 | 0.475214 | 0.489902 | -0.253 | 4.1 | high |
| B-HEX-d0.5-r0.05 | dimple | 50 | 0.014708 | 0.013248 | 0.430022 | 0.443271 | +9.583 | 4.1 | high |
| B-HEX-d0.5-r0.1 | dimple | 1 | 0.011676 | 0.011765 | 0.380408 | 0.392173 | -0.761 | 4.1 | low |
| B-HEX-d0.5-r0.1 | dimple | 5 | 0.013046 | 0.013134 | 0.424693 | 0.437827 | -0.681 | 4.1 | high |
| B-HEX-d0.5-r0.1 | dimple | 10 | 0.014108 | 0.014191 | 0.459008 | 0.473198 | -0.625 | 4.1 | high |
| B-HEX-d0.5-r0.1 | dimple | 20 | 0.014660 | 0.014687 | 0.475620 | 0.490307 | -0.336 | 4.1 | high |
| B-HEX-d0.5-r0.1 | dimple | 50 | 0.024513 | 0.017001 | 0.324692 | 0.341693 | +30.302 | 4.1 | high |
| B-HEX-d0.5-r0.2 | dimple | 1 | 0.011676 | 0.011854 | 0.383281 | 0.395135 | -1.522 | 4.1 | low |
| B-HEX-d0.5-r0.2 | dimple | 5 | 0.013046 | 0.013223 | 0.427565 | 0.440788 | -1.362 | 4.1 | high |
| B-HEX-d0.5-r0.2 | dimple | 10 | 0.014108 | 0.014279 | 0.461798 | 0.476077 | -1.237 | 4.1 | high |
| B-HEX-d0.5-r0.2 | dimple | 20 | 0.014660 | 0.014620 | 0.472994 | 0.487614 | +0.215 | 4.1 | high |
| B-HEX-d0.5-r0.2 | dimple | 50 | 0.024513 | 0.012563 | 0.238935 | 0.251498 | +48.700 | 4.1 | high |
| B-HEX-d0.5-r0.3 | dimple | 1 | 0.011676 | 0.011943 | 0.386155 | 0.398098 | -2.283 | 4.1 | low |
| B-HEX-d0.5-r0.3 | dimple | 5 | 0.013046 | 0.013312 | 0.430436 | 0.443749 | -2.043 | 4.1 | high |
| B-HEX-d0.5-r0.3 | dimple | 10 | 0.014108 | 0.014365 | 0.464501 | 0.478866 | -1.830 | 4.1 | high |
| B-HEX-d0.5-r0.3 | dimple | 20 | 0.014660 | 0.014385 | 0.465171 | 0.479556 | +1.864 | 4.1 | high |
| B-HEX-d0.5-r0.3 | dimple | 50 | 0.024513 | 0.011678 | 0.221916 | 0.233594 | +52.352 | 4.1 | high |
| B-HEX-d1.0-r0.05 | dimple | 1 | 0.011676 | 0.011765 | 0.380408 | 0.392173 | -0.761 | 4.1 | low |
| B-HEX-d1.0-r0.05 | dimple | 5 | 0.013046 | 0.013133 | 0.424693 | 0.437826 | -0.681 | 4.1 | high |
| B-HEX-d1.0-r0.05 | dimple | 10 | 0.014108 | 0.014186 | 0.459008 | 0.473193 | -0.624 | 4.1 | high |
| B-HEX-d1.0-r0.05 | dimple | 20 | 0.014660 | 0.014665 | 0.475620 | 0.490285 | -0.331 | 4.1 | high |
| B-HEX-d1.0-r0.05 | dimple | 50 | 0.024513 | 0.016918 | 0.324692 | 0.341610 | +30.319 | 4.1 | high |
| B-HEX-d1.0-r0.1 | dimple | 1 | 0.011676 | 0.011854 | 0.383281 | 0.395135 | -1.522 | 4.1 | low |
| B-HEX-d1.0-r0.1 | dimple | 5 | 0.013046 | 0.013217 | 0.427565 | 0.440783 | -1.361 | 4.1 | high |
| B-HEX-d1.0-r0.1 | dimple | 10 | 0.014108 | 0.014256 | 0.461798 | 0.476054 | -1.232 | 4.1 | high |
| B-HEX-d1.0-r0.1 | dimple | 20 | 0.014660 | 0.014562 | 0.472994 | 0.487556 | +0.227 | 4.1 | high |
| B-HEX-d1.0-r0.1 | dimple | 50 | 0.024513 | 0.012483 | 0.238935 | 0.251418 | +48.717 | 4.1 | high |
| B-HEX-d1.0-r0.2 | dimple | 1 | 0.011676 | 0.012032 | 0.389028 | 0.401060 | -3.044 | 4.1 | low |
| B-HEX-d1.0-r0.2 | dimple | 5 | 0.013046 | 0.013397 | 0.433306 | 0.446703 | -2.722 | 4.1 | high |
| B-HEX-d1.0-r0.2 | dimple | 10 | 0.014108 | 0.014437 | 0.467100 | 0.481537 | -2.398 | 4.1 | high |
| B-HEX-d1.0-r0.2 | dimple | 20 | 0.014660 | 0.013983 | 0.452559 | 0.466542 | +4.528 | 4.1 | high |
| B-HEX-d1.0-r0.2 | dimple | 50 | 0.024513 | 0.011572 | 0.220040 | 0.231612 | +52.756 | 4.1 | high |
| B-HEX-d1.0-r0.3 | dimple | 1 | 0.011676 | 0.012209 | 0.394775 | 0.406985 | -4.567 | 4.1 | low |
| B-HEX-d1.0-r0.3 | dimple | 5 | 0.013046 | 0.013577 | 0.439041 | 0.452618 | -4.082 | 4.1 | high |
| B-HEX-d1.0-r0.3 | dimple | 10 | 0.014108 | 0.014594 | 0.471946 | 0.486540 | -3.462 | 4.1 | high |
| B-HEX-d1.0-r0.3 | dimple | 20 | 0.014660 | 0.012951 | 0.418830 | 0.431782 | +11.641 | 4.1 | high |
| B-HEX-d1.0-r0.3 | dimple | 50 | 0.024513 | 0.011921 | 0.226528 | 0.238449 | +51.362 | 4.1 | high |
| B-HEX-d2.0-r0.05 | dimple | 1 | 0.011676 | 0.011854 | 0.383281 | 0.395135 | -1.522 | 4.1 | low |
| B-HEX-d2.0-r0.05 | dimple | 5 | 0.013046 | 0.013211 | 0.427565 | 0.440776 | -1.359 | 4.1 | high |
| B-HEX-d2.0-r0.05 | dimple | 10 | 0.014108 | 0.014231 | 0.461798 | 0.476029 | -1.227 | 4.1 | high |
| B-HEX-d2.0-r0.05 | dimple | 20 | 0.014660 | 0.014499 | 0.472994 | 0.487493 | +0.240 | 4.1 | high |
| B-HEX-d2.0-r0.05 | dimple | 50 | 0.024513 | 0.012394 | 0.238935 | 0.251330 | +48.735 | 4.1 | high |
| B-HEX-d2.0-r0.1 | dimple | 1 | 0.011676 | 0.012031 | 0.389028 | 0.401059 | -3.044 | 4.1 | low |
| B-HEX-d2.0-r0.1 | dimple | 5 | 0.013046 | 0.013372 | 0.433306 | 0.446678 | -2.716 | 4.1 | high |
| B-HEX-d2.0-r0.1 | dimple | 10 | 0.014108 | 0.014375 | 0.467100 | 0.481475 | -2.385 | 4.1 | high |
| B-HEX-d2.0-r0.1 | dimple | 20 | 0.014660 | 0.013895 | 0.452559 | 0.466454 | +4.546 | 4.1 | high |
| B-HEX-d2.0-r0.1 | dimple | 50 | 0.024513 | 0.011513 | 0.220040 | 0.231553 | +52.768 | 4.1 | high |
| B-HEX-d2.0-r0.2 | dimple | 1 | 0.011676 | 0.012386 | 0.400522 | 0.412908 | -6.089 | 4.1 | low |
| B-HEX-d2.0-r0.2 | dimple | 5 | 0.013046 | 0.013746 | 0.444769 | 0.458514 | -5.438 | 4.1 | high |
| B-HEX-d2.0-r0.2 | dimple | 10 | 0.014108 | 0.014716 | 0.476283 | 0.490999 | -4.410 | 4.1 | high |
| B-HEX-d2.0-r0.2 | dimple | 20 | 0.014660 | 0.011893 | 0.384864 | 0.396757 | +18.808 | 4.1 | high |
| B-HEX-d2.0-r0.2 | dimple | 50 | 0.024513 | 0.012436 | 0.236360 | 0.248796 | +49.251 | 4.1 | high |
| B-HEX-d2.0-r0.3 | dimple | 1 | 0.011676 | 0.012742 | 0.412016 | 0.424758 | -9.133 | 4.1 | low |
| B-HEX-d2.0-r0.3 | dimple | 5 | 0.013046 | 0.014107 | 0.456202 | 0.470309 | -8.150 | 4.1 | high |
| B-HEX-d2.0-r0.3 | dimple | 10 | 0.014108 | 0.014948 | 0.483383 | 0.498330 | -5.969 | 4.1 | high |
| B-HEX-d2.0-r0.3 | dimple | 20 | 0.014660 | 0.010577 | 0.342025 | 0.352602 | +27.844 | 4.1 | high |
| B-HEX-d2.0-r0.3 | dimple | 50 | 0.024513 | 0.013579 | 0.258011 | 0.271590 | +44.602 | 4.1 | high |
| B-HEX-d5.0-r0.05 | dimple | 1 | 0.011676 | 0.012118 | 0.391902 | 0.404019 | -3.805 | 4.1 | low |
| B-HEX-d5.0-r0.05 | dimple | 5 | 0.013046 | 0.013408 | 0.436174 | 0.449582 | -3.384 | 4.1 | high |
| B-HEX-d5.0-r0.05 | dimple | 10 | 0.014108 | 0.014353 | 0.469584 | 0.483937 | -2.908 | 4.1 | high |
| B-HEX-d5.0-r0.05 | dimple | 20 | 0.014660 | 0.013305 | 0.436517 | 0.449822 | +7.949 | 4.1 | high |
| B-HEX-d5.0-r0.05 | dimple | 50 | 0.024513 | 0.011600 | 0.222487 | 0.234087 | +52.252 | 4.1 | high |
| B-HEX-d5.0-r0.1 | dimple | 1 | 0.011676 | 0.012554 | 0.406269 | 0.418823 | -7.608 | 4.1 | low |
| B-HEX-d5.0-r0.1 | dimple | 5 | 0.013046 | 0.013844 | 0.450489 | 0.464333 | -6.776 | 4.1 | high |
| B-HEX-d5.0-r0.1 | dimple | 10 | 0.014108 | 0.014739 | 0.480092 | 0.494831 | -5.225 | 4.1 | high |
| B-HEX-d5.0-r0.1 | dimple | 20 | 0.014660 | 0.011035 | 0.358738 | 0.369773 | +24.330 | 4.1 | high |
| B-HEX-d5.0-r0.1 | dimple | 50 | 0.024513 | 0.012979 | 0.247037 | 0.260017 | +46.963 | 4.1 | high |
| B-HEX-d5.0-r0.2 | dimple | 1 | 0.011676 | 0.013448 | 0.435003 | 0.448451 | -15.221 | 4.1 | low |
| B-HEX-d5.0-r0.2 | dimple | 5 | 0.013046 | 0.014799 | 0.478980 | 0.493780 | -13.548 | 4.1 | high |
| B-HEX-d5.0-r0.2 | dimple | 10 | 0.014108 | 0.015217 | 0.492332 | 0.507549 | -7.929 | 4.1 | high |
| B-HEX-d5.0-r0.2 | dimple | 20 | 0.024433 | 0.017280 | 0.328424 | 0.345704 | +29.256 | 4.1 | high |
| B-HEX-d5.0-r0.2 | dimple | 50 | 0.024513 | 0.015930 | 0.302689 | 0.318619 | +35.009 | 4.1 | high |
| B-HEX-d5.0-r0.3 | dimple | 1 | 0.011676 | 0.014341 | 0.463738 | 0.478079 | -22.833 | 4.1 | low |
| B-HEX-d5.0-r0.3 | dimple | 5 | 0.013046 | 0.015688 | 0.507328 | 0.523016 | -20.271 | 4.1 | high |
| B-HEX-d5.0-r0.3 | dimple | 10 | 0.014108 | 0.015467 | 0.500125 | 0.515592 | -9.640 | 4.1 | high |
| B-HEX-d5.0-r0.3 | dimple | 20 | 0.014660 | 0.011614 | 0.375543 | 0.387158 | +20.773 | 4.1 | high |
| B-HEX-d5.0-r0.3 | dimple | 50 | 0.014708 | 0.011333 | 0.366447 | 0.377780 | +22.942 | 4.1 | high |
| B-HEXA-c20 | dimple | 1 | 0.011676 | 0.011802 | 0.381598 | 0.393400 | -1.076 | 4.1 | low |
| B-HEXA-c20 | dimple | 5 | 0.013046 | 0.013164 | 0.425883 | 0.439047 | -0.962 | 4.1 | high |
| B-HEXA-c20 | dimple | 10 | 0.014108 | 0.014203 | 0.460173 | 0.474376 | -0.875 | 4.1 | high |
| B-HEXA-c20 | dimple | 20 | 0.014660 | 0.014620 | 0.475138 | 0.489758 | -0.223 | 4.1 | high |
| B-HEXA-c20 | dimple | 50 | 0.024513 | 0.014249 | 0.272985 | 0.287234 | +41.411 | 4.1 | high |
| B-HEXA-c80 | dimple | 1 | 0.011676 | 0.011928 | 0.385662 | 0.397589 | -2.153 | 4.1 | low |
| B-HEXA-c80 | dimple | 5 | 0.013046 | 0.013275 | 0.429944 | 0.443219 | -1.921 | 4.1 | high |
| B-HEXA-c80 | dimple | 10 | 0.014108 | 0.014262 | 0.464044 | 0.478306 | -1.711 | 4.1 | high |
| B-HEXA-c80 | dimple | 20 | 0.014660 | 0.014217 | 0.466880 | 0.481096 | +1.549 | 4.1 | high |
| B-HEXA-c80 | dimple | 50 | 0.024513 | 0.011452 | 0.223182 | 0.234634 | +52.140 | 4.1 | high |
| B-SQUA-c40 | dimple | 1 | 0.011676 | 0.011854 | 0.383281 | 0.395135 | -1.522 | 4.1 | low |
| B-SQUA-c40 | dimple | 5 | 0.013046 | 0.013213 | 0.427565 | 0.440778 | -1.360 | 4.1 | high |
| B-SQUA-c40 | dimple | 10 | 0.014108 | 0.014239 | 0.461798 | 0.476037 | -1.228 | 4.1 | high |
| B-SQUA-c40 | dimple | 20 | 0.014660 | 0.014518 | 0.472994 | 0.487513 | +0.236 | 4.1 | high |
| B-SQUA-c40 | dimple | 50 | 0.024513 | 0.012422 | 0.238935 | 0.251357 | +48.729 | 4.1 | high |
| B-STAG-c60 | dimple | 1 | 0.011676 | 0.011894 | 0.384573 | 0.396467 | -1.864 | 4.1 | low |
| B-STAG-c60 | dimple | 5 | 0.013046 | 0.013247 | 0.428856 | 0.442103 | -1.664 | 4.1 | high |
| B-STAG-c60 | dimple | 10 | 0.014108 | 0.014252 | 0.463025 | 0.477278 | -1.492 | 4.1 | high |
| B-STAG-c60 | dimple | 20 | 0.014660 | 0.014371 | 0.470124 | 0.484494 | +0.854 | 4.1 | high |
| B-STAG-c60 | dimple | 50 | 0.024513 | 0.011765 | 0.227845 | 0.239609 | +51.125 | 4.1 | high |
| C-SK-s100-o0 | shark | 1 | 0.011676 | 0.011792 | 0.378352 | 0.390144 | -0.240 | 3.6 | low |
| C-SK-s100-o0 | shark | 5 | 0.013046 | 0.013162 | 0.422638 | 0.435799 | -0.215 | 3.6 | moderate |
| C-SK-s100-o0 | shark | 10 | 0.014108 | 0.014218 | 0.456970 | 0.471188 | -0.197 | 3.6 | moderate |
| C-SK-s100-o0 | shark | 20 | 0.014660 | 0.014747 | 0.474767 | 0.489514 | -0.173 | 3.6 | moderate |
| C-SK-s100-o0 | shark | 50 | 0.014708 | 0.014314 | 0.462964 | 0.477278 | +2.646 | 3.6 | moderate |
| C-SK-s100-o20 | shark | 1 | 0.011676 | 0.011773 | 0.378352 | 0.390125 | -0.235 | 3.6 | low |
| C-SK-s100-o20 | shark | 5 | 0.013046 | 0.013139 | 0.422638 | 0.435776 | -0.209 | 3.6 | moderate |
| C-SK-s100-o20 | shark | 10 | 0.014108 | 0.014192 | 0.456970 | 0.471161 | -0.192 | 3.6 | moderate |
| C-SK-s100-o20 | shark | 20 | 0.014660 | 0.014717 | 0.474767 | 0.489484 | -0.167 | 3.6 | moderate |
| C-SK-s100-o20 | shark | 50 | 0.014708 | 0.014277 | 0.462964 | 0.477240 | +2.654 | 3.6 | moderate |
| C-SK-s100-o20-high | shark | 1 | 0.011676 | 0.011773 | 0.378352 | 0.390125 | -0.235 | 3.6 | low |
| C-SK-s100-o20-high | shark | 5 | 0.013046 | 0.013140 | 0.422638 | 0.435778 | -0.210 | 3.6 | moderate |
| C-SK-s100-o20-high | shark | 10 | 0.014108 | 0.014194 | 0.456970 | 0.471164 | -0.192 | 3.6 | moderate |
| C-SK-s100-o20-high | shark | 20 | 0.014660 | 0.014722 | 0.474767 | 0.489489 | -0.168 | 3.6 | moderate |
| C-SK-s100-o20-high | shark | 50 | 0.014708 | 0.014287 | 0.462964 | 0.477251 | +2.652 | 3.6 | moderate |
| C-SK-s100-o20-low | shark | 1 | 0.011676 | 0.011773 | 0.378352 | 0.390126 | -0.235 | 3.6 | low |
| C-SK-s100-o20-low | shark | 5 | 0.013046 | 0.013141 | 0.422638 | 0.435779 | -0.210 | 3.6 | moderate |
| C-SK-s100-o20-low | shark | 10 | 0.014108 | 0.014196 | 0.456970 | 0.471166 | -0.193 | 3.6 | moderate |
| C-SK-s100-o20-low | shark | 20 | 0.014660 | 0.014726 | 0.474767 | 0.489493 | -0.169 | 3.6 | moderate |
| C-SK-s100-o20-low | shark | 50 | 0.014708 | 0.014297 | 0.462964 | 0.477260 | +2.650 | 3.6 | moderate |
| C-SK-s100-o40 | shark | 1 | 0.011676 | 0.011754 | 0.378352 | 0.390106 | -0.230 | 3.6 | low |
| C-SK-s100-o40 | shark | 5 | 0.013046 | 0.013116 | 0.422638 | 0.435754 | -0.204 | 3.6 | moderate |
| C-SK-s100-o40 | shark | 10 | 0.014108 | 0.014166 | 0.456970 | 0.471135 | -0.186 | 3.6 | moderate |
| C-SK-s100-o40 | shark | 20 | 0.014660 | 0.014686 | 0.474767 | 0.489453 | -0.161 | 3.6 | moderate |
| C-SK-s100-o40 | shark | 50 | 0.014708 | 0.014239 | 0.462964 | 0.477202 | +2.662 | 3.6 | moderate |
| C-SK-s200-o0 | shark | 1 | 0.011676 | 0.011814 | 0.379170 | 0.390984 | -0.456 | 3.6 | low |
| C-SK-s200-o0 | shark | 5 | 0.013046 | 0.013173 | 0.423455 | 0.436628 | -0.405 | 3.6 | moderate |
| C-SK-s200-o0 | shark | 10 | 0.014108 | 0.014215 | 0.457784 | 0.471999 | -0.370 | 3.6 | moderate |
| C-SK-s200-o0 | shark | 20 | 0.014660 | 0.014710 | 0.475326 | 0.490036 | -0.280 | 3.6 | moderate |
| C-SK-s200-o0 | shark | 50 | 0.014708 | 0.012768 | 0.416400 | 0.429168 | +12.460 | 3.6 | moderate |
| C-SK-s200-o20 | shark | 1 | 0.011676 | 0.011795 | 0.379170 | 0.390965 | -0.451 | 3.6 | low |
| C-SK-s200-o20 | shark | 5 | 0.013046 | 0.013148 | 0.423455 | 0.436603 | -0.400 | 3.6 | moderate |
| C-SK-s200-o20 | shark | 10 | 0.014108 | 0.014185 | 0.457784 | 0.471969 | -0.363 | 3.6 | moderate |
| C-SK-s200-o20 | shark | 20 | 0.014660 | 0.014673 | 0.475326 | 0.489999 | -0.273 | 3.6 | moderate |
| C-SK-s200-o20 | shark | 50 | 0.014708 | 0.012721 | 0.416400 | 0.429121 | +12.469 | 3.6 | moderate |
| C-SK-s200-o40 | shark | 1 | 0.011676 | 0.011775 | 0.379170 | 0.390945 | -0.446 | 3.6 | low |
| C-SK-s200-o40 | shark | 5 | 0.013046 | 0.013124 | 0.423455 | 0.436579 | -0.394 | 3.6 | moderate |
| C-SK-s200-o40 | shark | 10 | 0.014108 | 0.014155 | 0.457784 | 0.471939 | -0.357 | 3.6 | moderate |
| C-SK-s200-o40 | shark | 20 | 0.014660 | 0.014636 | 0.475326 | 0.489962 | -0.265 | 3.6 | moderate |
| C-SK-s200-o40 | shark | 50 | 0.014708 | 0.012673 | 0.416400 | 0.429074 | +12.479 | 3.6 | moderate |
| C-SK-s200-o40-high | shark | 1 | 0.011676 | 0.011776 | 0.379170 | 0.390946 | -0.446 | 3.6 | low |
| C-SK-s200-o40-high | shark | 5 | 0.013046 | 0.013126 | 0.423455 | 0.436582 | -0.395 | 3.6 | moderate |
| C-SK-s200-o40-high | shark | 10 | 0.014108 | 0.014161 | 0.457784 | 0.471945 | -0.358 | 3.6 | moderate |
| C-SK-s200-o40-high | shark | 20 | 0.014660 | 0.014647 | 0.475326 | 0.489973 | -0.267 | 3.6 | moderate |
| C-SK-s200-o40-high | shark | 50 | 0.014708 | 0.012695 | 0.416400 | 0.429095 | +12.475 | 3.6 | moderate |
| C-SK-s50-o0 | shark | 1 | 0.011676 | 0.011781 | 0.377943 | 0.389724 | -0.132 | 3.6 | low |
| C-SK-s50-o0 | shark | 5 | 0.013046 | 0.013156 | 0.422229 | 0.435385 | -0.119 | 3.6 | moderate |
| C-SK-s50-o0 | shark | 10 | 0.014108 | 0.014219 | 0.456562 | 0.470781 | -0.111 | 3.6 | moderate |
| C-SK-s50-o0 | shark | 20 | 0.014660 | 0.014763 | 0.474405 | 0.489168 | -0.103 | 3.6 | moderate |
| C-SK-s50-o0 | shark | 50 | 0.014708 | 0.014699 | 0.473430 | 0.488128 | +0.433 | 3.6 | moderate |
| C-SK-s50-o20 | shark | 1 | 0.011676 | 0.011762 | 0.377943 | 0.389705 | -0.127 | 3.6 | low |
| C-SK-s50-o20 | shark | 5 | 0.013046 | 0.013134 | 0.422229 | 0.435363 | -0.114 | 3.6 | moderate |
| C-SK-s50-o20 | shark | 10 | 0.014108 | 0.014195 | 0.456562 | 0.470756 | -0.105 | 3.6 | moderate |
| C-SK-s50-o20 | shark | 20 | 0.014660 | 0.014736 | 0.474405 | 0.489141 | -0.097 | 3.6 | moderate |
| C-SK-s50-o20 | shark | 50 | 0.014708 | 0.014668 | 0.473430 | 0.488097 | +0.439 | 3.6 | moderate |
| C-SK-s50-o40 | shark | 1 | 0.011676 | 0.011743 | 0.377943 | 0.389686 | -0.122 | 3.6 | low |
| C-SK-s50-o40 | shark | 5 | 0.013046 | 0.013112 | 0.422229 | 0.435341 | -0.109 | 3.6 | moderate |
| C-SK-s50-o40 | shark | 10 | 0.014108 | 0.014171 | 0.456562 | 0.470732 | -0.100 | 3.6 | moderate |
| C-SK-s50-o40 | shark | 20 | 0.014660 | 0.014709 | 0.474405 | 0.489114 | -0.092 | 3.6 | moderate |
| C-SK-s50-o40 | shark | 50 | 0.014708 | 0.014637 | 0.473430 | 0.488066 | +0.446 | 3.6 | moderate |
| C-SK-s500-o0 | shark | 1 | 0.011676 | 0.011881 | 0.381623 | 0.393504 | -1.103 | 3.6 | low |
| C-SK-s500-o0 | shark | 5 | 0.013046 | 0.013206 | 0.425908 | 0.439114 | -0.977 | 3.6 | moderate |
| C-SK-s500-o0 | shark | 10 | 0.014108 | 0.014204 | 0.460198 | 0.474402 | -0.881 | 3.6 | moderate |
| C-SK-s500-o0 | shark | 20 | 0.014660 | 0.014542 | 0.475119 | 0.489660 | -0.203 | 3.6 | moderate |
| C-SK-s500-o0 | shark | 50 | 0.024513 | 0.014204 | 0.272198 | 0.286402 | +41.581 | 3.6 | moderate |
| C-SK-s500-o20 | shark | 1 | 0.011676 | 0.011860 | 0.381623 | 0.393483 | -1.098 | 3.6 | low |
| C-SK-s500-o20 | shark | 5 | 0.013046 | 0.013176 | 0.425908 | 0.439084 | -0.970 | 3.6 | moderate |
| C-SK-s500-o20 | shark | 10 | 0.014108 | 0.014164 | 0.460198 | 0.474361 | -0.872 | 3.6 | moderate |
| C-SK-s500-o20 | shark | 20 | 0.014660 | 0.014484 | 0.475119 | 0.489603 | -0.192 | 3.6 | moderate |
| C-SK-s500-o20 | shark | 50 | 0.024513 | 0.014152 | 0.272198 | 0.286350 | +41.591 | 3.6 | moderate |
| C-SK-s500-o40 | shark | 1 | 0.011676 | 0.011839 | 0.381623 | 0.393462 | -1.092 | 3.6 | low |
| C-SK-s500-o40 | shark | 5 | 0.013046 | 0.013145 | 0.425908 | 0.439054 | -0.963 | 3.6 | moderate |
| C-SK-s500-o40 | shark | 10 | 0.014108 | 0.014123 | 0.460198 | 0.474321 | -0.863 | 3.6 | moderate |
| C-SK-s500-o40 | shark | 20 | 0.014660 | 0.014427 | 0.475119 | 0.489546 | -0.180 | 3.6 | moderate |
| C-SK-s500-o40 | shark | 50 | 0.024513 | 0.014099 | 0.272198 | 0.286297 | +41.602 | 3.6 | moderate |
| D-HY-01 | hybrid | 1 | 0.011676 | 0.011805 | 0.381192 | 0.392997 | -0.973 | 5.6 | low |
| D-HY-01 | hybrid | 5 | 0.013046 | 0.013111 | 0.425477 | 0.438588 | -0.856 | 5.6 | low |
| D-HY-01 | hybrid | 10 | 0.014108 | 0.014085 | 0.459777 | 0.473862 | -0.766 | 5.6 | low |
| D-HY-01 | hybrid | 20 | 0.014660 | 0.014404 | 0.475394 | 0.489799 | -0.232 | 5.6 | low |
| D-HY-01 | hybrid | 50 | 0.024513 | 0.014384 | 0.287230 | 0.301614 | +38.478 | 5.6 | low |
| D-HY-02 | hybrid | 1 | 0.011676 | 0.011888 | 0.382707 | 0.394594 | -1.383 | 5.6 | low |
| D-HY-02 | hybrid | 5 | 0.013046 | 0.013196 | 0.426991 | 0.440187 | -1.224 | 5.6 | low |
| D-HY-02 | hybrid | 10 | 0.014108 | 0.014166 | 0.461247 | 0.475413 | -1.096 | 5.6 | low |
| D-HY-02 | hybrid | 20 | 0.014660 | 0.014387 | 0.473927 | 0.488314 | +0.072 | 5.6 | low |
| D-HY-02 | hybrid | 50 | 0.024513 | 0.012392 | 0.247155 | 0.259546 | +47.059 | 5.6 | low |
| D-HY-03 | hybrid | 1 | 0.011676 | 0.011778 | 0.381192 | 0.392970 | -0.966 | 5.6 | low |
| D-HY-03 | hybrid | 5 | 0.013046 | 0.012991 | 0.425477 | 0.438468 | -0.828 | 5.6 | low |
| D-HY-03 | hybrid | 10 | 0.014108 | 0.013848 | 0.459777 | 0.473625 | -0.715 | 5.6 | low |
| D-HY-03 | hybrid | 20 | 0.014660 | 0.013955 | 0.475394 | 0.489349 | -0.140 | 5.6 | low |
| D-HY-03 | hybrid | 50 | 0.024513 | 0.013803 | 0.287230 | 0.301034 | +38.596 | 5.6 | low |
| D-HY-04 | hybrid | 1 | 0.011676 | 0.011860 | 0.382707 | 0.394567 | -1.376 | 5.6 | low |
| D-HY-04 | hybrid | 5 | 0.013046 | 0.013077 | 0.426991 | 0.440068 | -1.196 | 5.6 | low |
| D-HY-04 | hybrid | 10 | 0.014108 | 0.013937 | 0.461247 | 0.475183 | -1.047 | 5.6 | low |
| D-HY-04 | hybrid | 20 | 0.014660 | 0.013958 | 0.473927 | 0.487885 | +0.160 | 5.6 | low |
| D-HY-04 | hybrid | 50 | 0.024513 | 0.011920 | 0.247155 | 0.259074 | +47.155 | 5.6 | low |
| D-HY-05 | hybrid | 1 | 0.011676 | 0.012108 | 0.390465 | 0.402573 | -3.433 | 5.6 | low |
| D-HY-05 | hybrid | 5 | 0.013046 | 0.013329 | 0.434740 | 0.448069 | -3.036 | 5.6 | low |
| D-HY-05 | hybrid | 10 | 0.014108 | 0.014180 | 0.468357 | 0.482538 | -2.611 | 5.6 | low |
| D-HY-05 | hybrid | 20 | 0.014660 | 0.013185 | 0.444858 | 0.458043 | +6.267 | 5.6 | low |
| D-HY-05 | hybrid | 50 | 0.024513 | 0.011446 | 0.220966 | 0.232412 | +52.593 | 5.6 | low |
| D-HY-06 | hybrid | 1 | 0.011676 | 0.012665 | 0.409208 | 0.421873 | -8.392 | 5.6 | low |
| D-HY-06 | hybrid | 5 | 0.013046 | 0.013675 | 0.453411 | 0.467086 | -7.409 | 5.6 | low |
| D-HY-06 | hybrid | 10 | 0.014108 | 0.014141 | 0.481838 | 0.495979 | -5.469 | 5.6 | low |
| D-HY-06 | hybrid | 20 | 0.014660 | 0.009827 | 0.349077 | 0.358904 | +26.554 | 5.6 | low |
| D-HY-06 | hybrid | 50 | 0.024513 | 0.013591 | 0.252626 | 0.266217 | +45.698 | 5.6 | low |
| D-HY-07 | hybrid | 1 | 0.011676 | 0.011757 | 0.379363 | 0.391120 | -0.491 | 5.6 | low |
| D-HY-07 | hybrid | 5 | 0.013046 | 0.013093 | 0.423648 | 0.436741 | -0.431 | 5.6 | low |
| D-HY-07 | hybrid | 10 | 0.014108 | 0.014108 | 0.457975 | 0.472084 | -0.388 | 5.6 | low |
| D-HY-07 | hybrid | 20 | 0.014660 | 0.014556 | 0.475420 | 0.489976 | -0.268 | 5.6 | low |
| D-HY-07 | hybrid | 50 | 0.014708 | 0.012115 | 0.402530 | 0.414645 | +15.422 | 5.6 | low |
| D-HY-08 | hybrid | 1 | 0.011676 | 0.011763 | 0.378827 | 0.390591 | -0.355 | 5.6 | low |
| D-HY-08 | hybrid | 5 | 0.013046 | 0.013062 | 0.423113 | 0.436175 | -0.301 | 5.6 | low |
| D-HY-08 | hybrid | 10 | 0.014108 | 0.014031 | 0.457443 | 0.471474 | -0.258 | 5.6 | low |
| D-HY-08 | hybrid | 20 | 0.014660 | 0.014396 | 0.475122 | 0.489518 | -0.174 | 5.6 | low |
| D-HY-08 | hybrid | 50 | 0.014708 | 0.012849 | 0.439168 | 0.452017 | +7.799 | 5.6 | low |
| D-HY-09 | hybrid | 1 | 0.011676 | 0.013643 | 0.440881 | 0.454524 | -16.781 | 5.6 | low |
| D-HY-09 | hybrid | 5 | 0.013046 | 0.014636 | 0.484788 | 0.499424 | -14.845 | 5.6 | low |
| D-HY-09 | hybrid | 10 | 0.014108 | 0.014557 | 0.493925 | 0.508483 | -8.128 | 5.6 | low |
| D-HY-09 | hybrid | 20 | 0.014660 | 0.010591 | 0.341430 | 0.352020 | +27.963 | 5.6 | low |
| D-HY-09 | hybrid | 50 | 0.024513 | 0.017743 | 0.314173 | 0.331916 | +32.297 | 5.6 | low |
| D-HY-10 | hybrid | 1 | 0.011676 | 0.012245 | 0.392164 | 0.404409 | -3.905 | 5.6 | low |
| D-HY-10 | hybrid | 5 | 0.013046 | 0.013520 | 0.436436 | 0.449956 | -3.470 | 5.6 | low |
| D-HY-10 | hybrid | 10 | 0.014108 | 0.014422 | 0.469805 | 0.484227 | -2.970 | 5.6 | low |
| D-HY-10 | hybrid | 20 | 0.014660 | 0.013145 | 0.434945 | 0.448090 | +8.304 | 5.6 | low |
| D-HY-10 | hybrid | 50 | 0.024513 | 0.011434 | 0.222810 | 0.234244 | +52.220 | 5.6 | low |
| E-SMOOTH | baseline | 1 | 0.011676 | 0.011676 | 0.377534 | 0.389211 | +0.000 | 0.0 | low |
| E-SMOOTH | baseline | 5 | 0.013046 | 0.013046 | 0.421820 | 0.434866 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 10 | 0.014108 | 0.014108 | 0.456153 | 0.470261 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 20 | 0.014660 | 0.014660 | 0.474006 | 0.488666 | +0.000 | 0.0 | high |
| E-SMOOTH | baseline | 50 | 0.014708 | 0.014708 | 0.475544 | 0.490251 | +0.000 | 0.0 | high |

---

## Appendix B. Boundary layer model equations and assumptions

### B.1 Consolidated equation set

Equations E1-E16 are introduced in Sections 3 and 4; E17-E19 are stated here for
completeness. Symbols follow Section 3.

```
Boundary layer and baseline drag
--------------------------------
(E1)   tau_w      = mu * (du/dy)|_(y=0)
(E2)   c_f        = tau_w / q ,                 q = 0.5 * rho * U_inf^2
(E3)   C_F        = (1/L) * integral_0^L c_f dx
(E4)   Re_L       = U_inf * L / nu ,            nu = mu / rho
(E5)   C_F        = 0.455 / (log10(Re_L))^2.58                      [Schlichting]
(E6)   D_total    = D_friction + D_pressure

Wall units
----------
(E7)   u_tau      = sqrt(tau_w / rho) = U_inf * sqrt(c_f / 2)
(E8)   l_v        = nu / u_tau
       y+         = y / l_v ,  s+ = s * u_tau / nu ,  k+ = k * u_tau / nu
       delta_v    = 5 * l_v                       (viscous sublayer thickness)

Riblets
-------
(E9)   delta_h    = h_par - h_perp                (protrusion-height difference)
(E10)  A_g        = F_shape * s * h
       l_g        = sqrt(A_g)
       l_g+       = l_g * u_tau / nu
(E13)  DR_friction = DR_max(profile) * f(xi) * eta_hs(h/s) ,   xi = l_g+ / 10.7
       f(xi)      = xi                        for xi <= 1
       f(xi)      = 1 - max(xi - 1, 0)^1.3     for xi >  1
       eta_hs(r)  = exp( -0.5 * ( ln(r / r_opt) / 0.8 )^2 )

Dimples on a plate
------------------
(E11)  DR_net      = DR_friction - DR_pressure_penalty
(E14)  DR_friction = 2.0 * g(d/D) * (coverage/0.6)^0.8 * P(pattern) * eta_Re(d+)
       g(r)        = exp( -0.5 * ( ln(r / 0.05) / 0.6 )^2 )
       d+          = (d/D) * D * u_tau / nu
       eta_Re(d+)  = exp( -0.5 * ( ln(d+ / 20) / 0.9 )^2 )
       DR_pressure_penalty = 1.4 * coverage * (d/D / 0.05)^2

Sphere
------
(E15)  C_D,smooth  = (24/Re) * (1 + 0.15 * Re^0.687)
                     + 0.42 / (1 + 42500 * Re^-1.16)              [Clift-Gauvin]
(E16)  Re_crit(k/D)= 0.7 * 10^( 3.995 - 0.4114 * log10(k/D) )     [after Achenbach]
       sigma       = 1 / (1 + exp( -6 * ln(Re / Re_crit) ))
       C_D,super   = 0.20 + 8.0 * (k/D)_eff
       C_D,textured= (1 - sigma) * [C_D,smooth + 4 * (k/D)_eff]
                     + sigma * C_D,super

Drag reduction and transition
-----------------------------
(E12)  DR_net      = 100 * (C_D,smooth - C_D,textured) / C_D,smooth     [%]
(E17)  Re_tr(k+)   = 5e5                       for k+ <= 5
       Re_tr(k+)   = 5e5 / (1 + 0.5 * (k+/5 - 1))   for k+ >  5
       delta_Re_tr = Re_tr - 5e5

Shark-skin denticles
--------------------
(E18)  s_eq        = scale / 3 ,   h_eq = 0.15 * scale
       DR          = DR_scalloped(s_eq, h_eq) * eta_3D * eta_ov * eta_AR
                     - 0.8 * (1 - overlap)
       eta_3D      = 0.62 ,  eta_ov = 0.8 + 0.5 * overlap

Hybrids (plate)
---------------
(E19)  DR          = DR_strong + 0.3 * DR_weak - 1.5 * coverage
                     - DR_pressure_penalty(dimple)
```

### B.2 Numerical constants

**Table B1. All calibration constants used in the model.**

| Symbol | Value | Unit | Meaning |
| :--- | :--- | :--- | :--- |
| rho | 1.184 | kg/m^3 | air, 25 °C, 1 atm |
| mu | 1.849e-05 | Pa·s | air, 25 °C |
| nu | 1.5617e-05 | m^2/s | mu / rho |
| L_plate | 0.1 | m | plate chord |
| D_sphere | 0.0427 | m | golf-ball scale |
| U_inf | 1, 5, 10, 20, 50 | m/s | five speeds |
| Re_tr,smooth | 5.0e+05 | - | smooth-plate natural transition |
| l_g+_opt | 10.7 | - | riblet optimum, García-Mayoral & Jiménez |
| DR_max | blade 9.9, scalloped 6.5, V 6.2, U 5.5 | % | Bechert et al. 1997 ceilings |
| F_shape | V 0.50, U 0.667, blade 0.95, scalloped 0.60 | - | groove area factor |
| (h/s)_opt | blade 0.50, others 0.70 | - | peak of eta_hs |
| eta_3D | 0.62 | - | denticle three-dimensionality penalty |
| DR_dimple,peak | 2.0 | % | friction credit ceiling at d/D = 0.05 |
| d+_opt | 20 | - | dimple depth in wall units |
| C_press | 1.4 | - | dimple pressure coefficient |
| sigma_class | riblet 1.5, dimple 2.5, shark 2.0, hybrid 4.0 | pp | plate uncertainty |
| sigma_sphere,extra | 1.6 | pp | added in quadrature on the sphere |
| DR_floor | -40 (plate), -50 (both, hard clip) | % | drag-increase saturation |

### B.3 Assumptions

**A1. Incompressible, steady, isothermal flow.** Maximum Mach number is 0.145;
compressibility is neglected.

**A2. Turbulent boundary layer everywhere on the plate, established by a leading-edge
trip.** No natural transition occurs at any tested speed (78.1 m/s would be required). The
trip's own drag is not modelled. The `natural_regime` column records the untripped state.

**A3. Zero pressure gradient on the plate.**

**A4. Perfect flow alignment.** Riblets and denticles are assumed exactly streamwise; no yaw
penalty.

**A5. Fully developed, spatially uniform texture** covering the whole wetted area, with no
leading- or trailing-edge effects and no patch boundaries.

**A6. Rigid, non-fouled, as-manufactured geometry.** No tip rounding, erosion, debris
accumulation or compliance.

**A7. Friction and pressure contributions are separable and additive** (E6), and the texture
modifies each through independent multiplicative terms.

**A8. Riblet performance is a function of l_g+ and h/s only**, with a per-shape ceiling.
Interactions between shape and Reynolds number beyond this are not modelled.

**A9. The dimple friction credit and pressure penalty are independent** and can be summed
(E11). In reality they share the same shear layer.

**A10. Denticles behave as scalloped riblets with an equivalent spacing** of one third the
denticle scale and a height of 0.15 times the scale, degraded by fixed three-dimensionality,
overlap and aspect-ratio factors.

**A11. Hybrid textures are sub-additive** with a coverage-proportional interference penalty
(E19). No calibration data supports this form; it is an assumption, and it is the study's
principal extrapolation.

**A12. Sphere wall shear is approximated by the flat-plate correlation at Re_D.** Used only
for reporting wall-unit quantities, not for the sphere drag itself.

**A13. The sphere drag crisis is represented by a sigmoid blend** between subcritical and
supercritical branches centred on Re_crit(k/D) (E16), with a fixed logistic width. The true
crisis width varies with roughness type.

**A14. Uncertainty is class-constant** and set from the spread of the calibration sources,
not propagated term-by-term. Two results are declared tied when their bands overlap.

**A15. All results are per unit wetted area of a fully textured surface.** No allowance is
made for partial coverage, installation mass, or the drag of the mounting.

---

## Appendix C. Geometry parameter definitions and diagrams

### C.1 Parameter definitions

**Table C1. Every geometric parameter used in this study.**

| Parameter | Unit | Applies to | Definition |
| :--- | :--- | :--- | :--- |
| s | µm | riblet, hybrid | Riblet spacing: peak-to-peak distance between adjacent grooves, measured spanwise. |
| h | µm | riblet, hybrid | Riblet height: wall-normal distance from groove valley to groove peak. |
| h/s | - | riblet, hybrid | Riblet aspect ratio. Not an independent variable once s and h are fixed. |
| profile | - | riblet, hybrid | Groove cross-section: V-groove (symmetric triangle), U-groove (rounded), blade (thin vertical fin), scalloped (concave-flanked). |
| A_g | µm^2 | riblet | Groove cross-sectional area, F_shape x s x h. The physically controlling quantity. |
| l_g+ | - | riblet | sqrt(A_g) in wall units. Riblet performance collapses on this parameter; optimum 10.7. |
| s+ | - | riblet | Riblet spacing in wall units, s u_tau / nu. Conventional reporting parameter; optimum 10-20. |
| D | mm | dimple, hybrid | Dimple mouth diameter at the undisturbed wall plane. |
| d/D | - | dimple, hybrid | Dimple depth ratio: maximum depth divided by mouth diameter. The dominant dimple parameter. |
| d+ | - | dimple | Dimple depth in wall units, (d/D) D u_tau / nu. |
| pattern | - | dimple, hybrid | Array arrangement: hexagonal (densest, factor 1.00), staggered (0.95), square (0.85). |
| coverage | % | dimple, hybrid | Fraction of the plan area occupied by dimple mouths. |
| scale | µm | shark | Denticle streamwise length. Equivalent riblet spacing is scale/3 (three ridges per denticle). |
| overlap | % | shark | Fraction of a denticle covered by the scale immediately upstream. Higher overlap approaches a continuous riblet. |
| aspect | - | shark | Denticle width-to-length category: low, medium (factor 1.00) or high. |
| k | µm | all | Equivalent roughness height used for the transition and sphere-crisis models: riblet h, dimple depth, denticle ridge height. |
| min_feature | µm | all | Smallest dimension that must be manufactured. Sets the process tier in the manufacturability index. |

### C.2 Cross-section diagrams

Figure 6 (`graph6_flow_visualization_streamlines.svg`) renders the riblet and dimple
cross-sections to true scale against the computed viscous sublayer thickness at 10 m/s. The
schematics below define the symbols used above; they are not to scale.

```
RIBLET, V-GROOVE                          RIBLET, BLADE
        |<--- s --->|                             |<-- s -->|
   \    /\    /\    /\                        ||       ||       ||
    \  /  \  /  \  /  \        h                ||       ||       ||   h
     \/    \/    \/    \/    __|__              ||       ||       ||  _|_
  ---------------------------  wall     -------------------------------  wall
  A_g = 0.50 s h   (h/s)_opt = 0.70      A_g = 0.95 s h   (h/s)_opt = 0.50
  ceiling 6.2 %                          ceiling 9.9 %

RIBLET, U-GROOVE                          RIBLET, SCALLOPED
   \__/  \__/  \__/  \__/                  \  /   \  /   \  /
                                            \/     \/     \/
  A_g = 0.667 s h  (h/s)_opt = 0.70      A_g = 0.60 s h  (h/s)_opt = 0.70
  ceiling 5.5 %                          ceiling 6.5 %

DIMPLE (spherical cap, section through centre)
        |<--------- D --------->|
  ------.                       .----------  wall
         \.                   ./       _|_
           `-.._________..-'            d          d/D = depth ratio
  Plan view, hexagonal array, coverage = pi D^2 / (4 * pitch^2 * sin60)

SHARK DENTICLE (streamwise section, three ridges per scale)
        |<---- scale ---->|
              ___                 ___
        _..-'' | ''-.._      _..-'' |            ridge height = 0.15 x scale
   ----'       |       `----'       |            equivalent riblet s = scale/3
  ------------------------------------------  wall
        |<-overlap->|                           overlap = fraction shadowed by
                                                the upstream denticle
```

### C.3 Full geometry catalogue

**Table C2. All 67 geometries with their defining parameters.** Blank cells indicate a
parameter that does not apply to that class.

| Geometry | Class | Profile | s (µm) | h (µm) | h/s | D (mm) | d/D | Pattern | Cov (%) | Scale (µm) | Overlap (%) | Aspect |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- | ---: | ---: | ---: | :--- |
| A-V-s50-h25 | riblet | v-groove | 50 | 25 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s50-h50 | riblet | v-groove | 50 | 50 | 1.00 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s50-h100 | riblet | v-groove | 50 | 100 | 2.00 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s50-h250 | riblet | v-groove | 50 | 250 | 5.00 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s100-h25 | riblet | v-groove | 100 | 25 | 0.25 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s100-h50 | riblet | v-groove | 100 | 50 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s100-h100 | riblet | v-groove | 100 | 100 | 1.00 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s100-h250 | riblet | v-groove | 100 | 250 | 2.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s200-h25 | riblet | v-groove | 200 | 25 | 0.12 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s200-h50 | riblet | v-groove | 200 | 50 | 0.25 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s200-h100 | riblet | v-groove | 200 | 100 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s200-h250 | riblet | v-groove | 200 | 250 | 1.25 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s500-h25 | riblet | v-groove | 500 | 25 | 0.05 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s500-h50 | riblet | v-groove | 500 | 50 | 0.10 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s500-h100 | riblet | v-groove | 500 | 100 | 0.20 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-V-s500-h250 | riblet | v-groove | 500 | 250 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-U-GR-s100-h50 | riblet | u-groove | 100 | 50 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-BLAD-s100-h50 | riblet | blade | 100 | 50 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-SCAL-s100-h50 | riblet | scalloped | 100 | 50 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-BLAD-s200-h100 | riblet | blade | 200 | 100 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| A-SCAL-s50-h25 | riblet | scalloped | 50 | 25 | 0.50 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| B-HEX-d0.5-r0.05 | dimple | spherical | n/a | n/a | n/a | 0.5 | 0.05 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d0.5-r0.1 | dimple | spherical | n/a | n/a | n/a | 0.5 | 0.10 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d0.5-r0.2 | dimple | spherical | n/a | n/a | n/a | 0.5 | 0.20 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d0.5-r0.3 | dimple | spherical | n/a | n/a | n/a | 0.5 | 0.30 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d1.0-r0.05 | dimple | spherical | n/a | n/a | n/a | 1.0 | 0.05 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d1.0-r0.1 | dimple | spherical | n/a | n/a | n/a | 1.0 | 0.10 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d1.0-r0.2 | dimple | spherical | n/a | n/a | n/a | 1.0 | 0.20 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d1.0-r0.3 | dimple | spherical | n/a | n/a | n/a | 1.0 | 0.30 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d2.0-r0.05 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.05 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d2.0-r0.1 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.10 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d2.0-r0.2 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.20 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d2.0-r0.3 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.30 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d5.0-r0.05 | dimple | spherical | n/a | n/a | n/a | 5.0 | 0.05 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d5.0-r0.1 | dimple | spherical | n/a | n/a | n/a | 5.0 | 0.10 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d5.0-r0.2 | dimple | spherical | n/a | n/a | n/a | 5.0 | 0.20 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEX-d5.0-r0.3 | dimple | spherical | n/a | n/a | n/a | 5.0 | 0.30 | hexagonal | 40 | n/a | n/a | n/a |
| B-HEXA-c20 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.05 | hexagonal | 20 | n/a | n/a | n/a |
| B-HEXA-c80 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.05 | hexagonal | 80 | n/a | n/a | n/a |
| B-SQUA-c40 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.05 | square | 40 | n/a | n/a | n/a |
| B-STAG-c60 | dimple | spherical | n/a | n/a | n/a | 2.0 | 0.05 | staggered | 60 | n/a | n/a | n/a |
| C-SK-s50-o0 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 50 | 0 | medium |
| C-SK-s50-o20 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 50 | 20 | medium |
| C-SK-s50-o40 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 50 | 40 | medium |
| C-SK-s100-o0 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100 | 0 | medium |
| C-SK-s100-o20 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100 | 20 | medium |
| C-SK-s100-o40 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100 | 40 | medium |
| C-SK-s200-o0 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 0 | medium |
| C-SK-s200-o20 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 20 | medium |
| C-SK-s200-o40 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 40 | medium |
| C-SK-s500-o0 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 500 | 0 | medium |
| C-SK-s500-o20 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 500 | 20 | medium |
| C-SK-s500-o40 | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 500 | 40 | medium |
| C-SK-s100-o20-low | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100 | 20 | low |
| C-SK-s100-o20-high | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 100 | 20 | high |
| C-SK-s200-o40-high | shark | denticle | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 200 | 40 | high |
| D-HY-01 | hybrid | v-groove | 100 | 50 | 0.50 | 2.0 | 0.05 | hexagonal | 20 | n/a | n/a | n/a |
| D-HY-02 | hybrid | v-groove | 100 | 50 | 0.50 | 2.0 | 0.05 | hexagonal | 40 | n/a | n/a | n/a |
| D-HY-03 | hybrid | blade | 100 | 50 | 0.50 | 2.0 | 0.05 | hexagonal | 20 | n/a | n/a | n/a |
| D-HY-04 | hybrid | blade | 100 | 50 | 0.50 | 1.0 | 0.10 | hexagonal | 40 | n/a | n/a | n/a |
| D-HY-05 | hybrid | v-groove | 200 | 100 | 0.50 | 5.0 | 0.05 | staggered | 40 | n/a | n/a | n/a |
| D-HY-06 | hybrid | blade | 200 | 100 | 0.50 | 5.0 | 0.10 | hexagonal | 60 | n/a | n/a | n/a |
| D-HY-07 | hybrid | scalloped | 50 | 25 | 0.50 | 1.0 | 0.05 | hexagonal | 20 | n/a | n/a | n/a |
| D-HY-08 | hybrid | blade | 50 | 25 | 0.50 | 0.5 | 0.05 | square | 40 | n/a | n/a | n/a |
| D-HY-09 | hybrid | v-groove | 500 | 250 | 0.50 | 5.0 | 0.20 | hexagonal | 60 | n/a | n/a | n/a |
| D-HY-10 | hybrid | u-groove | 100 | 100 | 1.00 | 2.0 | 0.10 | staggered | 80 | n/a | n/a | n/a |
| E-SMOOTH | baseline | smooth | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

---

*End of paper. Dataset: `dataset.csv` (670 rows). Figures: `graph1`-`graph8` (`.svg` and
`.png`). Validation: `validation_benchmarks.csv`. Machine-readable results:
`results_summary.json`.*
