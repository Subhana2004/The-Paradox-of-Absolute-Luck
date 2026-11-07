# Phase 9 — Research Integrity, Mathematics, Source, and Publication Audit

**Project:** *The Paradox of Absolute Luck: Can Probability Favor Everyone?*  
**Date:** 7 November 2026  
**Source of record:** `Subhana2004/The-Paradox-of-Absolute-Luck`, GitHub commit `dc4f8efe12a72d5227e3903d6014f37aa2e9b0f3`  
**Previous verified CI run:** https://github.com/Subhana2004/The-Paradox-of-Absolute-Luck/actions/runs/42395305456  
**Reviewer status:** Independent *method of re-derivation* and fresh check code, performed by an AI assistant. **NOT** an independent human mathematical referee, plagiarism examiner, or editorial acceptance.

## Executive verdict

**MATHEMATICAL EXPOSITION: PASS within stated assumptions.** The five main mathematical constructions and reported Phase 5 numerical summaries survived a separate exact-rational, constrained-linear-programming and table-recalculation audit. The existing GitHub verification passed on its published commit, and Phase 2–5 tests replayed from a fresh scratch copy. No material mathematical contradiction was identified in the claims examined.

**UNCONDITIONAL PUBLICATION READINESS: HOLD.** Primary-panel support for the Lucky Coin mechanics is not verified; final scientific authorship, permissions/license and venue-specific AI-use disclosure are undecided; no external human mathematical review or independent similarity evaluation has occurred. The manuscript appropriately **does not** claim a novel theorem or measured comic probabilities. Because the work is explicit mathematical exposition, the unverified canon numbers must remain *hypothetical* rather than quietly promoted to factual source assertions.

**Phase 9 status:** Audit delivered, with the technical mathematics/citation checks passing and the external-review/publication gate **not yet cleared**. Any later claim that Phase 9 proves external peer-review status would be incorrect.

## Evidence boundary

- The **official WEBTOON series page** establishes the title, series creator **Sehoon Kim**, and basic fictional premise: https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221 . It does **not**, in the available accessible material, independently substantiate 50% to >99% Lucky Coin rates, precise simultaneous-coin performance, or events in a claimed episode panel.
- **Fan-maintained secondary sources**, not primary panel evidence, discuss those mechanics: https://hardcorelevelingwarrior.fandom.com/wiki/Absolute_Luck and https://hardcorelevelingwarrior.fandom.com/wiki/Lucky_Coin . Episode 13 and episode 83 (season 1) are candidate first-party checks, not verified citations in this audit.
- All percentages in the essay and manuscript must remain explicitly declared **synthetic thought experiments**. No fan-wiki percentage may be silently treated as a measured probability or certified authorial rule.

## Claim-by-claim mathematical audit

| Claim | Re-derivation / independent check | Finding |
| --- | --- | --- |
| Two mutually exclusive winners cannot both have 99% win probability | Their probabilities sum to 1.98 > 1; an alternative coherent *ranking* law has probabilities 0.89, 0.10, 0.01 and yields equal 99%-against-baseline but 90% A-versus-B | PASS |
| Three simultaneous 99.5%-reliable events cannot have 60% all-success | Union bound gives `P(all) >= 0.985`. If only the target 0.60 is fixed, `sum(p_i) <= 2.60` and total marginal reduction from 3 × 0.995 is at least 0.385 | PASS |
| Exactly one failure among 200 implies each marginal 99.5% and all-success 0% | Uniform failure index: `p_i = 199/200`; `P(all) = 0` | PASS |
| 200-coin model cannot extend to 201 exchangeable variables; exact TV distance = 1/201 | Pair correlation `-1/199` contradicts 201-exchangeable variance lower bound `-1/200`; counting failures proves maximum probability of exactly one failure in the first 200 is `200/201`, attained by a one-failure 201-coin law | PASS |
| Models L and H have the same single- and pairwise laws but different triple-success | Exact distributions of success counts: L = (0.1, 0, 0.6, 0.3), H = (0, 0.3, 0.3, 0.4). Both have single = 0.70 and pair = 0.50; independent 8-atom linear program produces sharp triple range [0.30, 0.40] | PASS |
| Fixed coupling reverses ranking of two boost allocations | Independent equal = 0.294079625 versus concentrated = 0.24875. Under the *same* fixed mixed coupling, equal = 0.330, concentrated = 0.495 | PASS; does **not** prove global optimality |
| Infinitely exchangeable Bernoulli mixture differs structurally | De Finetti mixture implies `E[Theta^n] >= (E Theta)^n` for n >= 2; the 200-coin exactly-one-failure construction is only finitely exchangeable | PASS with scope qualification |
| Monte Carlo summaries consistent with published synthetic source data | 63 archived metrics independently recalculated from success count/trial count; all show original engineering tolerance flags; 8 of 63 pointwise Wilson intervals exclude the generator's parameter | PASS; engineering tolerances are **not** hypothesis-test p-values |
| Classifier and paired allocation estimates | Binomial-tail theoretical classifier accuracies recalculated for m=200 and m=500; exact paired boost difference +0.165 | PASS |

**Reproduction details:** The new `phase9_independent_math_checks.py` deliberately does **not** import the previous phases' proof functions. It performs 23 independent rational-arithmetic, LP, probability and archived-table checks, all passed on the audited snapshot. It is a second *implementation*, not an independent human audit. The project's own `python tools/verify_publication.py` and `bash tools/run_regression.sh` both passed. The published PDF files have 10 and 5 pages, respectively, with extractable text and resolved figures.

## Source-by-source citation assessment

| Reference | Publisher/source check | Result |
| --- | --- | --- |
| Sehoon Kim, *Hardcore Leveling Warrior* | Official WEBTOON series page confirms creator/title, not exact mechanics | VERIFIED FOR ATTRIBUTION ONLY |
| Bradley & Terry (1952), *Biometrika* 39, 324–345, DOI `10.1093/biomet/39.3-4.324` | Oxford Academic journal metadata | VERIFIED |
| Luce (2008), Scholarpedia 3(12):8077, DOI `10.4249/scholarpedia.8077` | Author-attributed Scholarpedia article | VERIFIED |
| Hoppe & Nediak (2008), *Statistics & Probability Letters* 78(3), 311–319, DOI `10.1016/j.spl.2007.02.019` | Elsevier publisher metadata | VERIFIED |
| Kirsch (2019), *Statistics & Probability Letters* 151, 84–88, DOI `10.1016/j.spl.2019.03.014` | Elsevier publisher metadata | VERIFIED |
| Konstantopoulos & Yuan (2019), *Trans. AMS* 371, 7067–7092, DOI `10.1090/tran/7701` | AMS publisher record | VERIFIED |
| Shaked & Shanthikumar (1992), *Advances in Applied Probability* 24(4), 894–914, DOI `10.2307/1427718` | Cambridge journal archive, 1992 print date (2016 website posting is not the study year) | VERIFIED |
| Brown, Cai & DasGupta (2001), *Statistical Science* 16(2), main article 101–117, DOI `10.1214/ss/1009213286` | JSTOR issue contents: the discussions/rejoinder continue through 133 | VERIFIED |

**Citation audit limit:** Verification establishes existence, bibliographic accuracy and conceptual relevance of these cited works; it does not certify an exhaustive literature search or that every paragraph of every full text was independently compared to the manuscript.

## Scientific and statistical limitations that MUST stay in the paper

1. **Not novel theorems.** The claims are demonstrations of established probability and optimization ideas; originality is in *the expository arrangement and fictional framing*, not in a claimed first discovery of Fréchet bounds, de Finetti, or resource allocation.
2. **No observed webtoon probabilities.** The 0.99, 0.995, 200-coin, 0.60 and 0.495 parameters are hypothetical unless a future source audit separately verifies a particular narrative numerical claim.
3. **No universal claim of concentration optimality.** The fixed-coupling counterexample reverses two candidate policies only.
4. **Identifiability has a measurement-protocol restriction.** The L/H impossibility assumes one or two coordinates per independent draw; coordinated pair records from the same triple may contain additional information.
5. **Uncertainty reporting is pointwise.** Wilson 95% intervals in the synthetic study are not 63-fold simultaneous coverage intervals; the original engineering tolerances are not a statistical significance test.
6. **Numerical reproducibility has a software-version boundary.** GitHub Actions passed with recorded versions, but the workflow uses moving hosted runners and mutable action tags. Byte-identical PDFs on every future platform are not demonstrated.

## Publication and research ethics checklist

| Gate | Status | Remedy |
| --- | --- | --- |
| Coherent mathematical formulation, exact checks and internal CI | **PASS** | Preserve source and recorded versions |
| Scholarly bibliographic accuracy | **PASS** | Retain primary publisher links and current DOI records |
| Fictional title/creator attribution | **PASS** | Continue identifying the comic as fiction |
| Primary-panel confirmation of specific Lucky Coin mechanics | **OPEN** | Review the actual original panels with precise episode and panel references; do not upload copyrighted panels without permission |
| Independent HUMAN mathematics/editorial review | **OPEN** | Ask a mathematician/statistician to read the proofs and counterexamples; log corrections transparently |
| Independently certified text similarity/originality | **OPEN** | Perform an approved similarity/originality review; do not misrepresent an assistant search as certification |
| Scientific authorship/acknowledgments/AI-use disclosure | **OPEN** | Owner must approve contributor identities and target-venue disclosure wording |
| License and permissions | **OPEN** | Select a suitable author-approved license for original content, excluding third-party comic rights |
| Specific venue's live submission rules | **OPEN** | Phase 10: check venue, limits, human authorship, copyright and AI policies |

## Disposition

**Phase 9 research audit performed: technical mathematical and citation components PASS; complete publication clearance NOT YET GRANTED.** No new theorem, empirical comic study, originality certification, journal acceptance or external human review should be inferred. Proceed to venue preparation **only as a conditional draft**, resolving primary canon and human-review/authorship requirements before making publication-ready claims.

## Traceability

- GitHub snapshot audited: https://github.com/Subhana2004/The-Paradox-of-Absolute-Luck/tree/dc4f8efe12a72d5227e3903d6014f37aa2e9b0f3
- GitHub successful Phase 8 build: https://github.com/Subhana2004/The-Paradox-of-Absolute-Luck/actions/runs/42395305456
- Independent arithmetic check data: `phase9_math_audit.json`
- Independent arithmetic script: `phase9_independent_math_checks.py`
- Published input tables: `research/phase-5/*.csv`, manuscript/essay source under `manuscript/` and `essay/`.
