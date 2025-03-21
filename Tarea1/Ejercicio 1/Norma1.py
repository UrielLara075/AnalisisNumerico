# Norma 1 de una matriz.
# Lara Estrada Uriel Alejandro
import numpy as np
from utilidades import matriz
import timeit

def Norma1(A):
    """
    Calcula la norma 1 de una matriz A.
    
    Parámetros:
    A : list
        Matriz de tamaño n x m.
    
    Retorna:
    float
        Norma 1 de la matriz A.
    """
    n, m = len(A), len(A[0])
    Norma = 0
    for j in range (m):
        sum = 0
        for i in range(n):
            sum += abs(A[i][j])
        Norma = max(Norma, sum)
    return Norma

if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(5, 4, randomizar=True)
    print('A=', A)
    print('Norma 1 de A:', Norma1(A))
    print('¿La norma 1 con Numpy es igual a la norma 1 con Norma1?', np.linalg.norm(A, 1) == Norma1(A))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: Norma1(A), number=1000)
    print("Tiempo de ejecución de Norma1:", tiempo, "para 1000 iteraciones")