# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:16:01 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx0 = 2
r=0.7
tmax=1000
x0=[0.5, 0.5001]
#x=np.zeros((tmax, Nx0))
x=np.zeros((Nx0, tmax))
for i in range(Nx0):
    x[i][0] = x0[i]

ex=[[] for _ in range(Nx0)]
#ey=[[] for _ in range(Nx0)]
#ez=[[] for _ in range(Nx0)]
et=[]

for i in range(tmax-1):
    for j in range(Nx0):
        x[j][i+1] = 4*r*(1-x[j][i])*x[j][i]
    et.append(i)
et.append(tmax)    
    

ax.scatter(et,x[0],  label = '$x_0 = 0.5$')
ax.scatter(et,x[1],  label = '$x_0 = 0.5001$')

ax.legend()
#ax.set_xlabel(r'$\omega_d$')
#ax.set_ylabel('Amplitude')
#ax.set_zlabel('E')
plt.title('r = 0.91')
ax.set_xlabel('n')
ax.set_ylabel('$x$')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.show() 