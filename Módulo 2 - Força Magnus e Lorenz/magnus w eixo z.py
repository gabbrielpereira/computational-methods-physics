# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:37:28 2019

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
dt=0.1
v=[50.0,50.0,0.0]
w=[0.0,0.0,5.0]
x=[0.0,0.0,0.0]
g=[0.0,-9.8,0.0]
modv=math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
wxv=[(w[1]*v[2]-w[2]*v[1]),(w[2]*v[0]-w[0]*v[2]),(w[0]*v[1]-w[1]*v[0])]
a=[(g[0]-cd*modv*v[0]+cm*wxv[0]),(g[1]-cd*modv*v[1]+cm*wxv[1]),(g[2]-cd*modv*v[2]+cm*wxv[2])]
ex=[]
ey=[]
ez=[]
while t<20:
    for i in range(3):
        v[i]= v[i] + a[i]*dt
        x[i]= x[i] + v[i]*dt
    ex.append(x[0])
    ey.append(x[1])
    ez.append(x[2])
    modv=math.sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    wxv=[(w[1]*v[2]-w[2]*v[1]),(w[2]*v[0]-w[0]*v[2]),(w[0]*v[1]-w[1]*v[0])]
    a=[(g[0]-cd*modv*v[0]+cm*wxv[0]),(g[1]-cd*modv*v[1]+cm*wxv[1]),(g[2]-cd*modv*v[2]+cm*wxv[2])]
    t=t+dt
ax.scatter(ex,ey,ez, c='r', marker='o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.show()
    