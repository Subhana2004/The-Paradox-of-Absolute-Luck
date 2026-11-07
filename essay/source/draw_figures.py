"""Create original, mathematically exact vector diagrams for the Phase 7 essay.
No source comic artwork or external image assets are used.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]/'figures'; ROOT.mkdir(exist_ok=True)
INK='#1E3045'; MUTED='#667788'; TEAL='#0A9079'; LIGHT='#DCF3ED'; AMBER='#E5A339'; RED='#CA5B61'; PAPER='#FFFFFF'; LINE='#DFE7EC'; BLUE='#48749A'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'none','savefig.facecolor':'white','figure.facecolor':'white'})

def save(fig,name):
    fig.savefig(ROOT/(name+'.pdf'),bbox_inches='tight',pad_inches=.12,facecolor='white')
    fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight',pad_inches=.12,facecolor='white')
    fig.savefig(ROOT/(name+'.png'),dpi=220,bbox_inches='tight',pad_inches=.12,facecolor='white')
    plt.close(fig)

def box(ax,xy,w,h,fc=LIGHT,ec=None,rad=.11,lw=1):
    p=FancyBboxPatch(xy,w,h,boxstyle=f'round,pad=0.012,rounding_size={rad}',fc=fc,ec=ec or fc,lw=lw)
    ax.add_patch(p)

# 1 matchup cards
fig,ax=plt.subplots(figsize=(10.1,2.1));ax.set_xlim(0,10);ax.set_ylim(0,2);ax.axis('off')
for x,lead,sub,percent,detail in [(0.0,'A vs ordinary','A wins',99,'99 : 1 strengths'),(3.45,'B vs ordinary','B wins',99,'99 : 1 strengths'),(6.9,'A vs B','A wins',50,'99 : 99 strengths')]:
    box(ax,(x,.12),3.05,1.68,fc='#F5F8FA',ec=LINE,rad=.18)
    ax.text(x+.21,1.53,lead,fontsize=12,fontweight='bold',color=INK,va='center')
    ax.text(x+.21,1.12,sub,fontsize=9.5,color=MUTED,va='center')
    ax.text(x+2.80,1.10,f'{percent}%',fontsize=18,color=TEAL if percent==99 else AMBER,fontweight='bold',ha='right',va='center')
    ax.add_patch(Rectangle((x+.21,.69),2.60,.17,color=LINE,lw=0))
    ax.add_patch(Rectangle((x+.21,.69),2.60*percent/100,.17,color=TEAL if percent==99 else AMBER,lw=0))
    ax.text(x+.21,.42,detail,fontsize=8.5,color=MUTED)
ax.text(4.99,1.97,'SAME LUCKY STRENGTH, DIFFERENT CONTEST',ha='center',fontsize=10,weight='bold',color=INK)
save(fig,'fig01_matchups')

# 2 exactly-one-failure diagram: 200 world grid simplified as six sample worlds + final
fig,ax=plt.subplots(figsize=(10.1,3.0));ax.axis('off');ax.set_xlim(0,10);ax.set_ylim(0,3)
ax.text(.05,2.82,'THE 200-WORLD CONSTRUCTION',fontsize=11,color=INK,weight='bold')
worlds=[(1,0),(2,1),(3,2),(4,3),(5,4),(200,19)]
for row,(idx,bad) in enumerate(worlds):
    y=2.48-row*.38
    ax.text(.04,y+0.10,f'World {idx}',fontsize=8.3,va='center',color=INK)
    xs=np.linspace(1.33,8.7,20)
    for j,x in enumerate(xs):
        ax.add_patch(Rectangle((x,y),.245,.18,fc=RED if j==bad else '#BCE6DA',ec='white',lw=.6))
    ax.text(9.18,y+.1,'1 fail',color=RED,fontsize=8.5,va='center',fontweight='bold')
ax.text(4.95,.17,'Illustrative rows: positions 1-19 and 200 shown  |  positions 20-199 omitted',fontsize=8.5,color=MUTED,ha='center')
ax.text(5.0,2.78,'',fontsize=7)
save(fig,'fig02_failure_worlds')

# 3 joint success difference 200 coins
fig,ax=plt.subplots(figsize=(10.1,2.55));ax.set_xlim(-1,101);ax.set_ylim(-.7,2.9);ax.axis('off')
labels=['One failure in every world','200 independent coins','Shared latent parameter']
vals=[0,100*(.995**200),100*(199/399)]
colors=[RED,BLUE,TEAL]
for i,(lab,val,cl) in enumerate(zip(labels,vals,colors)):
    y=2.2-i*.94
    ax.text(0,y+.51,lab,fontsize=10.3,color=INK,weight='bold',va='bottom')
    ax.add_patch(Rectangle((0,y),100,.26,fc='#EAF0F3',lw=0))
    if val>0: ax.add_patch(Rectangle((0,y),val,.26,fc=cl,lw=0))
    ax.text(val+1.2,y+.13,f'{val:.2f}%',fontsize=10,va='center',color=cl,weight='bold')
ax.text(50,-.54,'Every individual coin succeeds with probability 99.5% in ALL THREE models.',fontsize=10.2,ha='center',color=MUTED)
save(fig,'fig03_two_hundred_models')

# 4 hidden triple: two distributions K=0,1,2,3
fig,ax=plt.subplots(figsize=(10.1,2.95));ax.set_xlim(-.8,4.1);ax.set_ylim(-.38,.78)
ks=np.arange(4); L=[.10,0,.60,.30]; H=[0,.30,.30,.40]; bw=.30
ax.bar(ks-bw/2,L,width=bw,color=BLUE,label='Model L')
ax.bar(ks+bw/2,H,width=bw,color=TEAL,label='Model H')
for xx,v in zip(ks-bw/2,L):
    if v:ax.text(xx,v+.018,f'{v:.0%}',ha='center',color=BLUE,fontsize=9,weight='bold')
for xx,v in zip(ks+bw/2,H):
    if v:ax.text(xx,v+.018,f'{v:.0%}',ha='center',color=TEAL,fontsize=9,weight='bold')
ax.set_xticks(ks,[f'{k} successes' for k in ks]);ax.set_ylim(0,.72);ax.set_xlim(-.65,3.65);ax.tick_params(axis='both',length=0,labelsize=9)
ax.set_yticks([0,.2,.4,.6],['0%','20%','40%','60%']);ax.spines[['top','right','left']].set_visible(False);ax.spines['bottom'].set_color(LINE)
ax.grid(axis='y',color=LINE,linewidth=.8,zorder=0);ax.set_axisbelow(True)
ax.legend(ncol=2,frameon=False,loc='upper right')
fig.tight_layout();save(fig,'fig04_hidden_triple')

# 5 reversal across two fixed dependence models
fig,ax=plt.subplots(figsize=(10.1,2.9));ax.set_xlim(-.75,1.75);ax.set_ylim(0,60)
pos=np.arange(2); vals_equal=[100*.665**3,33.0]; vals_conc=[100*.995*.5*.5,49.5]
ax.bar(pos-.18,vals_equal,.36,color=BLUE,label='Equal boost')
ax.bar(pos+.18,vals_conc,.36,color=AMBER,label='Concentrated boost')
for x,val in zip(pos-.18,vals_equal): ax.text(x,val+2,f'{val:.2f}%',ha='center',fontsize=9,color=BLUE,fontweight='bold')
for x,val in zip(pos+.18,vals_conc): ax.text(x,val+2,f'{val:.2f}%',ha='center',fontsize=9,color='#B37A16',fontweight='bold')
ax.set_xticks(pos,['Independent outcomes','Fixed mixed dependence']);ax.set_yticks([0,20,40,60],['0%','20%','40%','60%'])
ax.set_ylabel('All-three success',color=MUTED,fontsize=9);ax.spines[['top','right','left']].set_visible(False);ax.spines['bottom'].set_color(LINE)
ax.tick_params(length=0);ax.grid(axis='y',color=LINE,alpha=.9);ax.set_axisbelow(True);ax.legend(frameon=False,loc='upper left',ncol=2,fontsize=9)
fig.tight_layout();save(fig,'fig05_allocation_reversal')

print('Saved',len(list(ROOT.glob('*.pdf'))),'vector figures')
