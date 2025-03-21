# Transpuesta conjugada de una matriz compleja
# Lara Estrada Uriel Alejandro
from utilidades import matriz
import numpy as np
import timeit

def TranspuestaConjugada(A):
    """
    Calcula la transpuesta conjugada de una matriz A.
    
    Parámetros:
    A : list
        Matriz de tamaño m x n.
    
    Retorna:
    list
        Matriz de tamaño n x m.
    """
    m, n = len(A), len(A[0])
    # Crea una matriz de ceros de tamaño n x m.
    A_ct = matriz(n, m)
    for i in range(m):
        for j in range(n):
            A_ct[j][i] = A[i][j].conjugate()
    return A_ct

if __name__ == '__main__':
    A = [
        [1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j, 9 + 10j, 11 + 12j, 13 + 14j, 15 + 16j, 17 + 18j, 19 + 20j, 21 + 22j, 23 + 24j, 25 + 26j, 27 + 28j, 29 + 30j],
        [31 + 32j, 33 + 34j, 35 + 36j, 37 + 38j, 39 + 40j, 41 + 42j, 43 + 44j, 45 + 46j, 47 + 48j, 49 + 50j, 51 + 52j, 53 + 54j, 55 + 56j, 57 + 58j, 59 + 60j],
        [61 + 62j, 63 + 64j, 65 + 66j, 67 + 68j, 69 + 70j, 71 + 72j, 73 + 74j, 75 + 76j, 77 + 78j, 79 + 80j, 81 + 82j, 83 + 84j, 85 + 86j, 87 + 88j, 89 + 90j],
        [91 + 92j, 93 + 94j, 95 + 96j, 97 + 98j, 99 + 100j, 101 + 102j, 103 + 104j, 105 + 106j, 107 + 108j, 109 + 110j, 111 + 112j, 113 + 114j, 115 + 116j, 117 + 118j, 119 + 120j],
        [121 + 122j, 123 + 124j, 125 + 126j, 127 + 128j, 129 + 130j, 131 + 132j, 133 + 134j, 135 + 136j, 137 + 138j, 139 + 140j, 141 + 142j, 143 + 144j, 145 + 146j, 147 + 148j, 149 + 150j],
        [151 + 152j, 153 + 154j, 155 + 156j, 157 + 158j, 159 + 160j, 161 + 162j, 163 + 164j, 165 + 166j, 167 + 168j, 169 + 170j, 171 + 172j, 173 + 174j, 175 + 176j, 177 + 178j, 179 + 180j],
        [181 + 182j, 183 + 184j, 185 + 186j, 187 + 188j, 189 + 190j, 191 + 192j, 193 + 194j, 195 + 196j, 197 + 198j, 199 + 200j, 201 + 202j, 203 + 204j, 205 + 206j, 207 + 208j, 209 + 210j],
        [211 + 212j, 213 + 214j, 215 + 216j, 217 + 218j, 219 + 220j, 221 + 222j, 223 + 224j, 225 + 226j, 227 + 228j, 229 + 230j, 231 + 232j, 233 + 234j, 235 + 236j, 237 + 238j, 239 + 240j],
        [241 + 242j, 243 + 244j, 245 + 246j, 247 + 248j, 249 + 250j, 251 + 252j, 253 + 254j, 255 + 256j, 257 + 258j, 259 + 260j, 261 + 262j, 263 + 264j, 265 + 266j, 267 + 268j, 269 + 270j],
        [271 + 272j, 273 + 274j, 275 + 276j, 277 + 278j, 279 + 280j, 281 + 282j, 283 + 284j, 285 + 286j, 287 + 288j, 289 + 290j, 291 + 292j, 293 + 294j, 295 + 296j, 297 + 298j, 299 + 300j]
    ]

    print('A=', A)
    print('TranspuestaConjugada(A)=', TranspuestaConjugada(A))
    print('Numpy=', np.conj(np.transpose(A)))
    print('¿El resultado de TranspuestaConjugada es igual al de numpy?', np.allclose(TranspuestaConjugada(A), np.conj(np.transpose(A))))

    # Tiempo de ejecución.
    tiempo = timeit.timeit(lambda: TranspuestaConjugada(A), number=1000)
    print("Tiempo de ejecución de TranspuestaConjugada:", tiempo, "para 1000 iteraciones.")