# Independent inspection: REMoDNaV

The inspection report is complete. The native rubric assessment is **34/36
criteria answered**; M-05 and D-01 remain null. Its **75.63/100 provisional
score** retains both unanswered criteria in their fixed denominators. All seven
dimension weights are 1. This is a STAMPED profile under pilot rubric 0.1.0,
not a scientific-quality ranking or a claim of independent reproduction.

The assessed root is
[paper-remodnav at 34388d3](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2).
Scope includes numerical results, figures, manuscript, and explicitly linked
computational components. The frozen manifest's SHA-256 was verified as
`e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`.

| Dimension | Provisional score |
| --- | ---: |
| Self-containment | 91.67 |
| Tracking | 72.22 |
| Actionability | 88.89 |
| Modularity | 55.56 |
| Portability | 93.33 |
| Ephemerality | 88.89 |
| Distributability | 38.89 |

The [README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md)
provides a concrete acquisition and reproduction route. Root and nested Git
registrations select code and data; the saved image records content digests.
The analysis script, Make recipes and manuscript imports connect input data to
numeric macros, generated SVGs and the PDF. Precomputed event labels are fixed
inputs; reproducing the original lab acquisition is not required to consume
them. The private upstream lab-source URL therefore does not by itself defeat
the assessed root's result-production boundary.

A [historical DataLad run record](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d)
captures the result command, input patterns, image and outputs. The linked label
module also records its generation command. These are recorded past runs,
including a disclosed small Fig 4 difference from the original publication.
No corresponding captured PDF build was found. The signed result tag contains
a PGP signature, but a usable signer verification route was not established.

The [container adapter](https://github.com/datalad/datalad-container/blob/1.2.3/datalad_container/adapters/docker.py)
selects saved image content, starts a fresh container, mounts persistent results
and removes the container automatically. The mounted workspace still requires
care about modified or stray input files. The
[Docker recipe](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile)
covers the scientific and rendering dependencies, but its base, apt resolution
and other unpinned inputs do not define a frozen reconstruction. Host setup
also leaves current-user Docker daemon access implicit.

License declarations are reachable for the root, algorithm, raw-gaze and
Andersson modules. The inspected event-label module lacks an attributable
license declaration, and bundled container terms lack a complete mapping.
Compatibility handling across those module boundaries was not found. The
analysis also depends on algorithm test utilities and nested internal data
paths, which limits independent replacement despite separate repositories.

D-01 is unanswered because the frozen package deliberately excludes binary
and annex payloads and forbids network retrieval. Recorded blob URLs and data
routes are evidence of supplied locations; current availability was not tested.
M-05 is unanswered because public source metadata and the raw-data unrestricted
access statement do not establish uniform access conditions for every label
and container payload, or documented mixed-access interfaces. No access failure
or restriction was observed. Version identities and an original saved image
also do not establish independent preservation routes or artifact attestations.

The native bundle contains all 36 criterion responses with specific rationales,
immutable source citations, discovery paths and observations. The assigned
validator passed with `--scores`: 34 answered, 36 total, `complete: false`.
No scientific workflow, container build, payload acquisition or network call
was performed. No peer output or worked assessment was consulted.
