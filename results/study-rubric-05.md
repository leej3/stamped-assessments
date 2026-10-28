# Independent REMoDNaV inspection — replicate 5

Assessed repository revision `34388d3ca78fbd483e022e4e2851be390b7eebf2`
under rubric 0.1.0 with all seven dimension weights equal to one.
The frozen evidence manifest SHA-256 is
`e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`.
Scope covers numerical results, figures, manuscript and explicitly linked
computational components. Distributed data are inputs; reproducing upstream
laboratory acquisition is outside this computation scope.

The inspection report is complete. Native criterion completion is **35/36**:
D-01 remains null because this cohort cannot establish current retrieval of
all required payload versions. The fixed-denominator score is **provisional**.
All 36 criteria have criterion-specific rationales, observations and citations
in the native bundle. Null is not an assigned zero.

| Dimension | Provisional score / 100 |
| --- | ---: |
| Self-containment | 91.7 |
| Tracking | 72.2 |
| Actionability | 77.8 |
| Modularity | 55.6 |
| Portability | 93.3 |
| Ephemerality | 88.9 |
| Distributability | 38.9 |

Overall provisional score: **74.0/100**.

The object provides a coherent Git/git-annex state, explicit subdataset links,
a saved content-identified container, a tracked environment recipe and
historical DataLad run records. The [README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md)
gives acquisition, analysis replay and manuscript commands. The recorded
[analysis run](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d)
is historical provenance, not execution observed during this assessment.

Material gaps are distinct:

- The standard script dispatch omits `quality_stats()`, which generates
  `velhist.svg` consumed by the manuscript. Its docstring calls for adding the
  invocation manually. A claim to recompute all figures therefore exceeds the
  standard command's inspected coverage. Manually edited flowchart artifacts
  also have no complete replayable generation record.
- Root CC BY, software MIT, raw-data PDDL and comparison-repository GPL terms
  are identifiable. The event-label dataset lacks a located license
  declaration, and image package terms are not fully mapped. Combination
  compatibility is not explained.
- The Docker build uses an undigested Debian tag and unpinned apt resolution.
  A saved frozen image preserves the existing environment but does not fix
  every future reconstruction input.
- A PGP-signed result tag exists. No signer-key verification route or complete
  distributed-image origin attestation was located. Checksums establish
  content identity without establishing producer identity.
- Docker launches a fresh container with automatic removal and host-persisted
  outputs. The mounted repository remains shared state; clean/reset discipline
  is still needed for a full clean-workspace reconstruction.

Binary payloads, annex data, image layers and some rendering assets are absent
from the frozen package by design. Their absence is not an observed service
failure. Source metadata supplies retrieval routes, but those routes were not
tested. No scientific workflow, build, acquisition or network call was run;
there is **no claim of independent reproduction**. The historical README
also acknowledges a changed histogram relative to the journal publication.

Validation: the assigned native schema/cross-record validator was run with
`--scores`; the saved bundle passed. Binary criteria retain binary anchors.
The rubric is a pilot and these values are a STAMPED profile, not a measure of
scientific merit or a validated universal ranking.
