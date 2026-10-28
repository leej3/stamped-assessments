# Independent REMoDNaV inspection, replicate 3

The inspection report is complete. Native criterion completion is **34/36**, with M-05 and D-01 unanswered; its overall **70.71/100 is provisional**. Nulls remain in all fixed denominators. All seven dimension weights are 1. This is a pilot STAMPED profile, not a scientific-quality rating or a claim of independent reproduction.

Assessed [paper-remodnav](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2) at `34388d3ca78fbd483e022e4e2851be390b7eebf2`. Scope covers numerical results, figures, manuscript and explicitly linked computational components. Instrument: rubric 0.1.0 at e8d94d00d904058b8f87c8331cbe32e225a9490f; exact rubric SHA256 05d96a057d8cfe79927f587f6994cf386e12bca83d55b3e7deee8e37ab7bcbb4. Evidence manifest SHA256 e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499.

| Dimension | Score / 100 |
| --- | ---: |
| Self-containment | 91.67 |
| Tracking | 72.22 |
| Actionability | 72.22 |
| Modularity | 55.56 |
| Portability | 86.67 |
| Ephemerality | 77.78 |
| Distributability | 38.89 |

The [README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md) and nested registrations expose data, classifier, image and manuscript from one root. Git/annex content identities fix their intended joint distribution. A [historical DataLad record](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) captures analysis commands and input/output declarations, and another captures event-table production. These are recorded historical executions, not executions performed in this assessment.

Coverage falls short of the full stated reproduction claim. [quality_stats()](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/code/mk_figuresnstats.py#L458) produces `velhist.svg` but is omitted from command-line dispatch; [main.tex](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/main.tex#L1161) includes that figure. The flowchart helper also says it is not executable as a complete procedure. Manuscript compilation is instructed but no corresponding captured run was located. A complete rendered paper can therefore reuse tracked figures without demonstrating regeneration of each one.

Licenses are identifiable for the root, raw data, classifier and Andersson repository, but the [event-label dataset](https://github.com/psychoinformatics-de/studyforrest-data-eyemovementlabels/blob/92279db3850ee4282d97001a3f650fc55cb64b4e/README) has no located declaration. No cross-module compatibility handling was found. The [Dockerfile](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) has selected Python pins but moving Debian/apt inputs. The adapter creates disposable containers and persists outputs in the dataset, while its full-worktree mount and partial cleanup leave the initial workspace incompletely constrained.

M-05 remains null because uniform payload access conditions and the significance of a linked private acquisition-source module cannot be established for the whole graph. D-01 remains null because delivery of every intended payload version cannot be verified under this cohort. These are uncertainties, not observed download failures. No usable signer-verification route for provenance or image producer/build attestation was located.

All source/text evidence and histories were read from the frozen package. Binary data, image layers and SVG payloads are deliberately absent. No network calls, scientific workflow execution, image builds or payload acquisition occurred. Upstream acquisition infrastructure is distinguished from the published TSV inputs required by this result scope. The containerized historical record acknowledges a histogram change relative to the journal version, and the current root contains a later OCI conversion.

Native output: `study-rubric-03.bundle.json`, one independent assessment with criterion-specific rationales and immutable public evidence locators/discovery paths. Validation is performed with the assigned validator and exact rubric; the validator result is recorded below.

Validation passed (assigned validate.py --scores, exit 0): schema, rubric digest, anchor values and cross-record invariants valid. Validator reports 34/36 answered, complete=false, overall 70.71428571428571.
