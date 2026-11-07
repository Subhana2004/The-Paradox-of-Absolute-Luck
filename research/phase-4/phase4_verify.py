#!/usr/bin/env python3
"""Absolute Luck Phase 4: exact proof-oriented adversarial regression suite.

Inputs are fixed hypothetical probability models; no canonical webtoon trial data.
Dependencies: Python >=3.10, scipy, matplotlib (matplotlib only for figure.py).
Run: python phase4_verify.py

Writes only Phase 4's own validation JSON/CSV, plus replays preserved Phase 2/3
scripts inside the isolated source_phase3 copy.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys
import csv
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'source_phase3'
TOL = 1e-9
TESTS = []

def checked(name, test_fn):
    detail = test_fn()
    TESTS.append({'test': name, 'result': 'PASS', 'details': detail})
    return detail

def close(a, b, eps=TOL):
    assert abs(float(a)-float(b)) < eps, (a,b)

def finite_distribution(law, n):
    assert all(len(s)==n for s in law)
    assert all(v>=0 for v in law.values())
    assert sum(law.values())==1
    marg=[sum(v for s,v in law.items() if s[i]) for i in range(n)]
    pair={(i,j):sum(v for s,v in law.items() if s[i] and s[j]) for i in range(n) for j in range(i+1,n)}
    return {'p':marg, 'pairs':pair, 'all':sum(v for s,v in law.items() if all(s)),
            'any':sum(v for s,v in law.items() if any(s))}

def symmetric_count_dist(n, counts):
    assert sum(counts.values())==1
    law={}
    for s in product((0,1),repeat=n):
        k=sum(s)
        if k in counts and counts[k]:
            law[s]=counts[k]/math.comb(n,k)
    return law

def lp_extrema(p, target='all'):
    n=len(p)
    states=list(product((0,1),repeat=n))
    eq=[[1.0]*len(states)]+[[float(s[i]) for s in states] for i in range(n)]
    rhs=[1.0]+[float(x) for x in p]
    if target=='all': obj=[float(all(s)) for s in states]
    elif target=='any': obj=[float(any(s)) for s in states]
    else: raise ValueError(target)
    lo=linprog(obj,A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs')
    hi=linprog([-v for v in obj],A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs')
    assert lo.success and hi.success, (lo.message,hi.message)
    return lo.fun,-hi.fun

def baseline_integrity():
    files=['phase3_verify.py','phase3_validation.json','phase3_predictions.csv',
           'Absolute_Luck_Phase3_Mathematical_Model_Development_2026-11-07.md',
           'source_phase2/phase2_verify.py','source_phase2/phase2_validation.json',
           'source_phase2/Absolute_Luck_Phase2_Paradox_Construction_2026-11-07.md']
    before={x:hashlib.sha256((SOURCE/x).read_bytes()).hexdigest() for x in files}
    run=subprocess.run([sys.executable,str(SOURCE/'phase3_verify.py')],cwd=SOURCE,
                       capture_output=True,text=True,timeout=120)
    assert run.returncode==0,run.stdout+'\n'+run.stderr
    assert 'PASS:' in run.stdout,run.stdout
    after={x:hashlib.sha256((SOURCE/x).read_bytes()).hexdigest() for x in files}
    assert before==after, 'Phase 3 regression altered preserved baseline outputs'
    actual=json.loads((SOURCE/'phase3_validation.json').read_text())
    assert actual['gate']['phase3_passed'] and actual['phase2_regression']['passed']
    return {'phase2_and_phase3_replay':True, 'sha256':after}

def m1_coherence_and_ranking():
    assert F(99,100)*2>1
    weights={'A':F(99),'B':F(99),'N':F(1)}
    def choice(s,i):return weights[i]/sum(weights[k] for k in s)
    assert choice('AN','A')==F(99,100)
    assert choice('BN','B')==F(99,100)
    assert choice('AB','A')==F(1,2)
    assert choice('ABN','A')==F(99,199)
    for s in ('AB','ABN'):
        assert choice(s,'A')/choice(s,'B')==1
    # A coherent joint random ranking; no context-indexed arbitrary match tables.
    ranking={('A','B','N'):F(89,100),('B','A','N'):F(10,100),('N','A','B'):F(1,100)}
    assert sum(ranking.values())==1
    def ahead(a,b):return sum(v for order,v in ranking.items() if order.index(a)<order.index(b))
    assert ahead('A','N')==F(99,100)
    assert ahead('B','N')==F(99,100)
    assert ahead('A','B')==F(9,10)
    assert ahead('B','A')==F(1,10)
    assert ahead('A','B')/ahead('B','A')==9
    # In a two-winner symmetric match, exact label-exchange symmetry forces 50-50.
    assert choice('AB','A') == choice('AB','B') == F(1,2)
    return {'M1_BTL_duel':'1/2','random_ranking_duel':'9/10',
            'both_defeat_normal':'99/100',
            'random_ranking_3way_top':{k:str(sum(v for order,v in ranking.items() if order[0]==k)) for k in 'ABN'},
            'counterexample_is_coherent_joint_ranking':True}

def m2_sharp_bounds_exhaustive():
    scenarios=[]
    for n in range(2,6):
        for p in (F(1,5),F(1,2),F(133,200),F(199,200)):
            low,high=lp_extrema([p]*n,'all')
            analytical_low=max(F(0),n*p-(n-1))
            close(low,analytical_low)
            close(high,p)
            scenarios.append({'n':n,'p':str(p),'min_all':low,'max_all':high})
    return {'scenarios_checked':len(scenarios),'scenarios':scenarios}

def m2_pairwise_not_identifiable():
    low=symmetric_count_dist(3,{0:F(1,10),2:F(3,5),3:F(3,10)})
    high=symmetric_count_dist(3,{1:F(3,10),2:F(3,10),3:F(2,5)})
    a,b=finite_distribution(low,3),finite_distribution(high,3)
    assert a['p']==b['p']==[F(7,10)]*3
    assert a['pairs']==b['pairs']=={(0,1):F(1,2),(0,2):F(1,2),(1,2):F(1,2)}
    assert a['all']==F(3,10) and b['all']==F(2,5)
    # Exact count-moment parameterization q3=t:
    # q0=2/5-t, q1=3t-9/10, q2=3/2-3t.
    for t in (F(3,10),F(7,20),F(2,5)):
        q=[F(2,5)-t,3*t-F(9,10),F(3,2)-3*t,t]
        assert all(v>=0 for v in q) and sum(q)==1
        assert (sum(k*q[k] for k in range(4))/3)==F(7,10)
        assert (sum(k*(k-1)*q[k] for k in range(4))/6)==F(1,2)
    # Independence violation despite nonnegative pairwise correlations.
    even=symmetric_count_dist(3,{0:F(1,4),2:F(3,4)})
    mixture={s:F(19,20)*even.get(s,F(0)) for s in product((0,1),repeat=3)}
    mixture[(1,1,1)]+=F(1,20)
    mix=finite_distribution(mixture,3)
    assert mix['p']==[F(21,40)]*3
    assert all(x==F(23,80) for x in mix['pairs'].values())
    cov=F(23,80)-F(21,40)**2
    assert cov==F(19,1600)>0
    assert mix['all']==F(1,20)<F(21,40)**3
    return {'L_joint':'3/10','H_joint':'2/5','single_and_pairwise_equal':True,
            'positive_pairwise_covariance':'19/1600','positive_covariance_triple_joint':'1/20',
            'independent_at_same_marginal':str(F(21,40)**3),
            'pairwise_positive_does_not_imply_latent_iid':True}

def m2_finite_extendibility():
    n=200
    p=F(n-1,n)
    r=F(-1,n-1)
    assert p==F(199,200)
    assert r==F(-1,199)
    # Exchangeable X_1,...,X_m with shared nonzero marginal variance implies
    # Var(sum X_i)=m p(1-p)(1+(m-1)*rho) >= 0.
    assert 1+(n-1)*r==0
    assert 1+n*r<0   # hence no 201-exchangeable extension can share this 200-marginal law
    # Explicit hypergeometric bound: if Y_1,...,Y_201 exchangeable, given R total
    # failures in 201, number failures in first 200 equals R (if last is a success)
    # or R-1 (if last is a failure).
    # Thus P(first 200 contain exactly one failure) is at most 200/201, attained
    # when the full 201-vector has exactly one failure.
    m=n+1
    probabilities={k:((F(m-k,m) if k==1 else F(0))+
                      (F(k,m) if k==2 else F(0))) for k in range(m+1)}
    max_prob=max(probabilities.values())
    assert max_prob==F(200,201)
    min_total_variation_gap=1-max_prob
    assert min_total_variation_gap==F(1,201)
    # Sharpness: choose exactly one failure in 201; 200-marginal is the target
    # one-failure distribution with mass 200/201 + all-success with mass 1/201.
    jensen_lower=float(p)**n
    assert jensen_lower>0.36
    return {'n':n,'p_each':str(p),'corr':str(r),
            '201_exchangeable_extension_possible':False,
            'max_probability_exactly_one_failure_among_first_200':str(max_prob),
            'sharp_minimum_total_variation_gap':str(min_total_variation_gap),
            'infinite_exchangeable_all_success_min':jensen_lower}

def m3_dependency_adversarial():
    base=F(1,2)
    B=F(99,200) # 0.495
    eq_p=[base+B/3]*3 # .665
    con_p=[base+B,base,base]
    assert eq_p==[F(133,200)]*3
    assert con_p==[F(199,200),F(1,2),F(1,2)]
    independent_equal=math.prod(eq_p)
    independent_con=math.prod(con_p)
    any_ind_equal=1-math.prod(1-v for v in eq_p)
    any_ind_con=1-math.prod(1-v for v in con_p)
    assert independent_equal>independent_con
    assert any_ind_equal<any_ind_con
    # A valid exchangeable dependence at equal allocation: exactly one success
    # with mass .005 and exactly two successes with mass .995.
    eq_dep=finite_distribution(symmetric_count_dist(3,{1:F(1,200),2:F(199,200)}),3)
    assert eq_dep['p']==eq_p
    assert eq_dep['all']==0 and eq_dep['any']==1
    # A valid comonotone coupling at concentrated allocation:
    # 111: .5, 100: .495, 000: .005.
    con_dep=finite_distribution({(1,1,1):F(1,2),(1,0,0):F(99,200),(0,0,0):F(1,200)},3)
    assert con_dep['p']==con_p
    assert con_dep['all']==F(1,2) and con_dep['any']==F(199,200)
    # This reverses BOTH independent-allocation preferences.
    assert eq_dep['all']<con_dep['all']
    assert eq_dep['any']>con_dep['any']
    intervals={}
    for name, probabilities in [('equal',eq_p),('concentrated',con_p)]:
        all_lo,all_hi=lp_extrema(probabilities,'all')
        any_lo,any_hi=lp_extrema(probabilities,'any')
        close(all_lo,max(0,sum(probabilities)-2))
        close(all_hi,min(probabilities))
        close(any_lo,max(probabilities))
        close(any_hi,min(1,sum(probabilities)))
        intervals[name]={'all':[all_lo,all_hi],'any':[any_lo,any_hi]}
    assert intervals['equal']['all']==[0,0.665]
    assert intervals['concentrated']['all']==[0,0.5]
    assert intervals['concentrated']['any']==[0.995,1]
    # Budget fixes sum marginal probabilities, hence fixed sharp lower all bound.
    assert sum(eq_p)==sum(con_p)==F(399,200)
    assert max(0,sum(eq_p)-2)==0
    # Baseline heterogeneity alone and nonlinear response alone overturn AM-GM boost equality.
    hetero_all_to_low=F(3,10)*F(4,5)
    hetero_equal=F(1,4)*F(17,20)
    assert hetero_all_to_low>hetero_equal
    nonlinear_equal=(F(1,10)+F(1,4)**2)**2
    nonlinear_con=(F(1,10)+F(1,2)**2)*F(1,10)
    assert nonlinear_con>nonlinear_equal
    return {'independent_equal_all':float(independent_equal),
            'independent_concentrated_all':float(independent_con),
            'independent_equal_any':float(any_ind_equal),
            'independent_concentrated_any':float(any_ind_con),
            'dependent_equal_all':0.0,'dependent_concentrated_all':0.5,
            'dependent_equal_any':1.0,'dependent_concentrated_any':.995,
            'sharp_arbitrary_dependence_intervals':intervals,
            'heterogeneous_baseline_reversal':{'weak_target':float(hetero_all_to_low),'equal':float(hetero_equal)},
            'nonlinear_response_reversal':{'concentrated':float(nonlinear_con),'equal':float(nonlinear_equal)}}

def check_extension_boundary_grid():
    records=[]
    for n in range(2,12):
        for r in range(1,n):
            m=n+1
            # Hypergeometric n-subset event 'exactly r failures' in length n+1.
            # k total failures in n+1, last entry is 0 w.p. k/m or success w.p. (m-k)/m.
            vals=[(F(m-k,m) if k==r else F(0)) + (F(k,m) if k==r+1 else F(0))
                  for k in range(m+1)]
            best=max(vals)
            formula=F(max(m-r,r+1),m)
            assert best==formula and best<1
            records.append({'n':n,'r':r,'maximum_event_probability':str(best)})
    return {'n_r_scenarios':len(records), 'proposition_verified_on_grid':True}

def write_models_csv(out):
    rows=[]
    m3=out['M3_adversarial']['sharp_arbitrary_dependence_intervals']
    for mode in ('equal','concentrated'):
        for objective in ('all','any'):
            lo,hi=m3[mode][objective]
            rows.append({'model':mode,'objective':objective,'arbitrary_dependence_min':lo,
                         'arbitrary_dependence_max':hi})
    with (HERE/'phase4_model_bounds.csv').open('w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    out={
      'metadata': {'title':'Absolute Luck Phase 4 proof and stress test audit',
                   'date':'2026-11-07', 'webtoon_measurements':False,
                   'hypothetical_models_only':True,
                   'claims_of_new_theorems':False}
    }
    items=[
        ('preserved_baseline',baseline_integrity),
        ('M1_collision',m1_coherence_and_ranking),
        ('M2_sharp_event_bounds',m2_sharp_bounds_exhaustive),
        ('M2_pairwise_counterexamples',m2_pairwise_not_identifiable),
        ('M2_exchangeability',m2_finite_extendibility),
        ('M3_adversarial',m3_dependency_adversarial),
        ('finite_extendibility_grid',check_extension_boundary_grid)
    ]
    for label,fn in items:
        out[label]=checked(label,fn)
    out['gate']={
        'phase2_and_phase3_regression_pass':True,
        'M1_tested_with_joint_ranking':True,
        'M2_sharp_bounds_lp_checked':True,
        'finite_vs_infinite_exchangeability_verified':True,
        '201_extension_impossibility_proved':True,
        'pairwise_and_positive_covariance_counterexamples_verified':True,
        'M3_independence_assumption_stress_tested':True,
        'dependence_robust_bounds_checked':True,
        'proof_and_counterexample_scope_labeled':True,
        'phase4_complete':True
    }
    out['tests']=TESTS
    write_models_csv(out)
    (HERE/'phase4_validation.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n',encoding='utf8')
    print(json.dumps({'phase2_phase3_regression':'PASS',
        'checks_passed':len(TESTS),
        '200_to_201_extension':out['M2_exchangeability']['201_exchangeable_extension_possible'],
        'minimum_tv_gap':out['M2_exchangeability']['sharp_minimum_total_variation_gap'],
        'independence_dependent_all_equal':[out['M3_adversarial']['independent_equal_all'],out['M3_adversarial']['dependent_equal_all']],
        'phase4_complete':out['gate']['phase4_complete']},indent=2))
    print('PASS: Phase 2/3 regressions + exact counterexamples + LP extrema + extendibility checks')

if __name__=='__main__':main()
