# Absolute Luck — Phase 1 Deep Novelty and Mathematical Feasibility Audit

**Date:** 2026-11-07  
**Track:** Mathematical research first; Gojo-style explanatory essay second.  
**Decision:** **GO** for technical model development and rigorous exposition; **HOLD** on claiming an original theorem or journal-ready paper.  
**Scope:** Follow-up to `absolute_luck_phase0_phase1_audit_2026-11-06.md`. This report updates and extends the preliminary Phase 1 literature screen. No fictional episode is counted as empirical frequency data.

## 1. Core research question (revised)

What can be rigorously inferred and optimized when an uncertain task has high success probability in isolation but lower reliability when several tasks execute concurrently, under an execution deadline and limited reliability-enhancement resources?

This is deliberately **not** framed as "luck contradicts probability theory". Different batch sizes can define different statistical contexts and hence different random variables.

## 2. Sources checked and substantive overlap

| Source | Verifiable work and date | Core overlap | Assessment |
|---|---|---|---|
| A | Shaked & Shanthikumar, *Optimal allocation of resources to nodes of parallel and series systems*, **Advances in Applied Probability** 24(4):894–914 (1992). https://doi.org/10.2307/1427718 | Fixed resources allocated to improve reliability in series and parallel systems; stochastic order/majorization methods. | Generic equal-versus-concentrated allocation is not novel. |
| B | Falk, Singpurwalla & Vladimirsky, *Reliability Allocation for Networks and Systems*, **SIAM Review** 48(1):43–65 (2006). https://doi.org/10.1137/S0036144503434493 | Reliability allocation with component interdependencies, including networks and series systems. | Simply introducing dependence is insufficient. |
| C | Dzhafarov & Kujala, *Context–content systems of random variables: The Contextuality-by-Default theory*, **Journal of Mathematical Psychology** 74:11–33 (2016). https://doi.org/10.1016/j.jmp.2016.04.010 | Variables recorded in separate experimental contexts are distinguished; context-induced marginal changes are direct influences, not automatically exotic contextuality. | "Single-coin probability differs from simultaneous-coin probability" is conventional context dependence. |
| D | Fontaine, Mannor & Perchet, *An adaptive stochastic optimization algorithm for resource allocation*, **Proceedings of ALT**, PMLR 117:319–363 (2020). https://proceedings.mlr.press/v117/fontaine20a.html | Sequential stochastic budget allocation, diminishing returns, adaptation and regret guarantees. | Sequential decision-making under resource constraints is well established. |
| E | Fontem, *Budget allocation via data-driven distributionally robust probability maximization*, **Computers & Operations Research** 195:107605 (2026). https://doi.org/10.1016/j.cor.2026.107605 | Binary outcomes, concave resource-response, threshold-attainment probability, empirical distribution ambiguity via total variation, exact optimization method. | **Strongest static-probability-optimization overlap.** The public indexed text includes the mathematical model and algorithm description. |
| F | Koole & Righter, *A Stochastic Batching and Scheduling Problem*, **Probability in the Engineering and Informational Sciences** 15(4):465–479 (2001). https://doi.org/10.1017/S0269964801154033 | Random batch scheduling, policy structure, polynomial-time optimal-policy computation for studied cases. | Batched stochastic scheduling is an old and active line. |
| G | Agnetis, Hermans, Leus & Rostami, *Time-critical testing and search problems*, **European Journal of Operational Research** 296(2):440–452 (2022). https://doi.org/10.1016/j.ejor.2021.03.038 | Parallelization versus sequential testing to meet deadlines; formulations and complexity analysis. | Adding a deadline to parallel-vs-sequential success does not by itself create novelty. |
| H | Wang et al., *On Time, Within Budget: Constraint-Driven Online Resource Allocation for Agentic Workflows*, arXiv:2605.06110 (May 2026). https://arxiv.org/abs/2605.06110 | Finite-horizon online planning over parallel tasks; maximizes successful completion probability subject to budgets and deadlines. | **Strongest dynamic-workflow overlap found**, currently a preprint (do not assume peer review). |

These works differ in details; this comparison does **not** assert they solve the same exact proposed model. Fontem's source was available as indexed mathematical text; some older publisher articles provided only abstracts and metadata. This is a targeted literature screen, *not* an exhaustive theorem-by-theorem novelty certification.

## 3. A validated, sharp but **classical** baseline

Let event `A_i` denote success of coin/task `i` **in the same concurrent experiment**, with marginal `p_i = P(A_i)` and joint success rate `q = P(A_1 ∩ ... ∩ A_n)`. Then

`max(0, Σ p_i − (n − 1)) ≤ q ≤ min_i p_i`.

The left inequality is the Fréchet–Boole lower bound. Thus `Σp_i ≤ (n − 1) + q`.

Suppose single-task success probability for each task is `s` in a different, isolated context, and define aggregate context change `D = Σ (s − p_i)` (not necessarily each summand nonnegative). Then

`D ≥ n*s − (n − 1) − q`.

If `s = .995`, `n = 3`, and **hypothetically** `q = .60`, then:

- With unchanged concurrent marginals `p_i=.995`, the joint probability must be at least `.985` — inconsistent with the assumed `.60`.
- Sum of concurrent marginal probabilities can be at most `2.60`.
- The aggregate marginal decrease relative to three isolated-context probabilities must be at least `2.985−2.60=.385` (38.5 percentage points).
- Therefore at least one task's marginal must drop by `0.385/3≈0.12833` (12.83 percentage points).

**Sharpness witness:** Assign probability `.60` to outcome `(1,1,1)`, and probability `.40/3` to each of `(1,1,0)`, `(1,0,1)`, `(0,1,1)`. Then every concurrent marginal equals `.60 + 2(.40/3) = .8666667`, their sum is exactly `2.60`, and the lower bound is attained. A separate isolated experiment can independently stipulate success probability `.995` without contradiction.

**Computational sanity check:** A SciPy linear program over the eight outcome probabilities for `n=3`, fixing `q=.60` and imposing `p_i≤.995`, returned the exact optimum `Σp_i=2.60`; aggregate decrease `.385`. This checks arithmetic and feasibility but does **not** establish novelty.

**Interpretive guardrail:** A low joint success probability could arise from dependence while preserving the individual probabilities only down to the Fréchet lower bound. The bound supplies a necessary context change if observed joint success falls below that threshold. It does not infer why context changes occurred, or identify a supernatural mechanism.

## 4. Candidate formulations, with gates

### Candidate A: Context-penalized execution with limited rounds (retain for formal tests)

- `N` binary tasks, `T` available rounds, and a remaining-task set `U_t`.
- In round `t`, choose a batch `S_t ⊆ U_t` plus a nonnegative reliability-enhancement allocation `x_{i,t}` with budget `Σ_{i∈S_t} x_{i,t} ≤ B_t`.
- Conditional success probabilities can depend on batch size, selected tasks, remaining budget and an explicitly modeled latent state, e.g. `p_i(S_t,x_t,z_t)`.
- The outcome joint law must be specified or placed in a mathematically explicit ambiguity class. **Do not assume independence.**
- Goal: `max_π P_π(required task successes completed by round T)`.

This is a general finite-horizon stochastic control / scheduling formulation. **It is not novel as written.** A claim of novelty would require a particular, defensible structural theorem, sharp bound, computational improvement or identifiable phenomenon absent from the near-overlap sources.

**Minimal solvable pilot:** Start with `N≤6`, `T≤3`, known probability response functions and exactly specified dependence models. Enumerate all policies as a gold standard; compare any dynamic-programming scheme with the exact enumerated optimum. This avoids claims based solely on Monte Carlo error.

**Main risk:** Established stochastic batching, deadline scheduling, and 2026 agentic workflow allocation may already cover the proposed trade-off in more general forms.

### Candidate B: Infer unavoidable context deterioration from group success (retain only as an expository baseline)

Use sharp Fréchet bounds to place certified lower bounds on aggregate marginal changes when only isolated probabilities and a concurrent all-success rate are given. The result in §3 demonstrates this approach.

**Verdict:** Mathematically sound, conceptually compelling, *not new* as a mathematical theorem. Use in exposition, diagrams, or sanity tests.

### Candidate C: General luck-budget allocation across independent coins (reject for original-paper thesis)

Suppose independent `p_i=.5+x_i`, `Σx_i≤B`. Equal boosts maximize all-success probability, whereas a concentrated boost maximizes at-least-one-success probability under the simple capped model. These are known Jensen/majorization and series/parallel reliability consequences.

**Verdict:** Do not claim novelty. Useful as a deliberately simple opening paradox for the essay.

## 5. Strongest technical hypotheses to try *without presuming originality*

1. **Policy structure:** Is an optimal batch size monotone in remaining rounds, remaining tasks and resource level for an explicitly specified concave context-penalty response? Search for counterexamples first.
2. **Dependence robustness:** Under a narrowly defined family of joint laws or common-shock processes, can a policy yield a sharp and efficiently computable success guarantee beyond existing reliability bounds?
3. **Sequential vs simultaneous information:** When a first outcome reveals information about a shared hidden success factor, is there a rigorously characterized region where adaptive serial execution dominates a parallel policy despite higher time cost? This is a familiar value-of-information theme, so a **new result cannot be presumed**.

Any result should be benchmarked against a known-optimal small-instance solver, not just heuristic baselines.

## 6. Hard no-go statements

- No new theorem has yet been proved beyond classical Fréchet consequences.
- A "new probability paradox" based on changing contexts is not novel.
- Generalizing to correlated coins or adding a fixed budget alone is not novel.
- Adding deadlines or allowing batches alone is not novel.
- Simulation graphs alone would not validate a mathematical originality claim.
- The original webtoon is not a data-generating process from which empirical probability estimates can be derived by selecting dramatic scenes.

## 7. Recommended next gate (Phase 1B → Phase 2)

1. Freeze one **explicit** context-penalty function and one dependence family; mark them hypothetical.
2. Read exact relevant theorems in Fontem (2026), Koole & Righter (2001), Agnetis et al. (2022), and Wang et al. (2026), where accessible; make an assumption-by-assumption overlap table.
3. Formulate a falsifiable, narrowly stated proposition about the optimal policy. Prove or disprove it by small-instance exhaustive enumeration and counterexample search.
4. If theorem degenerates into known convexity, DP or stochastic order results, pivot before drafting a research-style claim.
5. Keep a separate essay outline based on **verified mathematical facts**, independent of whether original research succeeds.

**Research-phase decision:** The source audit supports continued theoretical exploration, but **there is no defensible claim of an original publishable result yet**. Candidate A is the best-defined test bed, not a validated novel research contribution.
