#!/usr/bin/env python3
"""Reproducible finite-model checks for Absolute Luck Phase 2.

All probabilities below are hypothetical thought-experiment parameters,
not measured frequencies from Hardcore Leveling Warrior.
Requires: Python 3.10+ and SciPy (for linear programming).
"""
from __future__ import annotations
from itertools import product
from math import isclose
import json
from pathlib import Path
from scipy.optimize import linprog

TOL = 1e-9


def close(a, b, tolerance=TOL):
    assert isclose(a, b, abs_tol=tolerance, rel_tol=0), (a, b)


def lp_collision():
    """Exactly one winner and both 99% guaranteed: infeasible."""
    result = linprog(
        c=[0, 0],
        A_ub=[[-1, 0], [0, -1]],
        b_ub=[-0.99, -0.99],
        A_eq=[[1, 1]],
        b_eq=[1],
        bounds=[(0, None), (0, None)],
        method="highs",
    )
    assert result.status == 2, result.message
    return {"requested_A_win": 0.99, "requested_B_win": 0.99, "feasible": False}


def lp_coin_intersection(n: int, p: float):
    states = list(product((0, 1), repeat=n))
    c = [float(all(state)) for state in states]
    A_eq = [[1.0] * len(states)]
    A_eq += [[float(state[i]) for state in states] for i in range(n)]
    b_eq = [1.0] + [p] * n
    low = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs")
    high = linprog([-v for v in c], A_eq=A_eq, b_eq=b_eq,
                   bounds=(0, None), method="highs")
    assert low.success and high.success, (low.message, high.message)
    return {"n": n, "marginal_probability": p,
            "minimum_joint": low.fun, "maximum_joint": -high.fun,
            "theoretical_minimum": max(0.0, 1 - n * (1 - p)),
            "theoretical_maximum": p}


def check_distribution(dist, n):
    close(sum(dist.values()), 1.0)
    for state, prob in dist.items():
        assert len(state) == n and prob >= -TOL
        assert set(state).issubset({0, 1})
    marginals = [sum(prob for state, prob in dist.items() if state[i])
                 for i in range(n)]
    joint = sum(prob for state, prob in dist.items() if all(state))
    return marginals, joint


def main():
    out = {"label": "Illustrative probability-model validation, not empirical webtoon data"}
    out["collision"] = lp_collision()

    # Luce-type example; both winning guarantees are only against a normal rival.
    close(99 / (99 + 1), 0.99)
    close(99 / (99 + 99), 0.50)
    out["weighted_choice"] = {"lucky_vs_ordinary": 0.99,
                              "equally_lucky_head_to_head": 0.50,
                              "three_equally_lucky": 1 / 3}

    # Non-exclusive goals are NOT paradoxical: both may succeed simultaneously.
    local = {(1, 1): 0.9801, (1, 0): 0.0099,
             (0, 1): 0.0099, (0, 0): 0.0001}
    p_local, joint_local = check_distribution(local, 2)
    close(p_local[0], 0.99)
    close(p_local[1], 0.99)
    close(joint_local, 0.9801)
    out["nonexclusive_counterexample"] = {"marginals": p_local, "joint": joint_local}

    # Three-coin Fréchet lower / upper bounds and their explicit witnesses.
    p = 0.995
    low_witness = {(1, 1, 1): 0.985, (1, 1, 0): 0.005,
                   (1, 0, 1): 0.005, (0, 1, 1): 0.005}
    high_witness = {(1, 1, 1): 0.995, (0, 0, 0): 0.005}
    low_marg, low_joint = check_distribution(low_witness, 3)
    high_marg, high_joint = check_distribution(high_witness, 3)
    for a in low_marg + high_marg:
        close(a, p)
    close(low_joint, 0.985)
    close(high_joint, 0.995)
    close(p**3, 0.985074875)
    out["three_coin_bounds"] = lp_coin_intersection(3, p)
    close(out["three_coin_bounds"]["minimum_joint"], low_joint)
    close(out["three_coin_bounds"]["maximum_joint"], high_joint)
    out["three_coin_bounds"]["independent_joint"] = p**3

    # Force joint probability 0.60 without changing p_i=0.995 -> infeasible.
    states = list(product((0, 1), repeat=3))
    c = [0.0] * len(states)
    A_eq = [[1.0] * len(states)]
    A_eq += [[float(state[i]) for state in states] for i in range(3)]
    A_eq += [[float(all(state)) for state in states]]
    b_eq = [1.0, p, p, p, 0.60]
    impossible = linprog(c, A_eq=A_eq, b_eq=b_eq,
                         bounds=(0, None), method="highs")
    assert impossible.status == 2, impossible.message

    # If marginals are allowed to change, the required drop 0.385 is attainable.
    lower_p_witness = {(1, 1, 1): 0.60,
                       (1, 1, 0): 2/15,
                       (1, 0, 1): 2/15,
                       (0, 1, 1): 2/15}
    marg, joint = check_distribution(lower_p_witness, 3)
    close(joint, 0.60)
    for x in marg:
        close(x, 13/15)
    aggregate_drop = 3*p - sum(marg)
    close(aggregate_drop, 0.385)
    out["forced_context_change"] = {
        "joint": joint, "marginals": marg,
        "sum_marginal_loss": aggregate_drop,
        "min_loss_of_at_least_one_coin": aggregate_drop / 3,
        "unchanged_0_995_marginals_feasible": False}

    # Remarkable 200-coin counterexample: every coin individually succeeds
    # with 199/200 probability, yet all 200 never succeed together.
    # Uniform state k means exactly coin k fails.
    n = 200
    marginals = [sum(1/n for k in range(n) if k != i) for i in range(n)]
    for x in marginals:
        close(x, 199/200, tolerance=1e-8)
    out["two_hundred_coin_construction"] = {
        "n": n, "each_marginal": 199/200,
        "joint_all_success": 0.0,
        "independent_joint_for_comparison": (199/200)**200,
        "number_of_equally_likely_failure_states": 200}

    for n in range(2, 6):
        v = lp_coin_intersection(n, p)
        close(v["minimum_joint"], v["theoretical_minimum"])
        close(v["maximum_joint"], v["theoretical_maximum"])

    print(json.dumps(out, indent=2))
    Path(__file__).with_name("phase2_validation.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print("PASS: collision infeasibility, contextual models, both sharp bounds,")
    print("      drastic-drop infeasibility, sharp marginal-loss witness, 200-coin counterexample")


if __name__ == "__main__":
    main()
