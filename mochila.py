import math
import random as rn
import numpy as np
import sys
T=5
L=20
alpha=.55
sAct= np.array([0,0,0,0,0])
sCand=sAct
v=np.array([20,4,25,2,8])
p=np.array([10,2,14,8,5])
R=0.2
cap=20
k=1.380649*pow(10,-23)
sys.setrecursionlimit(8000)
def Genera_Vecino():
    for i in range(sCand.shape[0]):
        r = rn.random()
        if r > .5:
            sCand[i] = 1
        else:
            sCand[i] = 0
    c=0
    for i in range(sCand.shape[0]):
        if sCand[i] == 1:
            c+=p[i]
    if c > cap:
        Genera_Vecino()
    else:
        return
    
def Costo(sol):
    f=0
    for i in range(sol.shape[0]):
        if sol[i] == 1:
            f+=v[i]
    return f

def recocido(sAct,T,L,alpha,R):
    while T > 0.001 :
        for i in range(L):
            Genera_Vecino()
            AE=Costo(sCand) - Costo(sAct)
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