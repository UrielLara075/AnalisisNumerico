import numpy as np
from numpy import linalg as LA

import numpy as np

def SubMat(Mat, ren, col):
    """
    Crea una submatriz eliminando un renglón y una columna específicos de la matriz original.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz original de la cual se obtendrá la submatriz.
    ren : int
        Índice del renglón que se eliminará de la matriz.
    col : int
        Índice de la columna que se eliminará de la matriz.

    Retorna:
    --------
    numpy.ndarray
        Submatriz resultante después de eliminar el renglón y la columna especificados.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 2, 3],
    ...                [4, 5, 6],
    ...                [7, 8, 9]])
    >>> SubMat(Mat, 1, 1)
    array([[1, 3],
           [7, 9]])
    """
    # Crear una copia de la matriz original para no modificarla
    M1 = np.copy(Mat)

    # Eliminar el renglón especificado
    M1 = np.delete(M1, ren, axis=0)

    # Eliminar la columna especificada
    M1 = np.delete(M1, col, axis=1)

    return M1

import numpy as np

def Det(Mat):
    """
    Calcula el determinante de una matriz cuadrada de manera recursiva.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz cuadrada de la cual se calculará el determinante.
        Debe ser de tamaño n x n, donde n >= 2.

    Retorna:
    --------
    float
        El determinante de la matriz.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 2],
    ...                [3, 4]])
    >>> Det(Mat)
    -2.0

    >>> Mat = np.array([[6, 1, 1],
    ...                [4, -2, 5],
    ...                [2, 8, 7]])
    >>> Det(Mat)
    -306.0
    """
    # Caso base: matriz 2x2
    if Mat.shape[0] == 2 and Mat.shape[1] == 2:
        return Mat[0][0] * Mat[1][1] - (Mat[0][1] * Mat[1][0])

    # Caso recursivo: matrices más grandes
    deter = 0.0
    for col in range(Mat.shape[0]):
        # Calcula el cofactor y suma al determinante
        deter += ((-1) ** col) * Mat[0][col] * Det(SubMat(Mat, 0, col))
    return deter

import numpy as np

def Transpuesta(Mat):
    """
    Calcula la transpuesta de una matriz cuadrada modificando la matriz original.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz cuadrada de tamaño n x n que se transpondrá.
        La matriz se modificará in situ.

    Retorna:
    --------
    numpy.ndarray
        La matriz transpuesta. La matriz original también se modifica.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 2, 3],
    ...                [4, 5, 6],
    ...                [7, 8, 9]])
    >>> Transpuesta(Mat)
    array([[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]])
    """
    for ren in range(Mat.shape[0]):
        for col in range(Mat.shape[1]):
            if ren < col:
                # Intercambia los elementos para obtener la transpuesta
                Mat[ren, col], Mat[col, ren] = Mat[col, ren], Mat[ren, col]
    return Mat

import numpy as np

def Cofactores(Mat):
    """
    Calcula la matriz de cofactores de una matriz cuadrada.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz cuadrada de tamaño n x n para la cual se calcularán los cofactores.

    Retorna:
    --------
    numpy.ndarray
        Matriz de cofactores, donde cada elemento es el cofactor correspondiente
        de la matriz original.

    Ejemplo:
    --------
    >>> Mat = np.array([[1, 2],
    ...                [3, 4]])
    >>> Cofactores(Mat)
    array([[ 4., -3.],
           [-2.,  1.]])
    """
    # Crear una matriz de ceros del mismo tamaño que Mat para almacenar los cofactores
    Cofa = np.zeros_like(Mat, dtype=float)

    # Calcular el cofactor para cada elemento de la matriz
    for ren in range(Mat.shape[0]):
        for col in range(Mat.shape[1]):
            # Calcular el determinante de la submatriz (menor) y aplicar el signo
            Cofa[ren, col] = ((-1) ** (ren + col)) * Det(SubMat(Mat, ren, col))
    return Cofa

import numpy as np

def Inv(Mat):
    """
    Calcula la inversa de una matriz cuadrada utilizando la matriz de cofactores.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz cuadrada de tamaño n x n que se invertirá.
        Debe ser una matriz no singular (su determinante debe ser distinto de cero).

    Retorna:
    --------
    numpy.ndarray
        La matriz inversa de la matriz original.

    Ejemplo:
    --------
    >>> Mat = np.array([[4, 7],
    ...                [2, 6]])
    >>> Inv(Mat)
    array([[ 0.6, -0.7],
           [-0.2,  0.4]])
    """
    # Calcular el determinante de la matriz
    deter = Det(Mat)

    # Verificar si la matriz es singular (determinante = 0)
    if deter == 0:
        raise ValueError("La matriz es singular y no tiene inversa.")

    # Calcular la matriz de cofactores
    Cofac = Cofactores(Mat)

    # Transponer la matriz de cofactores para obtener la matriz adjunta
    Cofac = Transpuesta(Cofac)

    # Calcular la inversa multiplicando la adjunta por 1/determinante
    Inversa = (1 / deter) * Cofac

    return Inversa

if __name__ == "__main__":
    A=np.array([[2,3,-4],[0,-4,2],[1,-1,5]])
    b=np.array([1.0,1.0,1.0])

import numpy as np

def SolveInv(Mat, vec):
    """
    Resuelve un sistema de ecuaciones lineales utilizando la matriz inversa.

    Parámetros:
    -----------
    Mat : numpy.ndarray
        Matriz cuadrada de coeficientes del sistema de ecuaciones.
        Debe ser una matriz no singular (su determinante debe ser distinto de cero).

    vec : numpy.ndarray
        Vector de términos independientes.
        Su tamaño debe coincidir con el número de filas de la matriz `Mat`.

    Retorna:
    --------
    numpy.ndarray
        Vector solución del sistema de ecuaciones `Mat @ x = vec`.

    Excepciones:
    ------------
    ValueError
        Se lanza un error si la matriz `Mat` no es invertible.

    Ejemplo:
    --------
    >>> Mat = np.array([[2, 1],
    ...                 [5, 3]])
    >>> vec = np.array([4, 10])
    >>> SolveInv(Mat, vec)
    array([2., 0.])

    """
    # Calcular la inversa de la matriz
    InvMat = Inv(Mat)

    # Multiplicar la inversa por el vector de términos independientes
    Solucion = InvMat @ vec

    return Solucion

if __name__ == "__main__":
    Sol=SolveInv(A,b)
    print(Sol)
    Sol_python=LA.solve(A,b)
    print(Sol_python)
    """
    print(A)
    InvA=Inv(A)
    print(A@InvA)
    print(InvA@A)
    """


