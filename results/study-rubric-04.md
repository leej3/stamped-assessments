# Independent REMoDNaV assessment, replicate 4

Assessed [paper-remodnav at 34388d3ca78fbd483e022e4e2851be390b7eebf2](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2), covering numerical results, figures, manuscript and explicitly linked computational components. Instrument: rubric 0.1.0 at e8d94d00d904058b8f87c8331cbe32e225a9490f; rubric SHA256 `05d96a057d8cfe79927f587f6994cf386e12bca83d55b3e7deee8e37ab7bcbb4`. Frozen evidence manifest SHA256: `e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`.

The inspection report is complete. Native criterion completion is separately **36/36 scored, 0 unanswered**; the bundle is complete under the rubric. All seven weights are 1. This is an inspection profile, not independent reproduction or a general scientific-quality score.

| Dimension | Score / 100 | Criterion scores in ID order |
| --- | ---: | --- |
| Self-containment | 91.67 | 3, 3, 3, 2 |
| Tracking | 72.22 | 3, 3, 3, 2, 2, 0 |
| Actionability | 77.78 | 3, 3, 1, 3, 2, 2 |
| Modularity | 72.22 | 3, 1, 2, 1, 3, 3 |
| Portability | 93.33 | 2, 3, 3, 1, 3 |
| Ephemerality | 88.89 | 3, 3, 2 |
| Distributability | 55.56 | 3, 1, 1, 2, 3, 0 |

Overall: **78.81/100**. Binary criteria T-06, P-04 and D-06 use maxima of 1; all others use maxima of 3.

The strongest evidence is the coherent Git/git-annex component selection, explicit data paths, tracked image state and executable Make/DataLad procedures. The [recorded containerized analysis](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) identifies commands, inputs, outputs and image input. The declared adapter launches a fresh disposable container with dataset-mounted outputs. These are inspected capabilities and historical records, not observed execution in this assessment.

The [updated instructions](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md) overstate complete result coverage. [quality_stats()](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/code/mk_figuresnstats.py#L463) explicitly says it is outside the Make command path, yet produces the velocity histogram and signal-loss values used by the manuscript. The flowchart helper is also a non-executed reference fragment. This limits result instructions, executable coverage and replay completeness despite substantial automation.

The [Dockerfile](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) supplies the environment but rebuilds from a moving Debian tag and unpinned apt resolution. Frozen image identities therefore support distribution more strongly than reproducible rebuilding. Image payload routes exist in supplied annex metadata; no independent image-preservation route or artifact-origin attestation was identified. The signed result tag was inspected, but its signing identity was not verified and a usable key-verification route was not found in the inspected object.

Reachable license texts cover several modules, but the derived-label module and container dependency mapping leave gaps. License compatibility at composition boundaries is not addressed. Module replacement also depends on internal data paths and implementation test utilities.

No network calls, scientific workflow execution, builds or payload acquisition occurred. Binary data, SVG payloads and container layers were intentionally absent from the frozen cohort; this is not an observed retrieval failure. The local-path original lab-acquisition submodule is not consumed by the paper runtime, which uses exported eye-gaze files. Current host-tool compatibility, payload availability, image internals and visual/numerical correctness remain unverified.

Validation: the prescribed `validate.py ... --scores` completed successfully, confirmed the rubric hash and valid anchor values, and reported `answered: 36`, `total: 36`, `complete: true`. Criterion-specific rationales, discovery paths and public source citations are retained in `study-rubric-04.bundle.json`.
