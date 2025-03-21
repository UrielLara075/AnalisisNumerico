# Producto punto por bloques.
# Lara Estrada Uriel Alejandro

import numpy as np
from utilidades import vector
import timeit

def ProductoPuntoBloques(u, v, tamaño_bloques):
    """
    Multiplica dos vectores u y v.
    
    Parámetros:
    u : list
        Vector de dimensión n.
    v : list
        Vector n.
    tamaño_bloques : int
        Tamaño de los bloques en los que se dividirán los vectores.
        
    Retorna:
    float
        Producto punto de los dos vectores.
    """
    if len(u) != len(v):
        return 'Los vectores no son del mismo tamaño.'
    # Obtiene la longitud de los vectores.
    n = len(u)
    producto_punto = 0
    for i in range(0, n, tamaño_bloques): # Recorre los bloques de u y v.
        for j in range(i, min(i + tamaño_bloques, n)): # Recorre el bloque actual.
            producto_punto += u[j] * v[j]
    return producto_punto

if __name__ == '__main__':
    # Ejemplo de uso.
    u = vector(50, randomizar=True)
    v = vector(50, randomizar=True)
    u_vec = np.array(u)
    v_vec = np.array(v)
    print('u=', u)
    print('v=', v)
    print('Por bloques, u*v=', ProductoPuntoBloques(u, v, 10))
    print('Con numpy, u*v=', np.dot(u_vec, v_vec))

    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: ProductoPuntoBloques(u, v, 50), number=1000)
    print("Tiempo de ejecución de ProductoPuntoBloques:", tiempo, "para 1000 iteraciones.")