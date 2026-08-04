# Cyber Ready for Small Business Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build, verify and publish a complete, accessible static GitHub Pages website for Cyber Ready for Small Business.

**Architecture:** A dependency-light single-page static site will use semantic HTML, a local stylesheet and a small native JavaScript module for the accessible mobile menu and active navigation state. Project-owned verification scripts will validate required content, sources, structure, metadata, links and forbidden claims without requiring a build system. The existing project citation ledger remains the authority for the public source register.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python 3 standard library, Git, GitHub Pages.

---

### Task 1: Create the public-site document structure

**Objective:** Establish the semantic page, approved metadata, landmarks, hero copy and navigation without external runtime dependencies.

**Files:**
- Create: `index.html`
- Create: `assets/css/site.css`
- Create: `assets/js/site.js`
- Create: `assets/images/cyber-ready-field-guide.svg`
- Create: `assets/images/social-card.svg`
- Create: `favicon.svg`

**Step 1: Write the failing content-verification fixture**

Create `scripts/verify-site.py` with assertions for the exact H1, hero support copy, canonical URL, mailto target, one H1, skip link and required disclaimer.

**Step 2: Run the verifier to verify failure**

Run: `python3 scripts/verify-site.py`

Expected: FAIL because `index.html` and its required copy do not yet exist.

**Step 3: Write the minimal semantic shell**

Implement `index.html` with a skip link, `header`, `nav`, `main`, `footer`, a single H1, approved title/description/canonical/OG metadata and `mailto:enzo491kw@gmail.com?subject=Cybersecurity%20training%20enquiry` CTA. Implement a native button-controlled mobile navigation using `aria-expanded` and `aria-controls`.

**Step 4: Add the visual foundation and signature illustration**

Create the local CSS tokens for cream, charcoal, rust and eucalyptus. Create the original inline-compatible SVG “Operational readiness field guide” illustration with meaningful alt text; use no government mark, stock image or cyber-fear motif.

**Step 5: Run the verifier**

Run: `python3 scripts/verify-site.py`

Expected: partial failures only for sections not yet authored.

**Step 6: Commit**

```bash
git add index.html assets/css/site.css assets/js/site.js assets/images/cyber-ready-field-guide.svg assets/images/social-card.svg favicon.svg scripts/verify-site.py
git commit -m "feat: add cyber ready site foundation"
```

### Task 2: Add the evidence-led public content

**Objective:** Add the required evidence, practical cybersecurity context, all Essential Eight strategies and citation anchors.

**Files:**
- Modify: `index.html`
- Modify: `scripts/verify-site.py`
- Reference: `docs/evidence/citation-ledger.json`
- Reference: `docs/evidence/source-excerpts-2026-08-04.txt`

**Step 1: Extend the verifier with required figures and attribution checks**

Assert the FY2024–25 ASD wording, “over 84,700”, “one report every six minutes”, “over 1,200”, all three self-reported cost figures, citations `[1]` through `[8]`, and eight Essential Eight headings in approved order.

**Step 2: Run the verifier to verify failure**

Run: `python3 scripts/verify-site.py`

Expected: FAIL because the evidence and strategy sections are absent.

**Step 3: Implement the evidence and strategy sections**

Add “Why this matters in Australia”, plain-English Australia context and eight equal strategy cards using the approved wording. Keep ASD’s ReportCyber/incident distinction, point-in-time self-reported qualifier and mitigation-not-complete-security statement. Link each inline citation to its source-register anchor.

**Step 4: Run the verifier to verify pass for Task 2 requirements**

Run: `python3 scripts/verify-site.py`

Expected: those evidence and Essential Eight checks PASS.

**Step 5: Commit**

```bash
git add index.html scripts/verify-site.py
git commit -m "feat: add evidence and Essential Eight guidance"
```

### Task 3: Add specialist healthcare, tailored-training and readiness sections

**Objective:** Provide the approved healthcare/privacy distinctions, tailored-training journey and incident-readiness basics without unsupported service claims.

**Files:**
- Modify: `index.html`
- Modify: `scripts/verify-site.py`

**Step 1: Extend the verifier with healthcare and safety guardrails**

Require “OAIC data, not ASD data”, 1,205/716/225/19%, NDB eligibility language, separate My Health Record treatment and disallow downtime/recovery numerical claims, security guarantees and government-affiliation claims.

**Step 2: Run the verifier to verify failure**

Run: `python3 scripts/verify-site.py`

Expected: FAIL because the specialist and readiness requirements are absent.

**Step 3: Implement the approved sections**

Create a three-topic healthcare distinction panel; clearly attribute the 2025 notification figures to OAIC. Add a four-step tailored-training journey and a practical incident-readiness checklist framed as training content, with source links for current official reporting and recovery channels.

**Step 4: Run the verifier**

Run: `python3 scripts/verify-site.py`

Expected: healthcare, readiness and forbidden-claim checks PASS.

**Step 5: Commit**

```bash
git add index.html scripts/verify-site.py
git commit -m "feat: add healthcare and training readiness content"
```

### Task 4: Generate source register and finish contact/disclaimer content

**Objective:** Render a full mechanically derived source register and complete public-contact/legal boundaries.

**Files:**
- Create: `scripts/verify-citation-ledger.py`
- Modify: `index.html`
- Modify: `scripts/verify-site.py`

**Step 1: Write a failing ledger check**

Create `scripts/verify-citation-ledger.py` that reads `docs/evidence/citation-ledger.json`, checks IDs 1–8, URLs, titles and non-empty evidence quotes, then validates matching source-register anchors in `index.html`.

**Step 2: Run the ledger verifier to verify failure**

Run: `python3 scripts/verify-citation-ledger.py`

Expected: FAIL until the source register anchors exist.

**Step 3: Implement source register, disclaimer and contact area**

Render each source from the project ledger as a numbered source-register entry with URL and a matching `id="source-N"` anchor. Add the exact approved educational/legal/non-affiliation disclaimer and the approved enquiry CTA.

**Step 4: Run both verifiers**

Run: `python3 scripts/verify-citation-ledger.py && python3 scripts/verify-site.py`

Expected: PASS with all sources, required copy and guardrails validated.

**Step 5: Commit**

```bash
git add index.html scripts/verify-citation-ledger.py scripts/verify-site.py
git commit -m "feat: add source register and contact boundaries"
```

### Task 5: Complete responsive, accessibility and asset validation

**Objective:** Ensure the design works from 390px mobile through wide desktop and meets the approved accessible interaction requirements.

**Files:**
- Modify: `assets/css/site.css`
- Modify: `assets/js/site.js`
- Modify: `scripts/verify-site.py`

**Step 1: Write validation checks for assets and accessibility structure**

Require each local asset, descriptive image alt text, no external scripts/styles, `prefers-reduced-motion`, focus styles, mobile menu labels and valid internal anchors.

**Step 2: Run the verifier to verify failure**

Run: `python3 scripts/verify-site.py`

Expected: FAIL until all structural accessibility hooks are present.

**Step 3: Implement responsive and reduced-motion rules**

Use a mobile-first single-column layout, accessible navigation breakpoint, practical card grids, table-to-card treatment, `:focus-visible` styling and a reduced-motion media query. Keep all normal content dark and opaque against light surfaces.

**Step 4: Run static checks**

Run: `python3 scripts/verify-site.py && python3 scripts/verify-citation-ledger.py && git diff --check`

Expected: all commands exit 0.

**Step 5: Commit**

```bash
git add assets/css/site.css assets/js/site.js scripts/verify-site.py
git commit -m "feat: complete responsive accessible presentation"
```

### Task 6: Run local served-site visual and interaction QA

**Objective:** Exercise the actual static site at required desktop, tablet and mobile widths, repair observed defects and preserve screenshots.

**Files:**
- Create: `docs/evidence/screenshots/local-1440.png`
- Create: `docs/evidence/screenshots/local-1024.png`
- Create: `docs/evidence/screenshots/local-768.png`
- Create: `docs/evidence/screenshots/local-390.png`
- Create: `docs/evidence/screenshots/local-mobile-nav.png`

**Step 1: Serve the repository**

Run: `python3 -m http.server 4173 --bind 127.0.0.1`

Expected: a local HTTP server serves `index.html`.

**Step 2: Test responsive rendering**

Use browser automation or Playwright at 1440, 1024, 768 and 390 CSS px. Capture full-page screenshots; inspect no horizontal overflow, clipping, overlap, broken grid, hero/signature element or unusable CTA.

**Step 3: Test interaction and accessibility**

Test the skip link, keyboard focus traversal, mobile navigation button/expanded state, reduced-motion media query, source links, internal anchors and browser console. Run axe if installed; otherwise record exact automated structural checks plus manual keyboard/visual checks.

**Step 4: Repair and rerun until clean**

Run: `python3 scripts/verify-site.py && python3 scripts/verify-citation-ledger.py && git diff --check`

Expected: all pass after UI repairs.

**Step 5: Commit verified site**

```bash
git add -A
git commit -m "feat: publish cyber ready training website"
```

### Task 7: Publish and independently verify GitHub Pages

**Objective:** Create the approved public repository, deploy from `main`/root and validate the cache-busted production site.

**Files:**
- No application-file changes unless deployment verification reveals a defect.

**Step 1: Confirm identity and target ownership**

Run a non-disclosing GitHub API request to confirm authenticated login is `492kw` and `GET /repos/492kw/australian-cybersecurity-training` is 404 before creation.

Expected: `492kw` authenticated and no conflicting target repo.

**Step 2: Create and push the public repository**

Create `492kw/australian-cybersecurity-training` as public with `auto_init: false`; add normal `https://github.com/492kw/australian-cybersecurity-training.git` remote; push `main` using the credential helper.

Expected: remote `main` SHA equals the local implementation commit.

**Step 3: Enable Pages from main/root**

Use `POST /repos/492kw/australian-cybersecurity-training/pages` with source `{ "branch": "main", "path": "/" }`; poll Pages/build or Actions APIs until success and record deployment/run identifier and SHA.

Expected: `https://492kw.github.io/australian-cybersecurity-training/` returns HTTP 200.

**Step 4: Perform cache-busted live checks**

At 1440, 1024, 768 and 390 CSS px, capture full-page production screenshots and test exact content, figures, links, anchors, mailto target, console, keyboard, mobile navigation, reduced motion, overflow and accessibility. Re-run project verifiers against the fetched HTML where applicable.

Expected: live site passes all static and manual checks, and the deployment SHA matches pushed `main`.

**Step 5: Record evidence**

Run:

```bash
git status --short
git log --oneline -3
git remote -v
```

Expected: clean working tree, intended remote only, and recorded plan/implementation commits.
