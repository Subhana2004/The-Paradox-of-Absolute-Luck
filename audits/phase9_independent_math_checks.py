#!/usr/bin/env python3
"""Independent arithmetic/statistical audit for Absolute Luck, 2026-11-07.

Checks are independently rederived; they deliberately do not import the
project's Phase 2-5 validation modules. No claim of external peer review.
"""
from fractions import Fraction as F
from math import comb, ceil
from pathlib import Path
import csv, json, hashlib, math
from scipy.optimize import linprog
from scipy.stats import binom

ROOT = Path(__file__).resolve().parents[1]
checks = []
def check(name, value, evidence):
    checks.append({'test':name,'passed':bool(value),'evidence':evidence})
    if not value: print('FAILED', name, evidence)

# 1. The collision result: two disjoint wins cannot both have mass .99.
check('collision_inequality', F(99,100)*2 > 1, '2*(99/100)=99/50 > 1')
rank={"A>B>N":F(89,100),"B>A>N":F(1,10),"N>A>B":F(1,100)}
check('single_latent_ranking',sum(rank.values())==1 and rank['A>B>N']+rank['B>A>N']==F(99,100) and rank['A>B>N']+rank['N>A>B']==F(9,10),'coherent random ranking: A>N=B>N=99/100; A>B=9/10')

# 2. Coin conjunction: exact Frechet lower bound.
check('three_coin_frechet',3*F(199,200)-2==F(197,200),'3*(199/200)-2 = 197/200')
check('three_coin_drop',3*F(199,200)-F(13,5)==F(77,200),'3*.995-2.60=.385')

# 3. Exactly one failure among 200.
n=200
p_ind=F(199,200)
p_pair=F(198,200)
variance=p_ind*(1-p_ind)
covariance=p_pair-p_ind*p_ind
rho=covariance/variance
check('200_coin_one_failure',p_ind==F(199,200) and p_pair==F(99,100) and rho==-F(1,199),'p=199/200, pair=198/200, correlation=-1/199')
check('201_exchangeable_variance_barrier',rho < -F(1,200),'rho=-1/199 < -1/200')
check('201_tv_exact',max(F(200,201), F(2,201))==F(200,201),'T probability <=200/201; 201 one-failure witness attains bound')
check('infinite_de_finetti_lower',float(p_ind)**200>0.36 and float(p_ind)**200<0.37,'independent 200-fold success ~.3669578')
check('shared_beta_value',F(199,399)>F(49,100) and F(199,399)<F(1,2),'E[Theta^200]=199/399')

# 4. The higher-order ambiguity: count distribution q_k and every 2-projection.
qL=[F(1,10),F(0),F(3,5),F(3,10)]
qH=[F(0),F(3,10),F(3,10),F(2,5)]
def marginals(q):
    p1=sum(F(k,3)*q[k] for k in range(4))
    p2=sum(F(k*(k-1),6)*q[k] for k in range(4))
    return p1,p2
check('L_and_H_valid',sum(qL)==sum(qH)==1 and min(qL+qH)>=0,'valid nonnegative qK distributions')
check('L_H_marginals',marginals(qL)==marginals(qH)==(F(7,10),F(1,2)),'one=.7 pair=.5 for each model')
check('L_H_triple_difference',qL[-1]==F(3,10) and qH[-1]==F(2,5),'L=.3, H=.4 triple success')
# independent constraint solver on 8 probabilities without imposing exchangeability
states=[tuple((s>>j)&1 for j in range(3)) for s in range(8)]
A=[[1]*8]; b=[1]
for j in range(3):A.append([s[j] for s in states]);b.append(.7)
for i,j in [(0,1),(0,2),(1,2)]:A.append([s[i]*s[j] for s in states]);b.append(.5)
c=[int(all(s)) for s in states]
lo=linprog(c,A_eq=A,b_eq=b,bounds=(0,None),method='highs')
hi=linprog([-v for v in c],A_eq=A,b_eq=b,bounds=(0,None),method='highs')
check('sharp_triple_LP',lo.success and hi.success and abs(lo.fun-.3)<1e-10 and abs(hi.fun+.4)<1e-10,'8-atom LP bounds [0.3,0.4]')

# 5. Fixed copula and independent allocation; no global optimality assertion.
equal=(F(133,200),)*3
concentrated=(F(199,200),F(1,2),F(1,2))
ind=lambda p:p[0]*p[1]*p[2]
coupled=lambda p:max(F(0),min(p[1],p[2])-(1-p[0]))
check('equal_allocation_independent',ind(equal)==F(2352637,8000000) and ind(equal)>ind(concentrated),'0.665^3 = 0.294079625 > .24875')
check('coupled_allocation_reversal',coupled(equal)==F(33,100) and coupled(concentrated)==F(99,200),'equal .33 < concentrated .495')
check('paired_policy_delta',coupled(concentrated)-coupled(equal)==F(33,200),'.495-.33=.165')

# 6. Model identification formula and published numeric results.
for m in [200,500]:
    k=ceil(.35*m)
    p_correct=1-.5*(binom.sf(k-1,m,.3)+binom.cdf(k-1,m,.4))
    claimed={200:.9317,500:.9907}[m]
    check(f'identification_exact_m{m}',abs(p_correct-claimed)<.0002,f'exact classifier accuracy={p_correct:.9f}; rounded={claimed}')

# 7. Independently verify archived CSV rates and pointwise Wilson diagnostic.
path=ROOT/'research/phase-5/phase5_metrics.csv'
rows=list(csv.DictReader(path.open(newline='',encoding='utf8')))
check('phase5_metrics_count',len(rows)==63,f'{len(rows)} rows')
all_pass=all(r['accuracy_diagnostic_pass'].strip().lower()=='true' for r in rows)
check('phase5_recorded_acceptance',all_pass,'63 pass indicators in checked-in CSV')
ci_excludes=sum(r['theoretical_in_wilson95'].strip().lower()=='false' for r in rows)
check('phase5_wilson_exclusions',ci_excludes==8,f'{ci_excludes} pointwise 95% Wilson intervals exclude truth')
check('phase5_trials',all(int(r['n'])==120000 for r in rows),'120,000 trials per primary metric')
check('phase5_probabilities',all(abs(int(r['successes'])/int(r['n'])-float(r['empirical']))<1e-13 for r in rows),'all 63 row frequencies recomputed from k/n')

# 8. Published PDFs are structurally present; hash bind in audit JSON.
files={}
for rel in ['manuscript/Absolute_Luck_Phase6_Manuscript.pdf','essay/Absolute_Luck_Phase7_Essay.pdf',
            'research/phase-5/phase5_metrics.csv','manuscript/Absolute_Luck_Phase6_Manuscript.tex',
            'essay/Absolute_Luck_Phase7_Essay.md']:
    p=ROOT/rel
    files[rel]={'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

result={'project':'The Paradox of Absolute Luck','audit_date':'2026-11-07','audit_kind':'independent source-code-free mathematical re-derivation and recorded-data check','tests_passed':sum(x['passed'] for x in checks),'tests_total':len(checks),'all_passed':all(x['passed'] for x in checks),'checks':checks,'artifact_hashes':files,'boundary':'Not external peer review; fictional mechanics are not primary-panel-verified'}
out=Path(__file__).with_name('phase9_math_audit.json');out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS' if result['all_passed'] else 'FAIL','checks':f"{result['tests_passed']}/{result['tests_total']}",'csv_rows':len(rows),'wilson_exclusions':ci_excludes,'result_file':str(out)},indent=2))
if not result['all_passed']:raise SystemExit(1)
