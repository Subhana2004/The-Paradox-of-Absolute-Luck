# Absolute Luck — Phase 3: Mathematical Model Development

**Date:** 7 November 2026  
**Project:** *The Paradox of Absolute Luck: Can Probability Favor Everyone?*  
**Method:** Gojo-style mathematical investigation: fictional premise → contradiction audit → mathematically consistent alternatives → precise predictions → adversarial counterexamples.  
**Phase status:** **PASS (construction/model-development gate)**, subject to the explicit novelty and canon limitations below.  
**Inputs:** Unmodified copies of the Phase 2 report, verification script, and validation results are under `source_phase2/`. Running `phase3_verify.py` replays the Phase 2 tests before any Phase 3 tests.

## Executive findings

1. **Collision:** a 99% probability of winning *against an ordinary opponent* can coexist for two lucky players without either retaining a 99% probability *against the other*. Fixed competitive weights produce a coherent model. However, those isolated results alone cannot identify fixed weights, and a single counterexample to the weight model is given.
2. **Multiplication:** even knowing the success probability of every coin *and every pair of coins* can fail to determine the chance that *all* coins succeed. Two exact, exchangeable three-coin distributions agree on all single- and pairwise measurements but have all-success probabilities **30% and 40%**. An additional pairwise-independent parity example yields **0% and 25%** all-success at 50% marginal reliability.
3. **A structural divide:** Phase 2's 200-coin example (each marginal = 99.5%, all-success = 0) is mathematically valid for a *finite* exchangeable family but is impossible under an *infinitely exchangeable Bernoulli sequence*. Under the latter hypothesis, de Finetti's theorem plus Jensen's inequality requires all-success probability at least `0.995^200 ≈ 36.6958%`. This is a comparison of known probability theory, **not** a new theorem.
4. **Budgeted amplification:** if a total 0.495 boost is allocated across three independent fair-baseline coins, equal allocation maximizes the probability *all three* succeed (29.4079625%), whereas concentration on one coin maximizes the probability *at least one* succeeds (99.875%). This is a particular established optimization pattern; conclusions depend on the budget constraint and independence.
5. **Identifiability:** an observed 60% chance that three coins all succeed is compatible with multiple mechanisms exhibiting very different individual marginals. Observing only the collective outcome cannot determine the source of the effect.

The original WEBTOON scenes have **not** been independently rechecked; the single-coin >99% statement is described in secondary fan-maintained documentation. The values 99%, 99.5%, 60%, 0.495, and all toy trial probabilities in this report are **hypothetical**. The source material does not provide repeated probabilistic data for any of these models.

---

## I. Preserve Phase 2's two paradoxes exactly

**Paradox A — Luck Collision.** One no-tie zero-sum match between A and B has two mutually exclusive, exhaustive outcomes. Claims `P(A wins) >= 0.99` and `P(B wins) >= 0.99` **in that same match** would imply `1 >= 1.98`, impossible. By contrast, A beating a normal player with 99% probability and B beating a normal player with 99% probability in **separate contexts** is consistent and says nothing by itself about A-versus-B.

**Paradox B — Luck Multiplication.** In one context with `n` successes `E_i` and marginals `p_i`, let `J=P(E_1 ∩ ... ∩ E_n)`. Then:

\[
 \max\{0,\sum_{i=1}^n p_i-(n-1)\}\le J\le\min_i p_i.
\]

For three coins retaining `p_i=.995` simultaneously, `0.985 <= J <= 0.995`. For 200 coins with a uniform, exactly-one-failure construction, all marginals are `.995` while `J=0`. The distinction is **not** quantum contextuality, nor is it a mathematical contradiction. It is an elementary but surprising dependence effect.

Both events and probabilities require an explicit **context**: participant set for matches; number of active coins, allocation rule, dependence law, and the definition of collective success for coin experiments. Write `P_c(E)`, not a purported globally fixed `P(E)` when the experiment changes.

## II. Unified finite mathematical framework

Let `c` index an experimental context and `Ω_c` its allowed finite outcomes. Assign outcome masses `x_c(ω) >= 0` with `Σ_{ω∈Ω_c} x_c(ω) = 1`.

- A win claim `P_c(W_A) >= q_A` is the linear constraint `Σ_{ω∈W_A} x_c(ω) >= q_A`.
- A coin marginal is `p_i^(c) = Σ_{ω:ω_i=1} x_c(ω)`.
- A pairwise success is `r_ij^(c) = Σ_{ω:ω_i=ω_j=1} x_c(ω)`.
- All-success is `J_c = x_c(1,1,...,1)`.

These are **observables**, not mechanisms. A mechanism restricts the allowable `x_c`, possibly across contexts, through weights, independence, latent variables, or a resource rule. An apparent paradox is meaningful only after these assumptions and observation levels are distinguished.

The general feasibility linear program asks for any distribution satisfying such constraints. It can reject impossible combinations, but feasibility does not identify how a valid distribution is generated.

## III. M1 — Relative Luck in Competition

### M1.1 Definition and assumptions

For a no-tie contest with candidate set `S`, assign every contender a strictly positive strength `w_i`. Define:

\[
 P(i\text{ wins}\mid S)=\frac{w_i}{\sum_{j\in S}w_j}.
\]

This is the known Bradley–Terry–Luce / Luce-type weighted-choice mechanism. Its assumptions include stable weights *across the compared contexts*, strictly positive probabilities, and a form of independence of irrelevant alternatives (IIA). It is not implied by the webtoon and is not a novel probability law.

Set `w_A=w_B=99`, `w_N=1`. The model predicts:

| Contest | P(A wins) | P(B wins) | P(N wins) |
|---|---:|---:|---:|
| A versus N | 0.99 | — | 0.01 |
| B versus N | — | 0.99 | 0.01 |
| A versus B | 0.50 | 0.50 | — |
| A, B and N | 99/199 = 0.4974874... | 99/199 = 0.4974874... | 1/199 = 0.0050251... |

The 99% advantage has not disappeared: it is **relative to an ordinary challenger**, rather than an immutable winning probability. If `w_A=w_B` and A/B are the only possible winners, symmetry yields 50–50 *under this model*.

### M1.2 Derivable prediction and proof

For any included players `i,j` and any two contestant sets `S,T` containing them:

\[
\frac{P(i\mid S)}{P(j\mid S)}=\frac{w_i}{w_j}=\frac{P(i\mid T)}{P(j\mid T)}.
\]

**Proof:** the common denominator cancels. Consequently, adding a third player cannot change A's odds relative to B in this model. For three pairwise comparisons, odds ratios are multiplicatively transitive:

\[
 O_{AB}=O_{AN}\,O_{NB},\quad O_{ij}:=P(i\text{ wins versus }j)/P(j\text{ wins versus }i).
\]

These are falsifiable consequences of the **specific M1 model**, not general probability axioms.

### M1.3 Explicit counterexample: same isolated wins, different duel

A different set of **perfectly coherent context-indexed probability laws** is:

- `P(A defeats N)=0.99`;
- `P(B defeats N)=0.99`;
- `P(A defeats B)=0.90`, with `P(B defeats A)=0.10`.

Every match separately defines a valid normalized distribution. Yet A/B odds of 9 violate the BTL prediction of 1 implied by the other two contests (`99 × 1/99 = 1`). Thus **isolated 99% observations alone do not force M1's 50–50 head-to-head result**.

A special advantage, matchup asymmetry, or changing strengths could produce the 90–10 duel. To identify M1, measure multiple contest sets and test its odds-ratio invariants; merely saying both players are “lucky” is insufficient.

**M1 limitations:** This model applies to a *single winner* contest. It does not treat concurrent, nonexclusive coin activations unless one explicitly defines a choice competition between coin outcomes. Transferring the formula directly to independent successes would be a modeling error.

## IV. M2 — Fixed Marginals with Dependent Coin Outcomes

### M2.1 Definition

In a simultaneous experiment with `n` binary variables `X_i∈{0,1}`, insist `P(X_i=1)=p` for every coin, independent of `n`; allow an arbitrary joint distribution. The sharp event-intersection bounds are:

\[
L_n:=\max\{0,1-n(1-p)\}\le J_n:=P(X_1=\cdots=X_n=1)\le p=:U_n.
\]

Examples of coherent but divergent dependence rules:

- **Independent:** `J_n=p^n`.
- **Common outcome / perfectly coincident failures:** all `X_i=Z` with `P(Z=1)=p`, giving `J_n=p`.
- **Disjoint failures if `n(1-p) <= 1`:** allocate disjoint failure events of probability `1-p`, giving `J_n=1-n(1-p)`.
- **For `n=200,p=.995`:** one uniformly selected coin fails in every outcome, giving `J_200=0`.

No single one of these laws is canonically selected by “luck.”

### M2.2 Finite exchangeability versus a common latent luck parameter

A finite family is **exchangeable** when permuting the coin labels does not change its joint distribution. The 200-coin exactly-one-failure construction is exchangeable; the failing index is uniform over 200 states.

Compute its pairwise relationship exactly. For distinct `i,j`:

\[
P(X_i=1)=199/200=0.995,\qquad
P(X_i=X_j=1)=198/200=0.99.
\]

Thus the covariance is `0.99 − 0.995² = −0.000025` and the pairwise correlation is `−1/199 ≈ −0.0050251`. The failures are weakly negatively correlated pairwise, yet this accumulates to a collectively impossible all-success event.

**Stronger structural assumption:** suppose the coin sequence is *infinitely exchangeable*. De Finetti's classical theorem gives a random parameter `Θ∈[0,1]` such that, conditionally on `Θ`, outcomes are independent Bernoulli(`Θ`). For every finite `n`:

\[
p=\mathbb E[\Theta], \qquad J_n=\mathbb E[\Theta^n].
\]

For integer `n>=2`, `x↦x^n` is convex on `[0,1]`, and Jensen gives:

\[
\boxed{J_n=\mathbb E[\Theta^n]\ge(\mathbb E[\Theta])^n=p^n.}
\]

Also `Θ^n<=Θ`, giving `J_n<=p`. Consequently, within the **infinitely exchangeable** class:

\[
\boxed{p^n\le J_n\le p.}
\]

For `p=.995` and `n=200`, this means **`J_200 >= 0.3669578217`**, incompatible with the Phase 2 zero-joint construction. The latter cannot be the 200-variable marginal of an *infinitely exchangeable* Bernoulli sequence. Finite exchangeability alone **does not** justify de Finetti's infinite representation.

A coherent latent-mixture example: let `Θ=.99` or `Θ=1`, each with probability 1/2. Then `E[Θ]=.995` and `J_n=(.99^n+1)/2`. At `n=200`, `J_n≈.56698984`, versus independent `.36695782`, versus finite one-failure construction `0`.

**Mathematical meaning:** if “shared luck” denotes a hidden common environmental success rate with conditionally independent coins, it cannot explain the 200-coin zero-event paradox at unchanged 99.5% marginal reliability. If “shared luck” instead imposes finite negative dependence or a global exactly-one-failure rule, it can. These hypotheses are very different.

This observation follows directly from established results, notably de Finetti's theorem and Jensen's inequality; **no original theorem is being claimed**.

### M2.3 A stronger nonidentifiability result: same pairwise data, different collective success

Let `K=X_1+X_2+X_3` and assume exchangeability. Construct two valid distributions by specifying the probabilities `q_k=P(K=k)` and choosing uniformly among all `C(3,k)` bitstrings with `k` successes:

| Count of successes `K` | Law L | Law H |
|---|---:|---:|
| 0 | 0.10 | 0 |
| 1 | 0 | 0.30 |
| 2 | 0.60 | 0.30 |
| 3 | 0.30 | 0.40 |

Both laws have, for **every** coin `i`,

\[
P(X_i=1)=\mathbb E[K]/3=0.70,
\]

and, for **every** pair `i≠j`,

\[
P(X_i=X_j=1)=\mathbb E[K(K-1)]/6=0.50.
\]

But they have different triple-success probabilities:

\[
J_3^{(L)}=0.30\quad\text{and}\quad J_3^{(H)}=0.40.
\]

**Exact range with these observed one- and two-way marginals.** Let `t=P(K=3)`. For `p=.70` and `r=.50`, simple moment constraints give:

\[
q_3=t,\quad q_2=1.5-3t,\quad q_1=-0.9+3t,\quad q_0=0.4-t.
\]

Nonnegativity of all four `q_k` is equivalent to **`0.30 <= t <= 0.40`**. Hence the two displayed laws attain the *sharp* extremes. An independent linear program on **all eight 3-bit outcomes** confirms this range without imposing exchangeability beforehand.

The conditional success probability of the third coin after observing two successes differs:

\[
P(X_3=1\mid X_1=X_2=1)=J_3/r=0.60 \quad\text{versus}\quad 0.80.
\]

**Why this matters:** measuring each coin's success rate and *every pairwise success rate* is not sufficient to reconstruct the full three-way dependence mechanism. Third-order measurements add information.

### M2.4 Even pairwise independence does not imply joint independence

A smaller, vivid example uses fair (`p=.5`) coins. In **even-parity law**, give probability 1/4 to each of `000, 011, 101, 110`. In **odd-parity law**, give probability 1/4 to each of `111, 100, 010, 001`.

For *both* laws, every coin succeeds with probability 1/2 and **every pair** succeeds together with probability 1/4; hence each pair is independent. Yet:

\[
P(111)=0 \quad\text{(even parity)},\qquad P(111)=1/4\quad\text{(odd parity)}.
\]

For fully independent fair coins it would instead be `1/8`. Thus **pairwise independence is insufficient for the multiplication formula `p^n`**. This classical counterexample is a useful mathematical surprise for the essay.

**M2 limitations:** “Any dependence law is possible” is an unrestricted finite-model claim. Scientific explanations require physical or narrative mechanisms restricting dependence. The 200-coin construction is *not* a documented WEBTOON scene.

## V. M3 — Context-Sensitive, Resource-Limited Probability Amplification

### M3.1 Definition and assumptions

Model an ordinary coin's activation chance as `p_0=0.5` and a *hypothetical total boost* as `B=.495`. For an `n`-coin batch, allocate nonnegative boosts `b_1,...,b_n` with:

\[
\sum_i b_i=B,\qquad p_i=0.5+b_i,\qquad 0\le b_i\le0.5.
\]

For the baseline illustration, outcomes are independent *conditional on the selected allocation* (an explicit model assumption). Then:

\[
J_{\text{all}}=\prod_i(0.5+b_i),\qquad
J_{\text{any}}=1-\prod_i(0.5-b_i).
\]

This model is **deliberately hypothetical**. Neither a divisible 0.495 boost nor independence is evidenced by the story. The formulation deliberately separates the *resource* restriction from M2's *dependence* restriction; both could be combined in future research.

### M3.2 Two opposing optimization results

**Proposition M3-A (all coins succeed).** Equal allocation `b_i=B/n` maximizes `J_all` among feasible allocations.

**Proof:** The success probabilities have fixed sum `Σ p_i = n/2+B`. By AM–GM, their product is at most `((n/2+B)/n)^n = (1/2+B/n)^n`, with equality when all `p_i` are equal. As `B<=0.5`, equal allocation is feasible.

**Proposition M3-B (at least one succeeds).** For `0<=B<=0.5`, concentrating all boost on one coin maximizes `J_any`.

**Proof:** For any pair of boosts `x,y>=0` with `x+y<=B`, the associated failure-factor product is

`(1/2−x)(1/2−y) = 1/4−(x+y)/2+xy`.

For fixed sum, this is minimized when `xy=0`, moving the pair's total boost to one coordinate. Repeatedly merge any two positive boosts; at the end, one coordinate carries all `B`. That globally minimizes all-failure probability `Π_i(1/2-b_i)` and hence maximizes `J_any`. (For `B=0`, all allocations coincide.)

For `n=3`, compare:

| Allocation strategy | Coin success probabilities | All succeed | At least one succeeds |
|---|---|---:|---:|
| Equal boost | (0.665, 0.665, 0.665) | **0.294079625** | 0.962404625 |
| Concentrated boost | (0.995, 0.500, 0.500) | 0.248750000 | **0.998750000** |

This illustrates that the mathematical meaning of **“luckiest outcome” changes when the objective changes**. It is also classical reliability allocation behavior, not a newly established finding.

### M3.3 Different batch-size prediction

If all `n` coins share the boost equally, then:

\[
p_n=0.5+\frac{0.495}{n}, \qquad J_n=(0.5+0.495/n)^n.
\]

For example: `p_1=.995`, `p_2=.7475`, `p_3=.665`, `p_10=.5495`. For three coins the all-success probability is **29.4079625%**. Compare the **98.5% minimum** under M2 with three unchanged `.995` marginals. Thus a drastic three-coin decline is feasible under M3 but impossible under that fixed-marginal version of M2.

This is a *distinct prediction from a specified functional model*. It is **not** a deduction from the narrative that the ability must split its chance boost equally, or that its effective probability must follow `1/n`.

### M3.4 Counterexamples to overgeneralizing allocation

- If the goal is *at least one* success, equal sharing is **not** optimal (M3-B).
- If the individual outcomes are dependent after allocation, the product formulas fail; M2's constraints must be combined with M3's changing marginals.
- If the budget can be saved, re-used, replenished, or allocated adaptively over time, the one-shot AM–GM and pairwise arguments do not solve the sequential scheduling problem.
- If individual coins have different baseline probabilities or nonlinear response curves, equal `b_i` need not maximize all-success. For instance, with two independent coins having baselines `.2` and `.8` and total boost `.1`, applying all boost to the weaker coin gives `.3×.8=.24`, whereas equal boost gives `.25×.85=.2125` (assuming the boosts are feasible). Identical baselines are necessary for the simple equal-boost conclusion.

## VI. Cross-model observational equivalence and discrimination

### VI.1 Three very different explanations for the *same* observed 60% triple-success rate

Suppose only `J_3=0.60` has been observed in some hypothetical batch.

| Construction | Marginal probability of each coin | Triple success |
|---|---:|---:|
| Three independent equal coins | `0.60^(1/3) ≈ 0.84343` | 0.60 |
| Perfectly coincident outcomes | 0.60 | 0.60 |
| `P(111)=0.60`, each exactly-one-failure state has probability `2/15` | `13/15 ≈ 0.86667` | 0.60 |

All three distributions are coherent. Therefore the **collective success frequency alone** does not identify dependence or changing individual marginals. If each coin's individual reliability were measured and remained `0.995`, a 60% triple-success rate would instead be mathematically infeasible (Phase 2's strict bound).

### VI.2 Observation and falsification table

| What one can measure | What it can test | What it cannot establish alone |
|---|---|---|
| A versus N and B versus N win rates | Whether both are strong against N | The A-versus-B probability or BTL model |
| A versus B and three-player contests | BTL odds transitivity / IIA prediction | The full causal origin of a stable weight |
| Individual batch marginals `p_i^(n)` at n=1,2,3,... | Whether coin reliability actually changes with batch size | Whether outcomes are independent |
| Pairwise intersections in each batch | Pairwise dependence and correlation | Triple and higher-order joint dependence |
| Exact all-success events | Joint success for that batch | Unique underlying mechanism if the other observables are missing |
| Conditional higher-order success events, interventions changing batch size and allocation | Discriminates the explicit candidate mechanisms | Does not prove a fictional canon law without canonical evidence |

**Falsification examples:**

- If both A and B defeat N with 99% frequency but A defeats B with 90%, **fixed** BTL strengths inferred from those two normal matches fail; a context-specific contest model remains coherent.
- If three coins **each** retain `.995` batch reliability but `J_3=.60`, then **no** joint distribution on three Bernoulli successes can reproduce those exact claims; revisit measurements and definitions.
- If three batch marginals drop to `.665` and outcomes are independent, the equal-budget toy M3 predicts `J_3=.665^3≈.29408`, distinguishable from the fixed-marginal M2 prediction interval `[.985,.995]`.
- If 200 coin activations satisfy `p=.995` but `J_200=0` exactly, the infinitely exchangeable conditional-i.i.d. shared-parameter submodel is excluded; not *all* dependence models are excluded.
- If all individual/pairwise values in the `p=.7, r=.5` example are known, `J_3` remains in `[.3,.4]`; estimate three-way frequencies directly.

### VI.3 A caveat on experimental feasibility

The report gives *logical and exact numerical* predictions only. We possess **no canon-certified frequency dataset**. Repeated experimental trials would need independent runs at comparable conditions, clear event definitions, uncertainty intervals, and controls for changes in opponents, batch size, allocation and time. Near-99.5% probabilities make certain dependence differences between 2–3 coins numerically small, potentially requiring many trials to distinguish. No fabricated sample size or empirical confidence claim is made here.

## VII. Numerical model comparison (values are hypothetical)

The complete machine-readable values for batch sizes `n∈{1,2,3,5,10,50,100,200}` are in `phase3_predictions.csv`.

| n | M2: min possible `J_n` at p=.995 | M2 independent `J_n` | M2 latent mixture `J_n` | M3 equal budget, independent `J_n` |
|---:|---:|---:|---:|---:|
| 1 | 0.995 | 0.995 | 0.995 | 0.995 |
| 3 | 0.985 | 0.985074875 | 0.9851495 | 0.294079625 |
| 10 | 0.950 | approx. 0.95111 | approx. 0.95219 | approx. 0.00251002 |
| 200 | 0 | approx. 0.366958 | approx. 0.566990 | extremely close to 0 |

The M2 model above **holds individual marginal reliability fixed** at `.995`. The M3 model above changes it by batch size. Comparing different assumptions is the point; no one curve is “Absolute Luck's true distribution.” The plot `phase3_model_comparison.png` visualizes these curves (as probability percentages).

## VIII. Computational verification, reproducibility, and limitations

Run from this directory:

```bash
python phase3_verify.py
```

**Dependencies:** Python 3.10+ with SciPy. All checks are deterministic and run without GPU, accounts, or web connection. The script writes `phase3_validation.json` and `phase3_predictions.csv`.

The verification script performs:

1. A full replay of `source_phase2/phase2_verify.py` and equality comparison against the frozen Phase 2 JSON; it preserves the source project folder outside this package.
2. Exact M1 win probabilities, IIA odds ratios, and a valid non-BTL matchup counterexample.
3. Explicit exchangeable triple-success distributions with matching one- and two-coin statistics; an independent linear program proves `J_3∈[.3,.4]` given p=.7 and pairwise joint=.5.
4. A parity counterexample where every coin pair is independent but the triple is not jointly independent.
5. Finite 200-coin negative pairwise correlation, independent and infinitely exchangeable shared-latent benchmarks, and Jensen lower-bound inequalities.
6. Budget-allocation exact values and a finite-grid adversarial sanity check against the analytically proven optima.
7. Three incompatible marginal mechanisms producing the same `.60` three-way intersection.
8. Automated consistency checks across the model-prediction table.

**Numerical tests are not substitutes for proofs.** The proofs are the finite additivity argument (Phase 2), M1 denominator cancellation, sharp three-coin moment-polytope argument, Jensen's inequality under the explicit infinite-exchangeability assumption, and AM–GM/pairwise resource-exchange arguments. Linear programming independently checks selected finite cases.

### Adversarial limitations

- **Not canon:** `B=.495`, equal resource-sharing, latent `Θ`, exact 200-coin scenario, fair parity examples, and the 99%-versus-99% duel are mathematical constructions. The WEBTOON's detailed scenes remain to be checked in official episodes.
- **Not inferred:** normalization with strengths is a *hypothesis*, not a consequence of two reported favorable matchups.
- **Not proven original:** BTL/Luce models, Fréchet/Boole bounds, finite/infinite exchangeability distinctions, Jensen, AM–GM, and parity counterexamples are established ideas. What is original here is the educational arrangement, problem framing and specific illustrative comparisons—not a claimed new theorem.
- **Not one universal model:** collision (single-winner contest) and multiplication (potentially simultaneous successes) have different sample-space semantics. The unified language is context-indexed finite probability, not a fabricated universal law of luck.
- **Not statistically measured:** The numerical table is a set of exact theoretical model predictions; no values are estimates from comic panels or real experiments.

## IX. Phase 3 completion gate

| Gate | Evidence | Verdict |
|---|---|---|
| Preserve both Phase 2 paradoxes | Section I; source report and reproducible baseline replay | **PASS** |
| Construct at least three coherent models | M1, M2, M3 with explicit sample spaces/conditional assumptions | **PASS** |
| Derive falsifiable predictions | M1 odds invariance; M2 dependence bounds and exchangeability; M3 budget response curves | **PASS** |
| Prove core propositions | Sections III–V with classical proof steps | **PASS** |
| Attempt meaningful counterexamples | Non-BTL matchup, matching pairwise but differing triple, parity independence, asymmetric budget | **PASS** |
| Identify ambiguity / non-identifiability | Section VI's same-J constructions and identifiability matrix | **PASS** |
| Reproduce mathematical checks | `phase3_verify.py`, `phase3_validation.json`, CSV and baseline replay | **PASS** |
| Separate fiction, hypotheses and established math | Each model scoped, no novel theorem or canon-frequency claim | **PASS** |

**Decision: PHASE 3 COMPLETE — PASS.** This is a verdict on mathematical-model construction and verification, *not* on originality, scientific validation of the story, or publication readiness.

## X. Phase 4 handoff — proof stress testing and discriminating limits

Recommended priorities:

1. **Proof audit:** independently scrutinize assumptions, extremal constructions, and all statements about finite versus infinite exchangeability. Check if any claims are true only under symmetry or conditional independence.
2. **Adversarial models:** break M1's IIA, M2's fixed-marginal hypothesis, and M3's equal-baseline/additive-budget assumption with explicit distributions.
3. **Model-selection analysis:** derive the minimal observable statistics needed to separate candidate mechanisms under controlled contexts; quantify finite-sample uncertainty only after an actual experiment design is fixed.
4. **Novelty positioning:** document the mathematical ingredients as established theory and frame the eventual paper honestly as a rigorous mathematical investigation or exposition unless a genuinely new theorem is developed.
5. **Canon verification:** separately inspect the original WEBTOON episodes and replace any fan-only mechanical claim with a verified primary-source description; otherwise mark as tentative.

**Potential essay's central reveal:** “Two 99% chances cannot both be the chances of mutually exclusive winners in one contest. But 200 successes can each be 99.5%-likely even when the conjunction is impossible—unless we additionally assume a common latent probability mechanism that can be extended indefinitely. It is not the word ‘luck’ that determines the answer. It is what we assume about the probability model.”

## Verified mathematical references

- J. I. Yellott, *Luce's Choice Axiom* (2001), eScholarship (University of California): https://escholarship.org/uc/item/02b7s10w .
- Scholarpedia, *Luce's choice axiom* (2008), including independence of irrelevant alternatives and odds-invariance discussion: https://doi.org/10.4249/scholarpedia.8077 .
- Encyclopedia of Mathematics, *De Finetti theorem* (finite versus infinite exchangeability): https://encyclopediaofmath.org/wiki/De_Finetti_theorem .
- *An elementary proof of de Finetti’s theorem* (published journal article; notes that the theorem does **not** hold in general for finite exchangeable sequences): https://www.sciencedirect.com/science/article/pii/S0167715219300902 .
- Book of Statistical Proofs, *Jensen's inequality*: https://statproofbook.github.io/P/jens-ineq .
- Book of Statistical Proofs, *Bonferroni's inequality*: https://statproofbook.github.io/P/bonf-ineq.html .
- Sums of exchangeable Bernoulli random variables, a research discussion of negative correlation within finite exchangeable families: https://pmc.ncbi.nlm.nih.gov/articles/PMC2682719/ .
- Source work (fictional inspiration): https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221 .
- Secondary fan-maintained skill notes (mechanical specifics **not yet primary-verified**): https://hardcorelevelingwarrior.fandom.com/wiki/Hardcore_Leveling_Warrior/Skills .

### Reproducibility manifest

- `Absolute_Luck_Phase3_Mathematical_Model_Development_2026-11-07.md` — this audit and phase completion gate.
- `phase3_verify.py` — deterministic proofs-as-tests and adversarial model checks.
- `phase3_validation.json` — numerical trace, baseline replay, predictions and gate statuses.
- `phase3_predictions.csv` — tabular predictions suitable for independent plotting/analysis.
- `phase3_model_comparison.png` — visualization of selected hypothetical models.
- `source_phase2/` — copies of the Phase 2 report, code, and frozen validation record (provenance hashes recorded in Phase 3 JSON).