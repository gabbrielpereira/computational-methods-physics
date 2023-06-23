# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:56:20 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy 

fig = plt.figure()

Nd=9
D = [2, 3, 4, 5, 6, 7, 8, 9 , 10]
N = 1000
Nin = np.zeros(Nd)
V = 0.0
Vd = np.zeros(Nd)
dV = np.zeros(Nd)
eN = []
Vhc = np.zeros(Nd)
Vext = np.zeros(Nd)
R = 1.0
R2 = R*R
D2 = 0.0

i = 0
    

for j in range(Nd):
    Vhc[j] = 2**D[j]
    while(i < N):
        r = 2*np.random.random_sample((D[j], 1)) - 1
        for k in range(D[j]):
            D2 = D2 + r[k]*r[k]
        if D2 < R2:
            Nin[j] = Nin[j] + 1
        i = i + 1  
        D2 = 0.0   
    Vd[j] = (Nin[j]/N)*Vhc[j]
    Vext[j] = (2*(np.pi**(D[j]/2))*(R**D[j]))/(D[j]*math.gamma(D[j]/2))
    dV[j] = np.absolute(Vext[j] - Vd[j])
    i = 0

plt.errorbar(D, Vd, yerr=dV, label='Numérico', marker = '.')
plt.plot(D, Vext, c = 'r', label = 'Analítico')
plt.legend()
#plt.subplot(211)
#plt.title("D = 3 dimensões")
#plt.scatter(eN, Vd, label ='Numérico')
#plt.plot([0,2000000],[Vext,Vext], c = 'r', label='Exato')
#plt.xscale('log')
plt.ylabel('Volume')
#plt.xlim(0,2000000)
#plt.subplot(212)
#plt.scatter(eN,dV)
#plt.xscale('log')
plt.xlabel('Dimensão')
#plt.xlim(0,2000000)
#plt.ylabel('Erro do Volume')
plt.show()