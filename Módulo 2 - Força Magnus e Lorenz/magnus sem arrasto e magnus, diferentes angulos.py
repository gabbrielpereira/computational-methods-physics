# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:39:36 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)

cd=0.0
cm=0.0
t=0.0
tmax=20.0
dt=0.01
v=[[100.0*math.cos(0),0.0*math.sin(0),0.0],[100.0*math.cos(math.pi/6),100*math.sin(math.pi/6),0.0],[100.0*math.cos(math.pi/4),100.0*math.sin(math.pi/4),0.0],[100.0*math.cos(math.pi/3),100.0*math.sin(math.pi/3),0.0]]
x=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
g=[[0.0,-9.8,0.0],[0.0,-9.8,0.0],[0.0,-9.8,0.0],[0.0,-9.8,0.0]]
w=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
a=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
wxv=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
modv=[0.0,0.0,0.0,0.0]

for i in range(4): 
    a[i]=[g[i][0],g[i][1],g[i][2]]
ex=[[],[],[],[]]
ey=[[],[],[],[]]
ez=[[],[],[],[]]
while t<tmax:
    for i in range(4):
        for j in range(3):
            v[i][j] = v[i][j] + a[i][j]*dt
            x[i][j] = x[i][j] + v[i][j]*dt
            if x[i][1] < 0.0:
                break
            else:
                ex[i].append(x[i][0])
                ey[i].append(x[i][1])
                ez[i].append(x[i][2])
                a[i]=[g[i][0],g[i][1],g[i][2]]
    #print (x)    
    t=t+dt
ax.plot(ex[0],ey[0], c='r', label= r'$\theta_0 = 0°$')    
ax.plot(ex[1],ey[1], c='g', label= r'$\theta_0 = 30°$')
ax.plot(ex[2],ey[2], c='m', label= r'$\theta_0 = 45°$')
ax.plot(ex[3],ey[3], c='b', label= r'$\theta_0 = 60°$')
ax.legend()
ax.grid()
#plt.title("Efeito Magnus")
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.set_ylabel('Y')
plt.show()