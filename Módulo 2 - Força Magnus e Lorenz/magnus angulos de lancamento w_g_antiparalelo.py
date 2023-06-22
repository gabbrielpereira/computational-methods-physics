# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:24:31 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')


cd=0.006
cm=0.0004
t=0.0
tmax=50.0
dt=0.1
v=[[100.0,0.0,0.0],[100.0,100*(math.sqrt(3)/3),0.0],[100.0,100.0,0.0],[100.0,100.0*math.sqrt(3),0.0]]
x=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
g=[[0.0,-9.8,0.0],[0.0,-9.8,0.0],[0.0,-9.8,0.0],[0.0,-9.8,0.0]]
w=[[0.0,10.0,0.0],[0.0,10.0,0.0],[0.0,10.0,0.0],[0.0,10.0,0.0]]
a=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
wxv=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
modv=[0.0,0.0,0.0,0.0]

for i in range(4): 
    modv[i]=math.sqrt(v[i][0]*v[i][0]+v[i][1]*v[i][1]+v[i][2]*v[i][2])
    wxv[i]=[(w[i][1]*v[i][2]-w[i][2]*v[i][1]),(w[i][2]*v[i][0]-w[i][0]*v[i][2]),(w[i][0]*v[i][1]-w[i][1]*v[i][0])]
    a[i]=[(g[i][0]-cd*modv[i]*v[i][0]+cm*wxv[i][0]),(g[i][1]-cd*modv[i]*v[i][1]+cm*wxv[i][1]),(g[i][2]-cd*modv[i]*v[i][2]+cm*wxv[i][2])]
ex=[[],[],[],[]]
ey=[[],[],[],[]]
ez=[[],[],[],[]]
while t<tmax:
    for i in range(4):
        for j in range(3):
            v[i][j] = v[i][j] + a[i][j]*dt
            x[i][j] = x[i][j] + v[i][j]*dt
            ex[i].append(x[i][0])
            ey[i].append(x[i][1])
            ez[i].append(x[i][2])    
        modv[i]=math.sqrt(v[i][0]*v[i][0]+v[i][1]*v[i][1]+v[i][2]*v[i][2])
        wxv[i]=[(w[i][1]*v[i][2]-w[i][2]*v[i][1]),(w[i][2]*v[i][0]-w[i][0]*v[i][2]),(w[i][0]*v[i][1]-w[i][1]*v[i][0])]
        a[i]=[(g[i][0]-cd*modv[i]*v[i][0]+cm*wxv[i][0]),(g[i][1]-cd*modv[i]*v[i][1]+cm*wxv[i][1]),(g[i][2]-cd*modv[i]*v[i][2]+cm*wxv[i][2])]
    t=t+dt
ax.plot(ex[0],ey[0],ez[0], c='r', label= r'$\theta_0 = 0°$')    
ax.plot(ex[1],ey[1],ez[1], c='g', label= r'$\theta_0 = 30°$')
ax.plot(ex[2],ey[2],ez[2], c='m', label= r'$\theta_0 = 45°$')
ax.plot(ex[3],ey[3],ez[3], c='b', label= r'$\theta_0 = 60°$')
ax.legend()
#plt.title("Efeito Magnus")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()