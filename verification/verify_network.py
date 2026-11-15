"""Read-only public-site checks. Python stdlib, installed Chrome, Node and Git only."""
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import deque
from html.parser import HTMLParser
from urllib.parse import unquote, urldefrag, urljoin, urlsplit
from urllib.request import Request, urlopen

BASE = 'https://sauravnrai.github.io/'
SITES = [BASE, BASE + 'discovery/', BASE + 'ASF/', BASE + 'ASF-analytics/', BASE + 'ASF-visualizer/']
SEEDS = SITES + [BASE + 'projects.html'] + [BASE + r + '/guide.html' for r in ['ASF', 'ASF-analytics', 'ASF-visualizer']]
RUN_URL = os.environ.get('GITHUB_SERVER_URL', 'https://github.com') + '/' + os.environ.get('GITHUB_REPOSITORY', 'sauravnrai/sauravnrai.github.io') + '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', 'local')
report = {'status': 'running', 'verified': False, 'run_url': RUN_URL, 'verification_commit': os.environ.get('GITHUB_SHA'), 'scope': SITES, 'pages': [], 'assets': [], 'cross_app_links': [], 'regression_tests': [], 'failures': [], 'notes': ['No email was sent or draft provider contacted.', 'Browser checks cover rendered navigation; scoring and draft construction are covered by existing unit tests, not a full accessibility or manual email-client certification.']}
cache = {}
asset_urls = set()

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.assets, self.ids = [], [], set()
        self.in_title = False
        self.in_head = False
        self.title = ''
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if tag == 'a' and a.get('name'): self.ids.add(a['name'])
        if tag == 'head': self.in_head = True
        if tag == 'title': self.in_title = self.in_head
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ['script', 'img', 'iframe', 'audio', 'video', 'source'] and a.get('src'): self.assets.append(a['src'])
        if tag == 'link' and a.get('href') and set(a.get('rel', '').lower().split()) & {'stylesheet', 'icon', 'manifest', 'preload', 'modulepreload'}: self.assets.append(a['href'])
    def handle_endtag(self, tag):
        if tag == 'head': self.in_head = False
        if tag == 'title': self.in_title = False
    def handle_data(self, text):
        if self.in_title: self.title += text

def local(url):
    p = urlsplit(url)
    return p.scheme == 'https' and p.netloc == 'sauravnrai.github.io'

def fetch(url):
    url = urldefrag(url)[0]
    if url in cache: return cache[url]
    if not local(url): raise AssertionError('Unexpected runtime dependency: ' + url)
    error = None
    for attempt in range(4):
        try:
            req = Request(url, headers={'User-Agent': 'sauravnrai-app-network-verifier/1.0', 'Cache-Control': 'no-cache'})
            with urlopen(req, timeout=25) as response:
                status, final_url = response.status, response.geturl()
                data = response.read(3 * 1024 * 1024 + 1)
                kind = response.headers.get('Content-Type', '')
            if status != 200 or not local(final_url): raise AssertionError('Expected same-origin HTTP 200: ' + url)
            if not data or len(data) > 3 * 1024 * 1024: raise AssertionError('Empty or unexpectedly large resource: ' + url)
            result = {'url': url, 'status': status, 'final_url': final_url, 'content_type': kind, 'body': data}
            cache[url] = result
            print('HTTP 200 ' + url, flush=True)
            return result
        except Exception as exc:
            error = exc
            if attempt < 3: time.sleep(2 * (attempt + 1))
    raise AssertionError('HTTP check failed for ' + url + ': ' + str(error))

def is_html(resource):
    return 'text/html' in resource['content_type'].lower()

def browser_document(url, source):
    chrome = next((shutil.which(c) for c in ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser'] if shutil.which(c)), None)
    if not chrome: raise AssertionError('A preinstalled Chrome/Chromium is required; no packages will be downloaded.')
    with tempfile.TemporaryDirectory(prefix='network-browser-') as profile:
        command = [chrome, '--headless=new', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--disable-background-networking', '--disable-component-update', '--disable-sync', '--no-first-run', '--no-default-browser-check', '--user-data-dir=' + profile, '--virtual-time-budget=1500', '--timeout=20000', '--dump-dom', url]
        result = subprocess.run(command, capture_output=True, text=True, timeout=40)
    if result.returncode or '<html' not in result.stdout.lower(): raise AssertionError('Browser rendering failed: ' + url + '\n' + result.stderr[-1200:])
    doc = Document(result.stdout)
    if doc.title.strip() != source.title.strip(): raise AssertionError('Browser did not render the expected page: ' + url + '; expected=' + repr(source.title.strip()) + '; actual=' + repr(doc.title.strip()))
    print('BROWSER RENDER PASS ' + url, flush=True)
    return doc

def check_asset(url):
    url = urldefrag(url)[0]
    if url in asset_urls: return
    item = fetch(url)
    if is_html(item): raise AssertionError('An asset unexpectedly returned HTML: ' + url)
    asset_urls.add(url)
    if urlsplit(url).path.endswith('.json'): json.loads(item['body'])
    if urlsplit(url).path.endswith('.css'):
        text = item['body'].decode('utf-8')
        refs = [m.group(2) for m in re.finditer(r'url\(\s*([\x22\x27]?)(.*?)\1\s*\)', text, re.I)]
        refs += re.findall(r'@import\s+[\x22\x27]([^\x22\x27]+)', text, re.I)
        for ref in refs:
            if ref and not ref.startswith(('data:', '#')): check_asset(urljoin(url, ref))

def regressions():
    node = shutil.which('node')
    if not node: raise AssertionError('Preinstalled Node is required.')
    for repo, testfile in [('ASF', 'tests/data.test.cjs'), ('discovery', 'tests/discovery.test.cjs')]:
        with tempfile.TemporaryDirectory(prefix='network-tests-') as directory:
            path = Path(directory) / repo
            subprocess.run(['git', 'clone', '--quiet', '--depth=1', 'https://github.com/sauravnrai/' + repo + '.git', str(path)], check=True, timeout=90)
            sha = subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True).strip()
            result = subprocess.run([node, testfile], cwd=path, capture_output=True, text=True, timeout=45)
            print(result.stdout, flush=True)
            if result.returncode: raise AssertionError(repo + ' unit tests failed: ' + result.stderr)
            count = len(re.findall(r'^PASS ', result.stdout, re.M))
            if not count: raise AssertionError(repo + ' produced no passing test assertions.')
            report['regression_tests'].append({'repository': 'sauravnrai/' + repo, 'commit': sha, 'passed': count, 'status': 'passed'})

def verify():
    regressions()
    pending, documents, edges = deque(SEEDS), {}, set()
    while pending:
        url = urldefrag(pending.popleft())[0]
        if url in documents: continue
        if len(documents) >= 100: raise AssertionError('Crawl safety limit reached; results are incomplete.')
        item = fetch(url)
        if not is_html(item): raise AssertionError('Expected an HTML page: ' + url)
        source = Document(item['body'].decode('utf-8'))
        doc = browser_document(url, source)
        documents[url] = doc
        report['pages'].append({'url': url, 'status': 200, 'browser_render': 'passed', 'title': doc.title.strip()})
        for ref in set(source.assets + doc.assets):
            if not ref.startswith(('data:', 'blob:', '#')): check_asset(urljoin(url, ref))
        for href in set(source.links + doc.links):
            if href.startswith('javascript:'): raise AssertionError('Unexpected JavaScript navigation URL: ' + url)
            target = urljoin(url, href)
            if not local(target): continue
            clean, fragment = urldefrag(target)
            edges.add((url, target))
            resource = fetch(clean)
            if is_html(resource):
                if clean not in documents: pending.append(clean)
            else:
                if fragment: raise AssertionError('Unverified fragment on a non-HTML resource: ' + target)
                asset_urls.add(clean)
    for source, target in sorted(edges):
        clean, fragment = urldefrag(target)
        if fragment and unquote(fragment) not in documents[clean].ids: raise AssertionError('Broken fragment link: ' + source + ' -> ' + target)
    for source in SITES:
        links = {urldefrag(urljoin(source, href))[0] for href in documents[source].links}
        for target in SITES:
            if source == target: continue
            if target not in links: raise AssertionError('Missing browser-rendered cross-app link: ' + source + ' -> ' + target)
            report['cross_app_links'].append({'from': source, 'to': target, 'status': 200})
    report['assets'] = [{'url': url, 'status': cache[url]['status'], 'content_type': cache[url]['content_type']} for url in sorted(asset_urls)]
    report['counts'] = {'sites': len(SITES), 'html_pages': len(documents), 'assets_and_supporting_resources': len(asset_urls), 'same_origin_link_edges': len(edges), 'directed_cross_app_links': len(report['cross_app_links']), 'http_200_resources': len(cache), 'unit_tests_passed': sum(t['passed'] for t in report['regression_tests'])}

try:
    verify()
    report['status'], report['verified'] = 'passed', True
except Exception as exc:
    report['status'] = 'failed'
    report['failures'].append(str(exc))
report['checked_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
Path('verification-report.json').write_text(json.dumps(report, indent=2) + '\n')
print('VERIFICATION_REPORT_JSON=' + json.dumps(report, separators=(',', ':')), flush=True)
summary = os.environ.get('GITHUB_STEP_SUMMARY')
if summary:
    lines = ['# App Network verification: ' + report['status'].upper(), '', 'Checked: ' + report['checked_at_utc'], '', '| Page | HTTP | Browser render |', '| --- | --- | --- |']
    lines += ['| [' + p['url'] + '](' + p['url'] + ') | 200 | Passed |' for p in report['pages']]
    lines += ['', 'Counts: `' + json.dumps(report.get('counts', {})) + '`', '', 'Failures: ' + ('; '.join(report['failures']) or 'None'), '', '```json', json.dumps(report, indent=2), '```']
    with open(summary, 'a') as output: output.write('\n'.join(lines) + '\n')
if not report['verified']: sys.exit(1)
