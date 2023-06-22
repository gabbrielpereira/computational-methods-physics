# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:58:18 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations_with_replacement

fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nwd = 4
X=np.zeros(Nwd)
V=np.zeros(Nwd)
a=np.zeros(Nwd)
fX=np.zeros(Nwd)
gX=np.zeros(Nwd)
amp=np.zeros(Nwd)

p=np.zeros(Nwd)

v=np.linspace(5.0,10.0,Nwd/2)
x=np.linspace(5.0,10.0,Nwd/2)

a = itertools.combinations_with_replacement([1,2,3], 2)
