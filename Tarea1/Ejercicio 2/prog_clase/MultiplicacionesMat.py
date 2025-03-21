import numpy as np

n=5
m=6
#A=n*[n*[1]]
A=np.ones((m,n))
b=np.ones(n)
A.shape

import numpy as np

def MatVec(Mat, vec):
    """
    Realiza la multiplicación de una matriz por un vector.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Una matriz bidimensional de forma (n, m), donde 'n' es el número de filas
        y 'm' es el número de columnas.
    vec : numpy.ndarray
        Un vector unidimensional de forma (m,), donde 'm' debe coincidir con el
        número de columnas de la matriz.

    Retorna:
    --------
    numpy.ndarray
        Un vector unidimensional de forma (n,) que representa el resultado de
        la multiplicación de la matriz por el vector.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> vec = np.array([1, 0, 2])
    >>> MatVec(Mat, vec)
    array([ 7., 16., 25.])
    """
    # Inicializa un vector de ceros con la misma cantidad de filas que la matriz Mat
    Mv = np.zeros(Mat.shape[0])

    # Itera sobre cada fila de la matriz
    for ren in range(Mat.shape[0]):
        # Itera sobre cada columna de la matriz
        for col in range(Mat.shape[1]):
            # Realiza la multiplicación de la fila actual de la matriz por el vector
            Mv[ren] += Mat[ren, col] * vec[col]

    # Devuelve el vector resultante
    return Mv


MatVec(A,b)

A=np.ones((m,n))
B=np.ones((n,m))
A.shape,B.shape

import numpy as np

def MultMat(Mat1, Mat2):
    """
    Realiza la multiplicación de dos matrices.

    Parámetros:
    -----------
    Mat1 : numpy.ndarray
        Una matriz bidimensional de forma (n, m), donde 'n' es el número de filas
        y 'm' es el número de columnas.
    Mat2 : numpy.ndarray
        Una matriz bidimensional de forma (m, p), donde 'm' es el número de filas
        (debe coincidir con el número de columnas de Mat1) y 'p' es el número de
        columnas.

    Retorna:
    --------
    numpy.ndarray
        Una matriz bidimensional de forma (n, p) que representa el resultado de
        la multiplicación de Mat1 por Mat2.

    Ejemplo:
    --------
    >>> Mat1 = np.array([[1, 2, 3], [4, 5, 6]])
    >>> Mat2 = np.array([[7, 8], [9, 10], [11, 12]])
    >>> MultMat(Mat1, Mat2)
    array([[ 58.,  64.],
           [139., 154.]])
    """
    # Inicializa una matriz de ceros con las dimensiones adecuadas
    Mat3 = np.zeros((Mat1.shape[0], Mat2.shape[1]))

    # Itera sobre cada fila de la primera matriz
    for row in range(Mat1.shape[0]):
        # Itera sobre cada columna de la segunda matriz
        for col in range(Mat2.shape[1]):
            # Realiza la multiplicación y suma los productos
            for aux in range(Mat2.shape[0]):
                Mat3[row, col] += Mat1[row, aux] * Mat2[aux, col]

    # Devuelve la matriz resultante
    return Mat3

MultMat(A,B)


