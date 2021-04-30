# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib import pyplot as plt
import numpy as np

ax=plt.axes(xlim=(-4,4),ylim=(-20,50))
ax.set_facecolor('black')
x=np.linspace(-5,5,100)
y=x*x
a,=plt.plot(x,y,'red',lw=2)
y=x*x+5
b,=plt.plot(x,y,'blue',lw=3)
y=-x*x
c,=plt.plot(x,y,'green',lw=2)
y=(x-3)**2
d,=plt.plot(x,y,'yellow',lw=2)
plt.legend([a,b,c,d],["x*x","x*x+5","-x*x","(x-3)**2"])


plt.show()

