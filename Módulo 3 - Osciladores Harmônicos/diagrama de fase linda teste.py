# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:34:33 2019

@author: gabri
"""
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#ex = np.linspace(0,5,2)
#ey=np.zeros((2,2))
#x=np.zeros((2,2))
#y=np.zeros((2,2))
#q=np.zeros((4,100))
#p=np.zeros((4,100))
#
#
#for i in range(2):
#    y[:,i]=ex[i]
#    x[i] = ex[i]

Nx=2
Nwd = Nx*Nx
X=np.zeros(Nwd)
V=np.zeros(Nwd)
a=np.zeros(Nwd)
fX=np.zeros(Nwd)
gX=np.zeros(Nwd)
amp=np.zeros(Nwd)
L = 10
dx = L/Nx
cont=0

q=np.zeros((Nwd,1))
p=np.zeros((Nwd,1))

for i in range(Nx):
    for j in range(Nx):
        n = Nx*i + j
        q[n][0] = i*dx
        p[n][0] = j*dx
        print('q = ',q[n][0],'p = ',p[n][0])
     
        
W = np.append(q[0],10)