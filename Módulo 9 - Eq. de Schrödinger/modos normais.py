# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:29:42 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

N=100
dx = 1
eigval = np.zeros(N)
eigvet = np.zeros((N,N))
H = np.zeros((N,N))
V = np.zeros(N)

#V[0] = V[N-1] = 1000000 #poço infinito
#poço finito
for i in range(N):
#    if i<20:
#        V[i] = 5
#    if i>80:
#        V[i] = 5
    V[i] = ((i - N/2)**2)/N**2 #poço parabolico
    

#FIXA
for i in range(N):
    H[i][i] = 2/(dx*dx) + V[i]
    if i<N-1:
        H[i+1][i] = -1/(dx*dx)
        H[i][i+1] = -1/(dx*dx)
        


##PERIÓDICO
#T[0][N-1] = -k[0]/m[0]
#T[N-1][0] = -k[N]/m[N-1]
        
lamb, eigv = np.linalg.eig(H)
ind = np.argsort(lamb)

#PLOT
for i in range(N):
    eigvet[:, i] = eigv[:,ind[i]]
    eigval[i] = lamb[ind[i]]
    plt.plot(eigvet[:,i])
    plt.show() 
    
#plt.plot(eigval) 
#plt.show()
