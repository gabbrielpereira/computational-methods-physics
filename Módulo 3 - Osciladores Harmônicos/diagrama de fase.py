# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:07:46 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations_with_replacement

#fig = plt.figure()
#ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx=2
Nwd = Nx*Nx
X=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
V=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
a=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
fX=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
gX=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
L = 10
dx = L/Nx
cont= 0        
t=0.0
tmax=10
dt=0.1
w0=1.0
alfa=w0*w0

#q=np.zeros((Nwd,int(t/dt)))
#p=np.zeros((Nwd,int(t/dt)))

q=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
p=[np.zeros(Nwd) for _ in range(int(tmax/dt))]
#
#v=np.linspace(5.0,10.0,Nwd/2)
#x=np.linspace(5.0,10.0,Nwd/2)

for i in range(Nx):
    for j in range(Nx):
        n = Nx*i + j
        q[0][n] = i*dx
        p[0][n] = j*dx
#        print('q = ',q[n],'p = ',p[n])



for i in range(Nwd): 
    a[i]=-alfa*fX[i]
    fX[i]=X[i]
    gX[i]=(X[i]*X[i])/2
    X[i] = q[i]
    V[i] = p[i]
    
#ex=[[] for _ in range(Nwd)]
#ey=[[] for _ in range(Nwd)]
#ez=[[] for _ in range(Nwd)]
#et=[]

while(t<tmax-1):      #Euler-Cromer
   for i in range(Nwd): 
       V[cont+1][i] = V[cont][i] + a[cont][i]*dt
       X[cont+1][i] = X[cont][i] + V[cont+1][i]*dt
      
       
       
       gX[cont][i]=(X[cont][i]*X[cont][i])/2
       fX[cont][i]=X[cont][i]
       a[cont][i]=-alfa*fX[cont][i]
               
   #et.append(t) 
   cont = cont + 1
   t=t+dt
   

plt.plot(X[0],V[0])
#ax.plot(ex[5],ey[5], c='r')
#ax.plot(et,ex[1], c='g')
#ax.plot(et,ex[2], c='b')
#ax.legend()
#ax.set_xlabel(r'$\omega_d$')
#ax.set_ylabel('Amplitude')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.show()   
            