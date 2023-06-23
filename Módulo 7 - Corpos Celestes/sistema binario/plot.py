# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:26:01 2019

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

#filename1="s_5p_r_periodo.txt"
filename2="bi_x.txt"
filename3="bi_y.txt"
#data1 = np.loadtxt(filename1)
data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)
#a = np.transpose(data1)
b = np.transpose(data2)
c = np.transpose(data3)

plt.plot(b[0],c[0], label = 'Estrela 1')
plt.plot(b[1],c[1], label = 'Estrela 2')
plt.plot(b[2],c[2], label = 'Planeta')

#plt.plot(c[0], c[1])
#
#plt.ylim(-38,-37)
#plt.ylabel('Energia Total')
#plt.xlabel('Tempo')
plt.legend()
plt.show()
