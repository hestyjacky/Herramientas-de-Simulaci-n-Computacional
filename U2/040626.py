# -----------   producto punto
#   ----------- 1) EJEMPLO 1
"""
import numpy as np
a = np.array([4, -1, 3])
b = np.array([-2, 5, 2])
c = np.dot(a, b)
"""
#   -----------   2) EJEMPLO  1
"""
import numpy as np
a = np.array([-3, 6, 1])
b = np.array([2, -3, 4])

# Producto punto
c = np.dot(a, b)
print(c)

z = 0
for i in b:
    w = i ** 2
    z += w
    print(z)

proj = (c/z) * b
print('Proyección de a sobre b: ', proj)

z = np.sqrt(z)
print('Magnitud de b: ', z)


# Magnitud de w
magnitud_w = np.linalg.norm(w)
print('Magnitud de w: ', magnitud_w)

proj_r = (np.dot(r, w) / magnitud_w**2) * w
print('Proyección de r sobre w: ', proj_r)
"""

# PRODUCTO CRUZ
#  -----------   3) EJEMPLO 3: find the volume of the parallelepiped with sides
# v = a . (b x c)
import numpy as np

a = np.array([2,0,1])
b = np.array([-3,1,5])
c = np.array([0,-2,-1])

cross_product = np.cross(b, c)
volume = np.dot(a, cross_product)
print('El volumen del paralelepípedo es: ', volume)

# matriz de identidad: matriz que tienen unos en la diagonal y ceros en el resto de sus elementos
#  -----------   4) EJEMPLO 4: matriz de identidad
import numpy as np
identity_matrix = np.eye(3)
print('Matriz de identidad 3x3: \n', identity_matrix)
 
matriz_a = np.array([[1, 2, 3], 
                      [4, 5, 6], 
                      [7, 8, 9]])
resultado = np.dot(identity_matrix, matriz_a)
print('Resultado de multiplicar la matriz de identidad por matriz_a: \n', resultado)

#  -----------   5) Ejercicio:
"""
A mass m is suspended by three cables attached tat three points B, C, and D, as shown in figure #. 
Let T1, T2, and T3 be the tension in the cables  AB, AC, and AD respectively. 
If the mass m is stationary, the sum of the tension components in the x, y, and z directions must be zero.

m = 1
g = 9.81
T1/sqrt(35) + 3*T2/sqrt(34) + T3/sqrt(42) = 0
3*T1/sqrt(35) - 4*T3/sqrt(42) = 0
5*T1/sqrt(35) + 5*T2/sqrt(34) + 5*T3/sqrt(42) - m*g = 0
                                                -> paso el valor de m*g a la derecha de la ecuación

"""