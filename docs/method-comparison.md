# Four STAMPED assessment approaches

Source inspection: 2026-10-27.
This document compares four sources.
The user selected three assessment arms: the local rubric and the two CON assessors.
The framework and STAMPED in Practice are background only.
The planned study therefore has 30 assessments and 90 reviews, three reviews per assessment.
No assessment was executed for this source comparison.
Exact identities and file digests are in [methods.json](../data/methods.json).

## What the four references actually contain

| Method ID | Instrument | Native result | Scope choice |
| --- | --- | --- | --- |
| `rubric` | Fixed rubric plus assessment protocol | 36 anchored ratings, seven normalized dimensions, weighted total, completion counts | Research object and discoverable components; fixed criterion set |
| `stamped-skills-assessment` | Record framework, schemas, offline validator and review CLI | Categorical criterion judgments, activity coverage, per-principle summaries; no total | A use case and suitable rubric must be selected first |
| `con-stamped-impl` | Assessor skill, shared conventions and scripted probes | All 31 checklist verdicts, MUST/SHOULD/MAY counts, findings and app link; no total | Committed state of the named project; kind changes emphasis and applicability |
| `con-narps-guidance` | Revised version of the same assessor family | Same checklist vocabulary and counts, with revised evidence rules; no total | Declared delivered state, including captured uncommitted artifacts and capture limits |

The fourth method is a revision of the third, not an independent methodological family.
The framework is infrastructure rather than an instruction to assess.
Treating its included historical assessment as a skill would compare unlike things without a defined framework treatment.

## Exact sources

1. **Rubric:** [stamped-rubric-schema](https://github.com/leej3/stamped-rubric-schema/tree/e8d94d00d904058b8f87c8331cbe32e225a9490f) at `e8d94d00d904058b8f87c8331cbe32e225a9490f`, entry point `docs/assessment-protocol.md`, rubric `rubric.json` version 0.1.0.
   The clean local commit was subsequently published at the same revision.
   Its 20 principles and 36 criteria derive from manuscript revision `5bbb3ed471a5e9bf8c8e91cdef6b96686c4c53ea`, marked provisional.
2. **Assessment framework:** [stamped-skills-assessment](https://github.com/stamped-principles/stamped-skills-assessment/tree/c4c0428e6962a631d910d0becb00b7bb1c3c903c) default branch `codex/assessment-foundation`, commit `c4c0428e6962a631d910d0becb00b7bb1c3c903c`.
   Read the README, design, contribution and automation-evidence guidance, model, reference lock and bundled rubric.
3. **Implementation branch:** [CON assessor](https://github.com/con/skills/blob/4fe5d7be82ed6c297747e8b838031aec88e75903/skills/assess-alignment-with-stamped-principles/SKILL.md) branch `stamped-skills-impl`, commit `4fe5d7be82ed6c297747e8b838031aec88e75903`.
4. **Research-guidance branch:** [CON revised assessor](https://github.com/con/skills/blob/326606610af6c261876c92032ca1f89f6d3ad1f1/skills/assess-alignment-with-stamped-principles/SKILL.md) branch `codex/narps-round3-research-guidance`, commit `326606610af6c261876c92032ca1f89f6d3ad1f1`.

The two CON skills both identify themselves and `stamped-conventions` as version 0.1.0.
Those labels do not distinguish the treatments.
Both pin checklist 0.3.1 at `af259bad237fa57b856417db8dba45a1b283a527`, SHA-256 `da2eb88ed49dff64f098ad92200dec81c1b4404cc2d3ba1e1e1404d0e10e7bba`, with principles 0.2.0.
Required sibling conventions, verdicts, response formats, project-kind rules and the DataLad stack reference were reviewed, along with the changed probe and replay behavior.
Repository-only calibration fixtures are background, not runtime prerequisites or assessment evidence.

These pins describe the remote branch heads observed for this inspection.
They are not moving branch references to use unqualified during a study.

## Framework background and a concrete companion assessor

The framework README points toward a separate agent-skills repository.
The current `stamped-principles/stamped-agent-skills` default branch, commit `a723c24585799e121c3f5ba046b1f50901492719`, contains only an older `stamped-skill-draft.md` and a working note.
That draft combines intervention and audit, asks to write project documentation, and cites the old app version as a checklist version.
It is not the framework's current installable assessor.

A concrete, remote-verifiable companion exists on the explicit fork:

- Repository: <https://github.com/leej3/stamped-agent-skills>
- Branch: `codex/assessment-foundation`
- Commit: `cda6aa85d5c41b63176032240e5da8a1d3934d7f`
- Entry point: [skills/stamped-assess/SKILL.md](https://github.com/leej3/stamped-agent-skills/blob/cda6aa85d5c41b63176032240e5da8a1d3934d7f/skills/stamped-assess/SKILL.md)
- Required references: `rubrics.md`, `record-guide.md`, `review.md`
- Declared runtime pin: `stamped-skills-assessment@e367080f40e5f99e9cad31e885c9549d37e21b42`

The requested framework head differs from that declared runtime only by a README link and `docs/automation-evidence.md`; its code, schemas and bundled pilot are unchanged.
Preserve both identities: the inspected framework and the actual runtime required by the companion skill.
Do not silently rewrite the dependency.

The companion explicitly chooses a fitting rubric or drafts one, records who chose priorities, plans evidence activities, and emits native framework records.
The bundled `paper-handoff-v0.1.0` rubric has seven narrow manuscript-authoring criteria, including separate author-metadata rendering.
It is not a defensible drop-in rubric for arbitrary research objects.

**Study decision:** the user excluded the framework from the runnable arms.
Its companion and declared runtime remain documented background, not an unannounced fourth treatment.
A later framework study would need to select or construct an appropriate rubric explicitly and freeze it before assessments.
The included manuscript-specific pilot should not be generalized silently.

## Differences that can change findings

### Scores, statuses and missingness

The local rubric uses concrete 0–3 or binary anchors.
Each dimension averages normalized criterion values, and the total averages dimensions with declared weights.
Unanswered criteria stay in the denominator, contribute zero to a provisional total, and remain visibly unanswered.
Freeform comments cannot exclude a criterion.
Optional evidence-support and confidence judgments do not alter scores.
Separate reviewers keep independent contributions and totals.

The framework uses `demonstrated`, `partial`, `not_demonstrated`, `unknown` and `not_applicable`.
Principle priorities and directions represent the use case, not numerical weights.
Planned activities distinguish `completed`, `blocked` and `not_attempted`.
Finalizing a report does not imply completing every activity.
Reviews bind to the assessment's semantic digest and retain separate agree/disagree/needs-evidence decisions.
Actor kind is explicit.

Both CON methods use `met`, `partial`, `unmet`, `not-checked` and `not-applicable`.
Only `met` satisfies MUST.
Counts retain unknowns and applicability information.
Their app encoding maps `met` to yes, partial/unmet to no, and unchecked/N/A to null; that compact URL loses distinctions available in the full response JSON.
Native reports explicitly prohibit a single overall score.
Do not manufacture one for a comparison dashboard.

Consequently, the local rubric's fixed-denominator total, the framework's categorical summaries and CON checklist counts are not directly comparable measures.
The same all-public access condition can receive full fulfillment on local M-05 and `not-applicable` on CON should/009 without either assessor making a factual error.

### Breadth and principle versions

The local rubric covers all 20 statements in its manuscript snapshot, with criterion-specific anchors and licensing criteria.
Both CON branches use the older 17-statement principle bundle and 31 checklist items.
They explicitly retain the licensing and T.4 gaps as extras and flag the duplicate update-process questions must/014 and should/008.
The framework can map criteria to that same older checklist but neither requires exhaustive coverage nor treats mapping as proof an item was passed.
Compare asserted propositions and stated coverage, not raw numbers of favorable answers.

### Evidence and the delivered object

The implementation branch restricts assessment to committed state.
Its probes recognize Git paths, familiar environment files, DataLad records and known module mechanisms.
The later branch includes the declared delivered bytes and capture omissions, distinguishes original worker actions from coordinator preservation, and requires inspection beyond representations the probes know.
A public URL still identifies the named public snapshot; it does not magically supply unpublished working files.

The later branch also makes explicit that package declarations can include software without physically vendoring it; interfaces need not be named README or Makefile; ordinary dependencies are not automatically independent project modules; and provenance must connect actual results and actions to their environment regardless of record format.
This can reduce tool/layout bias, but it remains an assessor duty: the probes still operate substantially on Git paths and recognized formats.

### Execution and retrieval are not definitions or location claims

The implementation skill permits a fresh-run CI workflow definition as alternative evidence for should/004. The later branch requires completed-run evidence plus the definition. Similarly, the older environment probe can use a lockfile to credit dependency completeness and a responding remote/location log to credit publication.
The later branch separates dependency inclusion from pinning and requires inspection of imports and invoked tools; it requires independent retrieval of the intended revision and payload identity before crediting publication.

Thus a later-branch report with fewer `met` responses may reflect a stricter claim threshold rather than a worse object.
Conversely, an unknown finding can be appropriately cautious rather than a failure to follow the method.

The revised replay helper also requires output selection, distinguishes same-host from other-host replay, handles declared local annex assistance explicitly, and compares table labels as well as numeric values.
Identical bytes, successful execution, scientific validity and portability remain distinct claims.
Optional replay is a separate authorized activity in both methods.
No replay was run here.

### Composition and review export

The local rubric separates content/schema from its lightweight website and portable multi-reviewer bundle. The framework separates object, use case, rubric, observation, judgment and review records, making criterion-specific activity plans and review digests natural. The CON pair separates shared conventions from probes and human/agent judgment and preserves probe overrides.

The implementation branch's response-format guide additionally calls for framework records during evaluations, but supplies no native exporter to make that instruction automatic.
The later branch makes such export conditional on a calling harness providing pinned schemas.
If the comparison needs a common review wrapper, define and label that wrapper as study infrastructure; preserve native records unchanged.
A wrapper must not imply native interoperation that the method does not supply.

## Proposed controlled run protocol

1. **Freeze instruments before looking at outcomes.** Retain the catalog pins, content hashes, exact entry points, required resources and validator versions.
   Exclude the framework from runnable arms.
   Keep skill version strings as metadata, but use commits to identify treatments.
2. **Define the common task.** Supply the same starting object identifier, immutable snapshot, computational scope and recipient access context to every arm.
   State the scientific product without giving expected verdicts.
   For a URL study, all arms start at that URL; do not quietly pre-link an undiscoverable implementation for one arm.
   For delivered-directory studies, retain a capture manifest and distinguish source bytes from coordinator-added packaging.
3. **Offer equivalent evidence access, not identical judgments.** Give every arm the same cached source bytes, source history, explicit links, network policy, tool environment, credentials availability and time/resource ceilings.
   Record any fresh retrieval and its date.
   A common inventory is logistical metadata, not a gold answer key or a license to bypass discoverability rules.
4. **Separate evidence acquisition from adjudication when useful.** An inspection-only condition permits source reads and reference checks and prohibits executing the target workflow.
   A separately declared retrieval or replay condition supplies the same permissions and resource ceiling to every arm.
   Do not force a positive result when a native method requires an activity outside that condition.
   Keep missing, blocked and unattempted work explicit.
5. **Use independent contexts.** Give each run only its own method, common task, source access and output contract.
   Hide other assessments, reference answers and investigator expectations.
   Use fresh output directories outside the source object.
   Do not repair the source, change its `.gitignore`, or allow assessment outputs to become evidence of the object's practices.
6. **Control model and harness.** Within a matched comparison, hold exact model, reasoning effort, runtime, tools, context policy and resource limits constant.
   Record unavailable metadata as unavailable.
   If testing models too, cross model with method and report both factors.
   Different models assigned to different methods would confound the comparison.
   Randomize or balance method order; use independent repeats rather than treating three reviews as three assessor replications.
7. **Retain native outputs and validation.** Local rubric: exact bundle and its rubric digest, scores and completion.
   CON: all 31 answers, raw probes, report, pin checks and app URL, plus optional replay receipt only when run.
   Record structural failure separately from a defect in the object.
8. **Review the reasoning independently.** Reviewers receive the source evidence, applicable native criteria and assessment, with investigator labels hidden where practical.
   Capture unsupported positive claims, unjustified negative claims, missed evidence, correct unknown/applicability handling, actionable recommendations, correction burden and review effort.
   Preserve disagreements and proposed corrections; do not rewrite original assessments.
   Record whether a reviewer is an agent or person accurately, without treating agreement as human approval or truth.
9. **Analyze within instruments first.** Report criterion-level correctness and uncertainty-handling under each method, with numerators and denominators.
   Compare common factual propositions through an explicitly documented crosswalk where definitions match.
   Keep native scores in separate panels.
   Do not map all statuses onto a synthetic 0–100 scale or pool unlike totals.
10. **Interpret the pilot narrowly.** A 30-assessment design with three reviews of each produces 90 review records, not 90 independent assessments.
    Objects, methods, repeated runs and reviewers are distinct units.
    Shared model blind spots, reviewer dependence, different criterion coverage, exposure to earlier runs and changing remote availability all limit causal claims.
    Human calibration of a sample is needed before treating agent consensus as a reference judgment.

This protocol is a proposal, not evidence that any model or method is more accurate.
Fixed native tools plus their instructions form each treatment; probe advantages and instruction length are part of the intervention, not nuisance factors to silently remove.
Tool ablation can be a later, separately declared experiment.

## Lessons from STAMPED in Practice

The additional background source is [STAMPED in Practice at e1550f6d](https://github.com/leej3/stamped-in-practice/tree/e1550f6d836c3b5a5ee988a4fe6616f914c3e5e4), resolved from `main`.
The README, lessons, results and skills guides, and the source/assessment version manifests were inspected.
Its underlying trial data and annex payloads were not reanalyzed or retrieved for this source comparison.
The following are the repository's reported findings, not newly verified study outcomes.

It describes 72 research attempts and 96 operational judgments, with corrected reporting exposing 70 primary scientific assessments and 68 valid primary checklists.
Five of eight duplicate judgment pairs in one retained reassessment differed on scientific adequacy.
The repository distinguishes an earlier reporting rejection from invalidity of the delivered research, and retains both original and corrected reports.

Its lessons support several controls here: capable and calibrated judges, explicit evidence boundaries, recognition of equivalent scientific representations, shared dependency guidance, recording coordinator assistance, fixed denominator definitions, and bounded repair/completion rules.
Scientific adequacy and checklist attainment remain separate outcomes.
The prior adaptive comparison does not establish causal or transferable skill benefit.

There is an important identity distinction.
The selected `codex/narps-round3-research-guidance` revision `32660661` was round-three **research guidance** in that experiment.
The completed operational assessor is reported as `9852d8360f9519d21d11099b45f5deb8ba80cb28` on `codex/pr26-neutral-assessor`, a different revision.
Our three-arm study can compare the assessor files present in the selected research-guidance branch, but must not claim they are the exact assessor that produced those historical NARPS judgments.
No additional arm or historical controller is introduced.

The prior reporting used both met/31 and met/(met + partial + unmet) in different plots.
Their distinction is useful background, not a reason to collapse native scores in this study.
Keep full responses because compact checklist URLs discard status distinctions and shorten explanations.

## Source-review process and licensing

Used the Skills Workshop source-review workflow and its pinned GitHub preview for both CON skills and the companion framework skill.
The task named the candidates, so no broad alternative search or adoption was necessary.
Detached read-only clones and preview output are under ignored `.cache/methods/`; no source repository was changed, installed into a project, pushed or published.
No Workshop feedback or memory was collected.

The local rubric is CC-BY-4.0.
The framework's code is MIT and its schemas, documentation and records are CC-BY-4.0.
The companion framework skill is CC-BY-4.0.
CON scripts carry MIT SPDX headers, while the repository README says its license is TBD; no blanket license for its skill prose was located.
The vendored checklist retains upstream CC-BY-4.0 attribution.
The catalog describes these distinctions rather than treating a script license as covering the entire skill package.
Cached third-party sources are not part of the comparison repository's published content.
