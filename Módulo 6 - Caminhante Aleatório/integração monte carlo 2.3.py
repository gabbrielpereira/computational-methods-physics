# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:47:11 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy 

fig = plt.figure()

Np = 100
D = 7
N = 1000000
Nin = 0
V = 0.0
Vd = []
eN = []
Vhc = 2**D
Vext = 0.0
R = 1.0
R2 = R*R
D2 = 0
dV = []
i = 0

while(i < N+1):
    r = 2*np.random.random_sample((D, 1)) - 1
    for k in range(D):
        D2 = D2 + r[k]*r[k]
    if D2 < R2:
        Nin = Nin + 1
    if i == 10:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    if i == 100:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    if i == 1000:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    if i == 10000:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    if i == 100000:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    if i == 1000000:
        V = (Nin/i)*Vhc
        Vd.append(V) 
        eN.append(i)
    i = i + 1  
    D2 = 0.0
    
    
Vext = (2*(np.pi**(D/2))*(R**D))/(D*math.gamma(D/2))

for i in range(6):
    dV.append(np.absolute(Vext - Vd[i]))

plt.subplot(211)
plt.title("D = 7 dimensões")
plt.scatter(eN, Vd, label ='Numérico')
plt.plot([0,2000000],[Vext,Vext], c = 'r', label='Exato')
plt.legend()
plt.xscale('log')
plt.ylabel('Volume')
plt.xlim(0,2000000)
plt.subplot(212)
plt.scatter(eN,dV)
plt.xscale('log')
plt.xlabel('N')
plt.xlim(0,2000000)
plt.ylabel('Erro do Volume')

plt.show()