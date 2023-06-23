import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


fig = plt.figure()
ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

D=0.25
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
eR = []
eRext = []
eN = []
eD = []


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
    
    if N%100 == 0:
        mx = np.mean(x)
        mx2 = np.mean(x2)
        my = np.mean(y)
        my2 = np.mean(y2)
        R = np.sqrt(mx2 - mx*mx + my2 - my*my)
        Rext = 2*np.sqrt(D*N)
        eRext.append(Rext)
        Dext = (R*R)/(4.0*N)
        eD.append(Dext)        
        eR.append(R)
        eN.append(N)

mD = np.mean(eD[1:20]) 
emD = np.full((20,1),mD)        
ax.scatter(eN[1:int(Nmax/100)],eD[1:int(Nmax/100)])
ax.plot(eN[1:int(Nmax/100)], emD[1:20])
#ax.scatter(eN[1:20],eR[1:20])
#ax.plot(eN[1:20],eRext[1:20], c='r')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('N')
plt.ylabel('D')
#plt.xscale('log')
#plt.yscale('log')
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
ax.set_xlabel('N')  
#plt.title("N = 1000 passos; M = 10000 caminhantes; C = 15.0")  
#print (x)
#print (y)
#print(mx)
#print (x2)
#print(mx2)
#plt.legend()
plt.show()       # -*- coding: utf-8 -*-