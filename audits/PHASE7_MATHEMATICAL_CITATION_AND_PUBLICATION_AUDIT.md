# Absolute Luck Phase 7 — Mathematics, Sources, Design & Publication Audit

**Date:** 7 November 2026  
**Scope:** Finished mathematical essay, original diagrams, preserved Phase 6 record.  
**Internal verdict:** PASS — a polished *expository mathematical essay*; not an original-research journal submission and not externally peer-reviewed.

## 1. Evidence integrity

- The Phase 6 source archive is included unchanged as `phase6_source_archive_unchanged.zip`; the audit script checks that its SHA-256 matches the source `/mnt/data/Absolute_Luck_Phase6_Complete_Package_2026-11-07.zip`.
- Phase 7 includes independent code (`source/verify_phase7.py`) checking contest coherence, the Bradley–Terry example, the alternative coherent ranking, the three-coin Fréchet–Boole bound, the 200-coin exactly-one-failure law, the 201-exchangeability obstruction, the three-coin marginal/pairwise counterexample, and the fixed-coupling allocation reversal.
- Phase 5 synthetic numerical rates are checked against the preserved `phase5_metrics.csv`. This is *a consistency comparison*, not a fresh independent Monte Carlo rerun.
- The validation JSON currently records **61/61 PASS** internal assertions.
- Mathematical ideas and original explanatory examples are not represented as newly discovered probability theorems.

## 2. Exact mathematical claims reviewed

| Essay claim | Independent validation / limit |
|---|---|
| Two mutually exclusive 99% victory events in one duel are inconsistent | Their probabilities sum to 1.98 > 1. |
| Two weighted lucky players each beat a strength-1 opponent 99% of the time but tie 50–50 against each other | The illustrative Bradley–Terry probability is `w_i/(w_i+w_j)`; **not** mandated by probability axioms. |
| Three same-context marginal probabilities of 0.995 imply joint probability at least 0.985 | By the union bound on failures, regardless of dependence. |
| 200 coins can have p=0.995 each and all-200 success probability 0 | Exactly one uniformly chosen failure among the 200 locations. |
| Independence gives `(0.995)^200 ≈ 0.3669578217` | Exact arithmetic and Phase 5 data checked. |
| Shared-beta mixture gives all-200 success `199/399 ≈ 0.4987468672` | The mixing distribution is `Beta(199,1)`; presented as an additional alternative only. |
| Exact 200-coin law cannot be extended to a 201-exchangeable law | Every 200-subset would need exactly one failure; no configuration of 201 variables allows all omissions to satisfy this. |
| Two three-coin models have the same single-coin and pairwise laws but triple rates 0.30 and 0.40 | Explicitly enumerated and validated using exact rational mass distributions. |
| Same allocations reverse rank under independence versus a fixed mixed coupling | Equal: 0.294079625 vs concentrated 0.24875 under independence; equal 0.330 vs concentrated 0.495 under the fixed mixed coupling. **Only two policies compared.** |

The coin experiments and all numerical percentages in the essay are *hypothetical*, not measurements from the fictional work. No original WEBTOON episodes were presented as verified numerical evidence.

## 3. References checked against external primary/publisher sources

1. Bradley, R. A., and Terry, M. E. (1952), *Biometrika* 39(3–4):324–345, DOI **10.1093/biomet/39.3-4.324**. Verified against Oxford Academic's journal metadata.
2. Luce, R. Duncan (2008), “Luce's choice axiom,” *Scholarpedia* 3(12):8077, DOI **10.4249/scholarpedia.8077**. Verified against the Scholarpedia article.
3. Hoppe, Fred M., and Nediak, Mikhail (2008), *Statistics & Probability Letters* 78(3):311–319, DOI **10.1016/j.spl.2007.02.019**. Verified against Elsevier's record.
4. Konstantopoulos, Takis, and Yuan, Linglong (2019), *Transactions of the AMS* 371:7067–7092, DOI **10.1090/tran/7701**. Verified against AMS journal metadata.
5. Kirsch, Werner (2019), *Statistics & Probability Letters* 151:84–88, DOI **10.1016/j.spl.2019.03.014**. Verified against Elsevier's record.
6. Sehoon Kim, *Hardcore Leveling Warrior*, official WEBTOON listing, `https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221`. Verified publisher and credit, not unreviewed specific luck mechanics.

All six corresponding hyperlinks are embedded in the finished PDF.

## 4. Essay and visual quality

- The finished document is **five A4 pages** and contains **five original vector figures** generated programmatically from exact mathematical examples. No copyrighted comic panels or third-party graphic assets appear in the essay.
- The editable Markdown source contains **1,415 whitespace-delimited words including references**. PDF text extraction counts **approximately 1,732 words**, including figure axis labels, captions and repeating headers; both measures are below 2,000.
- All figures are available as editable SVGs, vector PDFs, and high-resolution PNGs; the figure-generation Python code is provided.
- Visual review performed on a freshly rendered five-page PDF. No visible clipped content, isolated bibliography spillover, raw LaTeX markup, or missing formula glyphs. Fonts are embedded.
- The prose is a newly written, distinct storytelling adaptation of the verified Phase 6 mathematical work. It borrows the *investigative architecture* rather than copying prose or artwork from the separate Gojo Satoru essay. **No independent external plagiarism scan has been performed**, so originality cannot be independently certified.

## 5. Publication-readiness decision

**Editorial and technical presentation:** PASS for an accessible expository mathematical essay, subject to a final human review.

**2026 Tom Rocks Maths Essay Competition:** **CLOSED**. Oxford Lifelong Learning's official 2026 competition page states a **13 April 2026** deadline, **maximum 2,000 words**, and **PDF only**. This package fits the 2026 word-length and file-format requirements, but the 2026 competition is no longer open. Do not presume the same requirements in 2027 or a later cycle.

**Research journal:** NOT READY as an original-results submission. Current claims are an integrated exposition and application of established probability theory, not a verified new theorem.

**Remaining steps before submission anywhere:**

- Verify the *current* venue announcement, eligibility, word-count rules and deadline, and any required anonymity, author identity or title-page rules.
- Complete a fresh human mathematical/grammar review and independent originality check.
- Confirm the venue's policy on AI-assisted drafting, figures, attribution, and originality; disclose assistance where required.
- Do not add unverified WEBTOON scene references or numerical claims as if canonical.
- Choose author byline and affiliation only with the author's explicit instructions; this draft intentionally leaves the byline unspecified.
- Export/rename a venue-specific final PDF and check it again after modifications.

## 6. Limits of the internal audit

These tests provide arithmetic, data-reconciliation and PDF-output consistency evidence. They do not prove that the fictional power works this way, substitute for blind peer review, establish mathematical novelty, measure probability in any real system, or guarantee acceptance by a publisher.
