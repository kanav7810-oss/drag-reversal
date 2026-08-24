# Wind Tunnel & Drop Test Protocol (Handoff Step 2)

Pre-registration principle: **write the predicted DR for every coupon before
testing and publish it beside the result.** Predictions live in
`dataset.csv` / `results_summary.json`; do not edit them after data collection.

## Facility requirements

Low-speed subsonic tunnel, test section >= 0.15 m x 0.15 m, usable 5-30 m/s.
Accessible options: university outreach tunnels, community-college labs. The
sphere work needs only a well-instrumented open jet or a tall drop volume.

## Configuration A - flat plate (momentum-deficit method, preferred)

A 5% Cf change is a ~2.5% change in momentum thickness - below what a hobby
load cell resolves on a 12.8 mN drag budget at 20 m/s. Measure the momentum
deficit instead.

Rig:
- Coupon flush in splitter plate; leading-edge **trip mandatory** (0.4 mm
  zig-zag turbulator tape or 0.5 mm cylindrical roughness row at x/L = 0.05).
  Every plate prediction in the dataset assumes a tripped turbulent boundary
  layer - an untripped run corresponds to nothing in the study.
- Boundary-layer Pitot probe: flattened tip ~0.5 mm, micrometer traverse,
  station x = 0.95 L = 95 mm.
- Reference Pitot-static in the freestream; differential manometer or
  transducer with <= 0.1 Pa resolution; log temperature each session.

Procedure per coupon and speed (10, 15, 20, 25, 30 m/s):
1. Traverse wall-normal in >= 25 logarithmically spaced steps to y = 1.5 delta.
2. Compute u(y); theta = integral of (u/U)(1 - u/U) dy.
3. Re-measure the smooth reference between every textured coupon (drift catch).
4. Five repeat traverses minimum; randomise run order.
5. Relative metric: theta_textured / theta_smooth. Absolute: Cf = 2 dtheta/dx
   with two streamwise stations if the rig allows.

Control gate: the smooth-plate profile must collapse onto the law of the wall
in wall units before any textured measurement counts. If it does not, fix the
trip or pressure gradient first.

Uncertainty budget: propagate probe position (+/- 0.05 mm), pressure
resolution, temperature, and traverse repeatability into theta and DR. Report
the budget, not just scatter across repeats.

## Configuration B - sphere

Do the sphere FIRST to build confidence: predicted effect is enormous (52.8%),
not marginal.

Drop test E1 (under $100):
1. Mass-matched sphere pair from `fabrication/COUPON_SPECS.md` (<=1% mismatch).
2. Drop line with fiducial scale in frame; >= 8 m clear fall; phone @240 fps.
3. 20 alternating drops smooth/dimpled; log T and P each session.
4. Track position frame-by-frame (Tracker or OpenCV); fit m dv/dt =
   mg - 0.5 rho Cd A v^2 to extract Cd, or use terminal-velocity form
   Cd = 2mg/(rho A v_t^2) if reached.
5. Welch t-test across repeats; report effect size with 95% CI and the
   Reynolds number actually achieved (~Re_D 5e4-8e4 at terminal velocity -
   right at predicted crisis onset).
6. Reject tumbling runs (Magnus contamination); release without spin.

Predicted outcome: Cd 0.490 -> 0.232. If no difference appears, the model's
sphere calibration is wrong and that is a publishable finding - report it.

## Blockage corrections

At 42.7 mm in a 150 mm section, solid blockage is ~6.4% - not negligible.
Apply standard solid + wake blockage corrections (Allen & Vincenti or the
facility's documented method) and state which correction was used.

## Run matrix template

| config | coupon | speed | rep | theta | U_ref | T | notes |
|---|---|---|---|---|---|---|---|

Randomise within each speed block. Log everything raw; no hand-entered
derived values.
