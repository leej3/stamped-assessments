"""Build the public assessment dashboard from an explicit, local file allowlist."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path, PurePosixPath
import re
import shutil
import statistics

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ('index.html', 'app.js', 'style.css')
PUBLIC_EXTENSIONS = {'.json', '.md', '.txt'}
MAX_PUBLIC_FILE = 4_000_000
CATALOG_FIELDS = {
    'methods': ('id', 'title', 'repository', 'ref', 'revision', 'entrypoint', 'description', 'score_type', 'license', 'status', 'limitations', 'rubric_id', 'rubric_sha256'),
    'objects': ('id', 'title', 'locator', 'revision', 'scope', 'cache_status', 'description', 'license', 'status'),
}
STUDY_FIELDS = ('id', 'title', 'status', 'replicates_per_method', 'reviews_per_assessment', 'assessor_model', 'review_model', 'objects', 'methods', 'description', 'limitations', 'created_at', 'planned_assessments', 'planned_reviews', 'assessor_reasoning_effort', 'review_reasoning_effort', 'evidence_policy', 'score_policy')
RESULT_FIELDS = ('id', 'study_id', 'object_id', 'object_revision', 'method_id', 'method_revision', 'rubric_id', 'rubric_sha256', 'model_requested', 'model_observed', 'reasoning_effort', 'replicate', 'status', 'independent', 'exploratory', 'created_at', 'native_output', 'summary', 'limitations', 'evidence_cohort', 'evidence_cohort_id')
REVIEW_FIELDS = ('id', 'assessment_id', 'reviewer_id', 'model_requested', 'model_observed', 'reasoning_effort', 'status', 'findings', 'verdict', 'report', 'created_at', 'limitations')


def project(record, fields):
    return {key: record[key] for key in fields if key in record}


def public_safe(value):
    """Fail closed rather than publish user paths hidden in free-text output."""
    if isinstance(value, str):
        if re.search(r'(?:/Users/|/home/|file://|[A-Za-z]:\\Users\\)', value):
            raise ValueError('Public data contains an absolute personal or file URL path')
    elif isinstance(value, dict):
        for key, item in value.items():
            public_safe(key)
            public_safe(item)
    elif isinstance(value, list):
        for item in value:
            public_safe(item)
    elif isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Public data contains a non-finite number')


def load(path):
    if path.is_symlink():
        raise ValueError(f'Symlink input is not publishable: {path.name}')
    if path.stat().st_size > MAX_PUBLIC_FILE:
        raise ValueError(f'Public input exceeds size limit: {path.name}')
    def reject_constant(value):
        raise ValueError(f'Invalid JSON numeric value: {value}')
    return json.loads(path.read_text(encoding='utf-8'), parse_constant=reject_constant)


def linked_output(root, reference):
    """Only explicitly referenced results/reviews files can be published."""
    if not isinstance(reference, str) or '\\' in reference:
        raise ValueError('Output reference must be a relative POSIX path')
    path = PurePosixPath(reference)
    if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] not in {'results', 'reviews'}:
        raise ValueError('Output reference must remain inside results/ or reviews/')
    if path.suffix not in PUBLIC_EXTENSIONS:
        raise ValueError('Only JSON, Markdown, and text outputs are published')
    source = root / str(path)
    if not source.resolve().is_relative_to(root.resolve()) or any((root / Path(*path.parts[:i])).is_symlink() for i in range(1, len(path.parts) + 1)):
        raise ValueError('Output reference escapes the repository or is a symlink')
    if not source.is_file():
        raise ValueError(f'Referenced output is missing: {reference}')
    if source.stat().st_size > MAX_PUBLIC_FILE:
        raise ValueError(f'Output exceeds size limit: {reference}')
    text = source.read_text(encoding='utf-8')
    public_safe(text)
    parsed = load(source) if source.suffix == '.json' else text
    public_safe(parsed)
    return source, parsed


def group_key(record):
    # Unknown provenance remains explicit; it is never folded into a named cohort.
    key = tuple(record.get(key) or '' for key in (
        'object_id', 'object_revision', 'method_id', 'method_revision',
        'rubric_id', 'rubric_sha256', 'model_requested', 'model_observed',
        'reasoning_effort')) + (record.get('evidence_cohort') or record.get('evidence_cohort_id') or '',)
    # Absent provenance is not proof of equivalence: keep those runs separate.
    required = (key[1], key[3], key[6], key[8], key[9])
    unknown = record['id'] if not all(required) or (record.get('method_id') == 'rubric' and not record.get('rubric_sha256')) else ''
    native_assessments = record.get('native_data', {}).get('assessments', []) if isinstance(record.get('native_data'), dict) else []
    weights = record.get('summary', {}).get('weights')
    if weights is None and len(native_assessments) == 1:
        weights = native_assessments[0].get('weights')
    return key + (json.dumps(weights, sort_keys=True), unknown)


def variability(records):
    eligible = [r for r in records if r.get('status') == 'complete' and r.get('independent') is True and not r.get('exploratory', False)]
    buckets = {}
    for record in eligible:
        buckets.setdefault(group_key(record), []).append(record)
    groups = []
    for key, members in sorted(buckets.items()):
        # Scores with different maxima are separate even under identical provenance.
        maxima = sorted({r.get('summary', {}).get('scale_max') for r in members}, key=str)
        for maximum in maxima:
            same_scale = [r for r in members if r.get('summary', {}).get('scale_max') == maximum]
            values = [r['summary']['overall_score'] for r in same_scale
                      if isinstance(r.get('summary', {}).get('overall_score'), (int, float))
                      and not isinstance(r['summary']['overall_score'], bool)]
            groups.append({'key': list(key), 'assessment_ids': [r['id'] for r in same_scale],
                           'runs': len(same_scale), 'scored_runs': len(values), 'scale_max': maximum,
                           'mean': statistics.mean(values) if values else None,
                           'minimum': min(values) if values else None,
                           'maximum': max(values) if values else None,
                           'sample_sd': statistics.stdev(values) if len(values) > 1 else None,
                           'limitations': ['Requested model; actual model version unverified.'] if not key[7] else []})
    return groups


def build(root=ROOT, destination=None):
    root = Path(root).resolve()
    destination = Path(destination or root / 'dist').resolve()
    if destination != root / 'dist':
        raise ValueError('Public build destination must be the repository dist/ directory')
    study_path = root / 'data/study.json'
    study = project(load(study_path), STUDY_FIELDS) if study_path.exists() else {'title': 'STAMPED assessment study', 'status': 'preparing'}
    catalogs = {}
    for name, fields in CATALOG_FIELDS.items():
        path = root / f'data/{name}.json'
        raw = load(path) if path.exists() else {}
        entries = raw.get(name, []) if isinstance(raw, dict) else raw
        if not isinstance(entries, list):
            raise ValueError(f'{name} catalog must contain a list')
        catalogs[name] = [project(item, fields) for item in entries]
    results, reviews, files = [], [], {}
    for kind, fields, target in [('results', RESULT_FIELDS, results), ('reviews', REVIEW_FIELDS, reviews)]:
        for path in sorted((root / kind).glob('*.json')):
            raw = load(path)
            # Native assessment bundles are exposed only through a result reference.
            if not isinstance(raw, dict) or ('method_id' not in raw if kind == 'results' else 'assessment_id' not in raw):
                continue
            record = project(raw, fields)
            required = ('id', 'object_id', 'method_id', 'status') if kind == 'results' else ('id', 'assessment_id', 'status')
            if any(not isinstance(record.get(key), str) or not record[key] for key in required):
                raise ValueError(f'Malformed public record: {path.name}')
            reference = record.get('native_output' if kind == 'results' else 'report')
            if reference:
                source, native = linked_output(root, reference)
                files[reference] = source
                record['native_data' if kind == 'results' else 'report_content'] = native
            target.append(record)
    for records in (results, reviews):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate public record IDs')
    ids = {r['id'] for r in results}
    if any(r['assessment_id'] not in ids for r in reviews):
        raise ValueError('Review references an unknown assessment')
    payload = {'study': study, **catalogs, 'results': results, 'reviews': reviews,
               'variability': variability(results), 'generated_at': datetime.now(timezone.utc).isoformat()}
    public_safe(payload)
    # Validate everything before removing a previous successful build.
    for asset in ASSETS:
        if not (root / 'site' / asset).is_file():
            raise ValueError(f'Missing site asset: {asset}')
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for asset in ASSETS:
        shutil.copyfile(root / 'site' / asset, destination / asset)
    (destination / 'data').mkdir()
    (destination / 'data/site.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for reference, source in files.items():
        out = destination / reference
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, out)
    (destination / '.nojekyll').touch()
    return payload


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = build(args.root, args.output)
    print(f"Built dashboard: {len(data['results'])} assessments, {len(data['reviews'])} reviews")
