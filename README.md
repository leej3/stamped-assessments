# STAMPED assessment observatory

A public ledger for repeated research-object assessments and independent reviews.
The initial study compares three assessment methods on the pinned REMoDNaV research object.
Ten independent assessments per method and three reviews per assessment are planned.
Only recorded completed work contributes to completion counts; the exploratory rubric example is excluded from repeatability estimates.

This site is configured for [leej3.github.io/stamped-assessments](https://leej3.github.io/stamped-assessments/).
It complements the [interactive rubric](https://leej3.github.io/stamped-rubric/).

## Build and preview

The builder uses Python 3.11+ and the standard library.
No package installation is required for the static site or its Python tests.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000`.
All site asset and data URLs are relative, including native-output links, so the same build works beneath a GitHub Pages project path.
The test suite additionally checks browser rendering helpers with Node.js when it is available; it reports that check as skipped otherwise.

The GitHub Actions workflow tests and builds on pushes to `main` and on manual runs.
Set **Settings → Pages → Source** to **GitHub Actions** to publish `dist/`.
The workflow publishes existing records; it does not run assessments or reviews.

## Records and interpretation

- `data/study.json` declares study arms, planned repetitions, models and status.
- `data/methods.json` records method revisions, native scales and background references.
  Only methods selected in the study count as study arms.
- `data/objects.json` catalogs research objects and their assessed revisions.
- `results/*.json` contains assessment metadata and explicit native-output links.
- `reviews/*.json` contains review metadata and optional report links.
- `docs/protocol.md` defines how the study is executed and reviewed.
- `docs/method-comparison.md` and `docs/corpus.md` describe the instruments and candidate research objects.
- [Pilot findings](docs/pilot-findings.md) interprets the observed variation and links proposed rubric refinements to review records.
- [Descriptive results](docs/study-results.md) reports the recorded study counts and native summaries.

The dashboard exposes original responses, evidence, limitations, and review findings through expandable records.
Native JSON, Markdown, and text outputs can be downloaded without translating their scales.
A checklist verdict count is not converted into a rubric score; no cross-method total or ranking is computed.

Repeatability groups require matching object and method revisions, rubric identity/fingerprint, requested and observed model, reasoning effort, evidence cohort, and recorded score weights.
Different numeric scale maxima remain separate.
Missing method or evidence provenance keeps runs separate rather than assuming equivalence.
Runs with the same requested model and all other required pins may share a group when the observed model version is unavailable; the group explicitly states “requested model; actual model version unverified.”
Only completed, explicitly independent, non-exploratory runs enter these groups.
A single scored run has no sample standard deviation.
Review counts do not imply agreement, and repeated scores do not establish rubric validity.

## Public build boundary

`scripts/build_site.py` publishes only:

1. The three named files in `site/`.
2. An explicitly projected public study/method/object catalog and recognized result/review records, written to `dist/data/site.json`.
3. JSON, Markdown, or text files explicitly linked by those records within `results/` or `reviews/`.

It does not copy `.cache/`, arbitrary repository files, execution logs, or local checkout paths.
Path traversal and symlink outputs are rejected.
Personal absolute paths in published free text fail the build; they are not silently scrubbed from an evidence record.
All validation occurs before replacing a previous build.
Catalogs may contain private local-cache paths, but those fields are outside the public projection.
Authors remain responsible for reviewing record contents before adding them to a public repository.

## Development

Site presentation is in `site/index.html`, `site/app.js`, and `site/style.css`.
The standard-library builder and tests live in `scripts/build_site.py` and `tests/test_site.py`.
The public workflow does not require the research-object cache or any model credentials.

Documentation uses the pinned Snapper pre-commit hook:

```sh
uvx pre-commit run snapper --all-files
```

Site code and authored documentation are licensed under CC BY 4.0.
Source research objects and method repositories retain their own licenses and are referenced, not relicensed.
See `LICENSES/CC-BY-4.0.txt` and `REUSE.toml`.
