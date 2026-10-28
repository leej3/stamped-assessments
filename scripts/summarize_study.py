"""Descriptive within-method summaries; never convert native scales or grade truth."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json, statistics
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads(p.read_text())
def write(path,value):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n');tmp.replace(path)
def spread(values):
 return {'n':len(values),'mean':statistics.mean(values) if values else None,'sample_sd':statistics.stdev(values) if len(values)>1 else None,'minimum':min(values) if values else None,'maximum':max(values) if values else None}
def summarize():
 study=load(ROOT/'data/study.json')
 assessments=[]
 for p in (ROOT/'results').glob('study-*.json'):
  if any(t in p.name for t in ('.bundle.','.responses.','.probes.')):continue
  rec=load(p)
  if rec.get('study_id')==study['id']:assessments.append(rec)
 reviews=[]
 ids={a['id'] for a in assessments}
 for p in (ROOT/'reviews').glob('study-*.json'):
  receipt=ROOT/'.cache/study/receipts'/p.name
  if receipt.exists() and load(receipt).get('status') not in ('complete','failed'):continue
  rec=load(p)
  if rec.get('assessment_id') in ids:reviews.append(rec)
 out={'study_id':study['id'],'updated_at':datetime.now(timezone.utc).isoformat(),'assessment_status_counts':dict(Counter(a['status'] for a in assessments)),'review_status_counts':dict(Counter(r['status'] for r in reviews)),'planned_assessments':30,'planned_reviews':90,'methods':[],'interpretation':'Descriptive single-object pilot; requested models retained, actual underlying versions unverified. Review agreement is not a correctness reference. Native scales are not pooled.'}
 for mid in study['methods']:
  runs=[a for a in assessments if a['method_id']==mid];good=[a for a in runs if a['status']=='complete'];runids={a['id'] for a in runs};rr=[r for r in reviews if r['assessment_id'] in runids]
  row={'method_id':mid,'assessment_count':len(runs),'complete':len(good),'failed':len(runs)-len(good),'review_count':len(rr),'review_verdict_counts':dict(Counter(r['verdict'] for r in rr if r['status']=='complete')),'criteria':{},'replicates':[a['id'] for a in runs]}
  distributions=defaultdict(Counter)
  for a in good:
   native=load(ROOT/a['native_output']);responses=native['assessments'][0]['responses'] if mid=='rubric' else native['responses']
   for cid,value in responses.items():
    answer=value.get('score') if mid=='rubric' else value.get('status');distributions[cid]['unanswered' if answer is None else str(answer)]+=1
  row['criteria']={c:dict(v) for c,v in sorted(distributions.items())}
  if mid=='rubric':
   row['overall_scores']=spread([a['summary']['overall_score'] for a in good]);row['dimensions']={d:spread([a['summary']['dimension_scores'][d] for a in good]) for d in 'STAMPED'};row['answered_counts']=spread([a['summary']['completion']['answered'] for a in good])
  else:
   row['native_level_counts']={l:{s:spread([a['summary']['checklist_counts'][l][s] for a in good]) for s in ['met','partial','unmet','not-checked','not-applicable']} for l in ['must','should','may']}
  by_assessment=defaultdict(list)
  for r in rr:
   if r['status']=='complete':by_assessment[r['assessment_id']].append(r)
  complete_triples=[r for r in by_assessment.values() if len(r)==3]
  row['three_review_sets']={'complete_sets':len(complete_triples),'matching_overall_verdict_sets':sum(len({r['verdict'] for r in rs})==1 for rs in complete_triples),'interpretation':'Matching review verdicts do not establish factual correctness or human agreement.'}
  row['review_dispositions']=dict(Counter(f['disposition'] for r in rr if r['status']=='complete' for f in r.get('findings',[])))
  criterion_reviews={}
  completed_reviews=[r for r in rr if r['status']=='complete']
  for cid in sorted(distributions):
   checked=[r for r in completed_reviews if cid in r.get('checked_criteria',[])]
   dispositions=Counter();duplicates=[];missing=[]
   for r in checked:
    findings=[f for f in r.get('findings',[]) if f.get('criterion_id')==cid]
    if not findings:missing.append(r['id'])
    if len(findings)>1:duplicates.append(r['id'])
    # Count a review once per disposition, retaining conflicting dispositions visibly.
    dispositions.update({f['disposition'] for f in findings})
   criterion_reviews[cid]={'completed_review_denominator':len(completed_reviews),'checked_review_denominator':len(checked),'distinct_review_dispositions':{d:dispositions[d] for d in ('agree','disagree','needs_evidence')},'multiple_finding_review_ids':duplicates,'checked_without_finding_review_ids':missing}
  row['criterion_reviews']=criterion_reviews
  row['criterion_review_counting']='Each review counted once per disposition for each criterion. A review with conflicting multiple findings can contribute to more than one disposition; flagged IDs preserve that distinction. Denominators are completed reviews and reviews reporting the criterion checked; not correctness or consensus.'
  row['review_coverage']=[{'review_id':r['id'],**r.get('review_coverage',{'checked':len(r.get('checked_criteria',[])),'total':36 if mid=='rubric' else 31})} for r in rr]
  out['methods'].append(row)
 write(ROOT/'data/study-analysis.json',out)
 done=out['assessment_status_counts'].get('complete',0);reviewdone=out['review_status_counts'].get('complete',0)
 lines=['# REMoDNaV assessment-method pilot: descriptive results','',f'Updated {out["updated_at"]}. {done}/30 assessments and {reviewdone}/90 reviews are complete. Failed attempts remain in the ledger.','',
 'This is one research object at one fixed source revision, planned for ten independent assessments per method with fresh contexts. It is not ten different research objects. The exploratory worked example is excluded. Requested assessor model is `gpt-6.1-sol` with medium reasoning; requested reviewer model is `gpt-6-astra` with high reasoning. Actual underlying model versions were not independently exposed.','',
 'The shared cohort permits source inspection, not scientific workflow execution or independent annex-payload retrieval. Each native report preserves its own missingness and evidence judgments. These findings have not been adjudicated by human experts.','',
 '| Method | Completed assessments | Failed assessments | Reviews | Review verdicts |','| --- | ---: | ---: | ---: | --- |']
 for m in out['methods']:lines.append(f'| {m["method_id"]} | {m["complete"]} | {m["failed"]} | {m["review_count"]} | {", ".join(f"{k}: {v}" for k,v in m["review_verdict_counts"].items()) or "None yet"} |')
 lines+=['','## Native results','']
 for m in out['methods']:
  lines.append(f'### {m["method_id"]}');lines.append('')
  if m['method_id']=='rubric':
   st=m['overall_scores']
   if st['n']:lines.append(f'Native overall scores: n={st["n"]}, mean {st["mean"]:.2f}, range {st["minimum"]:.2f}–{st["maximum"]:.2f}. Sample standard deviation: '+(f'{st["sample_sd"]:.2f}.' if st['sample_sd'] is not None else 'not estimated with one run.'))
   else:lines.append('No completed numeric assessments yet.')
   lines.append('Unanswered criteria contribute zero to these provisional native totals and remain visible in completion counts. Evidence ratings and confidence do not alter scores.')
  else:lines.append('Native results are categorical checklist verdicts. No overall numeric score is created. Per-item verdict distributions and separate MUST/SHOULD/MAY counts are retained in the analysis JSON and dashboard.')
  t=m['three_review_sets'];lines.append(f'{t["complete_sets"]} assessments have all three reviews; {t["matching_overall_verdict_sets"]} of those sets share an overall review verdict. This is descriptive agreement, not accuracy.');lines.append('')
 lines+=['## Criterion review patterns','', 'Per-criterion distinct-review counts for agree, disagree and needs_evidence are in `criterion_reviews` in the analysis JSON. Each criterion records both completed-review and checked-review denominators. Multiple findings from one review count once per disposition; conflicting dispositions and checked criteria without findings are explicitly flagged. These counts identify recurring questions, not a consensus or correctness score.','', '## Interpretation limits','',
 'Different methods ask different questions and apply different evidence thresholds. The rubric includes manuscript-derived licensing and other criteria absent from the pinned checklist; checklist methods preserve unknown and not-applicable categories rather than the rubric’s numeric fixed denominator. Their totals must not be pooled or ranked.','',
 'Three independent review contexts use the same requested model family and can share systematic errors. They do not represent three human experts or three independent assessor replications. Partial review coverage is explicitly retained. Agreement alone cannot validate the assessment.','',
 'No controlled random seed, causal method benefit, general scientific-quality ranking, or execution reproducibility is claimed. Wall time and compute cost were not consistently measured at the individual assessment-activity level and are not inferred from preparation timestamps.','',
 'Machine-readable detail: [study-analysis.json](../data/study-analysis.json). Native outputs and all review records remain separate and unchanged. See [protocol](protocol.md) and [method comparison](method-comparison.md) for source identities and design.','']
 (ROOT/'docs/study-results.md').write_text('\n'.join(lines))
 print(json.dumps({'complete_assessments':done,'complete_reviews':reviewdone}))
if __name__=='__main__':summarize()
