# Norma infinito de una matriz.
# Lara Estrada Uriel Alejandro
import timeit
from utilidades import matriz
import numpy as np

def NormaInfinito(A):
    """
    Calcula la norma infinito de la matriz A.
    
    Parámetros:
    A : list
        Matriz de tamaño n x m.
    
    Retorna:
    float
        Norma infinito de la matriz A.
    """
    n, m = len(A), len(A[0])
    Norma = 0
    for i in range(n):
        Norma = max(Norma, sum(A[i]))
    return Norma

if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(5, 4, randomizar=True)
    print('A=', A)
    print('Norma infinito de A:', NormaInfinito(A))
    print('¿La norma infinito con Numpy es igual a la norma infinito con NormaInfinito?', np.linalg.norm(A, np.inf) == NormaInfinito(A))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: NormaInfinito(A), number=1000)
    print("Tiempo de ejecución de NormaInfinito:", tiempo, "para 1000 iteraciones")