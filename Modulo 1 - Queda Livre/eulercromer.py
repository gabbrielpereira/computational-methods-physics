# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 03:01:25 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig=plt.figure()
ax = fig.add_subplot(111)

y=100
t=0
v=0
g=9.8
e=0
dt=0.1

vmeio = 0
ymeio = 0
ameio = 0

a = -(1+(math.fabs(v))*v)

ex=[]
ey=[]

while(t<20):
    v = v + a*dt
    y = y + v*dt
    e = 0.5*v*v + y
    a = -(1+(math.fabs(v))*v)
    print(t,'\t',v,'\t',y,'\n')
    ey.append(math.fabs(v))
    ex.append(t)
    t = t+dt

ax.scatter(ex,ey, c='b', marker='o')
ax.set_xlabel('tempo')
ax.set_ylabel('v/vt')
plt.show()
       