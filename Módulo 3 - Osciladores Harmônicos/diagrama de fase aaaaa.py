# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:07:46 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations_with_replacement

#fig = plt.figure()
#ax=fig.add_subplot(111)
#ax = fig.gca(projection='3d')

Nx=2
Nwd = Nx*Nx
X=np.zeros(Nwd)
V=np.zeros(Nwd)
x=np.zeros(Nwd)
v=np.zeros(Nwd)
X1=[]
V1=[]
X2=[]
V2=[]
X3=[]
V3=[]
X4=[]
V4=[]
a=np.zeros(Nwd)
fX=np.zeros(Nwd)
gX=np.zeros(Nwd)
amp=np.zeros(Nwd)
fXmeio=np.zeros(Nwd)
Xmeio=np.zeros(Nwd)
Vmeio=np.zeros(Nwd)
ameio=np.zeros(Nwd)
L = 5
dx = L/Nx
cont=0
q=np.zeros((Nwd,1))
p=np.zeros((Nwd,1))

g=9.8
l=1.0

#v=np.linspace(5.0,10.0,Nwd/2)
#x=np.linspace(5.0,10.0,Nwd/2)

for i in range(Nx):
    for j in range(Nx):
        n = Nx*i + j
        q[n][0] = L/2+i*dx
        p[n][0] = L/2+j*dx
        print('q = ',q[n][0],'p = ',p[n][0])
        

t=0.0
tmax=20.0
dt=0.1
w0=1.0
#alfa=w0*w0 OHS
alfa = g/l


for i in range(Nwd): 
    a[i]=-alfa*fX[i]
#    fX[i]=X[i]
#    gX[i]=(X[i]*X[i])/2

    fX[i]=math.sin(X[i])
    gX[i]=1-math.cos(X[i])
    
    X[i] = q[i][0]*math.pi/180
    V[i] = p[i][0]*math.pi/180
    x[i] = q[i][0]*math.pi/180
    v[i] = p[i][0]*math.pi/180
    
ex=[[] for _ in range(int(Nwd))]
ey=[[] for _ in range(int(Nwd))]
eX=[[] for _ in range(int(Nwd))]
eY=[[] for _ in range(int(Nwd))]
et=[]

while(t<tmax):      #Euler-Cromer

#   plt.plot([ex[cont][0],ex[cont][1]],[ey[cont][0],ey[cont][1]])
#   plt.plot([ex[cont][1],ex[cont][3]],[ey[cont][1],ey[cont][3]])
#   plt.plot([ex[cont][3],ex[cont][2]],[ey[cont][3],ey[cont][2]])
#   plt.plot([ex[cont][2],ex[cont][0]],[ey[cont][2],ey[cont][0]])
   x[0] = (2.5*math.pi/180.0)*np.cos(math.sqrt(g/l)*t) + ((2.5*math.pi/180.0)/math.sqrt(g/l))*np.sin(math.sqrt(g/l)*t)
   v[0] = -(2.5*math.pi/180.0)*math.sqrt(g/l)*np.sin(math.sqrt(g/l)*t) + (2.5*math.pi/180.0)*np.cos(math.sqrt(g/l)*t)
   x[1] = (2.5*math.pi/180.0)*np.cos(math.sqrt(g/l)*t) + ((5.0*math.pi/180.0)/math.sqrt(g/l))*np.sin(math.sqrt(g/l)*t)
   v[1] = -(2.5*math.pi/180.0)*math.sqrt(g/l)*np.sin(math.sqrt(g/l)*t) + (5.0*math.pi/180.0)*np.cos(math.sqrt(g/l)*t)
   x[2] = (5.0*math.pi/180.0)*np.cos(math.sqrt(g/l)*t) + ((2.5*math.pi/180.0)/math.sqrt(g/l))*np.sin(math.sqrt(g/l)*t)
   v[2] = -(5.0*math.pi/180.0)*math.sqrt(g/l)*np.sin(math.sqrt(g/l)*t) + (2.5*math.pi/180.0)*np.cos(math.sqrt(g/l)*t)
   x[3] = (5.0*math.pi/180.0)*np.cos(math.sqrt(g/l)*t) + ((5.0*math.pi/180.0)/math.sqrt(g/l))*np.sin(math.sqrt(g/l)*t)
   v[3] = -(5.0*math.pi/180.0)*math.sqrt(g/l)*np.sin(math.sqrt(g/l)*t) + (5.0*math.pi/180.0)*np.cos(math.sqrt(g/l)*t)
   
   X1.append(x[0]*180/math.pi)
   V1.append(v[0]*180/math.pi)
   X2.append(x[1]*180/math.pi)
   V2.append(v[1]*180/math.pi)
   X3.append(x[2]*180/math.pi)
   V3.append(v[2]*180/math.pi)
   X4.append(x[3]*180/math.pi)
   V4.append(v[3]*180/math.pi)
   
   for i in range(Nwd): 
       ex[i].append(X[i]*180/math.pi)
       ey[i].append(V[i]*180/math.pi)
       
#       eX[i].append(x[i])
#       eY[i].append(v[i])
       
       
              
       V[i] = V[i] + a[i]*dt 
       X[i] = X[i] + V[i]*dt

       
      
#       a[i]=-alfa*X[i]
#       Vmeio[i] = V[i] + a[i]*dt/2
#       Xmeio[i] = X[i] + Vmeio[i]*dt/2
#        
#       fXmeio[i] = Xmeio[i]
#       ameio[i] = -alfa*fXmeio[i]
#       V[i] = Vmeio[i] + ameio[i]*dt/2
#       X[i] = Xmeio[i] + V[i]*dt/2
      
#       ex[i].append(X[i])
#       ey[i].append(V[i])
       
       fX[i]=math.sin(X[i])
       gX[i]=1-math.cos(X[i])
       a[i]=-alfa*fX[i]
   if cont%3==0:
       for i in range(Nwd):
           vecolor = np.array([((5+i)%3)/2.0,((5+i)%4)/3.0,((5+i)%7)/6.0])
           plt.scatter(ex[i][cont],ey[i][cont], c=vecolor)
#       plt.scatter(ex[1][cont],ey[1][cont], c='b')
#       plt.scatter(ex[3][cont],ey[3][cont], c='r')
#       plt.scatter(ex[2][cont],ey[2][cont], c='m')
       plt.plot([ex[0][cont],ex[1][cont]],[ey[0][cont],ey[1][cont]], c='grey')
       plt.plot([ex[1][cont],ex[3][cont]],[ey[1][cont],ey[3][cont]], c='grey')
       plt.plot([ex[3][cont],ex[2][cont]],[ey[3][cont],ey[2][cont]], c='grey')
       plt.plot([ex[2][cont],ex[0][cont]],[ey[2][cont],ey[0][cont]], c='grey')  
       
#       plt.plot(X1,V1)
#       plt.plot(X2,V2)
#       plt.plot(X3,V3)
#       plt.plot(X4,V4)
          
   #et.append(t)
   cont = cont + 1
   t=t+dt
#for i in range(Nwd):   
#    plt.plot(ex[i][0],ey[i][0])


plt.xlabel('q')
plt.ylabel('p')
#ax.plot(ex[5],ey[5], c='r')
#ax.plot(et,ex[1], c='g')
#ax.plot(et,ex[2], c='b')
#ax.legend()
#ax.set_xlabel(r'$\omega_d$')
#ax.set_ylabel('Amplitude')
#ax.set_zlabel('E')
#ax.set_zlim(0.045, 0.055)
#plt.grid()
plt.title(r'$l = 1.0$')
plt.show()   
            