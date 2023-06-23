# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:43:42 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


fig = plt.figure()
#ax=fig.add_subplot(111)

M = 1000
N = 0
Nmax = 2000
p = 0.25
x = np.zeros(M)
y = np.zeros(M)
y2 = np.zeros(M)
x2 = np.zeros(M)
a = 1.0
mx = 0.0
mx2 = 0.0
my = 0.0
my2 = 0.0
R2 = 0.0
R = []

for N in range(Nmax + 1):
    for i in range(M):
        r = np.random.random_sample()
        if r <= 0.25 :
            x[i] = x[i] + a
        if r > 0.25 and r <= 0.50:
            x[i] = x[i] - a
        if r > 0.50 and r <= 0.75:
            y[i] = y[i] + a
        if r > 0.75:
            y[i] = y[i] - a
        x2[i] = x[i]*x[i]
        y2[i] = y[i]*y[i]
    if N == 0:      
        plt.subplot(231)
        plt.scatter(x, y)
        plt.title('N = 0 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
       
    if N == 100:      
        plt.subplot(232)
        plt.scatter(x, y)
        plt.title('N = 100 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
        
    if N == 200:      
        plt.subplot(233)
        plt.scatter(x, y)
        plt.title('N = 200 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
        
    if N == 500:      
        plt.subplot(234)
        plt.scatter(x, y)
        plt.title('N = 500 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
        
        R.append(np.sqrt(R2))
    if N == 1000:      
        plt.subplot(235)
        plt.scatter(x, y)
        plt.title('N = 1000 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
        
        R.append(np.sqrt(R2))
    if N == 1500:      
        plt.subplot(236)
        plt.scatter(x, y)
        plt.title('N = 1500 passos')
        plt.ylim(-85,85)
        plt.xlim(-85,85)
        
        R.append(np.sqrt(R2))
       

#dx2 = mx2 - mx*mx
my = np.mean(y)
my2 = np.mean(y2)

R2 = mx2 - mx*mx + my2 - my*my

#ax.scatter(x,y)
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
#ax.set_xlabel('x')  
#plt.title("N = 1000 passos; M = 10000 caminhantes; C = 15.0")  
#print (x)
#print (y)
#print(mx)
#print (x2)
#print(mx2)
#plt.legend()

plt.show()       