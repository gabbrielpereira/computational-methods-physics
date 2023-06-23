# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:07:09 2019

@author: gabri
"""

import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy 

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

#filename1="s_5p_r_periodo.txt"
filename2="AMO_rmeu.txt"
filename3="AMO_vmeu.txt"
#data1 = np.loadtxt(filename1)
data2 = np.loadtxt(filename2)
data3 = np.loadtxt(filename3)
#a = np.transpose(data1)
b = np.transpose(data2)
c = np.transpose(data3)

#ax.plot(b[0],b[1],b[2])  
ax.plot(c[0],c[1],c[2])   
#ax.plot(ex[1],ey[1],ez[1], c='g', label= r'$\omega = 10$')
#ax.plot(ex[2],ey[2],ez[2], c='m', label= r'$\omega = 50$')
#ax.plot(ex[3],ey[3],ez[3], c='b', label= r'$\omega = 100$')
#ax.legend()
##plt.title("Efeito Magnus")
ax.set_xlabel('Vx')
ax.set_xlim(-3,3)
ax.set_ylabel('Vy')
ax.set_ylim(-1,1)
ax.set_zlabel('Vz')
ax.set_zlim(-1,1)
plt.show()

