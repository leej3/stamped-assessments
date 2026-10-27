# Prefetched research-object corpus

The catalog in `data/objects.json` identifies five assessment entry points:

| Object | Entry point | Selected material |
| --- | --- | --- |
| REMoDNaV | [paper-remodnav](https://github.com/psychoinformatics-de/paper-remodnav) | Pinned repository source snapshot and Git history |
| ReproNim containers | [containers](https://github.com/ReproNim/containers) | Pinned catalog/source snapshot and Git history; image payloads inventoried separately |
| ReproNim simple workflow | [simple_workflow](https://github.com/ReproNim/simple_workflow) | Pinned workflow source snapshot and Git history |
| Kayanattil et al. (2023) | [Publication DOI](https://doi.org/10.1073/pnas.2301956120) | Publication metadata/full text and the linked Edmond dataset, version 1.1 |
| Lang et al. (2023) | [Publication DOI](https://doi.org/10.1038/s41598-023-33998-z) | Publication metadata/full text, cited Zenodo record 6384937, and its GitHub v1.0 snapshot |

The last two were identified through the [MPSD reproducible-publication examples](https://computational-science.mpsd.mpg.de/docs/reproducibility.html#examples-for-reproducible-publications).
The paper, dataset and GitHub repository are related components of each example, not three independently selected assessment targets.
The catalog preserves the discovery route so an assessor can distinguish what is findable from the paper from what a curator happened to cache.

## Reproduce the download

Run the public-source prefetcher from this repository:

```sh
python3 scripts/prefetch.py
```

It uses Python's standard library and Git.
It does not install software from, execute notebooks in, build containers from, or run analysis code in any research object.
Ordinary Git metadata reads do not require invoking DataLad or git-annex.
Later annex retrieval requires a separately provisioned DataLad/git-annex environment and a new evidence acquisition record.

Existing catalog Git revisions are reused.
`--refresh` explicitly resolves new Git root revisions; it does not silently change the cited DOI dataset versions.
For the Lang example, the selected Git reference is the archived `v1.0` release, not the repository's evolving default branch.
The script records exact resolved commit IDs in the catalog.

To retry just one object:

```sh
python3 scripts/prefetch.py --only kayanattil-2023
```

The default artifact limit is 512 MiB.
The Edmond dataset's default total payload limit is 3,072 MiB, checked against the metadata's announced file sizes before downloads begin.
Both are configurable with `--max-file-mib` and `--max-total-mib`.
Smaller limits produce an explicit partial inventory rather than a false completeness claim.
`--workers` controls the number of concurrent Edmond file requests; the default is eight.

## What the inventory means

Downloaded third-party bytes stay in ignored `.cache/objects/`.
Public catalog paths are repository-relative; no credentials or private absolute paths are needed.
Each object has a local `manifest.json`.
The public catalog contains source URLs, exact revisions, selected versions, byte counts, artifact SHA-256 digests, and retrieval or verification timestamps.

For Git objects, the prefetcher keeps a partial bare clone for commit/tree history, a pinned source archive, a readable source snapshot, and a `snapshot-inventory.json`.
Every extracted regular file has a SHA-256 and byte count.
Archive symlinks are inventoried as pointers rather than followed or installed.
Annex symlink targets and pinned submodule commits are recorded as not downloaded; their presence is not confused with possession of the data.
The source snapshot therefore may intentionally lack files represented by those pointers.
The bare clone's promisor objects may still require network access; only the archived and inventoried regular-file snapshot is locally complete.

For Edmond, `edmond-version.json` preserves the selected dataset metadata and `dataset-inventory.json` records every file's identifier, path, announced size, upstream checksum, download status, and local SHA-256 when available.
Dataverse MD5 values are compared numerically because this record contains some MD5 strings with omitted leading zeroes.
Successful downloads are checked against the provider's checksum, not merely recorded after the fact.
The Zenodo archive is likewise checked against its published MD5.

`partial` means one or more selected artifacts, annex payloads or submodules remain absent, or an endpoint failed.
`selected_sources_downloaded` means only that the selected source artifacts succeeded; it does not promise that every runtime dependency or URL embedded in arbitrary scripts has been downloaded.
Consult individual artifacts and absence inventories.
HTTP failures are preserved as retrieval failures, and a publisher's HTML response is not accepted as a PDF.

## Deliberate boundaries

- The ReproNim container collection can reference many large images.
  Its Git catalog is downloaded, but no blanket download of the entire image collection is attempted.
- REMoDNaV's linked dataset payloads and container layers are not substituted for their small Git/annex pointers.
  Fetching the root source does not resolve its previous assessment's unanswered payload-retrieval question.
- Commercial COMSOL software mentioned by the Kayanattil publication is not downloaded.
  This limitation is distinct from retrieving the published dataset.
- Publication XML can support later source inspection when a publisher blocks direct PDF retrieval.
  The catalog records both the accessible representation and the failed PDF request rather than claiming identical artifacts.
- Cache availability is an acquisition fact, not a rubric score.
  In particular, downloading a component via a curator-supplied link does not establish that an assessor could discover it from the research object's own entry point.

These materials are preparation for assessment.
Their numerical results have not been recomputed, and the corpus does not yet establish comparative STAMPED scores or agreement between reviewers.

## Frozen REMoDNaV review cohort

`data/remodnav-evidence.json` describes a separate source-only evidence package for independent reviews.
Its matching local copy is `.cache/objects/paper-remodnav/evidence/evidence.json`.
This package contains no prior rubric answers, assessments, or scores.

The initial freeze has seven recursively pinned repository states, 260 selected text/source files, seven Git ancestor histories, a linked execution-adapter source file, and eight auxiliary annex-availability records. Its graph contains ten module-discovery edges. All 276 downloaded file hashes were checked; 3,281 binary/annex/symlink payload pointers remain explicitly absent. CSV/TSV files small enough for inspection may be present among the text files; this is not a claim that all scientific data is present.
The root is the same exact REMoDNaV commit selected in the catalog.

Initial cohort identifier: `remodnav-e3c6253bced7`.
Initial manifest SHA-256: `e3c6253bced7d959cd59873c3d49d166bf5793906bcdf65e49e265076d215499`.

To deliberately prepare a new evidence freeze:

```sh
python3 scripts/prefetch.py --remodnav-evidence
```

This rewrites the manifest and its creation timestamp.
Do not run it while a cohort is being assessed.
Record the new manifest digest as a new evidence cohort rather than silently substituting it for an earlier one.
Review agents should read the explicit source/history paths in the manifest.
Querying the partial bare clones for omitted blobs can access the network and expand the evidence beyond the frozen package.
