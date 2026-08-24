# Journal Submission Package (Handoff Step 5)

Ladder, easiest first. Be explicit in every cover letter that this is a
reduced-order semi-empirical study - accurate self-assessment reads well;
overclaiming kills student submissions.

## Target 1: Journal of Emerging Investigators (JEI) - realistic NOW

Free, mentored peer review built for middle/high-school authors.
- Format: original-research article; abstract <= 250 words; main text
  typically 2,500-4,000 words; figures referenced in text.
- Source material: `research_paper.md` (condense Sections 1-5 + validation
  table; move E-equations to supplementary), the 8 figures (SVG -> 600 dpi
  PNG), `dataset.csv` as supplementary data.
- Authorship: Kanav Thonda (independent researcher; school affiliation Rouse
  High School). Disclose that the computational pipeline was executed with AI
  research-tooling assistance per JEI AI policy, and that analysis/interpretation
  are the author's own. Check the current JEI author guidelines before
  submitting - AI-use disclosure rules tightened across journals in 2025-26.

### Cover letter draft

> Dear Editors,
>
> I am submitting "Which surface micro-texture reduces drag depends on what
> kind of drag: a systematic cross-class comparison" for consideration as an
> original research article in the Journal of Emerging Investigators.
>
> Prior riblet, dimple, denticle and hybrid studies each examine one texture
> class on one body at one Reynolds number. This work composes published,
> peer-reviewed drag correlations into one consistent semi-empirical framework
> and compares all four classes across two bodies (friction-dominated flat
> plate; pressure-dominated sphere) at five speeds - 670 cases with propagated
> uncertainty. The headline result is that the winning texture class reverses
> when the dominant drag mechanism changes: riblets win on the plate (+9.51%
> best case), dimples win on the sphere (+52.77%), and riblet-dimple hybrids
> never beat their best constituent. Three benchmarks the model was not fitted
> to (riblet optimal s+, drag-crossover s+, V-groove optimum) fall inside
> published bands independently.
>
> I state plainly in the manuscript that this interpolates the literature
> rather than performing new CFD or measurement; a wind-tunnel campaign on the
> top geometries is underway as follow-up. I believe the systematic cross-class
> framing and honest uncertainty treatment fit JEI's standards, and I would be
> glad to revise per reviewer guidance.
>
> Sincerely,
> Kanav Thonda
> Rouse High School, Leander TX

## Target 2: Journal of Student Research (JSR)

Realistic now; article processing charge applies. Same package as JEI, reformatted to JSR's template on acceptance of the JEI timeline slipping past ~4 months.

## Later targets (require Step 2 or Step 3 completed first)

| Venue | Gate |
|---|---|
| AIAA Journal | needs experimental or LES validation + faculty co-author |
| Experiments in Fluids | needs the measured uncertainty budget from Step 2 |

## Submission checklist

- [ ] Manuscript condensed from research_paper.md, AI-assistance disclosed
- [ ] Abstract <= 250 words, no jargon in title
- [ ] Figures exported >= 600 dpi PNG from the SVGs
- [ ] dataset.csv + results_summary.json attached as supplementary
- [ ] Validation table verbatim, with EMERGENT/CALIBRATED/IMPLEMENTATION labels
- [ ] Limitations section quotes Q1-Q10 honestly
- [ ] School sponsor/adult contact listed per JEI requirements
- [ ] Zenodo DOI minted first (see REPRODUCIBILITY.md) and cited in the draft
