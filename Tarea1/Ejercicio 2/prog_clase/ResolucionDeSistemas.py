import numpy as np
from numpy import linalg as LA

import numpy as np

def SolverDiagonal(A, b):
    """
    Resuelve un sistema de ecuaciones lineales donde la matriz A es diagonal.

    Esta función resuelve el sistema de ecuaciones Ax = b, donde A es una matriz diagonal
    representada por su diagonal principal (un vector). La solución se obtiene dividiendo
    cada elemento del vector b por el correspondiente elemento de la diagonal de A.

    Parámetros:
    -----------
    A : array_like
        Un arreglo unidimensional que representa la diagonal principal de la matriz A.
        Debe tener la misma longitud que el vector b.

    b : array_like
        Un arreglo unidimensional que representa el vector de términos independientes del sistema.

    Retorna:
    --------
    x : ndarray
        Un arreglo unidimensional que contiene la solución del sistema Ax = b.

    Ejemplo:
    --------
    >>> A = np.array([2, 4, 6])  # Diagonal principal de la matriz A
    >>> b = np.array([8, 16, 36])  # Vector de términos independientes
    >>> x = SolverDiagonal(A, b)
    >>> print(x)
    [4. 4. 6.]

    Notas:
    ------
    - La función asume que la matriz A es diagonal y que no hay elementos fuera de la diagonal.
    - Si algún elemento de la diagonal A es cero, se producirá un error de división por cero.
    """
    n = len(A)
    x = np.zeros_like(A, dtype=float)  # Asegura que x sea de tipo flotante
    for i in range(n):
        x[i] = b[i] / A[i]
    return x

AA=np.array([1.0,2.0,3.0])
bb=np.ones_like(AA)

SolverDiagonal(AA,bb)

import numpy as np

def SustitucionDelante(Mat, b):
    """
    Realiza la sustitución hacia adelante para resolver un sistema de ecuaciones lineales
    representado por una matriz triangular inferior.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Una matriz triangular inferior de tamaño n x n.
    b : numpy.ndarray
        Un vector de términos independientes de tamaño n.

    Retorna:
    --------
    x : numpy.ndarray
        Un vector solución de tamaño n que satisface la ecuación Mat @ x = b.

    Descripción:
    ------------
    Esta función resuelve un sistema de ecuaciones lineales de la forma Mat @ x = b,
    donde Mat es una matriz triangular inferior. Utiliza el método de sustitución hacia adelante,
    comenzando desde la primera fila de la matriz y avanzando hacia la última.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 0, 0],
    ...                 [2, 3, 0],
    ...                 [4, 5, 6]])
    >>> b = np.array([1, 8, 32])
    >>> SustitucionDelante(Mat, b)
    array([1., 2., 3.])
    """
    n = Mat.shape[0]
    x = np.zeros(n)

    for i in range(n):
        SumCum = 0.0
        for j in range(i):
            SumCum += Mat[i, j] * x[j]
        x[i] = (b[i] - SumCum) / Mat[i, i]

    return x

import numpy as np

# Crear una matriz cuadrada de ejemplo
matriz = np.array([[1.0, 2.0, 3.0],
                   [4.0, 5.0, 6.0],
                   [7.0, 8.0, 9.0]])

# Convertir la matriz en una matriz triangular inferior
MTI = np.tril(matriz)
MTS = np.triu(matriz)
print(MTS)

SustitucionDelante(MTI,bb)

LA.solve(MTI,bb)

import numpy as np

def SustitucionAtras(Mat, b):
    """
    Realiza la sustitución hacia atrás para resolver un sistema de ecuaciones lineales
    representado por una matriz triangular superior.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Una matriz triangular superior de tamaño n x n.
    b : numpy.ndarray
        Un vector de términos independientes de tamaño n.

    Retorna:
    --------
    x : numpy.ndarray
        Un vector solución de tamaño n que satisface la ecuación Mat @ x = b.

    Descripción:
    ------------
    Esta función resuelve un sistema de ecuaciones lineales de la forma Mat @ x = b,
    donde Mat es una matriz triangular superior. Utiliza el método de sustitución hacia atrás,
    comenzando desde la última fila de la matriz y avanzando hacia la primera.

    Ejemplo:
    --------
    >>> Mat = np.array([[3, 2, 1],
    ...                 [0, 2, 1],
    ...                 [0, 0, 1]])
    >>> b = np.array([6, 4, 1])
    >>> SustitucionAtras(Mat, b)
    array([1., 1., 1.])
    """
    n = Mat.shape[0]
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        SumCum = 0.0
        for j in range(i+1, n):
            SumCum += Mat[i, j] * x[j]
        x[i] = (b[i] - SumCum) / Mat[i, i]

    return x

SustitucionAtras(MTS,bb)

LA.solve(MTS,bb)


