# REMoDNaV assessment-method pilot: descriptive results

Updated 2026-10-28T00:24:44.471638+00:00.
3/30 assessments and 9/90 reviews are complete.
Failed attempts remain in the ledger.

This is one research object at one fixed source revision, assessed ten times per method with fresh contexts.
It is not ten different research objects.
The exploratory worked example is excluded.
Requested assessor model is `gpt-6.1-sol` with medium reasoning; requested reviewer model is `gpt-6-astra` with high reasoning.
Actual underlying model versions were not independently exposed.

The shared cohort permits source inspection, not scientific workflow execution or independent annex-payload retrieval.
Each native report preserves its own missingness and evidence judgments.
These findings have not been adjudicated by human experts.

| Method | Completed assessments | Failed assessments | Reviews | Review verdicts |
| --- | ---: | ---: | ---: | --- |
| rubric | 1 | 0 | 3 | needs_revision: 3 |
| con-stamped-impl | 1 | 0 | 3 | needs_revision: 3 |
| con-narps-guidance | 1 | 0 | 3 | needs_revision: 2, supported: 1 |

## Native results

### rubric

Native overall scores: n=1, mean 76.43, range 76.43–76.43.
Sample standard deviation: not estimated with one run.
Unanswered criteria contribute zero to these provisional native totals and remain visible in completion counts.
Evidence ratings and confidence do not alter scores. 1 assessments have all three reviews; 1 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

### con-stamped-impl

Native results are categorical checklist verdicts.
No overall numeric score is created.
Per-item verdict distributions and separate MUST/SHOULD/MAY counts are retained in the analysis JSON and dashboard. 1 assessments have all three reviews; 1 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

### con-narps-guidance

Native results are categorical checklist verdicts.
No overall numeric score is created.
Per-item verdict distributions and separate MUST/SHOULD/MAY counts are retained in the analysis JSON and dashboard. 1 assessments have all three reviews; 0 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

## Interpretation limits

Different methods ask different questions and apply different evidence thresholds.
The rubric includes manuscript-derived licensing and other criteria absent from the pinned checklist; checklist methods preserve unknown and not-applicable categories rather than the rubric’s numeric fixed denominator.
Their totals must not be pooled or ranked.

Three independent review contexts use the same requested model family and can share systematic errors.
They do not represent three human experts or three independent assessor replications.
Partial review coverage is explicitly retained.
Agreement alone cannot validate the assessment.

No controlled random seed, causal method benefit, general scientific-quality ranking, or execution reproducibility is claimed.
Wall time and compute cost were not consistently measured at the individual assessment-activity level and are not inferred from preparation timestamps.

Machine-readable detail: [study-analysis.json](../data/study-analysis.json).
Native outputs and all review records remain separate and unchanged.
See [protocol](protocol.md) and [method comparison](method-comparison.md) for source identities and design.
