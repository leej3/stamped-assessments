# REMoDNaV method comparison: preregistered pilot protocol

This experiment compares three assessment instruments on one fixed research object.
It estimates variability in their application; it does not validate a universal scale of scientific quality or rank people.

## Design

- Object: `psychoinformatics-de/paper-remodnav` at `34388d3ca78fbd483e022e4e2851be390b7eebf2`.
- Arms: the STAMPED rubric, CON `stamped-skills-impl`, and CON `codex/narps-round3-research-guidance`, pinned in `data/methods.json`.
- Ten independent assessments per arm: 30 assessments.
- Three independent reviews of each assessment: 90 reviews.
- Assessors: requested model `gpt-6.1-sol`, medium reasoning.
- Reviewers: requested model `gpt-6-astra`, high reasoning.
- Each worker starts with a fresh context, without parent conversation history, other assessments, the exploratory example, or peer reviews.
- Record requested model separately from observed model metadata.
  Do not infer an unavailable underlying model version or claim a controlled sampling seed.

The framework and `stamped-in-practice` repositories inform the method comparison but are not experimental arms.
The original REMoDNaV worked example is exploratory and is excluded from replicate statistics.

## Evidence access

All workers receive the same frozen evidence cohort and discovery graph in `data/remodnav-evidence.json`, together with their assigned instrument only.
The common scope is the numerical results, figures and manuscript and their explicitly linked computational components.
Cache availability does not make a source discoverable: reviewers must cite the route from the declared object.

This is an inspection cohort.
Inspect text, source, version history, manifests, recorded provenance and supplied metadata; run read-only instrument probes where available.
Do not execute the scientific workflow, build containers, or claim that cached source proves successful payload retrieval.
Record omitted activities and inaccessible content explicitly.
No worker may update upstream repositories or fetch additional evidence silently.
Material discovered missing from the cohort is a limitation, not permission to change one replicate's inputs.

The controlled boundary intentionally limits conclusions about actual execution.
Instrument-specific evidence demands remain visible: an instruction, configured workflow, successful historical run, and independently repeated computation are not interchangeable.
Differences caused by those policies are findings about methods, not changes in the assessed object.

## Native output and scoring

Preserve each method's native response and evidence records.
The rubric arm uses its exact 36 criteria, default equal dimension weights and fixed-denominator missingness.
The CON arms retain all 31 checklist verdicts, evidence and MUST/SHOULD/MAY denominators.
Do not invent a numeric overall score for a method that defines none.
Do not average different native scales.

Each assessment receives a stable run identifier, method revision, object revision, evidence cohort identifier, model request, reasoning setting, replicate number, completion status and native output locations.
Failed or incomplete runs remain in the ledger; they are never silently replaced by a successful retry.
A retry is a new attempt linked to the original.
A validation failure is distinct from a substantive unfavorable assessment.

## Independent review

A reviewer sees one assessment, its assigned method and the common evidence cohort.
They do not see the other two reviews, the assessment author's identity, or other assessments.
Method blinding is not claimed because the instrument and its criteria are necessary for a meaningful review.

Each review checks:

1. Whether cited evidence supports the individual judgments.
2. Whether the method's criteria and evidence rules were followed.
3. Missing or overstated claims, including access versus execution.
4. Internal consistency, completion, scoring and denominator handling.
5. Whether the feedback supports concrete improvements to the object or rubric.

Report criterion-level dispositions (`agree`, `disagree`, `needs_evidence`) where possible, supporting locators, suggested corrections and an overall verdict (`supported`, `needs_revision`, or `insufficient_evidence`).
These are review judgments about the assessment, not an additional STAMPED score.
Preserve all three reviews without manufacturing consensus.

## Analysis

Group only runs with matching object revision, method revision, rubric fingerprint, model request/observation, reasoning setting and evidence cohort. Show completion and failures alongside counts. For the numeric rubric, report per-criterion distributions, dimension/total distributions and dispersion; for checklist methods, show categorical verdict distributions and disagreements.

Ten runs describe within-model variability under this protocol, not variability between all models or human reviewers.
Three reviews from the same model family are not three independent human experts.
Shared model training and systematic errors remain limitations even when contexts are independent.
Cross-method comparisons should inspect evidence grounding, agreement patterns, coverage, missingness and actionable differences rather than treat unlike totals as equal.

Broader objects are prefetched and cataloged for later cohorts.
Do not fold new objects or changed source snapshots into this pilot without a new cohort ID.
