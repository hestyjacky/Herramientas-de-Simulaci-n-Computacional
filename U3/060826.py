"""
newton-rapson (initial guess) con varias variables

f1 (x,y,z) =    x**2 + y**2 + z**2 - 1  = 0
f2 (x,y,z) =    2x**2 + y**2 + 4z     = 0
f3 (x,y,z) =    3x**2 - 4y + z**2     = 0

x0, y0, z0 = 0.5, 0.5, 0.5
"""

from sympy import symbols, Matrix
import numpy as np

x, y, z = symbols('x y z')

# -- Escribir las ecuaciones
f1 = x**2 + y**2 + z**2 - 1
f2 = 2*x**2 + y**2 - 4*z
f3 = 3*x**2 - 4*y + z**2

# -- Usar Matrix de sympy en lugar de np.array para la parte simbólica
J = Matrix([[f1.diff(x), f1.diff(y), f1.diff(z)],
            [f2.diff(x), f2.diff(y), f2.diff(z)],
            [f3.diff(x), f3.diff(y), f3.diff(z)]])

print("Matriz Jacobiana:")
print(J)

# -- Evaluar la matriz Jacobiana en un punto inicial (x0, y0, z0)
x0, y0, z0 = 0.5, 0.5, 0.5  # Punto inicial

# -- J sigue siendo simbólico
J_eval = J.subs({x: x0, y: y0, z: z0})
# redondear a 4 cifras
J_eval = J_eval.evalf(4)

# print("\nMatriz Jacobiana evaluada en el punto inicial (SymPy):")
# print(J_eval)

# -- Convertir el resultado a decimales (float)
# para poder calcular la inversa
# redondear decimales a 4 cifras
J_eval_numpy = np.array(J_eval).astype(np.float64)
J_eval_numpy = np.round(J_eval_numpy, 4)

print("\nMatriz Jacobiana lista para operaciones numéricas (NumPy):")
print(J_eval_numpy)

# Sacar Matriz Inversa

#                           1 -- obtener determinante de la matriz
det_J = np.linalg.det(J_eval_numpy)
det_J = round(det_J, 4) # redondear a 4 cifras
print("\nDeterminante de la matriz Jacobiana:", det_J)

#                            2 -- obtener Adjunta (matriz de cofactores)
cofactors = np.linalg.inv(J_eval_numpy).T * det_J
cofactors = np.round(cofactors, 4) # redondear a 4 cifras
print("\nMatriz Adjunta:")
print(cofactors)

#                            3 -- obtener Transpuesta de la matriz de cofactores
adj = cofactors.T
adj = np.round(adj, 4) # redondear a 4 cifras
print("\nMatriz Transpuesta:")
print(adj)

#                            4 -- obtener Inversa con los datos que sacamos
inv_J = adj / det_J # t / -40
inv_J = np.round(inv_J, 4) # redondear a 4 cifras
print("\nMatriz Inversa:")
print(inv_J)


# -- Calcular el siguiente punto usando la fórmula de Newton-Raphson
F = np.array([f1.subs({x: x0, y: y0, z: z0}),
              f2.subs({x: x0, y: y0, z: z0}),
              f3.subs({x: x0, y: y0, z: z0})], dtype=np.float64)
F = np.round(F, 4)
print("\nX0 -- initial guess")
print(F)

# Calcular el siguiente punto
X0 = np.array([x0, y0, z0], dtype=np.float64)
X1 = X0 - inv_J @ F
X1 = np.round(X1, 4)
print("\nX1 -- next guess")
print(X1)


print("\n" + "-" * 20)
""" ESTO FUE MANUAL, AHORA HAY QUE HACERLO AUTOMATICO CON UN CICLO WHILE"""

# -- Calcular el siguiente punto usando la fórmula de Newton-Raphson
tolerance = 1e-4
max_iterations = 100
iteration = 0

while iteration < max_iterations:
    # Evaluar las funciones en el punto actual
    F = np.array([f1.subs({x: X0[0], y: X0[1], z: X0[2]}),
                  f2.subs({x: X0[0], y: X0[1], z: X0[2]}),
                  f3.subs({x: X0[0], y: X0[1], z: X0[2]})], dtype=np.float64)
    F = np.round(F, 4)

    # Evaluar la matriz Jacobiana en el punto actual
    J_eval = J.subs({x: X0[0], y: X0[1], z: X0[2]})
    J_eval_numpy = np.array(J_eval).astype(np.float64)
    J_eval_numpy = np.round(J_eval_numpy, 4)

    # Calcular la inversa de la matriz Jacobiana
    det_J = np.linalg.det(J_eval_numpy)
    if abs(det_J) < 1e-10:
        print("La matriz Jacobiana es singular. No se puede continuar.")
        break

    inv_J = np.linalg.inv(J_eval_numpy)
    inv_J = np.round(inv_J, 4)

    # Calcular el siguiente punto
    print(f"Iteration {iteration}: X0 = {X0}")
    X1 = X0 - inv_J @ F
    X1 = np.round(X1, 4)

    # Verificar la convergencia
    if np.linalg.norm(X1 - X0) < tolerance:
        print(f"Convergencia alcanzada después de {iteration + 1} iteraciones.")
        break

    # Actualizar el punto actual para la siguiente iteración
    X0 = X1
    iteration += 1
else:
    print("No se alcanzó la convergencia después del número máximo de iteraciones.")