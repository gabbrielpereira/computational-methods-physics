# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:45:30 2019

@author: gabri
"""

import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy 

fig = plt.figure()

N=100
T = 15000

filename1="dmol_100N_kbTo.txt"
#filename2="s_5p_L.txt"
#filename3="s_5p_E.txt"
data1 = np.loadtxt(filename1)
#data2 = np.loadtxt(filename2)
#data3 = np.loadtxt(filename3)
a = np.transpose(data1)
#b = np.transpose(data2)
#c = np.transpose(data3)
#print(a[1])

plt.plot(a[0],a[1])
plt.ylim(0,1)
plt.show()
