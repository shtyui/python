

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def fermi(E:float,E_f:float,T: float)->float:
    k_b=8.617*(10**-5)
    return 1/(np.exp((E-E_f)/(k_b*T))+1)


mpl.rcParams['font.family']='Avenir'
mpl.rcParams['font.size']=8
mpl.rcParams['axes.linewidth']=2
mpl.rcParams['axes.spines.top']=False
mpl.rcParams['axes.spines.right']=False
mpl.rcParams['xtick.major.size']=10
mpl.rcParams['xtick.major.width']=2
mpl.rcParams['ytick.major.size']=10;
mpl.rcParams['ytick.major.width']=2

fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot(111)

T=np.linspace(100,1000,10)

colors=plt.get_cmap('coolwarm',10)

for i in range(len(T)):
    x=np.linspace(0,1,100)
    y=fermi(x,0.5,T[i])
    ax.plot(x,y,color=colors(i),linewidth=2.5)

labels=['100 L','200 K','300 K','400 K','500 K','600 K','700 K','800 K','900 K','1000 K']
ax.legend(labels.bbox_to_anchor(1.05,-0.1),loc='lower left',frameon=False,labelspacing=0.2)