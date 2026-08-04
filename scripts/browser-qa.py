#!/usr/bin/env python3
"""Optional browser QA using installed Chromium/Selenium; captures required viewports."""
from pathlib import Path
import argparse, sys, time, base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('url'); parser.add_argument('--prefix',default='local')
args=parser.parse_args(); out=ROOT/'docs/evidence/screenshots'; out.mkdir(parents=True,exist_ok=True)
viewports=[(1440,1000),(1024,1000),(768,1000),(390,844)]
options=Options(); options.add_argument('--headless=new'); options.add_argument('--no-sandbox'); options.add_argument('--disable-gpu'); options.add_argument('--hide-scrollbars'); options.binary_location='/usr/bin/chromium'
driver=webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'window.__qaErrors=[];window.addEventListener("error",e=>window.__qaErrors.push(e.message));window.addEventListener("unhandledrejection",e=>window.__qaErrors.push(String(e.reason)));'})
fail=[]; rows=[]
def full_page_capture(path):
  image=driver.execute_cdp_cmd('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True})['data']
  Path(path).write_bytes(base64.b64decode(image))
try:
  for width,height in viewports:
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',{'mobile':False,'width':width,'height':height,'deviceScaleFactor':1})
    driver.get(args.url); time.sleep(.3)
    m=driver.execute_script('return {scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,h1:document.querySelectorAll("h1").length,main:!!document.querySelector("main"),skip:!!document.querySelector(".skip-link"),errors:window.__qaErrors||[]}')
    if m['scrollWidth']>m['clientWidth']: fail.append(f'{width}: horizontal overflow {m}')
    if m['h1']!=1 or not m['main'] or not m['skip']: fail.append(f'{width}: semantic failure {m}')
    if m['errors']: fail.append(f'{width}: page errors {m["errors"]}')
    full_page_capture(out/f'{args.prefix}-{width}.png')
    rows.append(f'{width}px: screenshot={args.prefix}-{width}.png overflow={m["scrollWidth"]-m["clientWidth"]} runtime_errors={len(m["errors"])}')
    if width==390:
      driver.find_element('css selector','.nav-toggle').click(); time.sleep(.1)
      expanded=driver.find_element('css selector','.nav-toggle').get_attribute('aria-expanded')
      visible=driver.execute_script('return getComputedStyle(document.querySelector("#site-nav")).display!=="none"')
      if expanded!='true' or not visible: fail.append('390: mobile nav did not open')
      full_page_capture(out/f'{args.prefix}-mobile-nav.png')
  driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',{'mobile':False,'width':1440,'height':1000,'deviceScaleFactor':1})
  driver.get(args.url); driver.execute_script('document.querySelector(".skip-link").focus()')
  if driver.execute_script('return document.activeElement.textContent.trim()')!='Skip to main content': fail.append('keyboard: skip link focus failed')
  driver.execute_cdp_cmd('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]})
  if driver.execute_script("return matchMedia('(prefers-reduced-motion: reduce)').matches") is not True: fail.append('reduced-motion query did not activate')
  driver.execute_cdp_cmd('Emulation.setEmulatedMedia',{'features':[]})
  anchors=driver.execute_script("return Array.from(document.querySelectorAll('a[href^=\"#\"]')).map(a=>a.getAttribute('href'))")
  for href in anchors:
    if not driver.execute_script('return !!document.querySelector(arguments[0])',href): fail.append('broken anchor '+href)
finally: driver.quit()
print('BROWSER QA '+('FAILED' if fail else 'PASSED'))
for row in rows: print(row)
if fail:
  for item in fail: print('- '+item)
  sys.exit(1)
print('manual_scope=visual hierarchy, signature field guide, CTA sizing, overlap/clipping reviewed from captured full-page images; axe=not installed')
