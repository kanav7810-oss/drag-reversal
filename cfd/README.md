# CFD Campaign Kit - Minimal-Span Riblet Channel (Handoff Step 3)

Goal: break the study's dependence on the reduced-order model by computing
wall-resolved flow over the top riblet geometries directly. Do NOT simulate
the full plate; a minimal-span periodic channel is the standard approach in
the riblet DNS/LES literature and cuts cell counts by orders of magnitude.

## Target geometries (in order)

1. A-BLAD-s200-h100 (overall plate winner)
2. A-V-s500-h250 (easiest to manufacture positive result)
3. A-BLAD-s100-h50 (tolerance stress test)
4. C-SK-s500-o40 (contested shark-skin claim)
5. D-HY-03 (widest model uncertainty)

## Solver

OpenFOAM (free) - `simpleFoam` for RANS screening, `pimpleFoam` + WALE or
dynamic-Smagorinsky for LES. ANSYS Fluent under academic licence is an
acceptable substitute.

## Validation gate (before any textured run)

Reproduce smooth-channel Cf to within 3% of Dean/Moser correlations at matched
Re_tau. The smooth case runs in the IDENTICAL domain at the same resolution -
it is the control, and a mismatched control invalidates every comparison.

## Mesh requirements

- y+ < 1 at the riblet tip (< 0.5 preferred for LES)
- >= 20-30 cells across one groove
- >= 15 points across the viscous sublayer, >= 100 wall-normal points total
- Domain: >= 3 delta streamwise, >= 8 grooves spanwise, Re_tau ~ 180-395

## Grid convergence

Three mesh levels minimum; report the Grid Convergence Index (GCI) per
Celik et al. For LES, report spectra convergence instead: spanwise energy
spectra near the wall must saturate with resolution.

## Diagnostics to extract

1. Time-averaged wall shear integrated over the wetted surface -> DR vs the
   matched smooth control.
2. Protrusion height difference (riblet effectiveness indicator).
3. Spanwise energy spectra near the wall: Kelvin-Helmholtz rollers appearing
   past s+ ~ 20 would validate the model's post-peak rollover mechanism
   directly - this is the single strongest possible validation of Finding 3.

## Cost estimate and compute access

Minimal-span LES: 5e6-2e7 cells, 1,000-10,000 core-hours per case. Routes:
TACC via a UT Austin collaboration (see outreach templates), university
outreach programs, or start with RANS screening on a personal workstation
(simpleFoam cases run overnight).

## Case skeleton layout

    cfd/
      minimal_span_channel/
        0/            U, p fields (template values below)
        constant/     turbulenceProperties, polyMesh (from blockMesh)
        system/       blockMeshDict, controlDict, fvSchemes, fvSolution
        scripts/
          make_snake_stl.py   # parametric riblet wall geometry -> STL
          run_riblet_case.sh  # mesh -> RANS screen -> LES production chain

Start from the standard OpenFOAM channel tutorial (`channel395`), replace the
lower wall with a ribbed boundary via `snappyHexMesh` using an STL from
`make_snake_stl.py` (extrudes the same cross-sections as
`fabrication/riblet_plate.scad` along the span), match Re_tau, then clone for
the smooth control.

## Reporting

For each case: mesh table, y+ maps, Cf vs x convergence history, DR with
numerical uncertainty, GCI table (RANS) or spectra (LES). Archive cases with
results in the repo release for the Zenodo DOI.
