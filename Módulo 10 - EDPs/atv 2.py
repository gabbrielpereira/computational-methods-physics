# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:28:35 2019

@author: gabri
"""
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

L = 1.0
n = 4
N = n*n
d = L/N
P = np.zeros((n,n))
Pold = np.zeros((n,n))
t = 0.0
dt = 0.1
T = 10.0
x = np.linspace(0,n-1,n)
y = np.linspace(0,n-1,n)
V = np.zeros(N)

fig = plt.figure()
ax = fig.gca(projection='3d')

for j in range(n):
    if j>int(n/10.0) and j<int(n-n/20.0):
        Pold[int(n/10.0)][j] = 1
        Pold[int(n-n/10.0)][j] = -1           
print(Pold)

while (t<T):
    for i in range(1,n-1):
        for j in range(1,n-1):
            P[i][j] = (Pold[i-1][j] + Pold[i+1][j] + Pold[i][j-1] + Pold[i][j+1])/4
    for i in range(1,n-1):
        for j in range(1,n-1):
            Pold[i][j] = P[i][j]
        
    plt.plot([i,j],P[i,j])
#    ax.plot(P)
    plt.show()
    t = t + dt

#for i in range(n):
#    for j in range(n):
#        k = n*i + j
#        x[k] = i
#        y[k] = j
#        V[k] = P[i][j]
    
#x,y = np.meshgrid(x,y)
#surf = ax.plot_surface( x, y, P, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)        
##ax.contour(x,y,V)
##fig.colorbar(surf, shrink=0.5, aspect=5)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Potencial')
#plt.show()