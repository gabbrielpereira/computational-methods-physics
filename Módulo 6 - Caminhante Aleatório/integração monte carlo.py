# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:04:14 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy 

fig = plt.figure()

NN = 6
D = 3
N = [10.0,100.0,1000.0,10000.0, 100000.0, 1000000.0]
Nin = np.zeros(NN)
Vd = np.zeros(NN)
Vhc = 2**D
Vext = 0.0
R = 1.0
R2 = R*R
D2 = np.zeros(NN)
dV = np.zeros(NN)
i = 0

for j in range(NN):
    while(i < N[j]):
        r = 2*np.random.random_sample((D, 1)) - 1
        for k in range(D):
            D2[j] = D2[j] + r[k]*r[k]
        if D2[j] < R2:
            Nin[j] = Nin[j] + 1
        i = i + 1  
        D2[j] = 0.0
    Vd[j] = (Nin[j]/N[j])*Vhc
    
Vext = (2*(np.pi**(D/2))*(R**D))/(D*math.gamma(D/2))

for i in range(NN):
    dV[i] = np.absolute(Vext - Vd[i])

plt.subplot(211)
plt.scatter(N, Vd)
plt.xscale('log')
plt.subplot(212)
plt.scatter(N,dV)
plt.xscale('log')
plt.show()