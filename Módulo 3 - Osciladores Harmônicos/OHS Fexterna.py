# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:26:08 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nwd = 20
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
gama=0.09
w0=2.0

wd=np.linspace(0,4.0,Nwd) #[1.5, 2.5, 3.0]


for i in range(Nwd): 
    a[i]=-alfa*fX[i]-gama*V[i]+10.0*math.cos(wd[i]*t)    
    fX[i]=X[i]
    gX[i]=(X[i]*X[i])/2
 
#X=np.copy(x)
#V=np.copy(v)
alfa=w0*w0


ex=[[] for _ in range(Nwd)]
ey=[[] for _ in range(Nwd)]
ez=[[] for _ in range(Nwd)]
et=[]
colors = ('r', 'g', 'b', 'k')

while(t<tmax):      #Euler-Cromer
   for i in range(Nwd): 
       V[i] = V[i] + a[i]*dt
       X[i] = X[i] + V[i]*dt
       e[i] = V[i]*V[i]/2 + alfa*gX[i]
       
       ez[i].append(e[i])
       ex[i].append(X[i])
       ey[i].append(V[i])
       et.append(t)
       
       gX[i]=(X[i]*X[i])/2
       fX[i]=X[i]
       a[i]=-alfa*fX[i]-gama*V[i]+10.0*math.cos(wd[i]*t) 
    
   t=t+dt
   
c_list = []
for c in colors:
    c_list.extend([c] * Nwd)

for i in range(Nwd):
    ax.plot(et,ex[i], c=c_list[i])
#ax.legend()
ax.set_xlabel('T')
ax.set_ylabel('Pos')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
plt.show()   
            