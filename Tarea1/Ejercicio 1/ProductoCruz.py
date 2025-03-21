# Producrto cruz de dos vectores.
# Lara Estrada Uriel Alejandro
from utilidades import vector
import numpy as np
import timeit

def ProductoCruz(u, v):
    """
    Calcula el producto cruz de dos vectores u y v.
    
    Parámetros:
    u : list
        Vector de dimensión 3.
    v : list
        Vector de dimensión 3.
    
    Retorna:
    list
        Vector de dimensión 3.
    """
    if [len(u), len(v)] != [3, 3]:
        return 'Los vectores no son de dimensión 3.'
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]

if __name__ == '__main__':
    # Ejemplo de uso.
    u = vector(3, randomizar=True)
    v = vector(3, randomizar=True)
    u_vec = np.array(u)
    v_vec = np.array(v)
    print('u=', u)
    print('v=', v)
    print('Resultado con ProductoCruz:', ProductoCruz(u, v))
    print('Resultado con Numpy:', np.cross(u_vec, v_vec))
    
    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: ProductoCruz(u, v), number=1000)
    print("Tiempo de ejecución de ProductoCruz:", tiempo, "para 1000 iteraciones.")