# Independent rubric assessment — replicate 8

Research object: [paper-remodnav](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2), revision `34388d3ca78fbd483e022e4e2851be390b7eebf2`. Scope: numerical results, figures and manuscript, including explicitly linked computational components.

Instrument: rubric 0.1.0 at `e8d94d00d904058b8f87c8331cbe32e225a9490f`; rubric SHA-256 `05d96a057d8cfe79927f587f6994cf386e12bca83d55b3e7deee8e37ab7bcbb4`. Frozen evidence cohort `remodnav-e3c6253bced7`; manifest SHA-256 `e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`. All seven dimension weights are 1.

The inspection report is complete. Native criterion completion is **34/36**, with **M-05 and D-01 unanswered**; the fixed-denominator overall score is therefore **provisional: 73.25/100**. This is a STAMPED profile, not a measure of scientific merit or proof of independent reproduction.

| Dimension | Score / 100 |
| --- | ---: |
| Self-containment | 91.67 |
| Tracking | 72.22 |
| Actionability | 77.78 |
| Modularity | 61.11 |
| Portability | 93.33 |
| Ephemerality | 77.78 |
| Distributability | 38.89 |

The root makes the computational assembly unusually explicit: data and algorithm subdatasets, analysis code, manuscript sources, stored image and configuration are reachable from its [README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md) and module declarations. Git states and annex/image content identities tie their intended combination to the assessed snapshot. The local-only ancestral raw-source module is visible but is not an input consumed by this scoped analysis, which uses the distributed BIDS files.

The [historical containerized run](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) records a command, input globs, image, outputs and exit status. It supports replay of the principal analysis; it does not establish full-scope execution provenance. In [the actual source](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/code/mk_figuresnstats.py), `quality_stats()` produces the velocity histogram and signal-loss values but is outside the default dispatcher; its docstring requires adding an invocation. `flowchart_figs()` is marked as a reference rather than an executable production procedure. Thus the README’s “recompute everything” claim exceeds the default command’s inspected coverage.

The [Docker adapter](https://github.com/datalad/datalad-container/blob/1.2.3/datalad_container/adapters/docker.py) creates fresh containers and removes them automatically, with outputs and Git provenance outside the mutable container. It also mounts the existing checkout: cleanup of named files/caches does not guarantee that only declared state is present. The [Dockerfile](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) specifies dependencies, but its Debian tag, apt packages and other unpinned build inputs prevent frozen reconstruction even though the stored executable image is content-addressed.

Root CC BY 4.0, algorithm MIT, raw-data PDDL and annotation-repository GPLv3 declarations are reachable. Event-label module licensing, bundled Springer asset scope and image dependency license mappings remain unresolved; composition compatibility is not addressed. Access conditions are not sufficiently established across every module to choose an M-05 anchor. A signed results tag exists, but no usable signing-identity verification route was found; it does not establish authenticated provenance or the origin of the later converted executable image.

D-01 remains unanswered because no exact-payload retrieval was permitted or observed. The supplied package explicitly omits data/annex payloads, container layers and some style/figure assets. Their absence is an inspection limitation, not evidence of failed retrieval. Some components have archival links, but preservation and independent recovery of every essential resource, especially image layers, are not established.

Validation passed with the assigned `validate.py --scores`: one structurally valid assessment, all 36 response keys present, 34 scored, binary anchors respected, exact rubric hash matched. No network calls, payload acquisition, scientific computation or container builds were performed. Historical run records were inspected; no independent reproduction is claimed. Criterion-specific rationales and immutable source citations are in `study-rubric-08.bundle.json`.
