# Fabrication Package - Test Coupons (Handoff Step 1)

Eight coupons to print/machine first, chosen so every class in the study is
represented and the model is exposed to falsification. Full rationale:
`handoff.md` Step 1.

## Coupon manifest

| # | Geometry ID | Class | Predicted DR | Min feature (um) | Manu. index | Route |
|---|---|---|---:|---:|---:|---|
| 1a | E-SMOOTH (copy A) | baseline | 0% reference | - | 0.0 | any |
| 1b | E-SMOOTH (copy B) | baseline | plate-to-plate variability | - | 0.0 | same as 1a |
| 2 | A-V-s500-h250 | riblet (V) | +5.344% @10 m/s | 250 | 1.0 | SLA first |
| 3 | A-BLAD-s200-h100 | riblet (blade) | +9.506% @20 m/s | 100 | 1.3 | CNC or SLA |
| 4 | A-BLAD-s100-h50 | riblet (fine blade) | tolerance test | 50 | 3.6 | CNC / laser |
| 5 | C-SK-s500-o40 | shark denticle | +2.033% @50 m/s | 167 | 4.08 | laser / resin |
| 6 | B-HEX-d2.0-r0.05 | dimple (plate) | +0.88% best case | 100 | 2.3 | SLA |
| 7 | D-HY-03 | hybrid | +2.04% @10 m/s | 50 | 4.6 | laser / resin |
| 8 | B-HEX-d5.0-r0.3 | dimple (negative control) | **-20.15% @10 m/s** | 1500 | 2.0 | SLA |

Print coupon 2 FIRST: easiest-to-manufacture positive result.

## Plate coupons

- Wetted test area: **100 mm x 80 mm** flush panel (matches the wind-tunnel
  splitter-plate mount in `wind_tunnel/PROTOCOL.md`). Add a 5 mm plain border
  around the textured field so the frame seals on smooth material.
- Thickness: 6 mm plate stock equivalent (print flat on the build plate, then
  post-cure and wet-sand the BACK face flat; do not sand the texture side).
- Riblet grooves run spanwise-to-flow when mounted: grooves must be **parallel
  to the flow** (streamwise). Mark flow direction on the back of each coupon.
- Tolerance requirement (handoff): hold riblet tip radius < 10% of s. For the
  blade coupons this is the make-or-break parameter - blunt tips are the most
  common cause of experimental riblets underperforming theory.
- As-built metrology is mandatory: optical profilometer, or calibrated
  microscope photographs at 3 locations plus a stylus scan if available.
  Report as-built s, h, tip radius next to nominal values in every result.

### OpenSCAD parametric sources

`fabrication/riblet_plate.scad` renders any V-groove or blade-riblet plate;
set `shape`, `s_um`, `h_um`, `plate_w_mm`, `plate_l_mm`, `thickness_mm`.
Render at 0.01 mm resolution and export STL. Note: consumer SLA at 25 um XY
resolves s >= 200 um reliably; treat finer spacings as CNC/laser work.

`fabrication/dimple_sphere.scad` renders the 42.7 mm sphere with a hexagonal
dimple array (`B-HEX-*` family): set `dimple_d_mm`, `depth_ratio`. The dimple
depth is depth_ratio x dimple_diameter, spherical-cap cut, hex-packed at 60%
pitch overlap to approximate the model's coverage fraction.

`fabrication/dimple_plate.scad` renders the plate dimple coupons (same array
logic on the 100 x 80 panel).

## Sphere coupons (E1 drop-test pair)

- Two spheres, D = 42.70 mm +/- 0.05 mm: one E-SMOOTH, one B-HEX-d2.0-r0.1
  (hexagonal, 2.0 mm prints, depth ratio 0.10 -> 0.20 mm deep).
- Mass-match to **within 1%**: adjust internal infill per sphere, add sealed
  ballast through a 3 mm filling hole opposite the pole, then seal. Weigh to
  0.01 g. A 1% mass mismatch corrupts a terminal-velocity comparison more
  than the entire drag effect being measured.
- Surface: cure fully; UV-yellowing is fine, gloss differences are not -
  varnish both spheres identically if either is glossy.
- Drop-test procedure, analysis, and failure modes: `wind_tunnel/PROTOCOL.md`
  section "Experiment E1".

## Post-processing checklist (SLA)

1. IPA wash 2 x 10 min, air-blow dry before curing.
2. Post-cure per resin datasheet (typically 5-15 min UV).
3. Wet-sand ONLY the reference/back face (400 -> 1200 grit).
4. Verify no uncured residue in groove roots (sticky tips = wrong drag).
5. Measure as-built geometry; log against nominal in `metrology_log.csv`.

## Cost snapshot (Aug 2026, round numbers)

| Item | Est. cost |
|---|---:|
| SLA printer (Form 3+/4 class or equivalent used market) | $300-$1,500 |
| Resin liter (tough/standard) | $40-$80 |
| IPA + curing station (DIY bucket + UV lamp works) | $30-$60 |
| Zig-zag turbulator tape (trip strip, 0.4 mm) | $10-$25 |
| Calipers 0.01 mm + USB microscope for metrology | $30-$60 |

The whole first campaign fits inside a MIT THINK budget ($1,000) if a printer
is available at school or a makerspace - see `funding/FUNDING_PLAN.md`.
