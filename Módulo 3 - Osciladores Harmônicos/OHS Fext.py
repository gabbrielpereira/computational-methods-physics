# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:46:51 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nwd = 3
X=np.zeros(Nwd)
V=np.zeros(Nwd)
e=np.zeros(Nwd)
a=np.zeros(Nwd)
fX=np.zeros(Nwd)
gX=np.zeros(Nwd)

v=np.zeros(Nwd)
x=10+np.zeros(Nwd)
t=0.0
tmax=150.0
dt=0.1
w0=2.0
gama=0.5
alfa=w0*w0


wd=[1.0, 3.0, 4.0]


for i in range(Nwd): 
    a[i]=-alfa*fX[i]-gama*V[i]+5.0*math.cos(wd[i]*t)    
    fX[i]=X[i]
    gX[i]=(X[i]*X[i])/2
    X[i] = x[i]
    V[i] = v[i]
    
ex=[[] for _ in range(Nwd)]
ey=[[] for _ in range(Nwd)]
ez=[[] for _ in range(Nwd)]
et=[]

while(t<tmax):      #Euler-Cromer
   for i in range(Nwd): 
       V[i] = V[i] + a[i]*dt
       X[i] = X[i] + V[i]*dt
       e[i] = V[i]*V[i]/2 + alfa*gX[i]
       
       ez[i].append(e[i])
       ex[i].append(X[i])
       ey[i].append(V[i])
       
       gX[i]=(X[i]*X[i])/2
       fX[i]=X[i]
       a[i]=-alfa*fX[i]-gama*V[i]+5.0*math.cos(wd[i]*t) 
   et.append(t) 
   t=t+dt

#ax.plot(et,ex[0], label='$\omega_d = 0.5\omega_0$')#, c='r')

ax.plot(et,ex[1], label='$\gamma = 0.1$')#, c='b')
#ax.plot(et,ex[2], label='$\omega_d = 2.0\omega_0$')#, c='g')
#ax.plot(et,ex[1], c='g')
#ax.plot(et,ex[2], c='b')
ax.legend()
ax.set_xlabel('Tempo')
ax.set_ylabel('Posição')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
plt.show()   
            