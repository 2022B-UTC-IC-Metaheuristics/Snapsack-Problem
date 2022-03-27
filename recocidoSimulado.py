import math
import random as rn
import numpy as np
#T= int ( input())
T=20
L=20
alpha=.55
sAct= np.array([])
sCand=sAct
H=[[]]
v=[]
p=[]
R=0.2
cap=0
k=1.380649*pow(10,-23)
print(k)
def Genera_Vecino():
    for i in range(sCand.shape[0]):
        r = rn.randint(0,1)
        sCand[i] = r
        if any(s == sCand for s in H):
            Genera_Vecino()
        else:
            return
    
def Costo(sol):
    f=0
    #c=0
    for i in range(sol.shape[0]):
        if sol[i] == 1:
            f+=v[i]
            #c+=p[i]
    #if c > cap:
        #return -1 # codigo de error
    #else: 
        #return f
    return f
    

def recocido(sAct,T,L,alpha,R):
    
    while T > 0.001 :
        for i in L:
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
            
#penalizacion
c=0
for i in range(sAct.shape[0]):
    if sAct[i] == 1:
        c+=p[i]
if c > cap:
    #penalizas restar al valor en funcion de los pesos
    ide=p.index(max(p))
    del sAct[ide]
else:
    print(sAct)