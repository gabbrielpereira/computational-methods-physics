# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:49:18 2019

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

filename1="100N_kbTo_5.txt"
#filename2="100N_T0_F50.txt"
#filename3="100N_T0_F90.txt"
data1 = np.loadtxt(filename1)
#data2 = np.loadtxt(filename2)
#data3 = np.loadtxt(filename3)
a = np.transpose(data1)
#b = np.transpose(data2)
#c = np.transpose(data3)
plt.scatter(a[0][0:1000],a[1][0:1000], label = 'Sistema')
#, label = r'$\nu = 10$')
#plt.scatter(b[0][0:1000],b[1][0:1000], label = r'$\nu = 50$')

#
#plt.scatter(c[0][0:1000],c[1][0:1000], label = r'$\nu = 90$')
plt.plot(a[0][0:1000],a[2][0:1000], label = 'Banho Térmico', c='r')
#plt.plot(b[2],c[2], label = 'Vênus')
#plt.plot(b[3],c[3], label = 'Terra')
#plt.plot(b[4],c[4], label = 'Marte')
##plt.plot(b[5],c[5], label = 'Júpiter')
##plt.plot(c[0], c[1])
plt.ylim(0,7)
plt.ylabel('Temperatura')
plt.xlabel('Tempo')
plt.title('N = 100')
#plt.title(r'$\nu = 90$')
plt.legend()
plt.show()