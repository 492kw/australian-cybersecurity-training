# SMB Healthcare Risk Context Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Replace the approved first plain-language context paragraph with the SMB and healthcare-risk wording, preserving the source-6 citation placement and all other public site content.

**Architecture:** This is a bounded static-content change in `index.html` plus a formatting-tolerant assertion in the existing Python release gate. The source register and citation ledger remain unchanged; the verifier will parse the target context paragraph structurally and check normalised rendered text plus the inline `#source-6` link.

**Tech Stack:** HTML5, Python 3 standard library, Git, GitHub Pages.

---

### Task 1: Establish the approved change baseline and regression check

**Objective:** Capture the exact approved copy in the repository’s verifier so the old opening cannot return unnoticed.

**Files:**
- Modify: `scripts/verify-site.py`
- Reference: `docs/superpowers/specs/2026-08-04-smb-healthcare-risk-context-design.md:8-17`
- Reference: `index.html:58-61`

**Step 1: Add the smallest structural assertion**

Parse the `section.context` first paragraph inside `div.prose`; normalise whitespace and require this rendered text:

```text
Small and medium businesses often hold valuable customer information while working within practical limits on time, budget and specialist cybersecurity support. Healthcare providers face an added concern: the sensitive health information they handle requires particular care.[6] Practical training puts everyday decisions in context: checking unexpected emails and invoices, protecting accounts, handling sensitive information, keeping devices current and knowing where to raise a concern.
```

Require `<a href="#source-6" aria-label="Read source 6 in the source register">[6]</a>` immediately after the healthcare sentence. Reject the removed opening wording `Small and medium businesses often balance customer service, cash flow and technology with limited time.`

**Step 2: Demonstrate the pre-change failure**

Run: `python3 scripts/verify-site.py`

Expected: FAIL with the new context-copy requirements because `index.html` still contains the removed opening wording.

**Step 3: Commit the implementation plan**

Run:

```bash
git add docs/superpowers/plans/2026-08-04-smb-healthcare-risk-context-implementation.md
git -c user.name='Simon Fung' -c user.email='simonfungwork@gmail.com' commit -m "docs: add SMB healthcare context implementation plan"
```

Expected: one documentation-only commit with a clean working tree.

### Task 2: Apply the approved one-paragraph replacement

**Objective:** Make the exact approved text and citation placement live in the static HTML without altering other visible content.

**Files:**
- Modify: `index.html:60`
- Modify: `scripts/verify-site.py`

**Step 1: Replace only the first context paragraph**

Use exactly:

```html
<p>Small and medium businesses often hold valuable customer information while working within practical limits on time, budget and specialist cybersecurity support. Healthcare providers face an added concern: the sensitive health information they handle requires particular care.<a href="#source-6" aria-label="Read source 6 in the source register">[6]</a> Practical training puts everyday decisions in context: checking unexpected emails and invoices, protecting accounts, handling sensitive information, keeping devices current and knowing where to raise a concern.</p>
```

Do not modify the following escalation paragraph, CSS, JavaScript, metadata, assets, source register or citation ledger.

**Step 2: Run the targeted regression gate**

Run: `python3 scripts/verify-site.py`

Expected: PASS; the target paragraph is present, the inline source-6 link follows the healthcare sentence, and the removed opening wording is absent.

**Step 3: Run required static checks and inspect scope**

Run:

```bash
git diff --check
python3 scripts/verify-site.py
python3 scripts/verify-citation-ledger.py
git diff -- index.html scripts/verify-site.py
```

Expected: all checks exit 0; the implementation diff changes only the first context paragraph and its verification assertion.

### Task 3: Commit, publish and verify GitHub Pages

**Objective:** Publish the implementation on `main` and prove the deployed page contains only the approved context change.

**Files:**
- Modify: `index.html`
- Modify: `scripts/verify-site.py`

**Step 1: Commit the verified implementation**

Run:

```bash
git add index.html scripts/verify-site.py
git -c user.name='Simon Fung' -c user.email='simonfungwork@gmail.com' commit -m "docs: add SMB healthcare risk context"
git push origin main
```

Expected: `origin/main` equals the local implementation SHA.

**Step 2: Confirm deployment source and success**

Derive `492kw/australian-cybersecurity-training` from `origin`; poll its GitHub Pages workflow/API until the successful deployment reports the pushed SHA as its source/version.

Expected: GitHub Pages deployment succeeds for the implementation commit.

**Step 3: Cache-bypass live-content validation**

Run a cache-bypassed request to:

```text
https://492kw.github.io/australian-cybersecurity-training/
```

Require the exact approved text and source-6 inline link; reject the removed opening wording.

**Step 4: Responsive smoke checks**

Serve the local site and use browser automation at desktop and 390px. Confirm no horizontal overflow, clipping, overlap, or browser-console errors from the longer paragraph. Repeat equivalent visual smoke inspection against the live URL if browser access permits.

**Step 5: Final repository state**

Run:

```bash
git status --short --branch
git log --oneline -3
git rev-parse HEAD
git rev-parse origin/main
```

Expected: clean tree and equal local/remote implementation SHAs.

## Self-review

- [x] Exact specification path, target path, copy and source-6 markup are recorded.
- [x] The change is limited to the specified paragraph and a minimal formatting-tolerant verifier assertion.
- [x] Commands state failure/pass expectations and include the required verifiers, diff check, commit, push, Pages monitoring and cache-bypassed live verification.
- [x] The plan separates the required plan and implementation commits and preserves the citation ledger/source register.
