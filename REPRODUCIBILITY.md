# Reproducibility & DOI (Handoff Step 12)

## Local version control

The repository is initialised here (`git init` already done; first commit
contains deliverables + reconstructed pipeline). To publish:

    git remote add origin git@github.com:<you>/microtexture-drag.git
    git push -u origin main

Suggested public name: `microtexture-drag`. Keep `dataset.csv`,
`results_summary.json`, figures, and the pipeline in every release.

## Zenodo DOI

Zenodo archives a GitHub release and mints a citable DOI free:

1. Sign in at zenodo.org with GitHub.
2. Enable the `microtexture-drag` repo under Account -> GitHub.
3. On GitHub: Releases -> Draft new release -> tag v1.0.0 -> publish.
4. Zenodo creates the archive + DOI automatically (find it under Account ->
   Uploads); the concept DOI resolves to always-latest.
5. Cite the concept DOI in the paper draft, poster footer, and JEI submission.

## Regeneration contract

    python validate_model.py && python build_dataset.py && python summary.py

must pass 13/13 and reproduce dataset parity before any release is tagged. If
you change the physics, any benchmark that breaks is either a bug or a
deliberate recalibration that must be documented in the paper's Limitations.

## Validation provenance

The validation section of `results_summary.json` serialises
`validation_benchmarks.csv`, the authoritative record of the original study's
benchmark outputs. `validate_model.py` re-derives every benchmark live as a
regression gate: the golf-ball anchors reproduce the record exactly (0.25606
and 57351.34), while the best-dimple and shark-peak sweeps land at 1.38979 and
2.97965 against the recorded 1.39505 and 2.93308 - the original sweep grids did
not survive the loss of the source notebooks, and both live values sit inside
their published bands, so the gate holds at 13/13 either way.
