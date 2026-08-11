"""
from sympy import symbols, Matrix
import numpy as np

# 1. Definir 4 variables
w, x, y, z = symbols('w x y z')

# 2. Definir un sistema de 4 ecuaciones
# (Este sistema está diseñado para que la respuesta exacta sea w=1, x=1, y=1, z=1)
f1 = w**2 + x - 2
f2 = x**2 + y - 2
f3 = y**2 + z - 2
f4 = z**2 + w - 2

# 3. Crear la Matriz Jacobiana de 4x4
# Nota cómo ahora cada fila tiene 4 derivadas, una para cada variable.
J = Matrix([[f1.diff(w), f1.diff(x), f1.diff(y), f1.diff(z)],
            [f2.diff(w), f2.diff(x), f2.diff(y), f2.diff(z)],
            [f3.diff(w), f3.diff(x), f3.diff(y), f3.diff(z)],
            [f4.diff(w), f4.diff(x), f4.diff(y), f4.diff(z)]])

# 4. Configurar las condiciones iniciales y del ciclo while
X0 = np.array([2.0, 2.0, 2.0, 2.0], dtype=np.float64) # Intento inicial
tolerancia = 0.01 # Queremos que el error sea menor al 0.01%
error_pct = 100.0 # Empezamos con un error alto para que el ciclo arranque
iteracion = 1
max_iteraciones = 20 # Un seguro de vida por si el método no converge

print(f"{'Ciclo':<7} | {'w':<8} | {'x':<8} | {'y':<8} | {'z':<8} | {'Error %':<10}")
print("-" * 65)

# 5. El ciclo while: "Mientras el error sea mayor a la tolerancia..."
while error_pct > tolerancia and iteracion <= max_iteraciones:
    
    # Evaluar las funciones con los valores actuales
    F = np.array([f1.subs({w: X0[0], x: X0[1], y: X0[2], z: X0[3]}),
                  f2.subs({w: X0[0], x: X0[1], y: X0[2], z: X0[3]}),
                  f3.subs({w: X0[0], x: X0[1], y: X0[2], z: X0[3]}),
                  f4.subs({w: X0[0], x: X0[1], y: X0[2], z: X0[3]})], dtype=np.float64)
    
    # Evaluar Jacobiana y sacar su inversa
    J_eval = np.array(J.subs({w: X0[0], x: X0[1], y: X0[2], z: X0[3]})).astype(np.float64)
    inv_J = np.linalg.inv(J_eval)
    
    # Fórmula de Newton-Raphson: Calcular el siguiente punto
    X1 = X0 - inv_J @ F
    
    # Calcular el error relativo en porcentaje
    distancia_cambio = np.linalg.norm(X1 - X0)
    magnitud_actual = np.linalg.norm(X1)
    error_pct = (distancia_cambio / magnitud_actual) * 100
    
    # Imprimir los resultados del ciclo actual
    print(f"Iter {iteracion:<2} | {X1[0]:<8.4f} | {X1[1]:<8.4f} | {X1[2]:<8.4f} | {X1[3]:<8.4f} | {error_pct:>7.4f} %")
    
    # Prepararnos para el siguiente ciclo
    X0 = X1
    iteracion += 1

print("\n¡Convergencia alcanzada!")
"""

from sympy import symbols, Matrix
import numpy as np

# 1. Definir variables y un nuevo sistema de ecuaciones
x, y, z = symbols('x y z')

f1 = x**2 + y**2 + z**2 - 1
f2 = 2*x**2 + y**2 - 4*z
f3 = 3*x**2 - 4*y + z**2

"""
f1 = x**2 + y - 37
f2 = x - y**2 - 5
f3 = x + y + z - 3
"""

# 2. Crear Matriz Jacobiana Simbólica
J = Matrix([[f1.diff(x), f1.diff(y), f1.diff(z)],
            [f2.diff(x), f2.diff(y), f2.diff(z)],
            [f3.diff(x), f3.diff(y), f3.diff(z)]])

# Punto inicial
X0 = np.array([.5, .5, .5], dtype=np.float64)
# X0 = np.array([1.0, 1.0, 1.0], dtype=np.float64)

print(f"{'Ciclo':<7} | {'x':<9} | {'y':<9} | {'z':<9} | {'Error %':<10}")
print("-" * 55)

# 3. Hacer exactamente 5 ciclos
for i in range(1, 6):
    # Evaluar funciones F(X0)
    F = np.array([f1.subs({x: X0[0], y: X0[1], z: X0[2]}),
                  f2.subs({x: X0[0], y: X0[1], z: X0[2]}),
                  f3.subs({x: X0[0], y: X0[1], z: X0[2]})], dtype=np.float64)
    
    # Evaluar Jacobiana y sacar su inversa usando numpy directamente para ser más rápidos
    J_eval = np.array(J.subs({x: X0[0], y: X0[1], z: X0[2]})).astype(np.float64)
    inv_J = np.linalg.inv(J_eval)
    
    # Calcular el siguiente punto X1
    X1 = X0 - inv_J @ F
    
    # Calcular el error en porcentaje: ||X1 - X0|| / ||X1|| * 100
    distancia_cambio = np.linalg.norm(X1 - X0)
    magnitud_actual = np.linalg.norm(X1)
    error_pct = (distancia_cambio / magnitud_actual) * 100
    
    # Imprimir la fila de la tabla
    print(f"Iter {i:<2} | {X1[0]:<9.4f} | {X1[1]:<9.4f} | {X1[2]:<9.4f} | {error_pct:>7.2f} %")
    
    # Actualizar X0 para el siguiente ciclo
    X0 = X1