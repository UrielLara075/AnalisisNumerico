# Norma 2 de una matriz.
# Lara Estrada Uriel Alejandro
from math import sqrt
from utilidades import matriz
import numpy as np
import timeit

def Norma2(A):
    """
    Calcula la norma 2 de la matriz A.
    
    Parámetros:
    A : list
        Matriz de tamaño n x m.
    
    Retorna:
    float
        Norma 2 de la matriz A.
    """
    n, m = len(A), len(A[0])
    Norma = 0
    for i in range(n):
        for j in range(m):
            Norma += A[i][j] ** 2
    return sqrt(Norma)

if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(5, 4, randomizar=True)
    print('A=', A)
    print('Norma 2 de A:', Norma2(A))
    print('¿La norma 2 con Numpy es igual a la norma 2 con Norma2?', np.linalg.norm(A) == Norma2(A))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: Norma2(A), number=1000)
    print("Tiempo de ejecución de Norma2:", tiempo, "para 1000 iteraciones")