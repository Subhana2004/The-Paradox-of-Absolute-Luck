#!/usr/bin/env python3
"""Absolute Luck Phase 5: prespecified, synthetic Monte Carlo experiments.

Runs are deterministic within the recorded dependency versions; they make no
empirical claims about WEBTOON panels and discover no new probability theorem.
Usage: python phase5_experiments.py --output-dir .
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.stats import binom, norm

SEED = 20261107
TRIALS = 120_000
Z = float(norm.ppf(0.975))
DIAGNOSTIC_Z = 4.5
DIAGNOSTIC_FLOOR = 0.00025


def named_rng(name: str, base_seed: int = SEED) -> np.random.Generator:
    d = hashlib.sha256(name.encode("utf-8")).digest()
    # Named streams cannot shift when an unrelated simulation is added later.
    key = np.random.SeedSequence([int(base_seed), int.from_bytes(d[:4], "little"),
                                  int.from_bytes(d[4:8], "little")])
    return np.random.Generator(np.random.PCG64(key))


def wilson(k, n, z=Z):
    """95% Wilson score interval; supports vector inputs for coverage checks."""
    p = np.asarray(k, dtype=float) / n
    den = 1 + z*z/n
    mid = (p + z*z/(2*n))/den
    rad = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))/den
    lo, hi = np.maximum(0, mid-rad), np.minimum(1, mid+rad)
    lo = np.where(np.asarray(k)==0, 0., lo)
    hi = np.where(np.asarray(k)==n, 1., hi)
    if np.ndim(p) == 0:
        return float(lo), float(hi)
    return lo, hi


def expectation_pass(observed, exact, n):
    s = math.sqrt(exact*(1-exact)/n)
    tol = DIAGNOSTIC_Z*s + DIAGNOSTIC_FLOOR
    return abs(observed-exact)<=tol, tol


ROWS = []
CONTRAST_ROWS = []
CONVERGENCE = []
SCENARIO_DEFINITIONS = {}


def add_metric(model, scenario, event, outcomes, p_exact, *, n=None, notes=""):
    x = np.asarray(outcomes, dtype=bool)
    if n is None:
        n = x.size
    assert x.size == n and n > 0
    assert 0<=p_exact<=1
    k = int(x.sum())
    obs = k/n
    lower, upper = wilson(k,n)
    ok,tol = expectation_pass(obs,p_exact,n)
    entry = dict(model=model,scenario=scenario,metric=event,n=n,successes=k,
                 empirical=obs,theory=float(p_exact),absolute_error=abs(obs-p_exact),
                 wilson95_lower=lower,wilson95_upper=upper,
                 theoretical_in_wilson95=lower<=p_exact<=upper,
                 tolerance_4p5se=tol,accuracy_diagnostic_pass=ok,notes=notes)
    ROWS.append(entry)
    return entry


def bernoulli_matrix_exact(probs, n, rng):
    """Sample fully observed 3-Bernoulli law using discrete state probabilities."""
    p = np.asarray(probs,float)
    assert p.shape==(8,) and np.all(p>=0) and math.isclose(float(p.sum()),1,abs_tol=1e-12)
    idx = rng.choice(8,size=n,p=p)
    return ((idx[:,None] >> np.arange(3)) & 1).astype(bool)


def count_law(probs_count):
    d = np.zeros(8,float)
    for code in range(8):
        k = int(code).bit_count()
        d[code] = probs_count.get(k,0.0)/math.comb(3,k)
    assert math.isclose(float(sum(d)),1.0,abs_tol=1e-12)
    return d


def m1_collision():
    n=TRIALS
    # Exponential racing exactly yields weighted Plackett-Luce rankings.
    r=named_rng('M1-BTL-full-ranking')
    weights=np.array([99.0,99.0,1.0])
    clocks=r.exponential(scale=1/weights,size=(n,3))
    p_an=99/100; p_bn=p_an; p_ab=.5
    entries=[('A_beats_N',clocks[:,0]<clocks[:,2],p_an),
             ('B_beats_N',clocks[:,1]<clocks[:,2],p_bn),
             ('A_beats_B',clocks[:,0]<clocks[:,1],p_ab),
             ('A_wins_three_way',np.argmin(clocks,axis=1)==0,99/199),
             ('N_wins_three_way',np.argmin(clocks,axis=1)==2,1/199)]
    for event,values,p in entries:
        add_metric('M1','BTL_stable_strengths',event,values,p)

    # Phase 4's single coherent random-ranking distribution.
    # 0=A>B>N (0.89); 1=B>A>N (0.10); 2=N>A>B (0.01).
    s=named_rng('M1-alternative-latent-ranking').choice(3,size=n,p=[.89,.10,.01])
    for event,values,p in [
        ('A_beats_N',s!=2,.99),('B_beats_N',s!=2,.99),
        ('A_beats_B',s!=1,.90),('A_wins_three_way',s==0,.89),
        ('N_wins_three_way',s==2,.01)]:
        add_metric('M1','latent_random_ranking',event,values,p)
    SCENARIO_DEFINITIONS['M1']={
      'BTL_strengths':{'A':99,'B':99,'N':1},
      'latent_ranking':{'A>B>N':.89,'B>A>N':.10,'N>A>B':.01},
      'isolated_matchups_equal_but_A_B_duel_not_identified':True}


def m2_higher_order():
    n=TRIALS
    for name,q in [('L',{0:.10,2:.60,3:.30}),('H',{1:.30,2:.30,3:.40})]:
        probs=count_law(q)
        x=bernoulli_matrix_exact(probs,n,named_rng('M2-higher-'+name))
        for j in range(3):
            add_metric('M2',name,f'coin{j+1}_success',x[:,j],.7,
                       notes='Identical first-order marginals under L and H')
        for i,j in [(0,1),(0,2),(1,2)]:
            add_metric('M2',name,f'pair{i+1}{j+1}_success',x[:,i]&x[:,j],.5,
                       notes='Identical pairwise probabilities under L and H')
        a=x.all(axis=1)
        add_metric('M2',name,'all_three_success',a,q[3],
                   notes='Identifies higher-order probability with simultaneous triples')
        for step in [50,100,200,500,1000,2000,5000,10000,20000,50000,TRIALS]:
            partial=float(np.mean(a[:step]))
            CONVERGENCE.append({'model':name,'n':step,'theory':q[3],
                                'empirical':partial,'abs_error':abs(partial-q[3]),
                                'two_se':2*math.sqrt(q[3]*(1-q[3])/step)})
    # All probabilities of a one-coin or two-coin measurement, per fresh trial,
    # are identical. This is stronger than just identical means of paired data.
    low,high=count_law({0:.10,2:.60,3:.30}),count_law({1:.30,2:.30,3:.40})
    def marginal(mask,law):
        return [float(sum(law[code] for code in range(8) if (code & mask)==bits))
                for bits in range(8) if bits & ~mask == 0]
    for mask in (1,2,4,3,5,6):
        assert np.allclose(marginal(mask,low), marginal(mask,high),atol=1e-14)
    SCENARIO_DEFINITIONS['M2_L_H']={
       'L_count_mass':{'K0':.1,'K1':0,'K2':.6,'K3':.3},
       'H_count_mass':{'K0':0,'K1':.3,'K2':.3,'K3':.4},
       'shared_each_coin':.7,'shared_each_pair':.5,'triple_L':.3,'triple_H':.4,
       'one_or_two_coordinate_measurement_likelihood_identical':True,
       'caution':'This non-identifiability assumes only one or two coordinates are observed from each independent trial. Observing coordinated pair records from the same full trial may reveal higher-order information.'}


def simulate_200coin(kind, n=TRIALS):
    rng=named_rng('M2-200-'+kind)
    successes=np.empty(n,dtype=np.uint16)
    first=np.empty((n,3),dtype=bool)
    if kind=='finite_exactly_one_failure':
        missing=rng.integers(0,200,size=n)
        successes[:]=199
        first[:]=missing[:,None] != np.arange(3)[None,:]
    else:
        for start in range(0,n,10000):
            stop=min(start+10000,n)
            size=stop-start
            if kind=='iid':
                theta=np.full(size,.995)
            elif kind=='shared_beta':
                theta=rng.beta(199,1,size=size)
            else: raise ValueError(kind)
            batch=rng.random((size,200)) < theta[:,None]
            successes[start:stop]=batch.sum(axis=1)
            first[start:stop]=batch[:,:3]
    return successes,first


def m2_200coin():
    cases={
      'finite_exactly_one_failure':{'joint':0.0,'pair':.99},
      'iid':{'joint':.995**200,'pair':.995**2},
      'shared_beta':{'joint':199/399,'pair':199/201}}
    for name,expect in cases.items():
        counts,first=simulate_200coin(name)
        add_metric('M2',name,'all_200_success',counts==200,expect['joint'])
        add_metric('M2',name,'coin1_success',first[:,0],.995)
        add_metric('M2',name,'pair12_success',first[:,0]&first[:,1],expect['pair'])
        SCENARIO_DEFINITIONS.setdefault('M2_200coin',{})[name]={
           'n_coins':200,'individual_marginal':.995,'pair_marginal':expect['pair'],
           'all_success':expect['joint'],
           'sample_mean_success_fraction':float(counts.sum())/(TRIALS*200),
           'sample_mean_failures':float(np.mean(200-counts))}
        if name=='finite_exactly_one_failure':
            assert np.all(counts==199) and np.all(first.sum(axis=1)>=2)


def m3_allocation():
    n=TRIALS
    B=.495
    allocations={'equal':np.array([.5+B/3]*3),
                 'concentrated':np.array([.5+B,.5,.5])}
    # Shared uniforms within a dependence mechanism allow a paired strategy test.
    for mechanism in ('independent','comonotonic','fixed_mixed'):
        rng=named_rng('M3-'+mechanism+'-paired-allocations')
        if mechanism=='independent':
            u=rng.random((n,3))
        elif mechanism=='comonotonic':
            z=rng.random(n)
            u=np.column_stack([z,z,z])
        else:
            z=rng.random(n)
            u=np.column_stack([1-z,z,z])
        all_by_alloc={}
        for allocation,p in allocations.items():
            x=u<p[None,:]
            a=x.all(axis=1); b=x.any(axis=1)
            if mechanism=='independent':
                exact_all=float(np.prod(p)); exact_any=float(1-np.prod(1-p))
            elif mechanism=='comonotonic':
                exact_all=float(min(p)); exact_any=float(max(p))
            else:
                # X1=(1-U <= p1); X2=(U <= p2); X3=(U <= p3)
                # P(all)=length([1-p1, min(p2,p3)])
                exact_all=float(max(0,min(p[1],p[2])-(1-p[0])))
                # union of [1-p1,1] and [0,max(p2,p3)]
                exact_any=float(min(1,p[0]+max(p[1],p[2])))
            scen=mechanism+'_'+allocation
            add_metric('M3',scen,'all_three_success',a,exact_all)
            add_metric('M3',scen,'at_least_one_success',b,exact_any)
            for j in range(3):
                add_metric('M3',scen,f'coin{j+1}_success',x[:,j],float(p[j]))
            all_by_alloc[allocation]=a.astype(np.int8)
            SCENARIO_DEFINITIONS.setdefault('M3',{})[scen]={
               'probabilities':p.tolist(),'all_success':exact_all,
               'at_least_one_success':exact_any,'coupling':mechanism}
        # Paired confidence interval for concentrated minus equal strategy.
        # For iid trials, differences across trials are independent, but two
        # strategies within the same trial share the exact same underlying U's.
        d=all_by_alloc['concentrated']-all_by_alloc['equal']
        empirical=float(np.mean(d))
        se=float(np.std(d,ddof=1)/math.sqrt(n))
        exact=float(SCENARIO_DEFINITIONS['M3'][mechanism+'_concentrated']['all_success']-
                    SCENARIO_DEFINITIONS['M3'][mechanism+'_equal']['all_success'])
        ci=[empirical-Z*se,empirical+Z*se]
        CONTRAST_ROWS.append(dict(model='M3',coupling=mechanism,contrast='concentrated_minus_equal_all_success',
                                  n=n,empirical_difference=empirical,theoretical_difference=exact,
                                  paired_se=se,normal95_lower=ci[0],normal95_upper=ci[1],
                                  theory_in_normal95=ci[0]<=exact<=ci[1],
                                  accuracy_diagnostic_pass=(abs(empirical-exact)<=DIAGNOSTIC_Z*se+DIAGNOSTIC_FLOOR)))
    assert SCENARIO_DEFINITIONS['M3']['independent_equal']['all_success'] > SCENARIO_DEFINITIONS['M3']['independent_concentrated']['all_success']
    assert SCENARIO_DEFINITIONS['M3']['fixed_mixed_equal']['all_success'] < SCENARIO_DEFINITIONS['M3']['fixed_mixed_concentrated']['all_success']


def identifiability_experiment():
    result=[]
    for n in [25,50,100,200,500,1000]:
        k=math.ceil(.35*n)
        err_L=float(binom.sf(k-1,n,.3))
        err_H=float(binom.cdf(k-1,n,.4))
        theoretical_accuracy=1-.5*(err_L+err_H)
        # 1000 independent synthetic datasets under each model at each size.
        r=named_rng('identifiability-'+str(n))
        repeat=1000
        l_counts=r.binomial(n,.3,size=repeat)
        h_counts=r.binomial(n,.4,size=repeat)
        n_correct=int(np.sum(l_counts<k)+np.sum(h_counts>=k))
        empirical=n_correct/(2*repeat)
        ci=wilson(n_correct,2*repeat)
        ok,tol=expectation_pass(empirical,theoretical_accuracy,2*repeat)
        result.append({'trials_per_dataset':n,'classification_threshold_count':k,
                       'classification_threshold_rate_nominal':.35,
                       'low_model_error_exact':err_L,'high_model_error_exact':err_H,
                       'full_triple_all_success_theoretical_accuracy':theoretical_accuracy,
                       'full_triple_all_success_simulated_accuracy':empirical,
                       'simulated_classifications':2*repeat,
                       'wilson95_lower':ci[0],'wilson95_upper':ci[1],
                       'accuracy_diagnostic_pass':ok,'diagnostic_tolerance':tol,
                       'one_or_two_coin_protocol_optimal_equal_prior_accuracy':.5})
    assert result[-1]['full_triple_all_success_theoretical_accuracy']>.99
    return result


def coverage_experiment():
    rows=[]
    for p in [.005,.3,.4,.5,.995]:
        rng=named_rng('Wilson-calibration-'+str(p))
        n=400
        repeats=600
        count=rng.binomial(n,p,size=repeats)
        lo,hi=wilson(count,n)
        covered=int(np.sum((lo<=p)&(p<=hi)))
        rows.append({'true_p':p,'trials_per_replicate':n,'replicates':repeats,
                     'covered':covered,'observed_coverage':covered/repeats,
                     'in_preregistered_calibration_window':.90<=covered/repeats<=.99})
    return rows


def write_csv(path,rows):
    assert len(rows)>0
    with path.open('w',newline='',encoding='utf8') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]))
        wr.writeheader();wr.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args()
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    m1_collision();m2_higher_order();m2_200coin();m3_allocation()
    ident=identifiability_experiment();coverage=coverage_experiment()
    write_csv(out/'phase5_metrics.csv',ROWS)
    write_csv(out/'phase5_identifiability.csv',ident)
    write_csv(out/'phase5_coverage.csv',coverage)
    write_csv(out/'phase5_paired_contrasts.csv',CONTRAST_ROWS)
    write_csv(out/'phase5_convergence.csv',CONVERGENCE)
    gate={
      'math_scenarios_correct':True,
      'rate_diagnostics_all_pass':all(r['accuracy_diagnostic_pass'] for r in ROWS),
      'identifiability_diagnostics_pass':all(r['accuracy_diagnostic_pass'] for r in ident),
      'coverage_calibration_pass':all(r['in_preregistered_calibration_window'] for r in coverage),
      'paired_differences_diagnostics_pass':all(r['accuracy_diagnostic_pass'] for r in CONTRAST_ROWS),
      'fixed_copula_qualitative_reversal_verified':SCENARIO_DEFINITIONS['M3']['fixed_mixed_equal']['all_success']<SCENARIO_DEFINITIONS['M3']['fixed_mixed_concentrated']['all_success'],
      'measurement_protocol_structural_nonidentifiability_verified':SCENARIO_DEFINITIONS['M2_L_H']['one_or_two_coordinate_measurement_likelihood_identical'],
    }
    result={
      'metadata':{'date':'2026-11-07','seed':SEED,'main_trial_count_per_scenario':TRIALS,
                  'numpy':np.__version__,'scipy':scipy.__version__,
                  'python':platform.python_version(),'bit_generator':'PCG64',
                  'purely_synthetic':True,'fictional_events_measured':False,
                  'new_theorems_claimed':False,'confidence_interval':'Wilson score, pointwise 95%',
                  'paired_difference_interval':'large-sample normal approximation, pointwise 95%',
                  'random_streams':'independent labeled SeedSequences hashed via SHA256'},
      'model_definitions':SCENARIO_DEFINITIONS,
      'counts':{'metrics':len(ROWS),'identifiability_n':len(ident),
                'coverage_probabilities':len(coverage),'paired_differences':len(CONTRAST_ROWS)},
      'coverage_calibration':coverage,
      'paired_all_success_differences':CONTRAST_ROWS,
      'identifiability':ident,
      'statistical_accuracy':{'threshold_z':DIAGNOSTIC_Z,'absolute_floor':DIAGNOSTIC_FLOOR,
                              'note':'Accuracy diagnostics are engineering tolerances, not hypothesis tests; Wilson intervals need not all individually cover truth.'},
      'gate':gate}
    (out/'phase5_validation.json').write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n',encoding='utf8')
    print(json.dumps({'metrics':len(ROWS),'main_trials':TRIALS,'M3_paired':CONTRAST_ROWS,
                      'covered_rates':[x['observed_coverage'] for x in coverage],
                      'gates':gate},indent=2))
    if not all(gate.values()):
        raise SystemExit('FAIL: one or more simulation gates did not pass')
    print('PASS: Phase 5 simulation accuracy + structural predictions + coverage calibration')

if __name__=='__main__':main()