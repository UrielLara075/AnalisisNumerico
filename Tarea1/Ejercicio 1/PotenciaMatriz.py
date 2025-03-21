# Potencia de una matriz.
# Lara Estrada Uriel Alejandro
from MultiplicacionMatricesBloques import MatMultBloques
from utilidades import matriz
import numpy as np
import timeit

def PotenciaMatriz(A, k):
    """
    Calcula la potencia de una matriz A usando la multiplicación matricial por bloques.
    
    Parámetros:
    A : list
        Matriz de tamaño n x n.
    k : int
        Potencia a la que se elevará la matriz.
        
    Retorna:
    list
        Matriz A elevada a la potencia k.
    """
    if len(A) != len(A[0]):
        return 'La matriz no es cuadrada.'
    Ak = matriz(len(A), len(A[0]))
    # Define Ak como la identidad.
    for i in range(len(A)):
        Ak[i][i] = 1
    for i in range(k):
        Ak = MatMultBloques(Ak, A, 25)
    return Ak

if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(3, 3, randomizar=True)
    A_mat = np.array(A)
    print('A=', A)
    print('¿La potencia con PotenciaMatriz es igual a la potencia con Numpy?', np.array_equal(PotenciaMatriz(A, 10), np.linalg.matrix_power(A_mat, 10)))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: PotenciaMatriz(A, 10), number=1000)
    print("Tiempo de ejecución de PotenciaMatriz:", tiempo, "para 1000 iteraciones")