# ---------------------------------------  EJERCICIO 1
"""
int(0, 3) sqrt(4+x**3) dx
n = 6
solucion por la regla del trapecio

formulas:
h = (b - a)/n
trapecio = (h/2) * [f(a) + 2*[ f(1) + ... + f(n-1) ] + f(b)]
                            sumatoria de los medios
"""

"""
from sympy import symbols, lambdify, sqrt, Subs
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 3
n = 6
x = symbols('x')
h = (b-a)/n

f = sqrt(4 + x**3)
calcular_f = lambdify(x, f, 'numpy')

# sumatoria de los medios
suma = 0
suma += calcular_f(a) + calcular_f(b)

for i in range(1, n):
    suma += 2 * calcular_f(a + i*h)

area_total = (h/2) * suma
print('Area total: ', area_total)

# graficar
num_grafica = np.linspace(a, b, 100)
plt.plot(num_grafica, calcular_f(num_grafica), label='f(x)', color='blue')
plt.fill_between(num_grafica, calcular_f(num_grafica), color = 'lightblue', alpha = 0.5)
plt.grid(True)
plt.legend()
plt.show()

"""

# ---------------------------------------  EJERCICIO 2
""" NEWTON - RAPHSON
E**2x = x + 6
xo = 1
rango = 5
"""

"""
from sympy import symbols, exp, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
f = exp(2*x) - x - 6
df = diff(f, x)
xo = 1

# aproximaciones
for i in range(5):
    x_new = xo - (f.subs(x, xo) / df.subs(x, xo))
    x_new = float(x_new)

    print(f'iteracion {i+1}: x = {x_new:.6f}, f(x) = {f.subs(x, x_new):.6f}')
    xo = x_new

# graficar
f_lambdified = lambdify(x, f, 'numpy')
x_vals = np.linspace(-2, 2, 100) 
y_vals = f_lambdified(x_vals)

plt.plot(x_vals, y_vals, label = 'f(x)', color = 'blue')
plt.axhline(0, color = 'black', linestyle = '--')
plt.axvline(0, color = 'black', linestyle = '--')
plt.grid(True)
plt.legend()
plt.show()
"""


from sympy import symbols, log, diff, lambdify

x = symbols('x')
f_expr = 5*x + log(x) - 10000
df_expr = diff(f_expr, x)

f = lambdify(x, f_expr)
df = lambdify(x, df_expr)

# Parámetros iniciales
xo = 1
tolerancia = 0.01  # 0.01%
error = 100.0      # Error inicial alto para entrar al bucle
iteracion = 1

print(f"{'Iteración':<10}{'x_new':<15}{'f(x)':<15}{'Error (%)':<15}")
print("-" * 55)

while error >= tolerancia:
    x_new = xo - (f(xo) / df(xo))
    error = abs((x_new - xo) / x_new) * 100
    
    print(f"{iteracion:<10}{x_new:<15.6f}{f(x_new):<15.6f}{error:<15.6f}%")
    
    xo = x_new
    iteracion += 1