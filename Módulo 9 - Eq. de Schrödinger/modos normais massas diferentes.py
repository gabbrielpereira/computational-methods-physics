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
k = np.zeros(N+1) + 1
m = np.zeros(N) + 1
eigval = np.zeros(N)
eigvet = np.zeros((N,N))
T = np.zeros((N,N))
mu, sigma = 1, 0.2

for i in range(N):
#    if i%2==0:
#        m[i] = 10*m[i]
    m[i] = np.random.normal(mu, sigma)
    
        
#m[49] = 1000*m[0]
#
#FIXA
for i in range(N):
    T[i][i] = (k[i] + k[i+1])/m[i]
    if i<N-1:
        T[i+1][i] = -k[i+1]/m[i+1]
        T[i][i+1] = -k[i+1]/m[i]

##PERIÓDICO
#T[0][N-1] = -k[0]/m[0]
#T[N-1][0] = -k[N]/m[N-1]
        
lamb, eigv = np.linalg.eig(T)
ind = np.argsort(lamb)

#PLOT
for i in range(N):
    eigvet[:, i] = eigv[:,ind[i]]
    eigval[i] = lamb[ind[i]]
    plt.plot(eigvet[:,i])
    plt.show() 
    
#plt.plot(eigval) 
#plt.show()
