#!/usr/bin/env python3
"""Download a versioned research corpus without running any scientific code.

Only public HTTPS and Git reads are used. Payloads remain in ignored .cache/.
The catalog distinguishes downloaded bytes from unresolved annex/submodule data.
Existing catalog revisions are reused; --refresh explicitly selects new roots.
"""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tarfile
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache' / 'objects'
CATALOG = ROOT / 'data' / 'objects.json'
PRIOR_DIGESTS = {}
PAGE = 'https://computational-science.mpsd.mpg.de/docs/reproducibility.html'
SEEDS = [
 {'id':'paper-remodnav','title':'REMoDNaV research object','locator':'https://github.com/psychoinformatics-de/paper-remodnav','repository':'psychoinformatics-de/paper-remodnav','discovery_path':'User-supplied research object','scope':'Numerical results, figures and manuscript, including explicitly linked computational components.'},
 {'id':'repronim-containers','title':'ReproNim containers','locator':'https://github.com/ReproNim/containers','repository':'ReproNim/containers','discovery_path':'User-supplied research object','scope':'The versioned container collection and its retrieval/execution documentation; the entire image catalog is not assumed downloaded.'},
 {'id':'repronim-simple-workflow','title':'ReproNim simple workflow','locator':'https://github.com/ReproNim/simple_workflow','repository':'ReproNim/simple_workflow','discovery_path':'User-supplied research object','scope':'The demonstrated research workflow and its explicitly linked data, code and environments.'},
 {'id':'kayanattil-2023','title':'Rubber-like elasticity in laser-driven free surface flow of a Newtonian fluid','locator':'https://doi.org/10.1073/pnas.2301956120','doi':'10.1073/pnas.2301956120','dataset_doi':'10.17617/3.BPNGXA','dataset_version':'1.1','discovery_path':PAGE+'#experimental-study-kayanattil-et-al-2023 → publication → Data, Materials, and Software Availability → Edmond DOI','scope':'The publication and its explicitly referenced Edmond data/code record. Commercial COMSOL software is not bundled or acquired.'},
 {'id':'lang-2023','title':'Bloch points in nanostrips','locator':'https://doi.org/10.1038/s41598-023-33998-z','doi':'10.1038/s41598-023-33998-z','dataset_doi':'10.5281/zenodo.6384937','dataset_record':'6384937','repository':'lang-m/2022-paper-multiple-bloch-points','git_ref':'v1.0','discovery_path':PAGE+'#simulation-study-lang-et-al-2023 → publication reference 38 → Zenodo record → GitHub v1.0','scope':'The publication and the cited frozen Zenodo/GitHub v1.0 data/code release, not the current default branch.'},
]

def now(): return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
def write_json(path, data):
 path.parent.mkdir(parents=True, exist_ok=True)
 path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
def digest(path, algorithm='sha256'):
 h=hashlib.new(algorithm)
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024), b''):h.update(block)
 return h.hexdigest()
def request(url):return urllib.request.Request(url,headers={'User-Agent':'STAMPED-corpus-prefetch/0.1 (public research metadata; no execution)'})
def relative(path):return str(path.relative_to(ROOT))
def error_text(exc):return (type(exc).__name__+': '+str(exc)).replace(str(ROOT),'.').replace(str(Path.home()),'~')
def fetch(url,path,limit,expected=None):
 record={'url':url,'cache_path':relative(path)}
 if not expected and relative(path) in PRIOR_DIGESTS:expected=('sha256',PRIOR_DIGESTS[relative(path)])
 try:
  if path.exists() and (not expected or digest(path,expected[0]).lstrip('0')==expected[1].lower().lstrip('0')):
   record.update(status='cached',bytes=path.stat().st_size,sha256=digest(path),verified_at=now());return record
  path.parent.mkdir(parents=True,exist_ok=True)
  part=path.with_name(path.name+'.part')
  with urllib.request.urlopen(request(url),timeout=90) as response:
   length=response.headers.get('Content-Length')
   record['resolved_url']=response.url
   record['content_type']=response.headers.get('Content-Type','')
   if length and int(length)>limit:raise ValueError(f'content length {length} exceeds configured artifact bound {limit}')
   size=0
   with part.open('wb') as out:
    for block in iter(lambda:response.read(1024*1024),b''):
     size+=len(block)
     if size>limit:raise ValueError(f'payload exceeds configured artifact bound {limit}')
     out.write(block)
  if expected:
   # Dataverse MD5 values sometimes omit leading zeroes; compare numeric hex.
   actual=digest(part,expected[0])
   if actual.lstrip('0')!=expected[1].lower().lstrip('0'):raise ValueError('upstream checksum mismatch')
   record['upstream_checksum']={'algorithm':expected[0],'value':expected[1]}
  part.replace(path)
  record.update(status='downloaded',bytes=size,sha256=digest(path),retrieved_at=now())
 except Exception as exc:
  record.update(status='unavailable',error=error_text(exc))
  if 'part' in locals() and part.exists():part.unlink()
 return record

def metadata(url,path,artifacts):
 r=fetch(url,path,32*1024*1024);artifacts.append(r)
 if r['status'] not in ('cached','downloaded'):raise RuntimeError(r['error'])
 return json.loads(path.read_text())

def git_read(args,cwd=None):
 return subprocess.check_output(['git',*args],cwd=cwd,text=True,stderr=subprocess.PIPE).strip()

def git_snapshot(obj,work,artifacts,limit):
 repo=obj['repository']; url='https://github.com/'+repo+'.git'
 if not obj.get('revision'):
  ref=obj.get('git_ref','HEAD')
  lines=git_read(['ls-remote',url,ref,ref+'^{}']).splitlines()
  if not lines:raise ValueError('Git reference did not resolve')
  obj['revision']=lines[-1].split()[0]
 revision=obj['revision']
 # Partial clone retains commit/tree history and annex metadata without fetching
 # all image/data content. No checkout hooks or repository code are executed.
 gitdir=work/'repository.git'
 if not gitdir.exists():git_read(['clone','--bare','--filter=blob:none',url,str(gitdir)])
 if git_read(['cat-file','-t',revision],gitdir)!='commit':raise ValueError('Pinned Git revision is not a commit')
 obj['git_history_cache']=relative(gitdir)
 archive=work/f'{revision}.tar.gz'
 a=fetch(f'https://codeload.github.com/{repo}/tar.gz/{revision}',archive,limit);artifacts.append(a)
 if a['status'] not in ('downloaded','cached'):return
 files=[]; absent=[]
 target=work/'snapshot';target.mkdir(exist_ok=True)
 with tarfile.open(archive,'r:gz') as tar:
  members=tar.getmembers();expanded=sum(m.size for m in members if m.isfile())
  if expanded>limit*5:raise ValueError('archive expanded size exceeds bound')
  for m in members:
   rel=PurePosixPath(*PurePosixPath(m.name).parts[1:])
   if not rel.parts:continue
   if rel.is_absolute() or '..' in rel.parts:raise ValueError('unsafe archive member')
   dest=target/str(rel)
   if m.isfile():
    data=tar.extractfile(m).read();dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    files.append({'path':str(rel),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
   elif m.issym():
    # Keep pointer text, never install or follow untrusted symlinks.
    absent.append({'path':str(rel),'kind':'annex_payload' if '/annex/' in m.linkname else 'symlink_target','pointer':m.linkname,'status':'not_downloaded'})
  tree=git_read(['ls-tree','-r',revision],gitdir)
  for line in tree.splitlines():
   if line.startswith('160000 '):
    meta,path=line.split('\t',1);absent.append({'path':path,'kind':'submodule','revision':meta.split()[2],'status':'not_downloaded'})
 inventory=work/'snapshot-inventory.json'
 write_json(inventory,{'revision':revision,'files':files,'absent_payloads':absent})
 obj.update(snapshot_path=relative(target),snapshot_inventory=relative(inventory),snapshot_inventory_sha256=digest(inventory),source_files=len(files),source_bytes=sum(f['bytes'] for f in files),absent_payloads=absent)


def publication(obj,work,artifacts,limit):
 doi=obj['doi']
 cross=metadata('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='/'),work/'crossref.json',artifacts)
 epmc=metadata('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='+urllib.parse.quote('DOI:'+doi)+'&format=json',work/'europe-pmc.json',artifacts)
 hits=epmc.get('resultList',{}).get('result',[])
 pmcid=next((h.get('pmcid') for h in hits if h.get('pmcid')),None)
 if pmcid:
  obj['pmcid']=pmcid
  artifacts.append(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/'+pmcid+'/fullTextXML',work/'publication.xml',limit))
 pdf=next((x['URL'] for x in cross['message'].get('link',[]) if '.pdf' in x['URL'] or '/pdf/' in x['URL']),None)
 if pdf:
  record=fetch(pdf,work/'publication.pdf',limit)
  if record['status'] in ('cached','downloaded') and not (work/'publication.pdf').read_bytes().startswith(b'%PDF-'):
   (work/'publication.pdf').rename(work/'publication-pdf-response.html')
   record.update(status='unavailable',error='Publisher returned a non-PDF response; retained as diagnostic HTML',cache_path=relative(work/'publication-pdf-response.html'))
  artifacts.append(record)


def edmond(obj,work,artifacts,args):
 version=obj['dataset_version']; endpoint='https://edmond.mpg.de/api/datasets/:persistentId/versions/'+version+'?persistentId=doi:'+obj['dataset_doi']
 data=metadata(endpoint,work/'edmond-version.json',artifacts)['data']
 files=data['files']; total=sum(f['dataFile']['filesize'] for f in files)
 obj.update(revision='doi:'+obj['dataset_doi']+'@'+version,dataset_file_count=len(files),dataset_bytes=total)
 print(obj['id']+f': inspected {len(files)} files, {total:,} bytes',flush=True)
 inventory=[];tasks=[];remaining=args.max_total_mib*1024*1024
 # The whole announced dataset is bounded before downloading any constituent.
 # A lower user-selected total limit admits small code/docs first, then data.
 for f in sorted(files,key=lambda f:f['dataFile']['filesize']):
  df=f['dataFile'];size=df['filesize'];directory=f.get('directoryLabel','');rel=PurePosixPath(directory)/f['label']
  if rel.is_absolute() or '..' in rel.parts:raise ValueError('unsafe Dataverse file path')
  item={'id':df['id'],'path':str(rel),'bytes':size,'upstream_checksum':df.get('checksum'),'url':'https://edmond.mpg.de/api/access/datafile/'+str(df['id']),'discovery_path':obj['discovery_path']+' → dataset v'+version+' file inventory'}
  inventory.append(item)
  if size>args.max_file_mib*1024*1024 or size>remaining:item.update(status='not_downloaded',reason='configured size bound');continue
  remaining-=size
  checksum=df.get('checksum',{});expected=(checksum['type'].lower(),checksum['value']) if checksum else None
  tasks.append((item,work/'dataset'/str(rel),expected))
 def download(task):
  item,path,expected=task
  item.update(fetch(item['url'],path,args.max_file_mib*1024*1024,expected));return item
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
  for i,item in enumerate(pool.map(download,tasks),1):
   if i%100==0:print(obj['id']+f': cached {i}/{len(tasks)} files',flush=True)
 inventory_path=work/'dataset-inventory.json';write_json(inventory_path,inventory)
 obj.update(dataset_inventory=relative(inventory_path),dataset_inventory_sha256=digest(inventory_path),dataset_downloaded_files=sum(f.get('status') in ('cached','downloaded') for f in inventory),dataset_downloaded_bytes=sum(f['bytes'] for f in inventory if f.get('status') in ('cached','downloaded')),dataset_unavailable=[{'path':f['path'],'status':f.get('status'),'reason':f.get('reason',f.get('error'))} for f in inventory if f.get('status') not in ('cached','downloaded')])


def zenodo(obj,work,artifacts,args):
 data=metadata('https://zenodo.org/api/records/'+obj['dataset_record'],work/'zenodo-record.json',artifacts)
 for f in data['files']:
  algorithm,value=f['checksum'].split(':',1);path=work/'zenodo'/Path(f['key']).name
  print(obj['id']+f": inspected {f['key']}, {f['size']:,} bytes",flush=True)
  if f['size']>args.max_file_mib*1024*1024:artifacts.append({'url':f['links']['self'],'status':'not_downloaded','bytes':f['size'],'reason':'configured artifact size bound'});continue
  artifacts.append(fetch(f['links']['self'],path,args.max_file_mib*1024*1024,(algorithm,value)))


def prefetch_remodnav_evidence():
 import concurrent.futures,configparser,hashlib,json,subprocess,urllib.request,re,tarfile
 from pathlib import Path, PurePosixPath
 from datetime import datetime,timezone
 ROOT=Path(__file__).resolve().parents[1]
 BASE=ROOT/'.cache/objects/paper-remodnav/evidence';BASE.mkdir(parents=True,exist_ok=True)
 START=('psychoinformatics-de/paper-remodnav','34388d3ca78fbd483e022e4e2851be390b7eebf2','root',[])
 queue=[START];nodes=[];seen={};edges=[]
 def run(args,cwd=None):return subprocess.check_output(['git',*args],cwd=cwd,text=True,stderr=subprocess.PIPE).strip()
 def save(p,b):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);return {'cache_path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
 def jsonsave(p,v):return save(p,(json.dumps(v,indent=2)+'\n').encode())
 def textlike(path):
  p=Path(path);return p.suffix.lower() in {'.md','.rst','.txt','.py','.sh','.bash','.json','.yaml','.yml','.toml','.ini','.cfg','.tex','.bib','.ipynb','.m','.r','.csv','.tsv','.xml','.submit','.j2'} or p.name.lower().startswith(('readme','license','copying','makefile','dockerfile','contributing')) or p.name in {'.gitmodules','.gitattributes','.gitignore','config','Docker-Makefile'}
 while queue:
  repo,rev,via,parents=queue.pop(0);key=repo+'@'+rev
  if key in seen:continue
  nodeid=repo.replace('/','--')+'--'+rev[:12];seen[key]=nodeid
  dst=BASE/nodeid;dst.mkdir(exist_ok=True);gitdir=dst/'repository.git'
  if not gitdir.exists():run(['clone','--bare','--filter=blob:none','https://github.com/'+repo+'.git',str(gitdir)])
  assert run(['cat-file','-t',rev],gitdir)=='commit'
  lines=run(['ls-tree','-r',rev],gitdir).splitlines();files=[];absent=[];submodules=[]
  preloaded={};pointers={}
  if repo!='richardandersson/EyeMovementDetectorEvaluation':
   archive=dst/'metadata-source.tar.gz'
   if not archive.exists():
    with urllib.request.urlopen('https://codeload.github.com/'+repo+'/tar.gz/'+rev,timeout=90) as response:
     body=response.read(64*1024*1024+1)
    if len(body)>64*1024*1024:raise RuntimeError('Metadata archive exceeds 64 MiB bound')
    archive.write_bytes(body)
   with tarfile.open(archive,'r:gz') as tar:
    for member in tar:
     path='/'.join(member.name.split('/')[1:])
     if member.issym():pointers[path]=member.linkname
     elif member.isfile() and textlike(path) and member.size<=5*1024*1024:preloaded[path]=tar.extractfile(member).read()
 
  # Serial Git fetches avoid conflicting partial-clone writes; inspect only
  # bounded source/text classes, never execute any fetched content.
  for line in lines:
   meta,path=line.split('\t',1);mode,typ,oid=meta.split();item={'path':path,'git_oid':oid,'mode':mode}
   if PurePosixPath(path).is_absolute() or '..' in PurePosixPath(path).parts:raise ValueError('unsafe Git tree path')
   if mode=='160000':submodules.append(item);continue
   if mode=='120000':
    pointer=pointers.get(path) or run(['show',rev+':'+path],gitdir);item.update(kind='annex_payload' if '/annex/' in pointer else 'symlink_target',pointer=pointer,status='not_downloaded');absent.append(item);continue
   if not textlike(path):item.update(kind='binary_or_other_payload',status='not_downloaded');absent.append(item);continue
   size=len(preloaded[path]) if path in preloaded else int(run(['cat-file','-s',oid],gitdir))
   if size>5*1024*1024:item.update(kind='large_text_payload',bytes=size,status='not_downloaded');absent.append(item);continue
   content=preloaded[path] if path in preloaded else subprocess.check_output(['git','show',rev+':'+path],cwd=gitdir,stderr=subprocess.PIPE)
   item.update(save(dst/'source'/path,content));item['status']='downloaded';files.append(item)
  history=subprocess.check_output(['git','log',rev,'--format=commit %H%nAuthor: %an%nAuthorDate: %aI%nCommitDate: %cI%n%B'],cwd=gitdir)
  h=save(dst/'history.txt',history)
  mods={}
  gm=dst/'source/.gitmodules'
  if gm.exists():
   cp=configparser.ConfigParser(interpolation=None);cp.read(gm)
   for section in cp.sections():
    if cp.has_option(section,'path') and cp.has_option(section,'url'):mods[cp.get(section,'path')]=cp.get(section,'url')
  for sub in submodules:
   url=mods.get(sub['path']);match=re.match(r'https://github.com/([^/]+/[^/]+?)(?:\.git)?$',url or '')
   edge={'parent':nodeid,'path':sub['path'],'revision':sub['git_oid'],'url':url,'discovery_path':parents+[via,'.gitmodules:'+sub['path']]}
   if match:
    childrepo=match.group(1);edge['child_key']=childrepo+'@'+sub['git_oid'];queue.append((childrepo,sub['git_oid'],sub['path'],parents+[via]))
   else:edge['status']='unresolved_module_url'
   edges.append(edge)
  n={'id':nodeid,'repository':'https://github.com/'+repo,'revision':rev,'source_path':str((dst/'source').relative_to(ROOT)),'history':h,'git_history_cache':str(gitdir.relative_to(ROOT)),'files':files,'absent_payloads':absent,'discovery_path':parents+[via]}
  nodes.append(n);jsonsave(dst/'inventory.json',n)
  print(nodeid,len(files),'source files;',len(absent),'payloads absent',flush=True)
  if len(nodes)>20:raise RuntimeError('Unexpected recursive corpus breadth')
 for edge in edges:
  if 'child_key' in edge:edge['child']=seen.get(edge.pop('child_key'));edge['status']='source_metadata_downloaded'
 # Explicitly linked execution adapter, version named in entry README.
 u='https://raw.githubusercontent.com/datalad/datalad-container/1.2.3/datalad_container/adapters/docker.py'
 b=urllib.request.urlopen(u,timeout=45).read();external=save(BASE/'external/datalad-container-1.2.3-docker.py',b)
 external.update(url='https://github.com/datalad/datalad-container/blob/1.2.3/datalad_container/adapters/docker.py',discovery_path=['root README.md','DataLad Containers project/version 1.2.3','.datalad/config adapter invocation','datalad_container/adapters/docker.py'])
 # Root auxiliary annex metadata are separately versioned, never misrepresented
 # as fixed by the research object's main branch revision.
 rootgit=BASE/nodes[0]['id']/'repository.git';branches=run(['for-each-ref','--format=%(refname)','refs/heads/git-annex'],rootgit)
 aux=[]
 if branches:
  arev=run(['rev-parse','refs/heads/git-annex'],rootgit)
  for line in run(['ls-tree','-r',arev],rootgit).splitlines():
   meta,path=line.split('\t',1)
   if path.endswith('.web'):
    b=subprocess.check_output(['git','show',arev+':'+path],cwd=rootgit,stderr=subprocess.PIPE);a=save(BASE/'annex-metadata'/path,b);a.update(path=path,revision=arev,discovery_path=['root annex pointer','repository git-annex availability metadata']);aux.append(a)
 manifest={'version':'0.1.0','created_at':datetime.now(timezone.utc).isoformat(),'object_id':'paper-remodnav','locator':'https://github.com/psychoinformatics-de/paper-remodnav','revision':START[1],'evidence_root':str(BASE.relative_to(ROOT)),'root_node':nodes[0]['id'],'nodes':nodes,'discovery_graph':edges,'external_sources':[external],'auxiliary_availability_metadata':aux,'limitations':['No prior assessment, rubric answers or scores are included.','No scientific code was executed.','This package freezes inspected source/text metadata and Git histories. Binary payloads, annex data and container layers are explicitly absent.','Partial bare clones can fetch omitted Git blobs on demand. Use downloaded source files/history/inventories for a network-independent review.','External software adapter is reachable through the README tool/version reference; it is not a bundled component.']}
 jsonsave(BASE/'evidence.json',manifest);jsonsave(ROOT/'data/remodnav-evidence.json',manifest)
 print('COMPLETE',len(nodes),'nodes',sum(len(n['files']) for n in nodes),'source files',flush=True)

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--remodnav-evidence', action='store_true', help='freeze recursively linked REMoDNaV source metadata and histories without assessment outputs')
 p.add_argument('--only',action='append',choices=[s['id'] for s in SEEDS]);p.add_argument('--refresh',action='store_true',help='resolve new Git root revisions instead of reusing existing catalog pins; DOI dataset versions remain explicit')
 p.add_argument('--max-file-mib',type=int,default=512);p.add_argument('--max-total-mib',type=int,default=3072,help='Dataverse dataset payload bound; sizes inspected before download')
 p.add_argument('--workers',type=int,default=8);args=p.parse_args()
 if args.remodnav_evidence:
  prefetch_remodnav_evidence();return 0
 if min(args.max_file_mib,args.max_total_mib,args.workers)<1:p.error('size limits and workers must be positive')
 previous=json.loads(CATALOG.read_text()) if CATALOG.exists() else {'objects':[]}
 prior={o['id']:o for o in previous['objects']};objects=[]
 for o in previous['objects']:
  for a in o.get('artifacts',[]):
   if a.get('cache_path') and a.get('sha256') and a.get('status') in ('cached','downloaded'):PRIOR_DIGESTS[a['cache_path']]=a['sha256']
 page=fetch(PAGE,CACHE/'discovery'/'mpsd-reproducibility.html',10*1024*1024)
 for seed in SEEDS:
  if args.only and seed['id'] not in args.only:
   if seed['id'] in prior:objects.append(prior[seed['id']])
   continue
  obj=dict(seed);work=CACHE/obj['id'];work.mkdir(parents=True,exist_ok=True);artifacts=[]
  if not args.refresh and obj['id'] in prior and prior[obj['id']].get('repository'):obj['revision']=prior[obj['id']].get('revision')
  try:
   if obj.get('repository'):git_snapshot(obj,work,artifacts,args.max_file_mib*1024*1024)
   if obj.get('doi'):publication(obj,work,artifacts,args.max_file_mib*1024*1024)
   if obj['id']=='kayanattil-2023':edmond(obj,work,artifacts,args)
   if obj['id']=='lang-2023':zenodo(obj,work,artifacts,args)
  except Exception as exc:obj['prefetch_error']=error_text(exc)
  obj['artifacts']=artifacts;obj['prefetched_at']=now()
  has_missing=bool(obj.get('absent_payloads') or obj.get('dataset_unavailable') or obj.get('prefetch_error') or any(a['status'] not in ('cached','downloaded') for a in artifacts))
  obj['cache_status']='partial' if has_missing else 'selected_sources_downloaded'
  obj['assessment_status']='not_assessed'
  obj['cache_note']='Cache availability does not establish discoverability from the assessment entry point. No scientific code was executed. Unfetched annex payloads and submodules are explicit; other runtime URLs/dependencies have not been exhaustively downloaded.'
  write_json(work/'manifest.json',obj);objects.append(obj)
  write_json(CATALOG,{'version':'0.1.0','generated_at':now(),'discovery_page':page,'objects':objects+[v for k,v in prior.items() if k not in {o['id'] for o in objects}]})
  print(obj['id']+': '+obj['cache_status'],flush=True)
 write_json(CATALOG,{'version':'0.1.0','generated_at':now(),'discovery_page':page,'objects':objects})
 print('Catalog:',relative(CATALOG))
 return int(any(o.get('prefetch_error') for o in objects))

if __name__=='__main__':sys.exit(main())
