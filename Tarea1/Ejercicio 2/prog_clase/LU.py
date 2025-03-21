import numpy as np
from numpy import linalg as LA

A=np.array([[4.,12.,-16.],[12.,37.,-43.],[-16.,-43.,98.]])
b=np.ones(3)

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


def LU(A):
  U=np.copy(A)
  L=np.eye(A.shape[0])

  for i in range(A.shape[0]):
    Li=np.eye(A.shape[0])
    for j in range(i+1,A.shape[0]):
      Li[j,i]=-U[j,i]/U[i,i]
      L[j,i]=U[j,i]/U[i,i]
    U=Li@U
  return L,U

def SolverLU(A,b):
  L,U=LU(A)
  # El sistema que se resuelve es Ly=b
  y=SustitucionDelante(L, b)
  # El sistema que se resuelve es Ux=y
  x=SustitucionAtras(U, y)

  return x

Sol=SolverLU(A,b)
Sol

LA.solve(A,b)


