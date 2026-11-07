#!/usr/bin/env python3
"""Regenerate Phase 5 figures from result tables; vector SVG and 300 DPI PNG."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

plt.rcParams.update({
 'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':13,
 'axes.titleweight':'bold','axes.labelsize':10,'xtick.labelsize':9,
 'ytick.labelsize':9,'legend.fontsize':9,'figure.dpi':160,
 'savefig.dpi':300,'svg.fonttype':'none','svg.hashsalt':'AbsoluteLuckPhase5Fixed',
 'axes.spines.top':False,'axes.spines.right':False,'axes.grid':False
})


def read(path):
    with path.open(newline='',encoding='utf8') as f:
        return list(csv.DictReader(f))


def lookup(rows,model,scenario,metric):
    xs=[r for r in rows if r['model']==model and r['scenario']==scenario and r['metric']==metric]
    assert len(xs)==1,(model,scenario,metric)
    return xs[0]


def finish(fig,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(path.with_suffix('.svg'),bbox_inches='tight',metadata={'Date':None})
    fig.savefig(path.with_suffix('.png'),bbox_inches='tight',dpi=300,metadata={'Software':'Absolute Luck Phase 5 matplotlib'})
    plt.close(fig)


def style(ax,axis='y'):
    ax.grid(True,axis=axis,color='.87',linewidth=.65,linestyle='-',zorder=0)
    ax.set_axisbelow(True)


def collision(rows,dest):
    labels=['A beats ordinary','B beats ordinary','A beats B','A wins 3-way','Ordinary wins 3-way']
    keys=['A_beats_N','B_beats_N','A_beats_B','A_wins_three_way','N_wins_three_way']
    x=np.arange(len(keys),dtype=float)
    fig,ax=plt.subplots(figsize=(9.3,5.1))
    for scenario,offset,marker,text in [
      ('BTL_stable_strengths',-.115,'o','Stable-weight model'),
      ('latent_random_ranking',.115,'s','Latent-ranking model')]:
        vals=[lookup(rows,'M1',scenario,key) for key in keys]
        ys=np.array([float(r['empirical']) for r in vals])
        lo=np.array([float(r['wilson95_lower']) for r in vals]);hi=np.array([float(r['wilson95_upper']) for r in vals])
        th=np.array([float(r['theory']) for r in vals])
        ax.errorbar(x+offset,ys,yerr=np.stack((ys-lo,hi-ys)),
                    fmt=marker,markersize=6.3,linestyle='none',capsize=3,
                    elinewidth=1.3,label=text+' · simulation',zorder=4)
        ax.scatter(x+offset,th,marker='_',s=180,linewidths=2,color='black',zorder=3)
    ax.set_xticks(x,labels,rotation=14,ha='right')
    ax.set_ylim(0,1.055);ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_ylabel('Probability of stated outcome')
    ax.set_title('Figure 1. Equal isolated luck does not identify duel outcomes',loc='left',pad=18)
    ax.legend(loc='upper right',frameon=False)
    ax.text(.01,-.30,'Markers: Monte Carlo estimates; black ticks: exact probabilities; whiskers: pointwise 95% Wilson intervals.',
            transform=ax.transAxes,fontsize=8,color='.34')
    style(ax)
    fig.tight_layout()
    finish(fig,dest/'fig01_collision')


def coins200(rows,dest):
    keys=['finite_exactly_one_failure','iid','shared_beta']
    labels=['Finite: exactly one failure','Independent Bernoulli','Shared beta parameter']
    vals=[lookup(rows,'M2',s,'all_200_success') for s in keys]
    x=np.arange(3)
    y=np.array([float(v['empirical']) for v in vals]);p=np.array([float(v['theory']) for v in vals])
    lo=np.array([float(v['wilson95_lower']) for v in vals]);hi=np.array([float(v['wilson95_upper']) for v in vals])
    fig,ax=plt.subplots(figsize=(8.8,5.0))
    ax.errorbar(x,y,yerr=np.stack((y-lo,hi-y)),fmt='o',markersize=8,
                color='C0',capsize=5,linestyle='none',elinewidth=1.7,zorder=3,label='Simulated (95% Wilson CI)')
    ax.scatter(x,p,marker='D',s=50,color='black',zorder=4,label='Exact theory')
    for j in range(3):
        ax.text(x[j],p[j]+.029,f'{100*p[j]:.2f}%',ha='center',fontweight='medium')
    ax.set_xticks(x,labels,rotation=9,ha='right')
    ax.set_ylim(-.04,.59);ax.set_xlim(-.4,2.4)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_ylabel('Probability all 200 coins succeed')
    ax.set_title('Figure 2. Same 99.5% marginal, three incompatible collective predictions',loc='left',pad=18)
    ax.legend(loc='upper left',frameon=False)
    ax.text(.01,-.27,'All models use 99.5% individual reliability. Dependence and extendibility assumptions differ.',
            transform=ax.transAxes,color='.34',fontsize=8)
    style(ax)
    fig.tight_layout()
    finish(fig,dest/'fig02_joint_200_coins')


def allocation(rows,dest):
    mechanisms=['independent','comonotonic','fixed_mixed']
    names=['Independent','Common U','Mixed fixed copula']
    fig,ax=plt.subplots(figsize=(8.6,5.15))
    xs=np.arange(3)
    palette=plt.rcParams['axes.prop_cycle'].by_key()['color']
    for idx,(alloc,offset,mark) in enumerate([('equal',-.14,'o'),('concentrated',.14,'s')]):
        vals=[lookup(rows,'M3',m+'_'+alloc,'all_three_success') for m in mechanisms]
        p=np.array([float(v['theory']) for v in vals]);y=np.array([float(v['empirical']) for v in vals])
        lo=np.array([float(v['wilson95_lower']) for v in vals]);hi=np.array([float(v['wilson95_upper']) for v in vals])
        ax.errorbar(xs+offset,y,yerr=np.stack((y-lo,hi-y)),fmt=mark,markersize=8,
                    color=palette[idx],linestyle='none',elinewidth=1.6,capsize=4,zorder=4,
                    label=alloc.title()+' · simulated')
        ax.scatter(xs+offset+.042,p,marker='D',s=34,color='black',zorder=3,
                   label='Exact predictions' if idx==0 else None)
    ax.set_xticks(xs,names)
    ax.set_ylim(0,.73)
    ax.set_ylabel('P(all three coins succeed)')
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_title('Figure 3. Optimal allocation reverses under a fixed dependence rule',loc='left',pad=18)
    ax.legend(loc='lower center',bbox_to_anchor=(.5,.035),ncol=3,frameon=False,fontsize=8.5)
    ax.text(.01,-.20,'Fixed mixed copula: X₁=1{1−U≤p₁}, X₂=1{U≤p₂}, X₃=1{U≤p₃}; same rule across allocations.',
            transform=ax.transAxes,fontsize=8,color='.34')
    style(ax)
    fig.tight_layout()
    finish(fig,dest/'fig03_allocation_dependence')


def identifiability(rows,dest):
    x=np.array([int(r['trials_per_dataset']) for r in rows]);
    t=np.array([float(r['full_triple_all_success_theoretical_accuracy']) for r in rows]);
    e=np.array([float(r['full_triple_all_success_simulated_accuracy']) for r in rows]);
    lo=np.array([float(r['wilson95_lower']) for r in rows]);hi=np.array([float(r['wilson95_upper']) for r in rows]);
    fig,ax=plt.subplots(figsize=(8.4,4.9))
    ax.plot(x,t,linewidth=2.5,label='Exact binomial-tail prediction')
    ax.errorbar(x,e,yerr=np.stack((e-lo,hi-e)),fmt='o',markersize=6,capsize=3,
                linewidth=0,elinewidth=1.1,label='Repeated simulations (95% Wilson CI)')
    ax.axhline(.5,linestyle='--',linewidth=1.4,color='grey',label='One/two-coin protocol: chance-level 50%')
    ax.set_xscale('log');ax.set_xticks(x,[str(q) for q in x]);ax.minorticks_off()
    ax.set_xlim(19,1400);ax.set_ylim(.44,1.035)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_xlabel('Independent trials per dataset (log scale)')
    ax.set_ylabel('Model discrimination accuracy, equal priors')
    ax.set_title('Figure 4. Triples identify dependence that pairs cannot',loc='left',pad=18)
    ax.legend(loc='center right',bbox_to_anchor=(.985,.34),frameon=False,fontsize=8.5)
    ax.text(.01,-.22,'Classify model H if the fraction of all-three-success events ≥ 35%; threshold fixed in advance.',
            transform=ax.transAxes,fontsize=8,color='.34')
    style(ax)
    fig.tight_layout()
    finish(fig,dest/'fig04_identifiability')


def convergence(rows,dest):
    fig,ax=plt.subplots(figsize=(8.3,4.95))
    for name in ('L','H'):
        seq=[r for r in rows if r['model']==name]
        x=np.array([int(r['n']) for r in seq]);
        y=np.array([float(r['abs_error']) for r in seq]);
        bound=np.array([float(r['two_se']) for r in seq]);
        ax.plot(x,np.maximum(y,1e-6),marker='o',markersize=3.6,linewidth=1.7,label=f'{name}: |empirical − truth|')
        ax.plot(x,bound,linestyle='--',linewidth=1.1,label=f'{name}: 2 theoretical SE')
    ax.set_xscale('log');ax.set_yscale('log');
    ax.set_xlabel('Independent trials (log scale)')
    ax.set_ylabel('Absolute probability error (log scale)')
    ax.set_title('Figure 5. Monte Carlo estimates converge toward exact triple probabilities',loc='left',pad=18)
    ax.legend(loc='upper right',frameon=False,fontsize=8)
    ax.text(.01,-.20,'Two-SE lines are reference scales, not guaranteed pathwise error bounds.',
            transform=ax.transAxes,fontsize=8,color='.34')
    style(ax)
    fig.tight_layout()
    finish(fig,dest/'fig05_convergence')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'figures')
    a=ap.parse_args()
    metrics=read(a.data_dir/'phase5_metrics.csv')
    collision(metrics,a.output_dir);coins200(metrics,a.output_dir);allocation(metrics,a.output_dir)
    identifiability(read(a.data_dir/'phase5_identifiability.csv'),a.output_dir)
    convergence(read(a.data_dir/'phase5_convergence.csv'),a.output_dir)
    print('PASS: 5 SVG and 5 publication-resolution PNG figures produced')

if __name__=='__main__':main()
