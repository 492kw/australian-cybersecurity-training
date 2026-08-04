#!/usr/bin/env python3
"""Validate project-owned citation ledger and rendered source register."""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
ledger=json.loads((ROOT/'docs/evidence/citation-ledger.json').read_text(encoding='utf-8'))
html=(ROOT/'index.html').read_text(encoding='utf-8')
errors=[]
sources=ledger.get('sources',[])
if [s.get('id') for s in sources] != list(range(1,9)): errors.append('ledger IDs must be 1..8 in order')
for source in sources:
    n=source.get('id'); url=source.get('url',''); title=source.get('title',''); quotes=source.get('quotes',[])
    if not url.startswith('https://'): errors.append(f'source {n}: invalid URL')
    if not title: errors.append(f'source {n}: missing title')
    if not quotes or not all(q.get('text','').strip() for q in quotes): errors.append(f'source {n}: missing evidence quote')
    pattern=rf'<li id="source-{n}"><a href="{re.escape(url)}"[^>]*>{re.escape(title)}</a></li>'
    if not re.search(pattern,html): errors.append(f'source {n}: rendered register entry does not match ledger')
for n in range(1,9):
    if not re.search(rf'href="#source-{n}"',html): errors.append(f'source {n}: no inline citation link')
if errors:
    print('CITATION LEDGER VERIFICATION FAILED')
    for e in errors: print('- '+e)
    sys.exit(1)
print('CITATION LEDGER VERIFICATION PASSED')
print('sources=8 evidence_quotes='+str(sum(len(s['quotes']) for s in sources))+' rendered_register_entries=8 inline_source_links='+str(sum(html.count(f'href="#source-{n}"') for n in range(1,9))))
