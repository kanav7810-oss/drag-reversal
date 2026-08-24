# Presentation Assets (Handoff Steps 7 + 8)

## 90-second elevator pitch (Finding 1)

> "If you ask 'what surface reduces drag the most?' you get a different answer
> depending on something most people never check: what kind of drag dominates.
> I built one consistent model from published experiments and compared four
> micro-texture families - riblets like shark-skin ridges, golf-ball dimples,
> shark denticles, and hybrids - on two bodies at five speeds, 670 cases with
> uncertainty on every number. On thin surfaces where friction dominates,
> riblets win - up to nine and a half percent. On blunt bodies where pressure
> drag dominates, dimples win - over fifty percent. Same textures, opposite
> winners, and riblet-dimple hybrids never beat their own ingredients. The
> lesson for engineers: pick your texture by asking what fraction of your drag
> is friction versus pressure first."

## Poster plan (tri-fold)

- **Left panel**: Question + why it matters (aircraft/fuel framing); study map
  (67 geometries x 5 speeds x 2 bodies); Figure 1 (top-20 bar).
- **Center panel**: Method in three steps (compose correlations -> validate ->
  rank); the validation table with EMERGENT rows highlighted; Finding 1 chart
  (Figure 2, sign-flip vs speed); Finding 1 statement large.
- **Right panel**: Findings 3-5 (s+ band chart = Figure 4; shark 2.0% vs 12%
  myth; hybrid failure); applications table (UAV/car/swimwear);
  next-steps QR code linking to repo + live demo.
- Footer: name, school, contact, DOI (mint before printing).

Figures to use: graph1 (bar), graph2 (speed lines), graph4 (s+ scatter),
graph6 (flow visualisation) as background art on the center panel.

## One-page technical summary (hand to judges/teachers)

Structure:
1. Objective (2 sentences) + gap statement.
2. Method: reduced-order semi-empirical model; correlations composed; 13-point
   validation; uncertainty propagated per class.
3. Validation table verbatim (13 rows, status column visible).
4. Findings 1-5, one line each, with numbers.
5. What would falsify this: E1-E4 experiment list, one line each.

## "Is this just curve fitting?" - defense script (Step 8)

One sentence: "The model is calibrated on seven published benchmarks, and it
independently reproduces three benchmarks it was never fitted to - the riblet
optimal s+ of 15.5 inside the published 13-20 band, the drag-crossover s+ of
31.1 inside the published 25-40 band, and the V-groove optimum - plus an
emergent dimpled-sphere drag crisis that appears at Reynolds numbers where the
smooth sphere shows no crisis at all."

Then show the table. Key distinctions to know cold:
- IMPLEMENTATION rows: textbook correlation coded correctly (not evidence).
- CALIBRATED rows: fit applied correctly (still not independent evidence).
- EMERGENT rows (exactly 3): genuine predictions the model was never fitted to.
- The dimple controversy is acknowledged, not hidden: best plate dimple is
  predicted near zero (+0.88%) because the conservative-consensus literature
  disagrees; the sphere is where dimples shine.
- Known modelling conveniences to concede if pressed: the deep-negative riblet
  floor clamp (Q5), fixed friction share on the sphere (Q6), no yaw dependence
  (Q7), hybrids are labelled extrapolation (Q1).

Follow-up attacks and answers:
- "Why not full CFD?" -> Resolving 50 um riblets needs wall-resolved LES at
  ~1e9 cells per case x 670 cases; instead the top five geometries get
  minimal-span LES (cfd kit) - the standard in the riblet literature.
- "Where does 9.9% come from?" -> Bechert et al. 1997 blade measurements;
  everything scales off that anchor via l_g+ collapse (Garcia-Mayoral &
  Jimenez).
- "What if your trip changes the answer?" -> Correct concern (handoff Q4):
  measure smooth plate with/without trip first; that's built into protocol E2.

## Live demo

`index.html` runs standalone (double-click, no server). Preload: ranking tab
sorted by DR_net_pct, explorer set to A-BLAD-s200-h100 vs B-HEX-d2.0-r0.1.
Run it on a tablet at the booth; keep dataset.csv downloads working offline.
