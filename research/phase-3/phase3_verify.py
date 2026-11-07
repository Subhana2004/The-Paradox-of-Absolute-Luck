#!/usr/bin/env python3
"""Absolute Luck Phase 3: exact model comparisons and adversarial tests.

All parameters are hypothetical; no WEBTOON measurements are claimed.
Requires Python 3.10+, SciPy (linear programming). No random experiments.
Re-runs the frozen Phase 2 verification copy before Phase 3 checks.
Writes phase3_validation.json and phase3_predictions.csv beside this file.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from itertools import product
from pathlib import Path
import subprocess
import sys
from typing import Dict, Tuple

from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
N = (1, 2, 3, 5, 10, 50, 100, 200)
P = 0.995
BASE = 0.5
BOOST = P - BASE
TOL = 1e-9


def near(a: float, b: float, tol: float = TOL) -> None:
    assert math.isclose(a, b, abs_tol=tol, rel_tol=0), (a, b)


def hashes() -> dict:
    names = ("Absolute_Luck_Phase2_Paradox_Construction_2026-11-07.md",
             "phase2_verify.py", "phase2_validation.json")
    return {name: hashlib.sha256((HERE / "source_phase2" / name).read_bytes()).hexdigest() for name in names}


def phase2_regression() -> dict:
    baseline = HERE / "source_phase2" / "phase2_validation.json"
    expected = json.loads(baseline.read_text(encoding="utf8"))
    # Copy of Phase 2 script writes only inside this Phase 3 package, not the original project.
    run = subprocess.run([sys.executable, str(HERE / "source_phase2" / "phase2_verify.py")],
                         cwd=str(HERE / "source_phase2"), capture_output=True, text=True)
    assert run.returncode == 0, run.stdout + "\n" + run.stderr
    observed = json.loads(baseline.read_text(encoding="utf8"))
    assert expected == observed, "Frozen Phase 2 baseline results changed on re-run"
    return {"passed": True, "last_line": run.stdout.strip().splitlines()[-1], "hashes": hashes()}


def weighted_choice(weights: dict, candidates: tuple) -> dict:
    assert all(weights[x] > 0 for x in candidates)
    total = sum(weights[x] for x in candidates)
    return {x: weights[x] / total for x in candidates}


def collision_checks() -> dict:
    w = {"A": 99.0, "B": 99.0, "N": 1.0}
    versus_normal_A = weighted_choice(w, ("A", "N"))["A"]
    versus_normal_B = weighted_choice(w, ("B", "N"))["B"]
    duel = weighted_choice(w, ("A", "B"))["A"]
    three = weighted_choice(w, ("A", "B", "N"))
    near(versus_normal_A, 0.99)
    near(versus_normal_B, 0.99)
    near(duel, 0.5)
    near(three["A"] / three["B"], 1.0)
    near(sum(three.values()), 1.0)
    # An alternative probability family matches BOTH vs-normal contests but
    # has a context-specific A-versus-B edge: violates BTL odds transitivity.
    counterexample = {"A_vs_N": 0.99, "B_vs_N": 0.99, "A_vs_B": 0.90}
    predicted_odds_A_B = (0.99 / 0.01) * (0.01 / 0.99)
    observed_odds_A_B = 0.9 / 0.1
    near(predicted_odds_A_B, 1.0)
    near(observed_odds_A_B, 9.0)
    assert abs(predicted_odds_A_B - observed_odds_A_B) > 1
    return {"lucky_vs_normal_A": versus_normal_A,
            "lucky_vs_normal_B": versus_normal_B,
            "equal_luck_duel_A": duel, "three_player": three,
            "context_specific_valid_non_BTL_counterexample": counterexample,
            "BTL_expected_A_vs_B_odds": predicted_odds_A_B,
            "counterexample_A_vs_B_odds": observed_odds_A_B,
            "IIA_test_passed": True}


def law_of_count_to_joint(n: int, masses: dict[int,float]) -> dict[tuple[int,...],float]:
    """Exchangeable bitstring distribution from P(K=number of successes)."""
    assert set(masses) <= set(range(n + 1))
    out = {}
    for k, mass in masses.items():
        assert mass >= 0
        for state in product((0, 1), repeat=n):
            if sum(state) == k and mass:
                out[state] = mass / math.comb(n, k)
    near(sum(out.values()), 1.0)
    return out


def moments(law: dict[Tuple[int,...],float], n: int) -> dict:
    near(sum(law.values()), 1.0)
    marginals = [sum(v for x, v in law.items() if x[i] == 1) for i in range(n)]
    pairs = {f"{i+1}{j+1}":sum(v for x,v in law.items() if x[i] and x[j])
             for i in range(n) for j in range(i+1, n)}
    all_success = sum(v for x,v in law.items() if all(x))
    return {"marginals": marginals, "pairs": pairs, "all_success": all_success}


def pairwise_nonidentifiability() -> dict:
    # Two 3-bit distributions with *identical* one- and two-body marginals.
    low = law_of_count_to_joint(3, {0: .1, 2: .6, 3: .3})
    high = law_of_count_to_joint(3, {1: .3, 2: .3, 3: .4})
    a, b = moments(low, 3), moments(high, 3)
    for i in range(3):
        near(a["marginals"][i], 0.7)
        near(b["marginals"][i], 0.7)
    for key in a["pairs"]:
        near(a["pairs"][key], 0.5)
        near(b["pairs"][key], 0.5)
    near(a["all_success"], 0.3)
    near(b["all_success"], 0.4)
    # Linear programming independently proves sharp bounds with these constraints.
    states = list(product((0,1),repeat=3))
    eq = [[1.0] * len(states)]
    rhs = [1.0]
    eq += [[float(x[i]) for x in states] for i in range(3)]
    rhs += [0.7] * 3
    eq += [[float(x[i] * x[j]) for x in states] for i,j in ((0,1),(0,2),(1,2))]
    rhs += [0.5] * 3
    goal = [float(all(x)) for x in states]
    lo = linprog(goal, A_eq=eq, b_eq=rhs, bounds=(0,None), method="highs")
    hi = linprog([-y for y in goal], A_eq=eq, b_eq=rhs,
                 bounds=(0,None), method="highs")
    assert lo.success and hi.success, (lo.message, hi.message)
    near(lo.fun, 0.3)
    near(-hi.fun, 0.4)
    # The conditional third success differs despite identical first/pairwise moments.
    return {"shared_marginals":a["marginals"], "shared_pair_intersections":a["pairs"],
            "law_low_count_masses":{"K0":.1,"K2":.6,"K3":.3},
            "law_high_count_masses":{"K1":.3,"K2":.3,"K3":.4},
            "min_all_success":lo.fun, "max_all_success":-hi.fun,
            "conditional_third_given_first_two_low":a["all_success"]/0.5,
            "conditional_third_given_first_two_high":b["all_success"]/0.5}


def parity_example() -> dict:
    even = {(0,0,0):.25,(0,1,1):.25,(1,0,1):.25,(1,1,0):.25}
    odd  = {(1,1,1):.25,(1,0,0):.25,(0,1,0):.25,(0,0,1):.25}
    a,b = moments(even,3),moments(odd,3)
    for law in (a,b):
        for m in law["marginals"]: near(m,.5)
        for p in law["pairs"].values(): near(p,.25)
    near(a["all_success"],0)
    near(b["all_success"],.25)
    return {"each_marginal":.5,"each_pair_intersection":.25,
            "all_success_even":a["all_success"],"all_success_odd":b["all_success"],
            "both_pairwise_independent":True, "neither_jointly_independent":True}


def finite_vs_infinite_exchangeability() -> dict:
    # exactly one of 200 coins fails, uniformly selected
    n=200
    p=(n-1)/n
    pair=(n-2)/n
    p2=p*p
    rho=(pair-p2)/(p*(1-p))
    near(rho, -1/(n-1), tol=1e-11)
    independent_joint=p**n
    # Theta is 1 or 0.99, each with probability 1/2;
    # P(success for all n) = E[Theta^n] in this infinitely extendible model.
    mixture_joint=(1+.99**n)/2
    near((1+.99)/2,p)
    assert mixture_joint > independent_joint > 0
    return {"n":n,"same_each_marginal":p,
            "finite_one_failure_joint":0.0,
            "finite_pair_success":pair,
            "finite_pair_correlation":rho,
            "independent_joint":independent_joint,
            "two_point_latent_mixture_joint":mixture_joint,
            "infinite_exchangeable_min_joint_by_Jensen":independent_joint,
            "finite_construction_not_infinitely_extendible":True}


def shared_budget_checks() -> dict:
    """Each chosen coin gets p_i=1/2+b_i, b_i>=0, sum b_i=0.495."""
    n=3
    equal_p=BASE+BOOST/n
    concentrated_p=BASE+BOOST
    J_equal=equal_p**n
    J_concentrated=concentrated_p*(BASE**(n-1))
    any_equal=1-(1-equal_p)**n
    any_concentrated=1-(1-concentrated_p)*(1-BASE)**(n-1)
    near(J_equal,.665**3)
    near(J_concentrated,.24875)
    near(any_equal,1-.335**3)
    near(any_concentrated,.99875)
    assert J_equal>J_concentrated
    assert any_concentrated>any_equal
    # AM-GM all-success inequality: product p_i <= (sum p_i/n)^n
    # Concentration maximizes any-success when budget B<=0.5 by pairwise exchange.
    # Brute finite lattice adversarial check (all allocations to hundredths & remainder).
    max_joint=-1
    max_any=-1
    min_joint=2
    min_any=2
    for a in range(100):
        for b in range(100):
            x=a*BOOST/99
            y=b*BOOST/99
            if x+y>BOOST+1e-12: continue
            z=BOOST-x-y
            pi=[BASE+x,BASE+y,BASE+z]
            J=math.prod(pi)
            anyp=1-math.prod(1-v for v in pi)
            max_joint=max(max_joint,J)
            min_joint=min(min_joint,J)
            max_any=max(max_any,anyp)
            min_any=min(min_any,anyp)
    assert max_joint<=J_equal+1e-7  # approximate grid can only approach the analytic max
    near(max_any, any_concentrated)
    return {"n":n,"boost_budget":BOOST,"baseline":BASE,
            "equal_all_success":J_equal, "concentrated_all_success":J_concentrated,
            "equal_at_least_one":any_equal,"concentrated_at_least_one":any_concentrated,
            "all_objective_prefers_equal":True,"any_objective_prefers_concentrated":True,
            "grid_max_joint":max_joint,"grid_max_any":max_any}


def three_mechanisms_same_joint() -> dict:
    s=.6
    p_ind=s**(1/3)
    # all-or-none perfect correlation: p=s
    # witness from Phase 2: 111: 0.6, and each exactly-two-success: 2/15
    p_neg=13/15
    near(p_ind**3,s)
    near(s,s)
    near(.6+2/15*2,p_neg)
    assert len({round(x,10) for x in [p_ind,s,p_neg]})==3
    return {"observed_3_coin_all_success":s,
            "independence_implied_marginal":p_ind,
            "all_or_none_implied_marginal":s,
            "exactly_two_failure_witness_implied_marginal":p_neg,
            "joint_only_nonidentifiable":True}


def make_prediction_table() -> list:
    rows=[]
    for n in N:
        p_n=BASE+BOOST/n
        concentrated=[P]+[BASE]*(n-1)
        theta_joint=(1+.99**n)/2
        row={
            "n":n,
            "M2_same_p_sharp_joint_lower":max(0,1-n*(1-P)),
            "M2_same_p_independent_joint":P**n,
            "M2_same_p_sharp_joint_upper":P,
            "M2_latent_mixture_joint":theta_joint,
            "M3_equal_budget_independent_joint":p_n**n,
            "M3_concentrated_budget_independent_joint":math.prod(concentrated),
            "M3_equal_budget_at_least_one":1-(1-p_n)**n,
            "M3_concentrated_budget_at_least_one":1-math.prod(1-v for v in concentrated),
            "M3_equal_budget_marginal":p_n,
        }
        assert row["M2_same_p_sharp_joint_lower"] - 1e-12 <= row["M2_same_p_independent_joint"] <= P + 1e-12
        assert row["M2_same_p_independent_joint"] - 1e-12 <= theta_joint <= P + 1e-12
        rows.append(row)
    with (HERE/"phase3_predictions.csv").open("w",newline="",encoding="utf8") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    report = {"metadata":{"title":"Absolute Luck Phase 3 Mathematical Model Verification",
                           "date":"2026-11-07","empirical_webtoon_measurements":False,
                           "source":"Fixed hypothetical parameters and exact finite probability models"}}
    report["phase2_regression"] = phase2_regression()
    report["M1_collision"] = collision_checks()
    report["M2_pairwise_nonidentifiability"] = pairwise_nonidentifiability()
    report["M2_parity_counterexample"] = parity_example()
    report["M2_finite_vs_infinite_exchangeability"] = finite_vs_infinite_exchangeability()
    report["M3_shared_budget"] = shared_budget_checks()
    report["cross_model_joint_nonidentifiability"] = three_mechanisms_same_joint()
    report["predictions"] = make_prediction_table()
    report["gate"]={"phase2_regression":True,
                   "three_coherent_model_families":True,
                   "proof_relevant_predictions_verified":True,
                   "two_distinct_nonidentifiability_examples":True,
                   "adversarial_counterexamples":True,
                   "hypothetical_vs_empirical_boundary":True,
                   "phase3_passed":True,
                   "novel_theorem_claimed":False}
    (HERE/"phase3_validation.json").write_text(json.dumps(report,indent=2,allow_nan=False)+"\n",encoding="utf8")
    print(json.dumps({"phase2":report["phase2_regression"]["passed"],
                      "M1_BTL":report["M1_collision"]["equal_luck_duel_A"],
                      "pairwise_same_but_triple_diff":[report["M2_pairwise_nonidentifiability"]["min_all_success"],report["M2_pairwise_nonidentifiability"]["max_all_success"]],
                      "finite_negative_dependence":report["M2_finite_vs_infinite_exchangeability"]["finite_one_failure_joint"],
                      "infinitely_exchangeable_lower_bound":report["M2_finite_vs_infinite_exchangeability"]["infinite_exchangeable_min_joint_by_Jensen"],
                      "budget_all_equal":report["M3_shared_budget"]["equal_all_success"],
                      "gate":report["gate"]["phase3_passed"]},indent=2))
    print("PASS: Phase 2 regression + all Phase 3 exact model/LP/adversarial checks")

if __name__ == "__main__":
    main()