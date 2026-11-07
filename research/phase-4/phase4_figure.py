#!/usr/bin/env python3
"""Render a single plot from the checked bounds; no external images/data."""
from pathlib import Path
import csv
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
with (HERE/'phase4_model_bounds.csv').open() as f:
    rows=list(csv.DictReader(f))
lookup={(r['model'],r['objective']):r for r in rows}
ylabels=['Equal boost — all succeed','Concentrated — all succeed',
         'Equal boost — at least one','Concentrated — at least one']
conditions=[('equal','all'),('concentrated','all'),('equal','any'),('concentrated','any')]
indep=[.294079625,.24875,.962404625,.99875]
dep=[0,.5,1,.995]
fig,ax=plt.subplots(figsize=(11,4.4))
for i,key in enumerate(conditions):
    r=lookup[key];left=float(r['arbitrary_dependence_min']);right=float(r['arbitrary_dependence_max'])
    ax.plot([left,right],[i,i],linewidth=7,solid_capstyle='round',alpha=.35,
            label='Sharp feasible range' if i==0 else None)
    ax.scatter([left,right],[i,i],s=30,marker='|',label=None)
ax.scatter(indep,list(range(4)),marker='o',s=92,label='Independent model',zorder=5)
ax.scatter(dep,list(range(4)),marker='D',s=72,label='Constructed dependent model',zorder=6)
ax.set_yticks(range(4),labels=ylabels)
ax.invert_yaxis()
ax.set_xlim(-.05,1.05)
ax.set_xlabel('Probability')
ax.set_title('Phase 4: Same boost rules, different dependence assumptions')
ax.grid(axis='x',alpha=.2)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.42),ncol=3,frameon=False)
fig.subplots_adjust(left=.28,right=.98,top=.87,bottom=.29)
fig.savefig(HERE/'phase4_dependence_stress_test.png',dpi=200)
print(HERE/'phase4_dependence_stress_test.png')
