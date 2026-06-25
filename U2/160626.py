# ---------------- EJERCICIO 1 ----------------

"""
import numpy as np
A = np.array([[-2,1],
              [1,1]])

B =  np.array([[3],[10]])

X = np.linalg.inv(A) @ B
print(X)
"""

# ---------------- EJERCICIO 2 ----------------
"""
import numpy as np
A = np.array([[5, 3, -1],
             [3, 2, 1],
             [4, -1, 3]])

B = np.array([[10],
             [4],
             [12]])

X = np.linalg.inv(A) @ B
print(X)
"""
# ---------------- EJERCICIO 3 ----------------
"""
import numpy as np
# a = np.eye(3)
# print(a)
# b = (a.shape)
# print(b)

A = np.array([[2,1,1],
             [1,3,1],
             [1,1,4]])

B = np.array([40,50,60])

X = np.linalg.solve(A,B)

print(X)
"""
# ---------------- EJERCICIO 4 ----------------
"""
import numpy as np

A = np.array([[3,2,1],
              [1,1,3]])

B = np.array([120,90])
X, _, _, _ = np.linalg.lstsq(A,B, rcond=None)
# Solucion, residuo, rango, singular
#                      lstsq -- minimos cuadrados
# imprimir el valor de la primer incognita
print(X)
"""

# ---------------- EJERCICIO 5 -----------------
import numpy as np

A = np.array([[3, 2, 5],
              [4, 5, -2],
              [1, 1, 1],
              [2, -4, -7]])

B = np.array([22, 8, 6, -28])
X, _, _, _ = np.linalg.lstsq(A,B, rcond=None)
print(X)