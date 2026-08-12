"""
from sympy import symbols, Matrix
import numpy as np

# 1. Definir variables y un nuevo sistema de ecuaciones
x, y, z = symbols('x y z')

f1 = x**2 + y**2 + z**2 - 1
f2 = 2*x**2 + y**2 - 4*z
f3 = 3*x**2 - 4*y + z**2

# f1 = x**2 + y - 37
# f2 = x - y**2 - 5
# f3 = x + y + z - 3

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

"""
from sympy import symbols, Matrix, log, cos, exp, lambdify
import numpy as np

x, y = symbols('x y')

# 1. Definimos las funciones simbólicamente
f1 = x - exp(y)
f2 = log(1 + x) - cos(y)

# 2. Usamos diff() de SymPy para calcular la Jacobiana (exactamente como lo tenías)
J = Matrix([ [f1.diff(x), f1.diff(y)],
             [f2.diff(x), f2.diff(y)] ])

F_matriz = Matrix([f1, f2])

# 3. LA MAGIA: Convertimos la matemática simbólica a funciones numéricas de NumPy
# lambdify crea una función que recibe (x, y) y devuelve el resultado numérico
F_num = lambdify((x, y), F_matriz, 'numpy')
J_num = lambdify((x, y), J, 'numpy')

X0 = np.array([1.0, 0.0])

# Variables para el ciclo
iteracion = 1
max_iteraciones = 5
tolerancia = 0.01
error = 100.0

print(f"{'Iteración':<10} | {'x':<9} | {'y':<9} | {'Error %':<10}")
print("-" * 50)

while iteracion <= max_iteraciones and error > tolerancia:
    # 4. Evaluamos llamando a las funciones generadas por lambdify (¡sin subs!)
    # .flatten() convierte la matriz columna de 2x1 a un vector plano de 1D
    F_eval = F_num(X0[0], X0[1]).flatten() 
    J_eval = J_num(X0[0], X0[1])
    
    # Inversa y siguiente paso (NumPy puro)
    inv_J = np.linalg.inv(J_eval)
    X1 = X0 - inv_J @ F_eval
    
    # Calcular el error
    distancia_cambio = np.linalg.norm(X1 - X0)
    magnitud_actual = np.linalg.norm(X1)
    error = (distancia_cambio / magnitud_actual) * 100
    
    # Imprimir la fila de la tabla
    print(f"{iteracion:<10} | {X1[0]:<9.4f} | {X1[1]:<9.4f} | {error:>7.2f} %")
    
    # Actualizar X0 para el siguiente ciclo
    X0 = X1
    iteracion += 1