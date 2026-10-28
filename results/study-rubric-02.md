# Independent rubric assessment — replicate 2

Object: [paper-remodnav at 34388d3ca78f](https://github.com/psychoinformatics-de/paper-remodnav/tree/34388d3ca78fbd483e022e4e2851be390b7eebf2). Scope: numerical results, figures and manuscript, including explicitly linked computational components. Rubric 0.1.0; all seven dimension weights are 1. Frozen evidence cohort: `remodnav-e3c6253bced7`.

The inspection report is complete. The native assessment is **provisional: 33/36 criteria answered**, with A-02, M-05 and D-01 unanswered and retained in the denominator. Its provisional overall score is **70.71/100**. This is a pilot STAMPED profile, not a scientific-quality score or evidence of independent reproduction.

| Dimension | Score / 100 |
| --- | ---: |
| Self-containment | 91.67 |
| Tracking | 72.22 |
| Actionability | 61.11 |
| Modularity | 55.56 |
| Portability | 86.67 |
| Ephemerality | 88.89 |
| Distributability | 38.89 |

The root makes its computational boundary unusually explicit: Gitlinks identify the raw-data, event-label and classifier modules, while Git/annex records also identify the saved container and manuscript artifacts. The inspected inventory covers paper analysis code, parameters, data references, figure sources, manuscript/TeX assets, the environment recipe/image and host orchestration prerequisites. The upstream laboratory-acquisition source has a private filesystem URL, but the paper computation consumes already-published raw recordings; that upstream acquisition module is not treated as a required paper-run dependency.

[The captured 2023 analysis run](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d) records command, inputs, image and outputs. A nested label-generation run supplies additional historical provenance. These records support meaningful replay capability, but the label-generation host environment is unresolved. The README’s tagged replay selects the older 2023 reference state; the assessed root additionally includes later manuscript/OCI changes. Historical notes document a small histogram difference from the journal publication.

A material coverage gap is visible in [the analysis source](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/code/mk_figuresnstats.py#L463): `quality_stats()` implements data loss and the velocity histogram but is excluded from the command dispatcher, and its docstring instructs recipients to edit the invocation list. The manuscript reports those data-loss results and includes the histogram. Main statistics/figure production and PDF compilation have executable paths; the full declared scope does not have one complete supplied execution sequence.

The [Docker recipe](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile) and saved-image selection are tracked and machine readable. Inspection of the explicitly referenced DataLad Containers 1.2.3 adapter establishes fresh `docker run` execution, automatic `--rm`, and persistence through a dataset mount. However, the mounted worktree is reused, and the build recipe resolves a moving Debian base and apt packages. Archived image identity therefore earns tracking credit without establishing frozen image reconstruction.

Licenses are reachable for the root, classifier, raw dataset and evaluation module, but the label-data module and bundled environment/assets do not have complete attributable declarations. No documented handling of combinations was found. The results tag contains a PGP signature, but no supplied signing-identity verification route or executable-artifact origin attestation was identified. Container annex metadata gives blob routes, while an independent recovery route for all essential bytes is not established.

A-02 remains unanswered because host installation is delegated to pages absent from the frozen package. M-05 remains unanswered because uniform access across the entire inventory is unestablished, without evidence of an actual restriction. D-01 remains unanswered because all intended payload versions could not be tested for recipient availability. These are uncertainties, not assigned zero scores.

Only frozen source/text, histories, manifests and supplied availability metadata were inspected. Scientific data, binary figures/style assets and container layers were deliberately not supplied. No network access, data acquisition, scientific workflow, container build or independent reproduction occurred. The bundle contains criterion-specific immutable public citations and discovery paths. The assigned validator passed with `--scores`: 33/36 answered, provisional 70.71/100; binary anchors and the exact rubric checksum validated.
