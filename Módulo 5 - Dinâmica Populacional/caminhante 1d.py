# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:22:19 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax=fig.add_subplot(111)

M = 10000
eM=[10,100,1000,10000]
N = 0
Nmax = 1000
H = 2*Nmax + 1
n_bins = Nmax/2
hist = np.zeros(H)
p = 0.5
x = np.zeros(M)
x2 = np.zeros(M)
Px = np.zeros(H)
a = 1.0
mx =  np.zeros(4)
mx2 = np.zeros(4)
dx2 = 0.0
x0 = np.linspace(-Nmax, Nmax, H)

while (N < Nmax):
    for i in range(M):
        r = np.random.random_sample()
        if p > r:
            x[i] = x[i] + a
        else:
            x[i] = x[i] - a
    N = N + 1

for i in range(M):
    x2[i] = x[i]*x[i] 

mx[0] = np.mean(x[0:9])
mx2[0] = np.mean(x2[0:9])
mx[1] = np.mean(x[0:99])
mx2[1] = np.mean(x2[0:99])
mx[2] = np.mean(x[0:999])
mx2[2] = np.mean(x2[0:999])
mx[3] = np.mean(x[0:9999])
mx2[3] = np.mean(x2[0:9999])


#for i in range(H):
#    Px[i] = 15.0*np.exp(-((x0[i]-mx)*(x0[i]-mx))/(2*dx2))/np.sqrt(2*np.pi*dx2)
#    
#plt.hist(x, bins = H , facecolor='r', density = True, label = 'Numérico')    
#ax.plot(x0,Px, c = 'b', label = 'Analítico')
#ax.set_xlabel('x')  
plt.plot(eM,mx2)
plt.xscale('log')
plt.xlabel('Número de caminhantes')
plt.ylabel(r'$\langle x^2 \rangle $')
#plt.yscale('log')
#plt.title("N = 1000 passos; M = 10000 caminhantes; C = 15.0")  
#print (x)
#print(mx)
#print (x2)
#print(mx2)
#plt.legend()
plt.show()       