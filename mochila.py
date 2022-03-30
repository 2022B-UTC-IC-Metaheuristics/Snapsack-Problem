import math
import random as rn
import numpy as np
import sys
sys.setrecursionlimit(8000)
T=5
L=5
alpha=.55
sAct= np.array([0,0,0,0,0,0,0,0,0,0])
sCand=sAct
v=np.array([20,4,5,2,8,20,4,5,2,8])
p=np.array([10,2,14,8,5,10,2,14,8,5])
size = v.shape[0]
R=0.2
cap=20
k=1.380649*pow(10,-23)

def Genera_Vecino(size, cap):
    sol = np.zeros(size)
    for i in range(size):
        r = rn.random()
        if r > .5:
            sol[i] = 1
        else:
            sol[i] = 0
    c=0
    #print("dentro fun:", sol)
    for i in range(size):
        if sol[i] == 1:
            c+=p[i]
    if c > cap:
        sol=Genera_Vecino(size,cap)
    
    return sol
    
def Costo(sol,size):
    f=0
    for i in range(size):
        if sol[i] == 1:
            f+=v[i]
    return f

def recocido(sAct,T,L,alpha,R):
    while T > 0.001 :
        for i in range(L):
            sCand = Genera_Vecino(size,cap)
            AE=Costo(sCand,size) - Costo(sAct,size)
            if AE >= 0:
                sAct = sCand
            else:
                proba= pow(math.e,-(-AE/(k*T)))
                if proba > R:
                   sAct = sCand 
        T=alpha*T
    return sAct
            
x = recocido(sAct,T,L,alpha,R)
print(x)