# Suma matricial por bloques
# Lara Estrada Uriel Alejandro

import numpy as np
import timeit
from utilidades import matriz

def SumaBloques(A, B, tamaño_bloques):
    """
    Suma dos matrices A y B.
    
    Parámetros:
    A : list
        Matriz de tamaño m x n.
    B : list
        Matriz de tamaño m x n.
    tamaño_bloques : int
        Tamaño de los bloques en los que se dividirán las matrices.
        
    Retorna:
    list
        Matriz de tamaño m x n.
    """
    if len(A[0]) != len(B[0]) or len(A) != len(B):
        return 'Las matrices no son del mismo tamaño.'
    m, n = len(A), len(A[0])
    # Crea una matriz de ceros de tamaño m x k.
    C = matriz(m, n)  
    for i in range(0, m, tamaño_bloques): # Recorre bloques de filas de A y B.
        for l in range(0, n, tamaño_bloques): # Recorre bloques de columnas de A y B.
            for o in range(i, min(i + tamaño_bloques, m)):  # Recorre las filas del bloque.
                for p in range(l, min(l + tamaño_bloques, n)): # Recorre las columnas del bloque.
                    C[o][p] = A[o][p] + B[o][p]
    return C

if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(10, 10, randomizar=True)
    B = matriz(10, 10, randomizar=True)
    A_mat = np.array(A)
    B_mat = np.array(B)
    print('A=', A)
    print('B=', B)
    print('Por bloques, A+B=', SumaBloques(A, B, 2))
    print('Con numpy, A+B=', A_mat + B_mat)

    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: SumaBloques(A, B, 2), number=1000)
    print("Tiempo de ejecución de SumaBloques:", tiempo, "para 1000 iteraciones.")