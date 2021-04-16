# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')
fig=plt.figure()
ax=plt.axes(xlim=(0,4),ylim=(-2,2))
line,=ax.plot([],[],lw=3)

def init():
    line.set_data([],[])
    return line,
def animate(i):
    t=np.linspace(0,4,1000)
    x=np.sin(2*np.pi*(t-0.001*i)*2)+2
    y=np.cos(2*np.pi*(t+0.001*i)*5)
    line.set_data(x,y)
    
    return line,


anim=FuncAnimation(fig, animate,init_func=init,frames=350,interval=20,blit=True)

anim.save('coils.gif',writer='pillow',fps=1/0.04)
