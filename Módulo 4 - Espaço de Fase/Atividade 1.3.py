# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:36:49 2019

@author: gabri
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:28:20 2019

@author: gabri
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:15:33 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx0 = 5
r=[0.752,0.8,0.862]
tmax=500
x0=np.linspace(0.1,0.9,Nx0)
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
        x[j][i+1] = 4*r[2]*(1-x[j][i])*x[j][i]
    et.append(i)
et.append(tmax)    
    

ax.scatter(et,x[0], c='r', label = '$x_0 = 0.1$')
ax.scatter(et,x[1], c='g', label = '$x_0 = 0.3$')
ax.scatter(et,x[2], c='b', label = '$x_0 = 0.5$')
ax.scatter(et,x[3], c='y', label = '$x_0 = 0.7$')
ax.scatter(et,x[4], c='tab:pink', label = '$x_0 = 0.9$')
ax.legend()
ax.set_xlabel('n')
ax.set_ylabel('$x$')
plt.title('r = 0.862')
#ax.set_xlabel(r'$\omega_d$')
#ax.set_ylabel('Amplitude')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.show() 