# Absolute Luck — Phase 5 computational preregistration

Date: 2026-11-07. This is an analysis plan for fully synthetic probability experiments; no licensed-comic observations were collected.

## Inputs and interpretation

Phase 4 is frozen as `phase4_input_unchanged.zip` and `source_phase4/`. The original Phase 4 archive's SHA-256 is recorded in validation metadata. No theorem novelty and no story-specific probability measurement are claimed.

## Simulation settings (declared before execution)

- Base seed: `20261107`. All scenarios have independent named PCG64 streams derived deterministically from SHA-256 labels and NumPy SeedSequence; streams do not depend on iteration order.
- Main runs: 120,000 independent **trials** per model/scenario. Coin outcomes within a trial may be dependent. 200-coin generation is chunked.
- Binomial event summaries: empirical rates, two-sided 95% Wilson score intervals, theoretical probabilities, 4.5-standard-error diagnostic tolerances plus 0.00025 for floating-point/boundary checks. Tolerances were chosen before simulation, not tuned post hoc. These diagnostic tolerances are not significance tests.
- Wilson coverage calibration: 600 independent binomial replicates with n=400 per probability in {0.005,0.3,0.4,0.5,0.995}; a rough 90%-99% calibration window, NOT a universal interval-coverage guarantee.
- Structural identifiability: M2 L/H with equal single/pairwise *marginals*. A measurement protocol that sees a single coin or one pair from each independent trial has identical likelihood under both. Three-way outcomes reveal a difference. Distinguishing accuracy uses only the all-three-success count and threshold 0.35, not optimally selected by training.
- M3: an explicit **fixed copula** across allocations (X1=1{1-U <= p1}, X2=X3=1{U <= p_i}) is paired using the same U for both equal and concentrated strategies. A second fixed copula (comonotonic) and independent outcomes are controls.
- Also test M1 BTL/Plackett-Luce exponential-race construction against Phase 4's coherent random-ranking counterexample.

## Experimental gates

1. Earlier Phase 2, 3 and 4 scripts replay in temporary copied artifacts without changing frozen baselines.
2. Analytical probabilities independently match simulation scenario definitions.
3. All simulated Bernoulli rates satisfy predefined 4.5-SE diagnostic thresholds.
4. The binomial Wilson interval coverage calibration falls within [0.90,0.99] on the five prespecified regimes, and reporting notes it is approximate.
5. Identical pairwise observed laws are proven exactly; triple observations provide information; sample-size discrimination is quantified.
6. Fixed-copula M3 concentration versus equal difference is positive and its paired confidence interval contains the analytic contrast.
7. A completely fresh replay of all Phase 5 experiment CSV/JSON outputs is byte-identical, with source hashes and all figures audited.

## Bibliographic methods references

Brown, Cai & DasGupta (2001), *Interval Estimation for a Binomial Proportion*, Statistical Science, https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/Interval-Estimation-for-a-Binomial-Proportion/10.1214/ss/1009213286

NumPy `Generator` documentation: https://numpy.org/doc/stable/reference/random/generator.html

SciPy binomial distribution: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

The mathematical background and story provenance are in the preserved Phase 4 report.