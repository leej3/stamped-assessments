# REMoDNaV assessment-method pilot: descriptive results

Updated 2026-10-28T02:56:02.246133+00:00.
21/30 assessments and 55/90 reviews are complete.
Failed attempts remain in the ledger.

This is one research object at one fixed source revision, planned for ten independent assessments per method with fresh contexts.
It is not ten different research objects.
The exploratory worked example is excluded.
Requested assessor model is `gpt-6.1-sol` with medium reasoning; requested reviewer model is `gpt-6-astra` with high reasoning.
Actual underlying model versions were not independently exposed.

The shared cohort permits source inspection, not scientific workflow execution or independent annex-payload retrieval.
Each native report preserves its own missingness and evidence judgments.
These findings have not been adjudicated by human experts.

| Method | Completed assessments | Failed assessments | Reviews | Review verdicts |
| --- | ---: | ---: | ---: | --- |
| rubric | 7 | 0 | 19 | needs_revision: 19 |
| con-stamped-impl | 7 | 0 | 18 | needs_revision: 18 |
| con-narps-guidance | 7 | 0 | 18 | needs_revision: 17, supported: 1 |

## Native results

### rubric

Native overall scores: n=7, mean 74.80, range 70.71–78.81.
Sample standard deviation: 3.24.
Unanswered criteria contribute zero to these provisional native totals and remain visible in completion counts.
Evidence ratings and confidence do not alter scores. 6 assessments have all three reviews; 6 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

### con-stamped-impl

Native results are categorical checklist verdicts.
No overall numeric score is created.
Per-item verdict distributions and separate MUST/SHOULD/MAY counts are retained in the analysis JSON and dashboard. 6 assessments have all three reviews; 6 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

### con-narps-guidance

Native results are categorical checklist verdicts.
No overall numeric score is created.
Per-item verdict distributions and separate MUST/SHOULD/MAY counts are retained in the analysis JSON and dashboard. 6 assessments have all three reviews; 5 of those sets share an overall review verdict.
This is descriptive agreement, not accuracy.

## Criterion review patterns

Per-criterion distinct-review counts for agree, disagree and needs_evidence are in `criterion_reviews` in the analysis JSON.
Each criterion records both completed-review and checked-review denominators.
Multiple findings from one review count once per disposition; conflicting dispositions and checked criteria without findings are explicitly flagged.
These counts identify recurring questions, not a consensus or correctness score.

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
