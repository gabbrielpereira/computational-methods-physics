# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:47:27 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx0 = 50
Nr = 2000
r=np.linspace(0.0, 1.0, Nr)
tmax=2000
t=0
x0=np.linspace(0.1,0.9,Nx0)
x=np.zeros((Nr, Nx0))



for k in range(Nr):
    for i in range(Nx0):
        x[k][i] = np.random.random_sample()

for k in range(Nr):
    for i in range(Nx0):
            t=0
            while(t<tmax):        
               x[k][i] = 4*r[k]*(1-x[k][i])*x[k][i]
               t = t + 1

ax.plot(r,x,'.')
#ax.scatter(r,x, s=1)
#ax.scatter(er,x[2], c='b')
#ax.scatter(er,x[3], c='y')
#ax.scatter(er,x[4], c='tab:pink')
#ax.legend()
ax.set_xlabel('r')
ax.set_ylabel('$x$')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.show() 