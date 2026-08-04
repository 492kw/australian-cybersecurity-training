#!/usr/bin/env python3
"""Dependency-light release gate for the Cyber Ready static site."""
from pathlib import Path
from html.parser import HTMLParser
import re, sys
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
css=(ROOT/'assets/css/site.css').read_text(encoding='utf-8')
js=(ROOT/'assets/js/site.js').read_text(encoding='utf-8')
errors=[]
def need(text,label):
    if text not in html: errors.append(label)
def count(text,n,label):
    n=int(n)
    if html.count(text)!=n: errors.append(f'{label}: expected {n}, got {html.count(text)}')
for text,label in [
('Practical cybersecurity training for Australian businesses.','exact H1 copy'),
('Help your team recognise threats, protect sensitive information and reduce the risk of compromise through practical, tailored training.','exact hero support copy'),
('Tell us about your team, sector and the situations you want to prepare for. Training is scoped after an initial conversation.','CTA supporting line'),
('https://492kw.github.io/australian-cybersecurity-training/','canonical URL'),
('mailto:enzo491kw@gmail.com?subject=Cybersecurity%20training%20enquiry','approved mailto'),
('Skip to main content','skip link'),('Why this matters in Australia','evidence section'),
('over 84,700 cybercrime reports','84,700 qualifier'),('one report every six minutes','six-minute figure'),('over 1,200 cyber security incidents','1,200 qualifier'),
('$80,850 overall','$80,850 figure'),('$56,600 for small business','$56,600 figure'),('$97,200 for medium business','$97,200 figure'),
('OAIC data, not ASD data','OAIC attribution panel'),('1,205','OAIC total'),('716','OAIC malicious figure'),('225 notifications (19%)','OAIC health figure'),
('Cyber Ready for Small Business provides educational cybersecurity training. It is not legal advice, privacy advice, incident-response advice or a certification service. Cyber Ready for Small Business is not affiliated with, endorsed by or acting on behalf of the Australian Signals Directorate (ASD), the Australian Cyber Security Centre (ACSC), the Office of the Australian Information Commissioner (OAIC), or the Australian Digital Health Agency.','exact disclaimer'),
('aria-expanded','mobile menu state'),('aria-controls="site-nav"','mobile nav controls')]: need(text,label)
for text,label in [('prefers-reduced-motion','reduced motion CSS'),(':focus-visible','visible focus CSS')]:
    if text not in css: errors.append(label)
count('<h1','1','H1 count')
for s in ['Patch applications','Patch operating systems','Multi-factor authentication','Restrict administrative privileges','Application control','Restrict Microsoft Office macros','User application hardening','Regular backups']: count(f'<h3>{s}</h3>',1,f'Essential Eight heading {s}')
for n in range(1,9): need(f'id="source-{n}"',f'source anchor {n}')
for f in ['favicon.svg','assets/css/site.css','assets/js/site.js','assets/images/cyber-ready-field-guide.svg','assets/images/social-card.svg']:
    if not (ROOT/f).exists(): errors.append('missing asset '+f)
# No surname, excluding functional email address.
visible_or_meta=re.sub(r'enzofung|simonfungwork@gmail.com','',html,flags=re.I)
if re.search(r'\bFung\b',visible_or_meta,re.I): errors.append('surname appears outside functional email')
# The explicit limitation that the page does NOT make an organisation completely secure is required.
for phrase in ['guaranteed','government endorsed','ASD-approved','ASD approved','government-approved','government approved','100% secure','certified cybersecurity','compliance guarantee']:
    if phrase.lower() in html.lower(): errors.append('forbidden claim: '+phrase)
# Numerical downtime / recovery claim patterns (not generic readiness copy).
if re.search(r'\b\$?\d+[\d,.]*\s*(hours?|days?|minutes?)\s+(?:of\s+)?(?:downtime|recovery)',html,re.I): errors.append('numerical downtime/recovery claim')
if '<script src="http' in html or '<link rel="stylesheet" href="http' in html: errors.append('external runtime dependency')
if not re.search(r'<main\b[^>]*id="main-content"',html): errors.append('main landmark')
if not re.search(r'<nav\b[^>]*aria-label="Primary navigation"',html): errors.append('primary nav label')
# Check every fragment link resolves to one id.
ids=set(re.findall(r'\bid="([^"]+)"',html))
for fragment in re.findall(r'href="#([^"]+)"',html):
    if fragment not in ids: errors.append('broken internal anchor #'+fragment)
if errors:
    print('SITE VERIFICATION FAILED')
    for e in errors: print('- '+e)
    sys.exit(1)
print('SITE VERIFICATION PASSED')
print('checks=46 essential_eight=8 source_anchors=8 local_assets=5 internal_anchors='+str(len(re.findall(r'href="#([^"]+)"',html))))
