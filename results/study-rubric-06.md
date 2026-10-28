# Independent STAMPED inspection — replicate 6

Assessed [paper-remodnav at 34388d3](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2), covering numerical results, figures, manuscript and explicitly linked computational components. Instrument: rubric 0.1.0 at e8d94d00d904058b8f87c8331cbe32e225a9490f; rubric SHA256 `05d96a057d8cfe79927f587f6994cf386e12bca83d55b3e7deee8e37ab7bcbb4`. Frozen evidence cohort: `remodnav-e3c6253bced7`; manifest SHA256 `e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`.

The inspection report is complete. Native criterion completion is **34/36**, so the score is **provisional: 74.84/100**, with equal dimension weights and unanswered criteria retained in their denominators.

| Dimension | Score /100 |
|---|---:|
| Self-containment | 91.67 |
| Tracking | 72.22 |
| Actionability | 83.33 |
| Modularity | 55.56 |
| Portability | 93.33 |
| Ephemerality | 88.89 |
| Distributability | 38.89 |

The strongest evidence is the explicit subdataset composition, versioned data/image identities, historical DataLad records and fresh disposable container execution procedure. The [recorded containerized analysis](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) specifies commands, input globs, image and result destinations. These are historical records, not observations of a successful run in this study.

A specific scope gap limits actionability and provenance coverage: [quality_stats](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/code/mk_figuresnstats.py#L463) computes data loss and `velhist.svg`, but the command-line dispatcher does not call it. The [manuscript includes these results](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/main.tex#L1144). Recomputing them requires manual integration beyond the advertised replay. Existing tracked figures can still support manuscript rendering.

The [Dockerfile](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) specifies the computational stack but resolves a moving Debian base and unpinned OS packages. The saved image fixes a runtime state; its recipe does not reconstruct a fully frozen build. License declarations cover several modules, while the derived-label dataset and complete container asset mapping remain unclear. The signed results tag was inspected, but a usable verification route for the signing identity and a producer/source attestation for the executable image were not established.

M-05 (access-condition separation/uniformity) and D-01 (retrieval in the intended state) remain null. Metadata and retrieval commands do not establish all payload access conditions or present obtainability, and this cohort prohibits retrieval tests. The local-path raw-acquisition submodule is upstream of the supplied published BIDS inputs and is not treated as an ingredient needed to consume those inputs.

No network calls, scientific workflow execution, builds or payload acquisition occurred. Binary figures, annex data and image layers were intentionally absent; this is not evidence of failed retrieval. No independent reproduction is claimed. The companion JSON preserves all 36 criterion-specific findings, evidence paths and uncertainties. The required validator passed; it reports 34 answered criteria and an incomplete native assessment.
