# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:06:53 2019

@author: gabri
"""

import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

X=0.0
V=0.0
fXmeio=0.0
Xmeio=0.0
Vmeio=0.0
ameio=0.0
e=0.0
E=0.0
fX=0.0
gX=0.0
t=0.0
tmax=10
dt=0.01
resp1=0
resp2=0

Xexato=0.0
Vexato=0.0
Eexato=0.0


vang= 0.0
ang = 5.0
rad = ang*math.pi/180
v=0.0
x=10.0
alfa=1.0
w0=2.0
m=2.0
g=9.8
l=1.0

a=-alfa*fX

ex=[]
ey=[]
ez=[]
et=[]

xteo=[]
yteo=[]
zteo=[]

resp1 = int(input('Digite 1 para OHS ou 2 para Pendulo Simples:  '))

if resp1==1:
    X=x
    V=v
    alfa=w0*w0
    fX=X
    gX=(X*X)/2
    fXmeio = Xmeio
    
    resp2 = int(input('Digite 1 para Euler, 2 para Euler-Cromer, 3 para Euler-Richardson:  '))
    
    if resp2==1:        #Euler
       while(t<tmax):
           X = X + V*dt
           V = V + a*dt  
           e = V*V/2 + alfa*gX
           
           ez.append(e)
           ex.append(X)
           ey.append(V)
           et.append(t)
           
           gX=(X*X)/2
           fX=X
           a=-alfa*fX
           t = t+dt
       plt.plot(et, ex, label = 'Euler') 
    
    if resp2==2:        #Euler-Cromer
       while(t<tmax):
           V = V + a*dt
           X = X + V*dt
           e = V*V/2 + alfa*gX
           
           ez.append(e)
           ex.append(X)
           ey.append(V)
           et.append(t)
           
           gX=(X*X)/2
           fX=X
           a=-alfa*fX
           
           Xexato = 10*math.cos(w0*t)
           Vexato = -w0*10*math.sin(w0*t) 
           Eexato = (1/2)*Vexato*Vexato + (1/2)*w0*w0*Xexato*Xexato
           zteo.append(Eexato)
           xteo.append(Xexato)
           yteo.append(Vexato)
           t=t+dt
       ax.plot(xteo,yteo,zteo, c='b', label = 'Analítico')
       ax.plot(ex,ey,ez, c='r', label = 'Numérico') 
       ax.set_zlim(175.0, 225.0)
        

    if resp2==3:        #Euler-Richardson
        while(t<tmax):
             
            a=-alfa*X
            Vmeio = V + a*dt/2
            Xmeio = X + Vmeio*dt/2
            
            fXmeio = Xmeio
            ameio = -alfa*fXmeio
            V = Vmeio + ameio*dt/2
            X = Xmeio + V*dt/2
            
#            Vmeio = V + a*dt/2
#            Xmeio = X + Vmeio*dt/2
#            fXmeio = Xmeio
#            ameio = -alfa*fXmeio   
#            
#            V = Vmeio + ameio*dt
#            X = Xmeio + V*dt
#            a=-alfa*X
            
            e = V*V/2 + w0*w0*X*X/2
            
            ez.append(e)
            ex.append(X)
            ey.append(V)
            et.append(t)
            #print(e)            
            t=t+dt
        plt.plot(et, ex, label = 'Euler-Richardson') 
        
if resp1==2:
    X=rad
    V=vang
    alfa=g/l
    fX=math.sin(X)
    gX=1-math.cos(X)
    fXmeio = math.sin(Xmeio)
    
    resp2 = int(input('Digite 1 para Euler, 2 para Euler-Cromer, 3 para Euler-Richardson:  '))
    
    if resp2==1:        #Euler
       while(t<tmax):
           X = X + V*dt
           V = V + a*dt  
           e = V*V/2 + alfa*gX
           
           ez.append(e)
           ex.append(180*X/math.pi)
           ey.append(V)
           et.append(t)
           
           gX=1-math.cos(X)
           fX=math.sin(X)
           a=-alfa*fX
           t = t+dt
           
       plt.plot(et, ex, label = 'Euler')   
    if resp2==2:        #Euler-Cromer
       while(t<tmax):
           V = V + a*dt
           X = X + V*dt
           e = V*V/2 + alfa*gX
           
           ez.append(e)
           ex.append(180*X/math.pi)
           ey.append(V)
           et.append(t)
           
           gX=1-math.cos(X)
           fX=math.sin(X)
           a=-alfa*fX
           
           
           Xexato = (5.0*math.pi/180.0)*math.cos(math.sqrt(g/l)*t)
           Vexato = -math.sqrt(g/l)*(5.0*math.pi/180.0)*math.sin(math.sqrt(g/l)*t) 
           Eexato = l*l*Vexato*Vexato/2 + g*(1.0-math.cos(Xexato))
           
           zteo.append(Eexato)
           xteo.append(Xexato)
           yteo.append(Vexato)
           
           
           t = t+dt
       #plt.plot(et, ex, label = 'Euler-Cromer')
       ax.plot(xteo,yteo,zteo, c='b', label = 'Analítico')
       #ax.plot(ex,ey,ez, c='r', label = 'Numérico')
       
    if resp2==3:        #Euler-Richardson
        while(t<tmax):
            
            Vmeio = V + a*dt/2
            Xmeio = X + Vmeio*dt/2
            
            fXmeio = math.sin(Xmeio)
            ameio = -alfa*fXmeio   
            
            V = Vmeio + ameio*dt/2
            X = Xmeio + V*dt/2
            fX = math.sin(X)
            a=-alfa*fX
            
            gX= 1-math.cos(X)
            e = V*V/2 + alfa*gX
            
            ez.append(e)
            ex.append(180*X/math.pi)
            ey.append(V)
            et.append(t)
            
            
            t = t+dt
        #plt.plot(et, ex, label = 'Euler-Richardson')
        ax.plot(ex,ey,ez, c='r', label = 'Numérico')
        t=0.0
        
        while(t<tmax):
            Xexato = (5.0*math.pi/180.0)*math.cos(math.sqrt(g/l)*t)
            Vexato = -math.sqrt(g/l)*(5.0*math.pi/180.0)*math.sin(math.sqrt(g/l)*t) 
            Eexato = Vexato*Vexato/2 + g*(1.0-math.cos(Xexato))
           
            zteo.append(Eexato)
            xteo.append(Xexato*180/math.pi)
            yteo.append(Vexato)
            t=t+dt
        #plt.plot(xteo,yteo)
        ax.plot(xteo,yteo,zteo, c='b', label = 'Analítico')
        ax.set_zlim(0.032, 0.04)
        
#plt.xlabel('Tempo')
#plt.ylabel('Ângulo')
#plt.legend()
           
#ax.plot(xteo,yteo,zteo, c='b', label = 'curva teórica')
#ax.plot(ex,ey,ez, c='r', label = 'curva numérica')
        

ax.legend()
ax.set_xlabel('Posição')
ax.set_ylabel('Velocidade')
ax.set_zlabel('Energia')

plt.show()   
            
 