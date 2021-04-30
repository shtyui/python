# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:44:03 2021

@author: Administrator
"""

import numpy as np
from matplotlib import pyplot as plt

plt.style.use('seaborn-pastel')
fig=plt.figure()
ax=plt.axes(xlim=(-4,4),ylim=(-100,100))
ax.set_facecolor('black')
x=np.linspace(-40,40,1000)
y=x**3+x**2+10*x+5
ax.plot(x,y)




