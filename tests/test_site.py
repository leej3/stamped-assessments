import copy
import base64
import gzip
import json
from pathlib import Path
import tempfile
import unittest
from scripts.build_site import build, group_key, linked_output, public_safe, variability

ROOT = Path(__file__).resolve().parents[1]


def result(id='r1', **changes):
    value = {'id': id, 'study_id': 'study', 'object_id': 'object', 'object_revision': 'obj-rev',
             'method_id': 'rubric', 'method_revision': 'method-rev', 'rubric_id': 'rubric-v1',
             'rubric_sha256': 'a' * 64, 'model_requested': 'model-a', 'model_observed': 'model-a',
             'reasoning_effort': 'medium', 'replicate': 1, 'status': 'complete',
             'independent': True, 'evidence_cohort': 'frozen-v1',
             'summary': {'overall_score': 75, 'scale_max': 100}}
    value.update(changes)
    return value


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ['data', 'results', 'reviews', 'site', '.cache']:
            (self.root / name).mkdir()
        for filename in ['index.html', 'app.js', 'style.css']:
            (self.root / 'site' / filename).write_text((ROOT / 'site' / filename).read_text())
        self.write('data/study.json', {'id':'study','title':'Test', 'methods':['rubric'], 'objects':['object'], 'replicates_per_method':10, 'reviews_per_assessment':3})
        self.write('data/methods.json', {'methods':[{'id':'rubric','title':'Rubric','local_repository':'/Users/private/secret'}]})
        self.write('data/objects.json', {'objects':[{'id':'object','title':'Object','cache_path':'/Users/private/cache'}]})

    def tearDown(self):
        self.temp.cleanup()

    def write(self, filename, value):
        (self.root / filename).write_text(json.dumps(value))

    def test_allowlist_copies_only_referenced_outputs(self):
        self.write('results/run.json', result(native_output='results/native.json'))
        self.write('results/native.json', {'responses': {'S-01': {'score': 3, 'evidence': ['README']}}})
        self.write('reviews/review.json', {'id':'review1','assessment_id':'r1','status':'complete','findings':[], 'report':'reviews/report.md'})
        (self.root / 'reviews/report.md').write_text('Observed finding.')
        (self.root / '.cache/secret.txt').write_text('never publish')
        (self.root / 'results/unlinked.txt').write_text('never publish')
        data = build(self.root)
        self.assertEqual(len(data['results']), 1)
        self.assertIn('responses', data['results'][0]['native_data'])
        self.assertEqual(len(data['reviews']), 1)
        self.assertTrue((self.root / 'dist/results/native.json').is_file())
        self.assertFalse((self.root / 'dist/results/unlinked.txt').exists())
        self.assertFalse((self.root / 'dist/.cache').exists())
        self.assertNotIn('/Users/', (self.root / 'dist/data/site.json').read_text())
        self.assertNotIn('local_repository', data['methods'][0])

    def test_exploratory_and_planned_runs_do_not_create_variability(self):
        records = [result(independent=False), result('r2',status='planned'), result('r3',exploratory=True)]
        self.assertEqual(variability(records), [])

    def test_variability_does_not_pool_different_provenance_or_scale(self):
        first = result()
        second = result('r2', summary={'overall_score':85,'scale_max':100})
        groups = variability([first, second])
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]['mean'], 80)
        self.assertAlmostEqual(groups[0]['sample_sd'], 7.0710678118654755)
        for field in ['object_revision','method_revision','rubric_sha256','model_requested','model_observed','reasoning_effort','evidence_cohort']:
            changed = copy.deepcopy(second)
            changed[field] = 'different'
            self.assertEqual(len(variability([first,changed])), 2, field)
        second['summary']['scale_max'] = 3
        self.assertEqual(len(variability([first,second])), 2)

    def test_rubric_link_round_trips_original_bundle(self):
        native = {'format_version':'1.0.0','assessments':[{'responses':{'S-01':{'score':3}}}]}
        self.write('results/run.json', result(native_output='results/native.json'))
        self.write('results/native.json', native)
        record = build(self.root)['results'][0]
        encoded = record['rubric_url'].split('v1.')[1]
        decoded = json.loads(gzip.decompress(base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4))))
        self.assertEqual(decoded, native)

    def test_native_distributions_keep_unknown_and_absent_distinct(self):
        a = result(native_data={'assessments':[{'responses':{'S-01':{'score':3}, 'D-01':{'score':None}}}]})
        b = result('r2', native_data={'assessments':[{'responses':{'S-01':{'score':0}}}]})
        distribution = variability([a,b])[0]['criterion_distributions']
        self.assertEqual(distribution['D-01']['counts'], {'unanswered':1,'absent':1})
        self.assertEqual(distribution['S-01']['counts'], {'3':1,'0':1})
        self.assertTrue(distribution['S-01']['disagreement'])
        a['native_data'] = {'responses':{'must/001':{'status':'met'}}}
        b['native_data'] = {'responses':{'must/001':{'status':'partial'}}}
        self.assertEqual(variability([a,b])[0]['criterion_distributions']['must/001']['counts'], {'met':1,'partial':1})

    def test_equal_totals_retain_different_dimension_profiles(self):
        a=result(summary={'overall_score':50,'scale_max':100,'dimension_scores':{'S':100,'T':0}})
        b=result('r2',summary={'overall_score':50,'scale_max':100,'dimension_scores':{'S':0,'T':100}})
        group=variability([a,b])[0]
        self.assertEqual(group['sample_sd'],0)
        self.assertEqual(group['dimension_statistics']['S']['mean'],50)
        self.assertEqual(group['dimension_statistics']['S']['minimum'],0)
        self.assertEqual(group['dimension_statistics']['S']['maximum'],100)

    def test_unknown_provenance_and_different_weights_remain_separate(self):
        first, second = result(), result('r2')
        first.pop('model_observed')
        second.pop('model_observed')
        self.assertEqual(group_key(first), group_key(second))
        groups = variability([first, second])
        self.assertEqual(groups[0]['runs'], 2)
        self.assertIn('actual model version unverified', groups[0]['limitations'][0])
        first.pop('method_revision')
        second.pop('method_revision')
        self.assertNotEqual(group_key(first), group_key(second))
        first, second = result(), result('r2')
        first['summary']['weights'] = {'S':1}
        second['summary']['weights'] = {'S':2}
        self.assertNotEqual(group_key(first), group_key(second))

    def test_traversal_absolute_and_symlink_outputs_rejected(self):
        for reference in ['../.cache/secret.txt','/etc/passwd','.cache/secret.txt','results/../../secret.txt','results/output.html']:
            with self.assertRaises(ValueError):
                linked_output(self.root,reference)
        (self.root / '.cache/secret.txt').write_text('secret')
        (self.root / 'results/shortcut').symlink_to(self.root / '.cache', target_is_directory=True)
        with self.assertRaises(ValueError):
            linked_output(self.root,'results/shortcut/secret.txt')

    def test_personal_paths_fail_before_build_replacement(self):
        (self.root / 'dist').mkdir()
        (self.root / 'dist/keep.txt').write_text('previous build')
        self.write('results/run.json', result(limitations=['/Users/person/private']))
        with self.assertRaises(ValueError):
            build(self.root)
        self.assertTrue((self.root / 'dist/keep.txt').exists())
        with self.assertRaises(ValueError):
            public_safe({'text':'file:///private/file'})

    def test_published_source_paths_are_preserved_as_evidence(self):
        public_safe({'evidence':'/home/data/psyinf/forrest_gump/collection/fg_eyegaze_raw'})
        public_safe({'evidence':'initialdir=/home/asimio/fg_eyegaze_preproc/'})
        with self.assertRaises(ValueError):
            public_safe({'evidence':'/home/unverified/private'})

    def test_unknown_review_assessment_rejected(self):
        self.write('reviews/review.json', {'id':'review','assessment_id':'missing','status':'complete'})
        with self.assertRaises(ValueError):
            build(self.root)

    def test_initial_render_defers_record_bodies(self):
        import shutil
        import subprocess
        if not shutil.which('node'):
            self.skipTest('Node unavailable')
        source = (ROOT/'site/app.js').read_text()
        renderer = source[source.index('const e ='):source.index("root.addEventListener('toggle'")]
        fixture = {'study':{},'methods':[],'objects':[],'reviews':[],'variability':[],
                   'results':[result('r1'),result('r2'),result('r3')]}
        script = "const root={innerHTML:''};\n" + renderer + '\ndata=' + json.dumps(fixture) + ";render();"
        script += "if(root.innerHTML.includes('run-body'))throw Error('Eager body rendering');"
        script += "if(!recordRow(data.results[0],true).includes('run-body'))throw Error('Missing expanded body');"
        subprocess.run(['node','-e',script],check=True,capture_output=True,text=True)

    def test_site_renders_untrusted_text_through_escaping_and_safe_links(self):
        # Executable JS behavior is checked using Node when available, without a browser dependency.
        import shutil
        import subprocess
        if not shutil.which('node'):
            self.skipTest('Node unavailable; browser rendering helper check skipped')
        source = (ROOT/'site/app.js').read_text()
        helper = source[source.index('const e ='):source.index('const completed =')]
        test = helper + '''
if(e('<script>"&') !== '&lt;script&gt;&quot;&amp;') throw Error('HTML escaping failed');
if(link('javascript:alert(1)', '<img>') !== '&lt;img&gt;') throw Error('Unsafe external link');
if(localLink('results/../private.json', 'bad') !== '') throw Error('Unsafe local link');
if(!localLink('results/native.json', 'Original').includes('./results/native.json')) throw Error('Missing native link');
'''
        subprocess.run(['node','-e',test],check=True,capture_output=True,text=True)


if __name__ == '__main__':
    unittest.main()
