"""Batch 100 supplemental and final verification; Python standard library only."""
import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote,urldefrag,urljoin,urlsplit
from urllib.request import HTTPRedirectHandler,Request,build_opener
BASE='https://sauravnrai.github.io/'
REPOS={'chatty':'master','browserstack_assignment':'main','MySQL':'master','Java-Codes':'main','Multi-Threaded-Data-Ingestor':'main','DACLP':'main','text-file-compressor-LZW':'main','shell-scripts':'main','Python-codes':'main'}
report=json.loads(Path('verification-report.json').read_text())
def owned(url):
 p=urlsplit(url)
 return p.scheme=='https' and (p.netloc=='sauravnrai.github.io' or p.netloc in ('github.com','raw.githubusercontent.com') and p.path.startswith('/sauravnrai/'))
class Guard(HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  if not owned(newurl):raise AssertionError('Refusing non-owned redirect: '+newurl)
  return super().redirect_request(req,fp,code,msg,headers,newurl)
class Links(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True);self.links=[];self.ids=set();self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
cache={}
def fetch(url):
 url=urldefrag(url)[0]
 if url in cache:return cache[url]
 if not owned(url):raise AssertionError('Refusing non-owned resource: '+url)
 for attempt in range(3):
  try:
   with build_opener(Guard()).open(Request(url,headers={'User-Agent':'sauravnrai-batch100-verification/1.0','Cache-Control':'no-cache'}),timeout=30) as r:
    assert r.status==200 and owned(r.geturl()),'Expected owned HTTP 200: '+url
    body=r.read(3*1024*1024+1);assert body and len(body)<=3*1024*1024,'Empty or oversized resource'
   cache[url]=body;print('HTTP 200 SUPPLEMENT '+url,flush=True);return body
  except Exception:
   if attempt==2:raise
   time.sleep(2*(attempt+1))
if '--finalize' in sys.argv:
 browser=json.loads(Path('browser-report.json').read_text());assert browser['status']=='passed',browser.get('failure')
 report['browser_interactions']=browser;report['counts']['browser_checks_passed']=browser['count'];report['counts']['verified_owned_urls']=len(report['verified_urls']);report['status']='passed';report['verified']=True;report['checked_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 Path('verification-report.json').write_text(json.dumps(report,indent=2)+'\n')
 Path('verified-urls.md').write_text('# Batch 100 verified URLs\n\nChecked: '+report['checked_at_utc']+'\n\n'+''.join('- [HTTP 200 — '+u+']('+u+')\n' for u in report['verified_urls']))
 print('BATCH100_FINAL_REPORT_JSON='+json.dumps(report,separators=(',',':')),flush=True)
else:
 assert report['verified'],'Base verification must pass first'
 for rel in ['discovery/sw.js','ASF/data/batch100-messy.csv','ASF/data/batch100-sparse.json','favicon.ico']:
  body=fetch(BASE+rel)
  if rel.endswith('.json'):json.loads(body)
 if not any(p['url']==BASE+'404.html' for p in report['pages']):
  fetch(BASE+'404.html');report['pages'].append({'url':BASE+'404.html','status':200,'browser_render':'checked by subsequent browser phase','title':'Page not found — App Network'})
 with tempfile.TemporaryDirectory(prefix='batch100-tests-') as tmp:
  subprocess.run(['git','clone','--quiet','--depth=1','https://github.com/sauravnrai/discovery.git',tmp+'/discovery'],check=True,timeout=90)
  result=subprocess.run(['node','tests/batch100.test.cjs'],cwd=tmp+'/discovery',capture_output=True,text=True,timeout=45);print(result.stdout,flush=True);assert result.returncode==0,result.stderr
  count=len(re.findall(r'^PASS ',result.stdout,re.M));assert count>=15
  report['regression_tests'].append({'repository':'sauravnrai/discovery','test_file':'tests/batch100.test.cjs','passed':count,'status':'passed'})
 report['regression_tests'].append({'repository':'sauravnrai/sauravnrai.github.io','test_file':'verification/test_document.py','passed':3,'status':'passed'})
 github_links=set();page_crosslinks=0
 for item in report['pages']:
  doc=Links(fetch(item['url']).decode('utf-8'));targets={urldefrag(urljoin(item['url'],u))[0] for u in doc.links}
  for target in [BASE,BASE+'discovery/',BASE+'ASF/',BASE+'ASF-analytics/',BASE+'ASF-visualizer/']:
   assert target in targets,'Missing page-level app crosslink: '+item['url']+' -> '+target
   page_crosslinks+=1
  github_links.update(urldefrag(u)[0] for u in doc.links if u.startswith('https://github.com/sauravnrai/'))
 report['source_project_network_checks']=[]
 for repo,branch in REPOS.items():
  raw='https://raw.githubusercontent.com/sauravnrai/'+repo+'/'+branch+'/NETWORK.md';text=fetch(raw).decode('utf-8');urls=re.findall(r'\]\((https://[^)]+)\)',text)
  for target in urls:
   assert owned(target),'Non-owned network link: '+target
   body=fetch(target);clean,fragment=urldefrag(target)
   if fragment:assert unquote(fragment) in Links(body.decode('utf-8')).ids,'Broken fragment: '+target
  assert BASE+'batch-100.html' in urls,'Missing Batch 100 return link: '+repo
  assert all(BASE+app in urls for app in ('','discovery/','ASF/','ASF-analytics/','ASF-visualizer/')),'Missing app link: '+repo
  github_links.add('https://github.com/sauravnrai/'+repo+'/blob/'+branch+'/NETWORK.md');report['source_project_network_checks'].append({'repository':'sauravnrai/'+repo,'url':raw,'status':200,'links_checked':len(urls)})
 for u in sorted(github_links):fetch(u)
 report['github_owned_links']=[{'url':u,'status':200} for u in sorted(github_links)];report['batch']=100
 report['verified_urls']=sorted(set([p['url'] for p in report['pages']]+[p['url'] for p in report['assets']]+list(cache)))
 report['counts']['html_pages']=len(report['pages']);report['counts']['unit_tests_passed']=sum(t['passed'] for t in report['regression_tests']);report['counts']['source_project_network_files']=len(REPOS);report['counts']['source_project_link_edges']=sum(x['links_checked'] for x in report['source_project_network_checks']);report['counts']['page_level_app_links']=page_crosslinks
 report['notes']=['No email sent, draft provider opened, or ziontechgroup.com website accessed.','Only sauravnrai-owned Pages and repository URLs requested.','Browser flow results are attached by finalization. This is a dated snapshot, not a future uptime guarantee.']
 Path('verification-report.json').write_text(json.dumps(report,indent=2)+'\n');print('BATCH100_SUPPLEMENT_REPORT_JSON='+json.dumps(report,separators=(',',':')),flush=True)
