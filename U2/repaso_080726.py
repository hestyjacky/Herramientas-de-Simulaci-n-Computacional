from sympy import symbols, lambdify, sqrt
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de integración
a = 0
b = 3
n = 6
x = symbols('x')
h = (b - a) / n

f_simbolica = sqrt(4 + x**3)
f = lambdify(x, f_simbolica, 'numpy')

# ==========================================
# 1. SOLUCIÓN POR LA REGLA DEL RECTÁNGULO (Izquierda)
# ==========================================
suma_rect = 0
for i in range(0, n):
    suma_rect += f(a + i * h)

total_rectangulo = h * suma_rect
print(f'rectangulo: {total_rectangulo}')

# ==========================================
# 2. SOLUCIÓN POR LA REGLA DEL TRAPECIO
# ==========================================
print('-' * 20)
suma_trap = f(a) + f(b)

for i in range(1, n):
    suma_trap += 2 * f(a + i * h)

total_trapecio = (h / 2) * suma_trap
print(f'trapecio: {total_trapecio}')

# ==========================================
# 3. SOLUCIÓN POR LA REGLA DE SIMPSON 1/3
# ==========================================
print('-' * 20)
suma_simp13 = f(a) + f(b)

for i in range(1, n):
    punto_x = a + i * h
    if i % 2 == 0:  # PAR
        suma_simp13 += 2 * f(punto_x)
    else:           # IMPAR
        suma_simp13 += 4 * f(punto_x)
    
total_simpson = (h / 3) * suma_simp13
print(f'simpson 1/3: {total_simpson}')

# ==========================================
# 4. SOLUCIÓN POR LA REGLA DE SIMPSON 3/8
# ==========================================
print('-' * 20)
suma_simp38 = f(a) + f(b)

for i in range(1, n):
    punto_x = a + i * h
    if i % 3 == 0:  # Múltiplo de 3
        suma_simp38 += 2 * f(punto_x)
    else:           # Resto de puntos
        suma_simp38 += 3 * f(punto_x)

total_simpson8 = (3 * h / 8) * suma_simp38
print(f'simpson 3/8: {total_simpson8}')