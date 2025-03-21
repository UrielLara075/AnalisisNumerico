# Rotación de un vector en R^3.
# Lara Estrada Uriel Alejandro
import math
import timeit
import numpy as np
from utilidades import vector
from ProductoPuntoBloques import ProductoPuntoBloques

def RotacionVector(v, angulo, eje='x'):
    """
    Rota un vector al rededor de un eje.
    
    Parámetros:
    v : list
        Vector de dimensión 3.
    angulo : float
        Ángulo de rotación en radianes.
    eje : str
        Eje de rotación 'x', 'y' o 'z'.
    
    Retorna:
    list
        Vector rotado.
    """
    if eje == 'x':
        R = [[1, 0, 0],
            [0, math.cos(angulo), -math.sin(angulo)],
            [0, math.sin(angulo), math.cos(angulo)]
            ]
    elif eje == 'y':
        R = [[math.cos(angulo), 0, math.sin(angulo)],
            [0, 1, 0],
            [-math.sin(angulo), 0, math.cos(angulo)]
            ]
    elif eje == 'z':
        R = [[math.cos(angulo), -math.sin(angulo), 0],
            [math.sin(angulo), math.cos(angulo), 0],
            [0, 0, 1]
            ]
    else:
        return 'El eje de rotación no es válido.'
    v_rot = vector(3)
    for i in range(3):
        v_rot[i] = ProductoPuntoBloques(R[i], v, 1)
    return v_rot

if __name__ == '__main__':
    # Ejemplo de uso.
    v = vector(3, randomizar=True)
    print('v=', v)
    print('v rotado al rededor de x 90 grados:', RotacionVector(v, np.pi/2, 'x'))
    print('¿v rotado con RotacionVector es igual a v rotado con numpy?', np.allclose(RotacionVector(v, np.pi/2, 'x'), np.dot(np.array([[1, 0, 0], [0, np.cos(np.pi/2), -np.sin(np.pi/2)], [0, np.sin(np.pi/2), np.cos(np.pi/2)]]), v)))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: RotacionVector(v, np.pi/2, 'x'), number=1000)
    print("Tiempo de ejecución de RotacionVector:", tiempo, "para 1000 iteraciones.")