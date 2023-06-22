# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:44:43 2019

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
dt=0.01
tmax=7.0
v=[[5.0,0.0,0.0],[5.0,0.0,0.0],[5.0,0.0,0.0],[5.0,0.0,0.0]]
x=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
E=[[0.0,0.0,1.0],[0.0,0.0,1.0],[0.0,0.0,1.0],[0.0,0.0,1.0]]
B=[[0.0,1.0,0.0],[0.0,2.0,0.0],[0.0,5.0,0.0],[0.0,10.0,0.0]]
a=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
vxB=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
modv=[0.0,0.0,0.0,0.0]

for i in range(4): 
    modv[i]=math.sqrt(v[i][0]*v[i][0]+v[i][1]*v[i][1]+v[i][2]*v[i][2])
    vxB[i]=[(v[i][1]*B[i][2]-v[i][2]*B[i][1]),(v[i][2]*B[i][0]-v[i][0]*B[i][2]),(v[i][0]*B[i][1]-v[i][1]*B[i][0])]
    a[i]=[(E[i][0]+vxB[i][0]),(E[i][1]+vxB[i][1]),(E[i][2]+vxB[i][2])]
ex=[[],[],[],[]]
ey=[[],[],[],[]]
ez=[[],[],[],[]]

while t<tmax:
    for i in range(4):
        for j in range (3):
            v[i][j] = v[i][j] + a[i][j]*dt
            x[i][j] = x[i][j] + v[i][j]*dt
            ex[i].append(x[i][0])
            ey[i].append(x[i][1])
            ez[i].append(x[i][2])
            modv[i]=math.sqrt(v[i][0]*v[i][0]+v[i][1]*v[i][1]+v[i][2]*v[i][2])
            vxB[i]=[(v[i][1]*B[i][2]-v[i][2]*B[i][1]),(v[i][2]*B[i][0]-v[i][0]*B[i][2]),(v[i][0]*B[i][1]-v[i][1]*B[i][0])]
            a[i]=[(E[i][0]+vxB[i][0]),(E[i][1]+vxB[i][1]),(E[i][2]+vxB[i][2])]
    #print(x)
    t=t+dt
ax.plot(ex[0],ey[0],ez[0], c='r', label= 'B = 1.0')    
ax.plot(ex[1],ey[1],ez[1], c='g', label= 'B = 2.0')
ax.plot(ex[2],ey[2],ez[2], c='m', label= 'B = 5.0')
#ax.plot(ex[3],ey[3],ez[3], c='b', label= 'B = 10.0')
ax.legend()
ax.grid()
#plt.title("Efeito Magnus")
#ax.set_zlim(-10.0,10.0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
    