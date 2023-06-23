# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:56:52 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx0 = 4
Nr = 1000
r=np.linspace(0.01, 1.0, Nr)
tmax=5000
t=0
x0=np.linspace(0.1,0.9,Nx0)
x=np.zeros((Nr, Nx0))
lamb = np.zeros((Nr, Nx0))

#for k in range(Nr):
#    for i in range(Nx0):
#        x[k][i] = np.random.random_sample()

for k in range(Nr):
    for i in range(Nx0):
            t=0
            while(t<tmax):        
               x[k][i] = x[k][i]*np.exp(r[k]*(1.0-x[k][i]))
               if t>1000:
                   dv = (1  - r[k]*x[k][i])*np.exp(r[k]*(1-x[k][i]))
                   lamb[k][i] = lamb[k][i] + np.log(abs(dv))
               t = t + 1
            lamb[k][i] = lamb[k][i]/4000.0

ax.plot(r,lamb,'.')
#ax.scatter(r,x, s=1)
#ax.scatter(er,x[2], c='b')
#ax.scatter(er,x[3], c='y')
#ax.scatter(er,x[4], c='tab:pink')
#ax.legend()
ax.set_xlabel('r')
ax.set_ylabel(r'$\lambda$')