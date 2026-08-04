# Design specification — SMB healthcare risk context

Status: approved design-specification stage only
Date: 2026-08-04

## Change

Replace the first paragraph in the `Cybersecurity in Australia, in plain language` section with this exact final paragraph:

> Small and medium businesses often hold valuable customer information while working within practical limits on time, budget and specialist cybersecurity support. Healthcare providers face an added concern: the sensitive health information they handle requires particular care.[6] Practical training puts everyday decisions in context: checking unexpected emails and invoices, protecting accounts, handling sensitive information, keeping devices current and knowing where to raise a concern.

## Exact location and citation handling

- Target `index.html`, in `<section class="section context" aria-labelledby="context-title">`, inside `<div class="prose">`.
- Replace only its first `<p>`: the paragraph immediately after `<h2 id="context-title">Cybersecurity in Australia, in plain language</h2>`.
- Render `[6]` immediately after the healthcare sentence as the existing inline source-link pattern: `<a href="#source-6" aria-label="Read source 6 in the source register">[6]</a>`.
- Keep the existing source-6 register entry and citation ledger unchanged. The citation remains attached to the healthcare claim, not the preceding SMB-risk sentence or the practical-training sentence.

## Scope boundaries

- This is copy-only. Do not make visual, layout, style, navigation, asset, metadata, source-register, citation-ledger, deployment, remote, or live-site changes.
- Do not alter the second paragraph in the section or any other website copy.
- Do not push, deploy, or publish during this work.

## Test impact

- `scripts/verify-site.py` has no exact assertion for the current first context paragraph. No test change is required unless an exact-copy assertion is introduced or exists when implementation begins.
- If an exact-copy assertion is added, update it to require the final paragraph text and ensure the source-6 inline-link assertion covers the healthcare sentence.
- Run the existing site and citation-ledger verifiers after the future implementation; they must pass without changing the source register or ledger.

## Acceptance checks for future implementation

- The first context paragraph exactly matches the final paragraph above in rendered text, with `[6]` immediately following the healthcare sentence.
- The practical-training sentence and every listed everyday staff decision remain present in that first paragraph.
- `#source-6` still resolves to the OAIC Guide to health privacy entry, and source 6 remains an inline citation.
- Only the intended first context paragraph changes; there are no visual or layout changes.
- `python3 scripts/verify-site.py`, `python3 scripts/verify-citation-ledger.py`, and `git diff --check` pass.

## Self-review

This specification contains no placeholders, conflicting copy, or implementation/deployment direction. It identifies one paragraph, states the exact rendered text and citation markup, preserves the approved text verbatim, and confines future work to the specified copy replacement.
