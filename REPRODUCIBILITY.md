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
