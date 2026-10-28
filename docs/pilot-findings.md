# What the REMoDNaV pilot tells us

This pilot tests how consistently three frozen assessment methods describe one research object under the same inspection boundary.
It does not establish which method measures scientific quality best.
See the [descriptive results](study-results.md) for counts and distributions and the [source comparison](method-comparison.md) for instrument differences.

## Variation across ten assessments per method

| Method | Native summary across ten runs | Criteria with more than one response |
| --- | --- | --- |
| Manuscript rubric | Mean 74.65/100; range 70.71–78.81; sample SD 2.72 | 8/36 |
| CON implementation | MUST items met: mean 9.3/17; range 7–13 | 16/31 |
| CON research guidance | MUST items met: mean 10.4/17; range 7–12 | 16/31 |

The checklist figures count only MUST items rated met, not total fulfillment scores.
The variation column counts criteria with any differing native response, including unknown or unanswered states; it does not measure the size or correctness of a difference.
Different questions, anchors, and principle versions prevent treating these columns as a ranking of methods.
Nine rubric runs leave at least one criterion unanswered, so their totals are provisional; all unanswered values remain in the denominator.
The [analysis JSON](../data/study-analysis.json) retains every criterion distribution and dimension statistic.

## What each approach contributes

The manuscript-derived rubric supplies explicit rating anchors, a seven-dimension profile, and a total with declared weights.
It covers 20 manuscript principles through 36 criteria, including licensing questions absent from the older checklist.
That makes it useful for recording degrees of fulfillment and identifying improvements within a dimension.
The total is a summary of those declared choices, not a universal ordering of research objects.

The two CON skills supply an assessment procedure, source-inspection guidance, scripted probes, and 31 categorical checklist judgments.
They retain distinctions among partial fulfillment, unknown evidence, and inapplicability that cannot be reconstructed from a binary checklist URL alone.
The later research-guidance version is a revision of the implementation skill, with more explicit treatment of completed-run evidence, alternative technical representations, and delivered scope.
Those differences change the claims an assessor is asked to substantiate; fewer favorable answers would not by itself demonstrate a better assessment.

The practical opportunity is to combine explicit rubric anchors with careful evidence-discovery and scope instructions.
This pilot preserved the three instruments separately and did not test such a combined method.

## Recurring questions worth resolving

**Define the included computation once and carry it through every criterion.** Several reviews question assessments that include linked label production when discussing missing dependencies but credit only the root container when discussing environment instructions or fresh execution.
A small component table could record each discoverable component, its role, whether regenerating it is within the assessment boundary, and the discovery link.
That would make scope choices reviewable without asking projects to declare an elaborate priority model.
See, for example, the [implementation review of replicate 7](../reviews/study-con-stamped-impl-07-review-1.json).

**Separate existing code, documented invocation, and observed execution.** Reviews repeatedly flag the velocity-histogram regeneration path: a function's presence does not establish that the documented command invokes it for a reported manuscript result.
Conversely, an old successful run record is evidence of that historical run even when a new replay is outside this study's scope.
Criterion examples should show these distinct cases rather than using “reproducible” as shorthand for all of them.
See the [research-guidance review of replicate 7](../reviews/study-con-narps-guidance-07-review-1.json).

**Make unknown handling consistent with criterion-specific anchors.** Reviewers repeatedly identify rubric M-05's explicit zero anchor for undetermined access conditions as incompatible with leaving that same judgment unanswered.
Changing null to zero would improve completion semantics without changing the fixed-denominator total.
Meanwhile, an unperformed availability check must not be represented as an observed retrieval failure.
Worked examples should explain when the absence of required information is itself the assessed condition and when the assessor simply has not checked it.
See the [rubric review of replicate 8](../reviews/study-rubric-08-review-1.json).

**Review rationales even when scores look stable.** All three reviewers of rubric replicate 8 questioned its description of an OCI conversion commit as unsigned.
They distinguished a visible signature from a verified producer identity; correcting the factual explanation need not change the binary score.
Stable totals can therefore conceal evidence errors, and identical totals can arise from different dimension profiles.
Original responses and criterion-level reviews are essential parts of the report.

**Require a concrete basis for negative modularity claims.** Some reviews challenge deductions based only on coupling or absence of a demonstrated update test.
An unstable internal interface, an observed incompatibility, and untested compatibility are different claims.
Examples should make clear which supports a negative rating and which supports an evidence limitation.
The research-guidance replicate 7 review linked above illustrates this concern.

## How to use these findings

These are candidates for a human-adjudicated rubric revision, not automatic corrections to the research object or its scores.
The frozen pilot ratings remain unchanged.
A next rubric version could add the component table, sharpen missing-evidence examples, and clarify overlapping automation, portability, preservation, and modularity anchors.
Retest a revised instrument on additional objects; the prefetched corpus is a starting point, not an already assessed benchmark.

The three reviews per assessment use fresh contexts but the same requested model family.
They can share errors and are not independent human ground truth.
Their permitted input is the native assessment response and frozen source/method evidence; the separate prose report and raw assessment probes were not mandatory review inputs.
No current payload retrieval, scientific workflow execution, signature verification, or human adjudication was performed as part of this pilot.
The [protocol](protocol.md) records model-observation and evidence-capture limitations, including the unavailable historical blobs and the timing of the explicit Git no-lazy-fetch guard.
