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
filename2="5p_L.txt"
filename3="5p_E.txt"
#data1 = np.loadtxt(filename1)
data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)
#a = np.transpose(data1)
b = np.transpose(data2)
c = np.transpose(data3)
#print(a[1])

plt.plot(c[0], c[1])
#plt.plot(a[1],a[2], label = 'Sol')
#plt.plot(a[3],a[4], label = 'Mercúrio')
#plt.plot(a[5],a[6], label = 'Vênus')
#plt.plot(a[7],a[8], label = 'Terra')
#plt.plot(a[9],a[10], label = 'Marte')
#plt.plot(a[11],a[12], label = 'Júpiter')

#plt.plot(b[0],b[1], label = 'Sol')
#plt.plot(b[0],b[2], label = 'Mercúrio')
#plt.plot(b[0],b[3], label = 'Vênus')
#plt.plot(b[0],b[4], label = 'Terra')
#plt.plot(b[0],b[5], label = 'Marte')
#plt.plot(b[0],b[6], label = 'Júpiter')



#plt.plot(c[0],c[1], label = 'Sol')
##plt.plot(c[0],c[2], label = 'Mercúrio')
##plt.plot(c[0],c[3], label = 'Vênus')
##plt.plot(c[0],c[4], label = 'Terra')
##plt.plot(c[0],c[5], label = 'Marte')
#plt.plot(c[0],c[6], label = 'Júpiter')
plt.ylim(-38,-37)
plt.ylabel('Energia Total')
plt.xlabel('Tempo')

#plt.legend()
plt.show()