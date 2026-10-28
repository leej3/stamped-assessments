# Independent REMoDNaV inspection — replicate 7

Assessed [paper-remodnav](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2) at `34388d3ca78fbd483e022e4e2851be390b7eebf2`, covering numerical results, figures and manuscript plus explicitly linked computational components. Instrument: rubric 0.1.0 at `e8d94d00d904058b8f87c8331cbe32e225a9490f`; exact rubric SHA256 is recorded in the native bundle.

This inspection report is complete. Native criterion completion is **34/36**, so the **78.02/100** total is provisional. All seven dimension weights are 1; unanswered M-05 and D-01 remain in their denominators. All 36 response entries include criterion-specific rationales and evidence discovery paths.

| Dimension | Provisional score /100 |
| --- | ---: |
| S | 91.67 |
| T | 72.22 |
| A | 94.44 |
| M | 55.56 |
| P | 93.33 |
| E | 100.00 |
| D | 38.89 |

The scoped inventory comprises root analysis and manuscript sources, generated TeX values and figure assets, raw-gaze and event-label subdatasets, REMoDNaV software and its comparison-data submodule, and the stored container image, recipe and runtime configuration. The private original-source `src/lab-eyetracking` link within the raw dataset is not consumed by the scoped root calculations and was not treated as an essential replay input.

The strongest support is for discoverability, executable instructions, component tracking and disposable execution. The [README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md) maps tagged numerical/SVG replay and manuscript generation; the [historical numerical run](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) records inputs, outputs, command and image. The linked adapter uses image identity, a dataset mount and automatic container removal. These are inspected definitions and historical author records, not observed successful execution in this assessment.

Material gaps concern license coverage, composition compatibility, internal module coupling, preservation and verification. Separate MIT, PDDL, GPLv3 and root CC-BY declarations are reachable, but the event-label dataset lacks a located license declaration and container asset terms lack a complete mapping. Root analysis reaches into software test internals and fixed data subtrees. The [Docker recipe](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) uses a floating Debian base and apt dependencies despite pinning selected Python packages. Saved image identity therefore exceeds the precision of rebuilding the image. The signed results tag was inspected, but no supplied signer-verification route or executable-artifact attestation was established. Manuscript generation has executable instructions without an equivalent located captured execution record.

M-05 remains unanswered: unrestricted raw-data access is explicit, but supplied evidence does not establish uniform access conditions across every module or an actual mixed restriction. D-01 remains unanswered: explicit routes and annex web metadata are present, but current retrieval of every intended payload is unknown. Missing cached payloads are deliberate limitations, not observed retrieval failures.

Evidence boundary: frozen manifest SHA256 `e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`, cohort `remodnav-e3c6253bced7`. Discovery began at the root and followed explicit links. No peer outputs or other assessment methods were consulted. No network calls, scientific computation, container builds or payload acquisition occurred. Binary, annex and container-layer contents were unavailable by design. Historical exit-zero records and the README's reported verification do not establish independent reproduction. The documented small difference from the journal-era figure remains a source qualification.

Validation: the assigned validator accepts the native bundle, including rubric hash and legal binary anchors. Its summary reports 34 answered, 36 total, and `complete: false`. A report-generation helper initially used a Python lacking jsonschema; it was rerun using the assigned virtual environment. This did not affect scientific evidence or validation.
