# Multiplicación matricial  por bloques.
# Lara Estrada Uriel Alejandro

import timeit
import numpy as np
from utilidades import matriz
from utilidades import MultMat

def MatMultBloques (A, B, tamaño_bloques):
    '''
    Multiplica dos matrices A y B.
    
    Parámetros:
    A : list
        Matriz de tamaño m x n.
    B : list
        Matriz de tamaño n x k.
    tamaño_bloques : int
        Tamaño de los bloques en los que se dividirán las matrices.
        
    Retorna:
    list
        Matriz de tamaño m x k.
    
    Ejemplo:
    >>> A = [[1, 2], [3, 4]]
    >>> B = [[5, 6], [7, 8]]
    >>> MatMult(A, B, 1)
    [[19, 22], [43, 50]]
    '''
    # Verifica si las matrices se pueden multiplicar.
    if len(A[0]) != len(B):
        return "Las matrices no se pueden multiplicar"
    m, n, k = len(A), len(A[0]), len(B[0])
    # Crea una matriz de ceros de tamaño m x k.
    C = matriz(m, k)
        
    for i in range(0, m, tamaño_bloques): # Recorre bloques de filas de A.
        for j in range(0, k, tamaño_bloques): # Recorre bloques de columnas de B.
            for l in range(0, n, tamaño_bloques): # Recorre bloques de columnas de A (filas de B).
                for o in range(i, min(i + tamaño_bloques, m)): # Recorre las filas del bloque C.
                    for p in range(j, min(j + tamaño_bloques, k)): # Recorre las columnas del bloque C.
                        suma = 0
                        for q in range(l, min(l + tamaño_bloques, n)) : # Recorre los indices intermedios de los bloques de A y B.
                            suma += A[o][q] * B[q][p] # Multiplica los bloques y se suman al total.
                        C[o][p] += suma
    return C            


if __name__ == '__main__':
    # Ejemplo de uso.
    A = matriz(20, 20, randomizar=True)
    B = matriz(20, 20, randomizar=True)
    A_mat = np.array(A)
    B_mat = np.array(B)
    print('A=', A)
    print('B=', B)
    print('Por bloques, AB=', MatMultBloques(A, B, 10))
    print('Con codigo de clase, AB=', MultMat(A_mat, B_mat))


    # Comparación de velocidad de ejecución con la multiplicación usual.

    # Matriz de tamaño 10 x 10.
    print("Matriz de tamaño 10 x 10.")
    A = matriz(10, 10, randomizar=True)
    B = matriz(10, 10, randomizar=True)
    A_mat = np.array(A)
    B_mat = np.array(B)
    tiempo1 = timeit.timeit(lambda: MultMat(A_mat, B_mat), number=1000)
    print("Tiempo de ejecución de MultMat:", tiempo1, "para 1000 iteraciones.")
    # Bloques de 2 x 2.
    print("Bloques de 2 x 2.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 2), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")
    # Bloques de 5 x 5.
    print("Bloques de 5 x 5.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 5), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")


    # Matriz de tamaño 50 x 50.
    print("Matriz de tamaño 50 x 50.")
    A = matriz(50, 50, randomizar=True)
    B = matriz(50, 50, randomizar=True)
    A_mat = np.array(A)
    B_mat = np.array(B)
    tiempo1 = timeit.timeit(lambda: MultMat(A_mat, B_mat), number=1000)
    print("Tiempo de ejecución de MultMat:", tiempo1, "para 1000 iteraciones.")
    # Bloques de 5 x 5.
    print("Bloques de 5 x 5.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 5), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")
    # Bloques de 10 x 10.
    print("Bloques de 10 x 10.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 10), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")
    # Bloques de 25 x 25.
    print("Bloques de 25 x 25.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 25), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")


    # Matriz de tamaño 100 x 100.
    print("Matriz de tamaño 100 x 100.")
    A = matriz(100, 100, randomizar=True)
    B = matriz(100, 100, randomizar=True)
    A_mat = np.array(A)
    B_mat = np.array(B)
    tiempo1 = timeit.timeit(lambda: MultMat(A_mat, B_mat), number=1000)
    print("Tiempo de ejecución de MultMat:", tiempo1, "para 1000 iteraciones.")
    # Bloques de 10 x 10.
    print("Bloques de 10 x 10.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 10), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")
    # Bloques de 25 x 25.
    print("Bloques de 25 x 25.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 25), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")
    # Bloques de 50 x 50.
    print("Bloques de 50 x 50.")
    tiempo2 = timeit.timeit(lambda: MatMultBloques(A, B, 50), number=1000)
    print("Tiempo de ejecución de MatMultBloques:", tiempo2, "para 1000 iteraciones.")


    # Se puede ver en las pruebas que la multiplicación por bloques es signifiativamente
    # más eficiente que el algoritmo hecho en clase, y la diferencia es más clara cuando 
    # aumentamos el tamaño de la matriz y los bloques.
