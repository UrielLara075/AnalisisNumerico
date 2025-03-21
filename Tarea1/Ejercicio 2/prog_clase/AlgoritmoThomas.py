import numpy as np
from numpy import linalg as LA

# Tamaño de la matriz
n = 5

# Crear la diagonal principal
DP=2*np.ones(n)
diagonal_principal = np.diag(DP)

# Crear la diagonal superior
DS=-np.ones(n-1)
diagonal_superior = np.diag(DS, k=1)

# Crear la diagonal inferior
DI=-np.ones(n-1)
diagonal_inferior = np.diag(DI, k=-1)

# Sumar las tres diagonales para obtener la matriz tribanda
matriz_tribanda = diagonal_principal + diagonal_superior + diagonal_inferior
print(matriz_tribanda)

b=np.ones(n)

from scipy.linalg import lu
P, L, U = lu(matriz_tribanda)
U

def Thomas(DP,DS,DI,b):
  n=len(DP)
  x=np.zeros(n)

  for i in range(1,n):
    DP[i]=DP[i]-(DI[i-1]/DP[i-1])*DS[i-1]


  x[-1]=b[-1]/DP[-1]

  for i in range(n-2,-1,-1):
    x[i]=(b[i]-DS[i]*x[i+1])/DP[i]
  return x

Thomas(DP,DS,DI,b)

LA.solve(U,b)
