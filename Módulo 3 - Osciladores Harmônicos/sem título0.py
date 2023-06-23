# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 02:34:07 2021

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)

x = np.linspace(0.0, 6.5, 14)
p2 = np.zeros(14)
p7 = np.zeros(14)
P2 = np.zeros(14)
P7 = np.zeros(14)
fE = np.zeros(14)
FE = np.zeros(14)
w=5.0

p2 = [3.45, 3.45, 3.45, 3.44, 3.43, 3.39, 3.19, 2.59, 1.49, 0.592, 0.168, 0.041, 0.011, 0.004]

for i in range(14):    
    fE[i] = 0.5 + 0.5*(math.erf((1.4*x[i])/w))

for i in range(14):
    P2[i] = p2[i]/p2[0]
    #fE[i] = (0.5 + math.erf(50.0*P2[i]))/p2[0]
    FE[i] = fE[i]/p2[0]
    

ax.plot(x , FE, c='b')
ax.plot(x , P2, c='r')
ax.set_xlabel('x (mm)')
ax.set_ylabel('$P/P_0$')

plt.grid()
plt.show()   

