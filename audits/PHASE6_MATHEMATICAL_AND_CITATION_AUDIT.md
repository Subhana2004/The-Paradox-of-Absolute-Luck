# Absolute Luck — Phase 6 Mathematical and Citation Audit

**Date:** 7 November 2026  
**Document audited:** `Absolute_Luck_Phase6_Manuscript.pdf` and the same-named LaTeX source  
**Audit type:** in-session independent recomputation from original Phase 5 archive, mathematical proof checking, bibliographic metadata verification, and PDF visual inspection. **Not external peer review.**

## 1. Decision

**PASS — Phase 6 expository-manuscript deliverables and internal audit.**  
**HOLD — original-theorem claim, primary-canon authentication, and journal submission readiness.**

The manuscript presents five mathematically coherent, explicitly conditional results, makes no claim of discovering a new probability theorem, correctly labels all computational observations as simulated, and preserves the Phase 7 Gojo-style essay as a separate future output.

## 2. Source integrity and replay

| Audit gate | Method | Result |
|---|---|---|
| Source Phase 5 ZIP | CRC check and SHA-256 | PASS |
| Archived source manifest | Recompute all 43 entry hashes | **43/43 PASS** |
| Full prior reproduction | Fresh extraction, original `phase5_audit.py` | **PASS** (six detailed audit checks, eight Phase 5 completion gates) |
| Fresh Phase 6 program | Rational arithmetic, independent LP, CSV checks and binomial calculations | **133/133 PASS** |
| Figures | Extracted five original publication-resolution PNGs and five SVGs; no new data plotted | PASS |
| PDF | Two LaTeX passes, reference resolution, PDF rendering (10 A4 pages), all-page contact-sheet visual QA | PASS |

**Frozen source archive SHA-256:** `d43e99eebcbc0842a0df9b6e03ee717b833b816ffb5d9a5cb9c7cb7beb060a3f`.

The original Phase 5 ZIP is preserved without alteration at `archive/Absolute_Luck_Phase5_Complete_Package_2026-11-07.zip`. Phase 2–4 artifacts reside within that archive. The Phase 6 tests read the archive and do not modify it.

## 3. Independent mathematical checks

| Manuscript claim | Exact audit | Verdict |
|---|---|---|
| Two incompatible 99% disjoint wins | Rational sum 1.98 > 1 | PASS; requires same contest and exclusive wins |
| Equal baseline performance need not imply equal duel probability | Single ranking distribution (.89, .10, .01) gives 99%, 99%, 90% | PASS |
| Sharp three-event intersection under identical marginals .995 | Fresh linear programs give min .985, max .995 | PASS |
| Two three-coin laws with same first and second moments | Exact mass functions give marginals .7, pairwise .5, triple .3 vs .4 | PASS |
| 200 near-certain coins with impossible all-success | Exactly-one-failure construction and exact covariance -1/40000 | PASS |
| No 201-coordinate exchangeable extension | Correlation -1/199 below 201 lower bound -1/200 | PASS |
| Total-variation extension gap | Exact attainable distance 1/201 | PASS |
| Infinite-exchangeability lower bound | `E[Theta^200] >= (E Theta)^200` and Beta example 199/399 | PASS (conditional on infinite exchangeability) |
| Equal-versus-concentrated reversal | Independent .294079625 vs .248750; fixed coupling .330 vs .495 | PASS; **pairwise policy contrast**, not global optimum |
| Main simulation estimates | Every archived estimate recomputed from its recorded count; prespecified tolerance checked | 63/63 PASS |
| Restricted observation protocol | Exact pair-law equality; six exact binomial discrimination probabilities recalculated | PASS; protocol restriction necessary |
| Paired contrasts | All three sign and theoretical magnitude checks | PASS |
| Pointwise Wilson caveat | Eight of 63 pointwise intervals exclude their exact generating truth | Reported accurately; not a simultaneous 95% statement |

**Audit boundary:** Automated arithmetic checks are evidence of internal consistency, not a substitute for full external mathematical refereeing. The proofs in the manuscript are independently inspectable.

## 4. Reference audit

The following metadata and links were verified against the named publisher, official series page, or author/journal source on 7 November 2026. The verification scope is bibliographic metadata and accessible summaries, not a full-text expert review of every cited paper.

| ID | Publication or source | Verification / caution |
|---|---|---|
| [1] | Sehoon Kim, *Hardcore Leveling Warrior*, WEBTOON | [Official series](https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221). Series and creator verified; **specific Lucky Coin mechanics not authenticated**. |
| [2] | Bradley & Terry (1952), *Biometrika* 39(3–4), 324–345 | [Publisher record](https://doi.org/10.1093/biomet/39.3-4.324) |
| [3] | R. Duncan Luce (2008), *Scholarpedia* 3(12):8077 | [Author entry and formula](https://doi.org/10.4249/scholarpedia.8077) |
| [4] | Hoppe & Nediak (2008), *Statistics & Probability Letters* 78(3), 311–319 | [Publisher record](https://doi.org/10.1016/j.spl.2007.02.019). Explicitly works with Fréchet-optimal union bounds and LP. |
| [5] | Kirsch (2019), *Statistics & Probability Letters* 151, 84–88 | [Publisher record](https://doi.org/10.1016/j.spl.2019.03.014). States infinite, not arbitrary finite, de Finetti theorem. |
| [6] | Konstantopoulos & Yuan (2019), *Transactions AMS* 371, 7067–7092 | [AMS record](https://doi.org/10.1090/tran/7701). Finite exchangeable extendibility. |
| [7] | Shaked & Shanthikumar (1992), *Advances in Applied Probability* 24(4), 894–914 | [Publisher record](https://doi.org/10.2307/1427718). Reliability resource allocation. |
| [8] | Brown, Cai & DasGupta (2001), *Statistical Science* 16(2), 101–117 | [Main article/with discussion DOI](https://doi.org/10.1214/ss/1009213286). **Important bibliographic distinction:** the main article occupies pp. 101–117; related comments/rejoinder extend through p. 133. |

**No invented papers, paper titles, DOIs or statistics were knowingly included.** The cited articles are established prior work. None is used to assert a new Absolute Luck result.

## 5. Manuscript boundary and residual risks

1. **The story remains creative inspiration, not an empirical source.** No comic-panel counting, no measured ability activation rates, and no authenticated precise Lucky Coin formula.
2. **Model selection is not causal identification.** The simulated scenarios establish behavior of specified distributions and an observation-protocol identifiability limit. They cannot identify the comic's unknown probability law.
3. **Exchangeability conditions are not interchangeable.** A finite exchangeable distribution can have negative covariance; an infinite exchangeable Bernoulli sequence obeys de Finetti's mixture-of-i.i.d. representation.
4. **Allocation reversal is limited to comparing the two specified allocations.** Equal allocation is globally optimal only for the explicitly assumed symmetric independent all-success product model.
5. **Pointwise confidence intervals are not a familywise confidence procedure.** The reported 8/63 misses are retained instead of being hidden.
6. **Novelty remains in exposition, question arrangement, and worked examples—not a validated new theorem.** A new research-paper claim would require additional prior-art and theorem-level review.
7. **No external peer reviewer has evaluated this manuscript.** A submission version should undergo professional mathematical and copyediting review.
8. **Authorship and venue are not assigned.** The file is labeled an anonymous research draft until its author(s) and intended submission venue are confirmed.

## 6. Completion gate

- [x] Formal abstract, definitions, propositions, proofs, examples, and counterexamples.
- [x] Five original reproducible Phase 5 figures imported without alteration.
- [x] Complete simulation methodology, numerical results, uncertainty interpretation.
- [x] Eight bibliographic references checked at metadata/source level.
- [x] Separate mathematical/citation audit with machine-readable evidence.
- [x] Phase 2–5 materials preserved as read-only archive provenance.
- [x] Manuscript PDF compiled and all pages visually inspected.
- [x] No claim of new theorem or verified numerical story mechanics.
- [x] Phase 7 narrative essay **not** drafted or mixed into this formal manuscript.

**Final status: PHASE 6 COMPLETE as an expository manuscript and internal audit; not independently refereed or submission-approved.**