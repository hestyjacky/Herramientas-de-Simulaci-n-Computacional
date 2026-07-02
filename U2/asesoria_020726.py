# -------------- EJERCICIO 1 ---------------- método del trapecio
"""
from sympy import symbols, lambdify, integrate
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')

a = 0
b = 10
n = 100  # Número de subintervalos (trapecios)

h = (b - a) / n

# Cambiado a 20.2 para coincidir con tu enunciado
f = x**3 + 3.2*x**2 - 3.4*x + 20.2

# 1. Cálculo exacto con SymPy
integral_exacta = integrate(f, (x, a, b))
print(f'Integral exacta (SymPy): {float(integral_exacta):.4f}')

# Convertir a función numérica
calcular_f = lambdify(x, f, 'numpy')

# 2. Método del Trapecio
suma = calcular_f(a) + calcular_f(b)  # Extremos f(a) y f(b)

# El bucle debe iterar sobre los N subintervalos intermedios (de 1 a n-1)
for i in range(1, n):
    punto_x = a + i * h        # Calculamos el valor real de x para este paso
    suma += 2 * calcular_f(punto_x)

total_trapecio = (h / 2) * suma
print(f'Resultado Trapecio:      {total_trapecio:.4f}')

# --- Gráfica (opcional por si querías terminarla) ---
rango_grafica = np.linspace(a, b, 200)
plt.plot(rango_grafica, calcular_f(rango_grafica), label='f(x)', color='blue')
plt.fill_between(rango_grafica, calcular_f(rango_grafica), alpha=0.2, color='gray')
plt.title('Método del Trapecio')
plt.legend()
plt.show()
"""

# -------------- EJERCICIO 2 ---------------- metodo de simpson
from sympy import symbols, lambdify, log
x = symbols('x')
a = 4
b = 5.2
n = 6  # Número de subintervalos (trapecios)

h = (b - a) / n

# funcion es log de x con sympy
f = log(x)
calcular_f = lambdify(x, f, 'numpy')

suma = calcular_f(a) + calcular_f(b)  # Extremos f(a) y f(b)

# ciclo para la regla de simpson 
#   pares x 4
#   impares x 2
for i in range(1,n):
    punto_x =  a + i*h
    if i % 2 == 0: # PAR
        suma += 2 * calcular_f(punto_x)
    else: # IMPAR
        suma += 4 * calcular_f(punto_x)

total_simpson = (h / 3) * suma
print(f'total Simpson: {total_simpson:.4f}')