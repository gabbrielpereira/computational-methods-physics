# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:43:15 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

N=100
L = 10.0
a = 0.0
b = L
u = np.zeros(N)
x=np.linspace(a,b,N)
uold = np.zeros(N)
unew = np.zeros(N)
dt = 0.1
t=0.0
T=50.0
mu,sigma = 0.2, 0.03

for i in range(N):
    uold[i] = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x[i]-mu)/sigma)**2)
    u[i] = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x[i]+0.1-mu)/sigma)**2)
    
#plt.plot(x,uold)
#plt.plot(x,u)
#plt.show()


while(t<T):
    unew[0] = u[1] + u[N-1] - uold[0]
    for i in range(1,N-1):
        unew[i] = u[i+1] + u[i-1] - uold[i]
    unew[N-1] = u[0] + u[N-2] - uold[N-1]
    for i in range(N):            
        uold[i] = u[i]
        u[i] = unew[i]    
    plt.plot(x,unew)
    plt.ylim(-50,50)
    plt.show()
    t = t+dt