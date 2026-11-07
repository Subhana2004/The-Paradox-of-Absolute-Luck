# Absolute Luck — Phase 0 Canon Audit and Phase 1 Prior-Art Audit

**Date:** 2026-11-06  
**Project:** Original mathematics first; Gojo-style explanatory essay second.  
**Status:** Initial source/prior-art screening completed; original research contribution **not yet established**.

## 1. Scope and evidence classification

This project uses *Hardcore Leveling Warrior* by Sehoon Kim as a fictional stimulus for mathematical modeling of resource-constrained probability amplification. The comic is **not empirical data** for estimating a stochastic law. Separate (a) licensed original scenes, (b) archived reproductions, (c) fan summaries, and (d) researcher-specified hypothetical models.

### Canon claims

| Claim | Current best evidence | Source grade | Decision |
|---|---|---|---|
| Official series and creator | Official WEBTOON series page | Primary | Confirmed |
| Lucky Coin normally 50% and single-use activation over 99% when enhanced | Screenshot reproduced in a third-party character profile; fan wiki | Reproduced original-looking panel / secondary | Strong indication; verify the licensed episode directly |
| Simultaneous multiple coins are possible | Fan descriptions; examples in episode guides | Secondary | Working assumption; verify panels |
| Simultaneous use markedly reduces luck effectiveness | Fan wiki (Absolute Luck and Skills) | Secondary | Plausible; exact functional law unknown |
| Number of coins increases duration penalty for buffs | Fan wiki (Lucky Coin / Skills) | Secondary | Separate from probability penalty; do not conflate |
| First appearance of trait in S1 Ep 25 | Fan wiki | Secondary | Target for direct review |
| Three coin heads in S1 Ep 83 | Fan wiki usage table | Secondary | Target for direct review, counters blanket 'multi-coin never works' |
| Floor-related skill uncertainty in S1 Ep 139 | Fan wiki usage table | Secondary | Confounder / context effect; verify |
| Three-coin buff in S1 Ep 138, single buff not desired in Ep 142 | Fan wiki usage table | Secondary | Check whether 'success' means activation or desired buff |
| Finite divisible total luck budget, independence, equal allocation, deterministic dilution law | No canon evidence found | Hypothetical research assumptions | Do not present as story facts |

**Primary source:** https://www.webtoons.com/en/action/hardcore-leveling-warrior/list?title_no=1221

**Secondary / reproduction sources:**
- https://hardcorelevelingwarrior.fandom.com/wiki/Absolute_Luck
- https://hardcorelevelingwarrior.fandom.com/wiki/Lucky_Coin
- https://hardcorelevelingwarrior.fandom.com/wiki/Hardcore_Leveling_Warrior/Skills
- https://animevice.boards.net/thread/14724/leveling-warrior-character-profile (includes reproduced panel asserting 50% and >99%)

**Primary-source blockage:** The official series page establishes the work and author but individual relevant panels are not reliably text-extractable here and some episodes require WEBTOON app access. No original-episode primary verification was completed. Do not elevate fan interpretations into primary evidence.

## 2. Formal modeling distinctions

Let Y_i^(S) be the binary success indicator for coin i when the simultaneously active set is S; let p_i(S)=P(Y_i^(S)=1). The single-coin statement is about p_i({i}), not automatically p_i(S) with |S|>1.

Separate at least three mechanisms:
1. **Fixed marginals, dependence changes:** p_i(S)=p_i({i}); correlations change. Marginal event bounds still apply within the same context.
2. **Context-dependent marginals:** p_i(S) decreases when S grows, independent of any correlation change.
3. **Resource allocation:** a hypothetical total boost B is divided among several coins, p_i(S)=1/2+x_i, x_i>=0, sum_i x_i<=B and x_i<=1/2. This does **not** come from canon.

Also separate (i) coin flip activates, (ii) favorable buff is selected, and (iii) a buff lasts long enough; they are distinct random/temporal outcomes.

### Foundational, previously known probability bound

For n events in one probability space, with marginal probabilities p_i, the sharp Fréchet/Boole bound is

max(0, sum_i p_i-(n-1)) <= P(all succeed) <= min_i p_i.

For 3 coins each with p_i=.995 in the **same simultaneous experiment**, all succeed with probability at least .985, regardless of dependence. Thus a very low joint success rate is incompatible with keeping the same .995 marginals *within that setting*. This does not contradict >99% success in a **single-coin** setting, which is a different experiment.

Source: https://causality.cs.ucla.edu/blog/index.php/2019/11/05/frechet-inequalities/

### Illustrative allocation comparison (old mathematics, not a new theorem)

Assume two independent fair coins and fixed total additive probability boost B=.495; p_i=.5+x_i. Two possible allocations:

| Allocation | p_1 | p_2 | P(both succeed) | P(at least one succeeds) |
|---|---:|---:|---:|---:|
| Equal, x_1=x_2=.2475 | .7475 | .7475 | .55875625 | .93624375 |
| Concentrated, x_1=.495,x_2=0 | .995 | .5 | .4975 | .9975 |

General justification under independence and B<=.5: equal boosts maximize product_i(.5+x_i) (Jensen/concavity of log); concentrating boosts minimizes product_i(.5-x_i), and so maximizes 1-product_i(.5-x_i) (minimum of concave function over simplex occurs at an extreme point). This is a **classical optimization consequence**.

## 3. Verified prior-art anchors and overlap screening

1. **Mueller & Pearl (2019), “Fréchet Inequalities – Visualization, Applications, and History”**. The n-event bounds are established mathematics. https://causality.cs.ucla.edu/blog/index.php/2019/11/05/frechet-inequalities/
2. **Dzhafarov & Kujala (2016), “Context–content systems of random variables: The Contextuality-by-Default theory,” Journal of Mathematical Psychology 74:11–33**, DOI 10.1016/j.jmp.2016.04.010. Distinct contexts need different variable treatment; specialized contextuality claims require stronger conditions than a simple context effect. https://www.sciencedirect.com/science/article/pii/S0022249616300207
3. **Shaked & Shanthikumar (1992), “Optimal allocation of resources to nodes of parallel and series systems,” Advances in Applied Probability 24(4):894–914**, DOI 10.2307/1427718. Resource allocation in series/parallel reliability already well developed. The Cambridge page lists online publication 2016 but the ORIGINAL print publication is **1992**. https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/optimal-allocation-of-resources-to-nodes-of-parallel-and-series-systems/312778DC33D2D6667D43891C495DAD92
4. **Falk, Singpurwalla & Vladimirsky (2006), “Reliability Allocation for Networks and Systems,” SIAM Review 48(1)**, DOI 10.1137/S0036144503434493. Explicitly studies allocation with component dependence; cannot claim dependence alone as novel. https://epubs.siam.org/doi/10.1137/S0036144503434493
5. **Kim & Kim (2022 print; online 2021), “Optimal allocation of reliability improvement target under dependent component failures”**, DOI 10.1177/1748006X211035635. Common-cause and cascading failures with allocation interdependence. https://journals.sagepub.com/doi/10.1177/1748006X211035635
6. **Zhang, Yan & Wang (2022), “Reliability optimization of parallel-series and series-parallel systems with statistically dependent components,” Applied Mathematical Modelling 102:618–639**, DOI 10.1016/j.apm.2021.10.003. Copula-based dependent reliability optimization. https://www.sciencedirect.com/science/article/pii/S0307904X21004649
7. **Kumar, Rao & Naqvi (2025), “Redundancy Allocation for Series and Parallel Systems: A Copula-Based Approach,” Applied Stochastic Models in Business and Industry 41(1)**, DOI 10.1002/asmb.2928. Dependence + redundancy allocation overlap. https://onlinelibrary.wiley.com/doi/full/10.1002/asmb.2928
8. **Alshehri (2026), “Reliability analysis of parallel systems with dependent components and Archimedean copulas,” Journal of Inequalities and Applications (2026):20**, DOI 10.1186/s13660-026-03427-6. Dependence modeling remains active in 2026. https://link.springer.com/article/10.1186/s13660-026-03427-6
9. **Fontem (2026), “Budget allocation via data-driven distributionally robust probability maximization,” Computers & Operations Research 195:107605**, DOI 10.1016/j.cor.2026.107605. **Major near-overlap:** binary outcomes, limited budget, aggregate-return success threshold, unknown joint probabilities, robust optimization. https://www.sciencedirect.com/science/article/pii/S0305054826002236
10. **Zhang, Li & Fang (2026), “Reliability Certification and Tail-Risk Assessment of k-Out-of-n Systems Under Widely Orthant Dependence,” IEEE Access 14:141158–141172**, DOI 10.1109/ACCESS.2026.3729824. Product inequalities / concentration / copula-free bounds already studied. https://ieeexplore.ieee.org/abstract/document/11675832

**Access limitation:** This screening compared verified abstracts/metadata and accessible excerpts, **not** a full-text theorem-by-theorem novelty proof of all works. A missing exact match is not evidence of novelty.

## 4. Initial novelty decisions

| Candidate claim | Verdict | Reason |
|---|---|---|
| Near-certain marginals constrain joint event | NOT NOVEL | Fréchet/Boole bounds |
| Single-use 99% does not imply concurrent 99% | NOT NOVEL | Context-specific probability definitions |
| Uniform allocation best for independent all-success goal | NOT NOVEL | Concave optimization / series reliability |
| Concentration best for independent any-success goal | NOT NOVEL | Parallel reliability / concave optimization |
| Dependence-aware optimization with budget | HEAVY PRIOR-ART OVERLAP | Reliability allocation and copula methods |
| Distributionally robust budget to maximize threshold attainment | MAJOR PRIOR-ART OVERLAP | Fontem 2026 near match |
| Dynamic coupling of simultaneous vs sequential activation under a **specified new** mechanism, with sharp regime-switching bounds | UNPROVEN CANDIDATE ONLY | Requires exact problem statement and full-text comparison with dynamic allocation, stochastic scheduling, and robustness literature |

### Research gate

- **GO** for a rigorous mathematical investigation and accompanying essay.
- **CONDITIONAL / HOLD** for claiming an original research paper. Novel theorem or algorithm has not been identified or proved.
- **NO-GO** for advertising familiar bounds or Jensen-style resource allocation as novel.

## 5. Next research sequence

1. Verify S1 episodes 25, 83, 138–142 directly on the licensed platform where available, logging precise scene, asserted probability, concurrency, buff selection, and buff duration. The secondary-source scenes can prioritize review but cannot replace it.
2. Extract the mathematical statements and the assumptions under which they hold from Falk et al. (2006), Shaked & Shanthikumar (1992), Kim & Kim (2022), and especially Fontem (2026). Full text when legitimately accessible; otherwise maintain uncertainty.
3. Formulate a **new question** that includes explicitly stated sequential and concurrent execution rules, context-dependent marginals, reward definition, and an allowed family of joint distributions. Establish at least one mathematically nontrivial theorem beyond the baseline literature or honestly pivot to an expository paper.
4. Create exact small-n enumerations or linear programming benchmarks before large Monte Carlo simulation. Verify bounds and search for counterexamples to any proposed theorem.
5. Only after novelty survives: manuscript; then the Gojo-style accessible essay with citations and clear separation from canon.

## 6. Scientific cautions

- The story depicts luck, but does not provide repeated independent measurements suitable for estimating real frequencies. Do not fit arbitrary power laws to selected narrative scenes.
- ‘Simultaneous 3 heads’ is not a contradiction of a qualitative luck penalty. A rare event remains possible.
- ‘Buff expiration’ and ‘coin activation’ are distinct mechanisms and must not be conflated.
- The research must be useful without relying on an unsupported claim that a fictional story violates probability laws.

**Audit conclusion:** A compelling exposition is feasible now. An original research contribution remains contingent on defining, differentiating, and proving something that reliability and robust optimization literature has not already established.
