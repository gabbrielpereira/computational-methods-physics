# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:38:13 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx0 = 30
Nr = 1000
r=np.linspace(0.0, 1.0, Nr)
tmax=2000
t=0
x0=np.linspace(0.1,0.9,Nx0)
x=np.zeros(Nr)

er = []
ex = []


for k in range(Nr):
        x[k] = np.random.random_sample()

for k in range(Nr):
    t=0
    while(t<tmax):        
        x[k] = 4*r[k]*(1-x[k])*x[k]
        t = t + 0.1
    ax.scatter(r,x)


ax.scatter(r,x)
#ax.scatter(er,x, c='g')
#ax.scatter(er,x, c='b')
#ax.scatter(er,x, c='y')
#ax.scatter(er,x, c='tab:pink')
#ax.legend()
#ax.set_xlabel(r'$\omega_d$')
#ax.set_ylabel('Amplitude')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.show() 