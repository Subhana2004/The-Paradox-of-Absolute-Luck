# The Paradox of Absolute Luck — Phase 4: Proofs and Stress Testing

**Date:** 7 November 2026  
**Status:** **PASS — Phase 4 proof/counterexample gate**  
**Project approach:** Gojo-style mathematical investigation: fictional premise → precise formalism → proof → attempted falsification → honestly qualified conclusion.  
**Preserved inputs:** Phase 3 mathematical report, verifier, prediction table, and validation JSON, plus its Phase 2 source materials, are copied without modification to `source_phase3/`. `phase4_verify.py` reruns earlier checks in those isolated copies.

> **Scope alert.** All probabilities (0.99, 0.995, 0.60 and resource budget 0.495) are *hypothetical* mathematical parameters. They are not measured WEBTOON outcomes. The original story's relevant panels have **not** been fully authenticated against the licensed edition. None of the derivations below is claimed as a newly discovered probability theorem.

## Executive verdict

- **M1 — Relative luck:** The Bradley–Terry–Luce (BTL) resolution is coherent but *not forced* by two players each beating an ordinary opponent with 99% probability. A coherent **single random-ranking distribution** permits those isolated win rates but gives a 90–10 duel.
- **M2 — Dependence:** Our 200-coin, exactly-one-failure construction is valid and finitely exchangeable; it is **not 201-exchangeable-extendible**. The best possible 201-exchangeable approximation assigns at most 200/201 probability to its defining “exactly one failure among the first 200” event; the minimum total-variation distance is exactly 1/201.
- **M2 — Higher-order interactions:** Identical single- and pairwise-success probabilities do not fix triple success. Even *strictly positive pairwise covariances* do not force triple success to be at least the independent benchmark.
- **M3 — Resource allocation:** Equal sharing optimizes all-success only with the **independence + identical baselines + linear response** structure used in Phase 3. Removing independence allows an exact reversal of **both** Phase 3 allocation preferences. With unrestricted dependence and three coins, no allocation provides a positive guaranteed probability of *all* successes under the stated 0.495 budget.
- **Publication status:** Rigorous mathematical exposition is viable. A novel theorem is **not established**. Phase 5 should test numerical reproducibility and sample-level identifiability, not manufacture new scientific evidence.

## 1. Frozen assumptions and evidence boundaries

### Paradox A — Luck Collision

In a no-tie, exactly-one-winner contest in **one** context, events `A wins` and `B wins` are disjoint and exhaustive. Requiring both probabilities to be ≥0.99 is infeasible: their sum would be ≥1.98 although the probability of their union is 1. The 99% probabilities are **not interchangeable across matchups**.

### Paradox B — Luck Multiplication

For successes `E_1,...,E_n` in one context, with `p_i=P(E_i)` and all-success probability `J`, the sharp Fréchet–Boole limits are:

\[
\max(0,\sum_{i=1}^n p_i-n+1)\le J\le \min_i p_i.
\]

Under 200 equal marginals `p_i=199/200`, the lower bound is 0. The finite construction with **exactly one failure** uniformly located among 200 coins achieves this bound. Nothing here says the story contains 200 coins or that a fictional 99% activation guarantee must persist in every context.

### Scope of model labels

- **M1:** A context-free set of positive strengths `w_i` generates contest probabilities `w_i / sum_{j∈S}w_j` for candidate sets `S`.
- **M2:** A finite vector of Bernoulli outcomes with fixed marginal reliability; joint dependence can be arbitrary unless additional structure is stated.
- **M3:** Each activated coin has baseline probability 1/2 and receives a share `b_i≥0` of a total **hypothetical** resource budget `B=99/200=0.495`; probability `p_i=1/2+b_i`. Product formulas require **independence** after allocation.

These models are deliberate mathematical hypotheses, not claims about the fictional power's actual mechanism.

---

## 2. M1 adversarial audit: Does relative strength *force* a 50–50 duel?

### Proposition 1 — Conditional BTL prediction

For strictly positive, *stable* player weights and no ties,

\[
P(i\mid S)=\frac{w_i}{\sum_{j\in S}w_j}.
\]

The odds between any two players `i,j` in a candidate set `S` satisfy

\[
\frac{P(i\mid S)}{P(j\mid S)}=\frac{w_i}{w_j},
\]

which is unaffected by adding candidates. This follows immediately from cancellation of the common denominator (an IIA-type invariant).

If `w_A=w_B=99` and `w_N=1`, then `P(A beats N)=P(B beats N)=.99`, `P(A beats B)=.5`, and the three-way probabilities are `P(A)=P(B)=99/199`, `P(N)=1/199`.

**Do not infer:** every probabilistic competition must obey IIA or fixed weights. That is an empirical/modeling assumption, not a probability axiom.

### Counterexample 1 — One coherent latent ranking with a 90–10 duel

Define a random **complete ranking** of three players:

| Ranking from first to last | Probability |
|---|---:|
| A > B > N | 0.89 |
| B > A > N | 0.10 |
| N > A > B | 0.01 |

For any head-to-head match, the higher-ranked player wins. Thus:

\[
P(A>N)=.99,\qquad P(B>N)=.99,\qquad P(A>B)=.90.
\]

The three-player contest winner is also well defined: A wins .89, B wins .10, N wins .01. All these probabilities arise from **one joint probability space**, not ad hoc unrelated match tables. The BTL odds prediction `P(A>B)=.5` is false in this valid alternative.

**True statement:** A 50–50 duel follows if the duel's probability model is invariant under interchanging A and B and there is exactly one winner. It does **not** follow merely because both defeat N with the same frequency.

**Phase 4 conclusion:** The collision paradox establishes a coherence constraint, but a probability-normalization rule is not uniquely determined.

---

## 3. M2 audit: Dependence and the cost of extra symmetry

### Proposition 2 — Sharp intersection bounds survive all admissible dependence

For fixed marginal success probabilities `p_i`, the intersection is bounded as in §1. Sharpness follows by choosing overlapping or disjoint failure events with the required marginal measures. Equivalently, feasibility can be checked by linear programming over `2^n` outcome masses `x_ω≥0` subject to `sum x_ω=1` and `sum_{ω:ω_i=1}x_ω=p_i`.

**Numerical audit:** 16 distinct `(n,p)` combinations with `n=2,3,4,5` and `p=1/5,1/2,133/200,199/200` were checked by separate minimization/maximization linear programs. All match the analytic endpoints to solver tolerance. These finite checks supplement, not replace, the general proof.

### Proposition 3 — The 200-coin counterexample cannot extend exchangeably to 201

Let `X_i=1` when coin `i` succeeds, and take the exchangeable 200-coin construction with exactly one failure. Then:

\[
p=P(X_i=1)=199/200,\qquad P(X_i=X_j=1)=198/200.
\]

The common covariance is

\[
(198/200)-(199/200)^2=-1/40000,
\]

and the common pairwise correlation is `ρ=-1/199`.

**Variance proof:** If `Y_1,...,Y_m` have the same nonzero variance `σ²` and the same pairwise correlation `ρ`, then

\[
\operatorname{Var}(\sum_{i=1}^mY_i)=m\sigma^2[1+(m-1)\rho]\ge0.
\]

Thus `ρ≥-1/(m-1)`. For a hypothetical **201-exchangeable extension** preserving the original 200-coin marginal, the correlation would still be `-1/199` but would need to be at least `-1/200`. Impossible.

**Critical qualification:** We can always append an arbitrary 201st random variable *without* requiring exchangeability of the enlarged family. The impossibility is specifically for an **exchangeable extension**.

### Proposition 4 — Exact 201-exchangeability approximation bound

Let a 201-coin exchangeable family contain `R=k` failures in total. The first 200 have exactly **one** failure if:

- `k=1` and the removed 201st coin succeeds, with probability `200/201`; or
- `k=2` and the removed coin fails, with probability `2/201`.

For all other `k`, the event is impossible. Since an arbitrary 201-exchangeable law is a mixture over counts `R=k`, it follows that

\[
P(\text{exactly one failure in first 200})\le\frac{200}{201}.
\]

Our 200-coin law assigns probability 1 to this event. Hence any 200-coin marginal of a 201-exchangeable law is at least `1/201` away in total-variation distance.

This bound is **sharp**. Take a 201-exchangeable distribution with exactly one uniformly positioned failure among all 201 coins. Its first-200 restriction has exactly one failure with probability `200/201` and no failures with probability `1/201`. It is a mixture of the ideal 200-coin exactly-one-failure law (weight `200/201`) and the all-success state (weight `1/201`), yielding total-variation distance precisely `1/201`.

**Generalization, for context:** If a length-`n` exchangeable binary law has exactly `r` failures with probability 1, where `1≤r≤n−1`, then the maximum probability of exactly `r` failures in an `n`-coordinate restriction of an `(n+1)`-exchangeable family is

\[
\frac{\max(n+1-r,r+1)}{n+1}<1.
\]

The proof is the same two-case conditioning on whether the omitted coordinate is a success or failure. Our verifier checks 55 `(n,r)` instances. This is an **elementary consequence of the known finite-hypergeometric representation**, not claimed as an original theorem.

### Proposition 5 — Infinite exchangeability rules out negative pairwise covariance

An **infinitely exchangeable** Bernoulli sequence admits a latent parameter `Θ∈[0,1]` with the outcomes conditionally i.i.d. Bernoulli(`Θ`), by de Finetti's theorem. Hence:

\[
P(X_1=\cdots=X_n=1)=\mathbb E[\Theta^n]\ge (\mathbb E[\Theta])^n=p^n
\]

for integer `n≥2` by Jensen's inequality; and

\[
\operatorname{Cov}(X_1,X_2)=\operatorname{Var}(\Theta)\ge0.
\]

Thus an infinitely exchangeable shared-parameter model cannot represent our 200-coin negative-covariance distribution. For `p=.995` it requires `J_200≥(.995)^{200}≈0.3669578217`, whereas our finite model has `J_200=0`.

This does **not** mean every exchangeable finite model has nonnegative covariance, nor that 201 finite exchangeability by itself implies `J_200≥p^200`. Different assumptions, different conclusions.

### Counterexample 2 — Identical marginals and pairs, different triple probability

Two exchangeable three-coin laws specify `K=number of successes`:

| K | Law L | Law H |
|---:|---:|---:|
| 0 | 1/10 | 0 |
| 1 | 0 | 3/10 |
| 2 | 3/5 | 3/10 |
| 3 | 3/10 | 2/5 |

Both yield `P(X_i=1)=7/10` and `P(X_i=X_j=1)=1/2` for every `i≠j`, yet `P(111)=3/10` versus `2/5`. For given identical individual/pairwise probabilities, write `t=P(K=3)`. The moment constraints uniquely impose

\[
(q_0,q_1,q_2,q_3)=(2/5-t,\,3t-9/10,\,3/2-3t,\,t).
\]

Nonnegativity yields **exactly** `3/10≤t≤2/5`. Both endpoints have explicit witnesses.

### Counterexample 3 — Even positive pairwise correlation is not enough

Mix these two laws:

- with probability `19/20`, choose uniformly one of `000,011,101,110` (even parity);
- with probability `1/20`, choose `111`.

The resulting binary variables have exact statistics

\[
P(X_i=1)=21/40=0.525,\qquad P(X_i=X_j=1)=23/80=0.2875.
\]

Their **pairwise covariance is positive**:

\[
23/80-(21/40)^2=19/1600=0.011875>0.
\]

Nonetheless,

\[
P(111)=1/20=0.05 < (21/40)^3\approx0.144703125.
\]

Therefore neither *pairwise independence* nor even *positive pairwise covariance* suffices for the Jensen/de Finetti joint-success lower bound. An actual mixture-of-i.i.d. (infinitely exchangeable) assumption is much stronger.

---

## 4. M3 audit: Independence, baseline equality and linear response are doing real work

Set baseline `1/2`, total budget `B=99/200`, and `p_i=1/2+b_i`, `sum b_i=B`.

- **Equal allocation:** `b_i=B/3`, so every marginal is `133/200=0.665`.
- **Concentrated allocation:** one coin receives all `B`, so marginals are `(199/200,1/2,1/2)`.

### Proposition 6 — Under conditional independence, the Phase 3 optimization remains correct

With independent coin outcomes:

\[
P(\text{all succeed})=\prod_i(1/2+b_i),\qquad
P(\text{at least one succeeds})=1-\prod_i(1/2-b_i).
\]

For fixed sum of boosts and equal baselines, AM–GM maximizes the first product at **equal boosts**. Since `(1/2-x)(1/2-y)=1/4-(x+y)/2+xy`, merging boosts while preserving their sum reduces the two-factor all-failure product and therefore maximizes at-least-one success by **concentrating** the budget, for `B≤1/2`.

Numbers for `n=3`:

| Allocation | Independent `P(all)` | Independent `P(any)` |
|---|---:|---:|
| Equal | 0.294079625 | 0.962404625 |
| Concentrated | 0.248750000 | 0.998750000 |

These are valid theorems **within the assumptions**, not universal laws of luck.

### Counterexample 4 — Dependence reverses the rankings

Use the **same allocation-dependent marginals** but different valid couplings:

**Equal boosts:** Choose `K=1` successful coin with probability `1/200` and `K=2` successful coins with probability `199/200`, selecting successful indices uniformly within each count. Each coin succeeds with probability exactly `133/200=.665`, yet `P(all)=0`, `P(any)=1`.

**Concentrated boost:** Use a common uniform `U`, with `X_i=1` when `U≤p_i`. The joint outcomes and their probabilities are:

| Outcome | Probability |
|---|---:|
| 111 | 0.500 |
| 100 | 0.495 |
| 000 | 0.005 |

This has marginals `(0.995,0.5,0.5)`, `P(all)=0.5`, and `P(any)=0.995`.

**Reversal:** Under the dependent constructions, concentrating is **better for all-success** (0.50 versus 0), and equal sharing is **better for at-least-one** (1 versus .995). This does not prove either strategy is optimal under arbitrary dependence; it shows that the independent optimum cannot be exported to a different dependence law. The couplings themselves are hypothetical and not canon claims.

### Proposition 7 — With fully unknown dependence, the sharp guarantees change

For any fixed marginals:

\[
\underline J_{\mathrm{all}}=\max(0,\sum_i p_i-(n-1)),\quad
\overline J_{\mathrm{all}}=\min_i p_i,
\]

\[
\underline J_{\mathrm{any}}=\max_i p_i,\quad
\overline J_{\mathrm{any}}=\min(1,\sum_i p_i).
\]

These endpoints are attainable by appropriate couplings. Since `sum_i p_i=n/2+B` is **fixed by the budget** in M3, the sharp lower all-success bound is independent of how we allocate boosts.

For `n=3`, `sum_i p_i=1.995 <2`, so the worst-case guarantee that **every coin succeeds is zero for *every* allocation**.

| Allocation | Sharp range `P(all)` | Sharp range `P(any)` |
|---|---|---|
| Equal | [0, 0.665] | [0.665, 1] |
| Concentrated | [0, 0.500] | [0.995, 1] |

Maximizing the worst-case `P(any)` still favors concentration because `max_i p_i` is largest there; maximizing the worst-case `P(all)` gives a **tie at zero** among all feasible allocations. The previous independent-model all-success recommendation was therefore not robust.

At `n=2`, the worst-case all-success probability equals `max(0,B)=.495` *regardless of allocation*, emphasizing how the conclusion changes with concurrency.

### Counterexample 5 — Equal boosts cease being optimal with heterogeneous baselines

For independent coins with starting probabilities `(0.2,0.8)` and budget `0.1`, putting all boost on the weaker coin yields `0.3×0.8=0.24`, while equal boosts yield `0.25×0.85=0.2125`. Thus a **fixed sum of boosts** alone does not make equal boost optimal for heterogeneous baselines.

### Counterexample 6 — Nonlinear boost response can also reverse the conclusion

Let independent coins have baseline `0.1`, budget `B=0.5`, and response `p_i=0.1+b_i^2` rather than the linear Phase 3 rule. Equal sharing gives `(0.1625)^2=0.02640625` for both succeeding. Concentrating gives `0.35×0.1=0.035`. This hypothetical convex response makes concentration better for all-success.

---

## 5. Cross-model identifiability: what can we actually conclude?

| Observation or premise | What it establishes | What it does **not** establish |
|---|---|---|
| Both A and B beat N with 99% frequency | Two pairwise context probabilities | A–B must be 50–50; BTL/IIA holds |
| All 200 marginal coin probabilities are 99.5% | `p_i=.995` in that context | Independence, infinite extendibility, or `P(all)>0` |
| Weakly negative pairwise correlation in 200 coins | Not an infinitely exchangeable Bernoulli marginal | A physical mechanism or supernatural interaction |
| Positive pairwise correlation | Some second-order dependence | De Finetti mixture; lower bound `J≥p^n` |
| Three equal-boost marginals at 66.5% | Probabilistic means under a chosen budget rule | An optimal **all-success** allocation without knowing dependence |
| Only the all-success frequency | A single joint observable | A unique luck mechanism or causal explanation |

**Precise model selection:** To distinguish M2 from M3, measure batch-size-specific individual marginals `p_i^(n)`; to distinguish independent M2 from finite dependence, measure joint and higher-order frequencies; to test M1, measure multiple candidate sets and odds invariants. These are *hypothetical future experiments*, not an assertion that repeated independent in-story trials can be obtained.

## 6. Research novelty and canon audit

### Established prior work (not new theorems)

1. **de Finetti representation and its infinite-sample requirement** — Werner Kirsch, *An elementary proof of de Finetti's theorem*, *Statistics & Probability Letters* **151** (2019), 84–88, DOI: https://doi.org/10.1016/j.spl.2019.03.014 .
2. **Finite exchangeable extendibility** — Takis Konstantopoulos and Linglong Yuan, *On the extendibility of finitely exchangeable probability measures*, *Transactions of the American Mathematical Society* **371** (2019), 7067–7092. DOI: https://doi.org/10.1090/tran/7701 .
3. **Sharp bounds with additional event information** — Hoppe and Nediak, *Fréchet optimal bounds on the probability of a union with supplementary information*, *Statistics & Probability Letters* (2008), journal page: https://www.sciencedirect.com/science/article/pii/S016771520700243X .
4. **Exchangeable Bernoulli event bounds** — Zaigraev and Kaniovski, *Exact bounds on the probability of at least k successes in n exchangeable Bernoulli trials as a function of correlation coefficients*, *Statistics & Probability Letters* (2010), https://www.sciencedirect.com/science/article/pii/S0167715210000714 .
5. **Random choice and Luce's axiom** — *Multinomial Logit Processes and Preference Discovery: Inside and Outside the Black Box*, *Review of Economic Studies* **90** (2023), https://academic.oup.com/restud/article/90/3/1155/6654601 .
6. **Finite exchangeable sums with negative dependence** — *Sums of Exchangeable Bernoulli Random Variables for Family and Litter Frequency Data*, journal full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2682719/ .

These references corroborate the *mathematical framework and prior-art boundaries*. The numerical examples, sharp 200-to-201 approximation within our chosen example, and new illustrative constructions are **Phase 4 derivations/syntheses of established mathematics**, with explicit proofs or computations provided. They should not be advertised as breakthroughs without a separate theorem-level originality audit.

### Canon verification debt — still open

- Verify the specific Lucky Coin ability/activation passages against original licensed WEBTOON episodes and record panel/episode evidence.
- Distinguish statements in fan-maintained references from authenticated primary text.
- Do **not** assert a fixed luck budget, coin independence, a duel of two identical Absolute Luck users, exactly one failure among 200, or numerical frequency measurements as story facts.

## 7. Reproducibility and gate audit

Run `python phase4_verify.py` in the Phase 4 directory. Requires Python ≥3.10 and SciPy; no GPU, paid service, secret or network needed. The script:

1. Replays the frozen **Phase 3 verifier**, which itself replays Phase 2; SHA256 checks ensure those outputs did not change.
2. Checks the **single-space random-ranking counterexample** and BTL odds invariant with exact rational arithmetic.
3. Solves **16 pairs** of linear programs for sharp event bounds (`n=2...5`, four marginal values).
4. Verifies two exact triple laws and the positive-pairwise-covariance counterexample.
5. Checks the 200-to-201 exchangeability covariance contradiction and sharp total-variation gap `1/201`.
6. Verifies the finite-extension count bound on a grid of **55** additional `n,r` cases.
7. Constructs dependent M3 counterexamples and checks **8 optimization LPs** (all/any objectives, equal/concentrated, upper/lower).
8. Verifies heterogeneous-baseline and nonlinear-response counterexamples.

Results are in `phase4_validation.json` (full data) and `phase4_model_bounds.csv` (compact robust intervals).

**Scope of "PASS":** Every check above has a derivation or explicit witness and passed under the stated finite mathematical models; it is **not** a formal machine-checked proof system, empirical validation of fiction, or certification of novel science.

### Completion gate

| Required Phase 4 deliverable | Evidence | Verdict |
|---|---|---|
| Preserve prior paradoxes and phase baselines | Replay + hashes | PASS |
| Test M1 against coherent alternatives | Random-ranking law | PASS |
| Check sharp event bounds | Proof + LP endpoints | PASS |
| Challenge exchangeability and extensibility | Correlation proof + 201 count bound | PASS |
| Test higher-order dependence | Identical pairwise laws; positive-covariance counterexample | PASS |
| Challenge M3 optima | Dependence, heterogeneity, nonlinear response | PASS |
| Clarify what observations can identify | Distinguishability table | PASS |
| Avoid novelty and canon overclaims | Explicit scope and source debt | PASS |

**Final Phase 4 verdict: PASS for proof/stress-test work.**

## 8. Handoff to Phase 5 — Computational Experiments

The next phase should simulate **existing precisely specified** models and compare empirical estimates to exact analytic predictions. Suggested protocols:

- Sample `n∈{3,10,50,200}` under independent, common-latent, and exactly-one-failure (finite) laws. Record whole-batch success and individual outcomes; report confidence intervals and seeds.
- For three-coin laws L/H, deliberately attempt identification with only marginal and pairwise statistics; then add triple observations and test distinguishability.
- Compare equal vs concentrated budget policies under independence **and** the Phase 4 adversarial couplings.
- Check whether observations from different context sets can identify BTL/IIA or only estimate within-context win probabilities.
- Explicitly separate **mathematical simulations** from canon measurements. Do not claim that simulation confirms the webtoon or demonstrates a new physical phenomenon.

For the eventual Gojo-style essay, the strongest arc is: **Two 99% winners → coherence of context → 200 near-certain coins with certain failure → finite versus infinitely extensible luck → the dependence of optimal luck on what success means.**