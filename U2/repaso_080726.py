from sympy import symbols, lambdify, sqrt
import numpy as np

# Parámetros de integración
a = 0
b = 3
n = 6
x = symbols('x')
h = (b - a) / n

f_simbolica = sqrt(4 + x**3)
f = lambdify(x, f_simbolica, 'numpy')

# Puntos específicos que evalúan los métodos
puntos_x = np.linspace(a, b, n + 1)
valores_y = f(puntos_x)

# ==========================================
# 1. CÁLCULO: REGLA DEL RECTÁNGULO (Izquierda)
# ==========================================
suma_rect_izq = 0

for i in range(0, n):
    x_izq = a + i * h
    y_izq = f(x_izq)
    suma_rect_izq += y_izq

total_rect_izq = h * suma_rect_izq

# ==========================================
# 2. CÁLCULO: REGLA DEL RECTÁNGULO (Derecha)
# ==========================================
suma_rect_der = 0

for i in range(1, n + 1):
    x_der = a + i * h
    y_der = f(x_der)
    suma_rect_der += y_der

total_rect_der = h * suma_rect_der

# ==========================================
# 3. CÁLCULO: REGLA DEL TRAPECIO
# ==========================================
suma_trap = f(a) + f(b)
for i in range(1, n):
    suma_trap += 2 * f(a + i * h)
total_trapecio = (h / 2) * suma_trap

# ==========================================
# 4. CÁLCULO: REGLA DE SIMPSON 1/3
# ==========================================
suma_simp13 = f(a) + f(b)
for i in range(1, n):
    if i % 2 == 0:
        suma_simp13 += 2 * f(puntos_x[i])
    else:
        suma_simp13 += 4 * f(puntos_x[i])
total_simpson = (h / 3) * suma_simp13

# ==========================================
# 5. CÁLCULO: REGLA DE SIMPSON 3/8
# ==========================================
suma_simp38 = f(a) + f(b)
for i in range(1, n):
    if i % 3 == 0:
        suma_simp38 += 2 * f(puntos_x[i])
    else:
        suma_simp38 += 3 * f(puntos_x[i])
total_simpson8 = (3 * h / 8) * suma_simp38

# Imprimir resumen compacto en consola
print("-" * 30)
print(f'Rectángulo Izq: {total_rect_izq:.4f}')
print(f'Rectángulo Der: {total_rect_der:.4f}')
print(f'Trapecio:       {total_trapecio:.4f}')
print(f'Simpson 1/3:    {total_simpson:.4f}')
print(f'Simpson 3/8:    {total_simpson8:.4f}')
print("-" * 30)

# SASCAR EL VALOR REAL DE LA INTEGRAL PARA COMPARAR
from sympy import integrate
integral_real = integrate(f_simbolica, (x, a, b))
print(f'Valor real de la integral: {float(integral_real):.4f}')


""" 
PARA VISUALIZAR LOS MÉTODOS DE INTEGRACIÓN NUMÉRICA
Se implementan los métodos de integración numérica: regla del rectángulo, regla del trapecio y regla de Simpson (1/3 y 3/8) para la función f(x) = sqrt(4 + x**3) en el intervalo [0, 3] con n=6 subintervalos.
Se generan gráficos que muestran la función original y las aproximaciones de cada método, junto con el área calculada por cada uno. Además, se imprime un resumen compacto de los resultados en la consola.


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

# NUEVO TAMAÑO COMPACTO: (Ancho=9, Alto=8) para que no llene la pantalla
fig, axs = plt.subplots(3, 2, figsize=(9, 8))
fig.suptitle('Visualización de Métodos Numéricos de Integración', fontsize=12, fontweight='bold')

# Eje X continuo para pintar la curva f(x) real de fondo
x_curva = np.linspace(a, b, 200)
y_curva = f(x_curva)

# Puntos específicos que evalúan los métodos
puntos_x = np.linspace(a, b, n + 1)
valores_y = f(puntos_x)

# ==========================================
# 1. GRÁFICA: REGLA DEL RECTÁNGULO (Izquierda)
# ==========================================
suma_rect_izq = 0
ax = axs[0, 0]
ax.plot(x_curva, y_curva, color='blue', label='f(x)')

for i in range(0, n):
    x_izq = a + i * h
    y_izq = f(x_izq)
    suma_rect_izq += y_izq
    ax.bar(x_izq, y_izq, width=h, align='edge', alpha=0.3, color='orange', edgecolor='red')

total_rect_izq = h * suma_rect_izq
ax.set_title(f'Rectángulo Izq. (Área: {total_rect_izq:.4f})', fontsize=10)
ax.legend(fontsize=8)

# ==========================================
# 2. GRÁFICA: REGLA DEL RECTÁNGULO (Derecha)
# ==========================================
suma_rect_der = 0
ax = axs[0, 1]
ax.plot(x_curva, y_curva, color='blue', label='f(x)')

for i in range(1, n + 1):
    x_der = a + i * h
    y_der = f(x_der)
    suma_rect_der += y_der
    ax.bar(x_der, y_der, width=-h, align='edge', alpha=0.3, color='olive', edgecolor='darkgreen')

total_rect_der = h * suma_rect_der
ax.set_title(f'Rectángulo Der. (Área: {total_rect_der:.4f})', fontsize=10)
ax.legend(fontsize=8)

# ==========================================
# 3. GRÁFICA: REGLA DEL TRAPECIO
# ==========================================
suma_trap = f(a) + f(b)
for i in range(1, n):
    suma_trap += 2 * f(a + i * h)
total_trapecio = (h / 2) * suma_trap

ax = axs[1, 0]
ax.plot(x_curva, y_curva, color='blue', label='f(x)')
ax.fill_between(puntos_x, valores_y, alpha=0.3, color='green', edgecolor='darkgreen')
ax.scatter(puntos_x, valores_y, color='red', s=15, zorder=5)
ax.set_title(f'Trapecio (Área: {total_trapecio:.4f})', fontsize=10)
ax.legend(fontsize=8)

# ==========================================
# 4. GRÁFICA: REGLA DE SIMPSON 1/3
# ==========================================
suma_simp13 = f(a) + f(b)
for i in range(1, n):
    if i % 2 == 0:
        suma_simp13 += 2 * f(puntos_x[i])
    else:
        suma_simp13 += 4 * f(puntos_x[i])
total_simpson = (h / 3) * suma_simp13

ax = axs[1, 1]
ax.plot(x_curva, y_curva, color='blue', label='f(x)')

for i in range(0, n, 2):
    xs = np.linspace(puntos_x[i], puntos_x[i+2], 50)
    coefs = np.polyfit(puntos_x[i:i+3], valores_y[i:i+3], 2)
    ys = np.polyval(coefs, xs)
    ax.fill_between(xs, ys, alpha=0.3, color='purple')
    ax.plot(xs, ys, color='purple', linestyle='--', linewidth=1)

ax.scatter(puntos_x, valores_y, color='red', s=15, zorder=5)
ax.set_title(f'Simpson 1/3 (Área: {total_simpson:.4f})', fontsize=10)
ax.legend(fontsize=8)

# ==========================================
# 5. GRÁFICA: REGLA DE SIMPSON 3/8
# ==========================================
suma_simp38 = f(a) + f(b)
for i in range(1, n):
    if i % 3 == 0:
        suma_simp38 += 2 * f(puntos_x[i])
    else:
        suma_simp38 += 3 * f(puntos_x[i])
total_simpson8 = (3 * h / 8) * suma_simp38

ax = axs[2, 0]
ax.plot(x_curva, y_curva, color='blue', label='f(x)')

for i in range(0, n, 3):
    xs = np.linspace(puntos_x[i], puntos_x[i+3], 50)
    coefs = np.polyfit(puntos_x[i:i+4], valores_y[i:i+4], 3)
    ys = np.polyval(coefs, xs)
    ax.fill_between(xs, ys, alpha=0.3, color='cyan')
    ax.plot(xs, ys, color='darkcyan', linestyle='--', linewidth=1)

ax.scatter(puntos_x, valores_y, color='red', s=15, zorder=5)
ax.set_title(f'Simpson 3/8 (Área: {total_simpson8:.4f})', fontsize=10)
ax.legend(fontsize=8)

# ==========================================
# 6. ESPACIO DISPONIBLE
# ==========================================
ax = axs[2, 1]
ax.axis('off')
ax.text(0.1, 0.5, "💡 Espacio libre para\notro método (Punto Medio).", 
        fontsize=10, style='italic', color='gray')

# Imprimir resumen compacto en consola
print("-" * 30)
print(f'Rectángulo Izq: {total_rect_izq:.4f}')
print(f'Rectángulo Der: {total_rect_der:.4f}')
print(f'Trapecio:       {total_trapecio:.4f}')
print(f'Simpson 1/3:    {total_simpson:.4f}')
print(f'Simpson 3/8:    {total_simpson8:.4f}')
print("-" * 30)

# Ajustar diseño de forma compacta
plt.tight_layout()
plt.show()
"""

# METODO NEWTON-RAPHSON
"""
5*x + log(x) - 10000

x_new = x_old - f(x_old)/f'(x_old)

# Parámetros iniciales
xo = 1
tolerancia = 0.01  # 0.01%
error = 100.0      # Error inicial
iteracion = 1
"""
print('\nNEWTON-RAPHSON ' + '-' * 20)
from sympy import symbols, diff, log, lambdify, exp

x = symbols('x')
f_simbolica = 5*x + log(x) - 10000
##f_simbolica = exp(2*x) - x - 6
df_simbolica = diff(f_simbolica, x)

f = lambdify(x, f_simbolica, 'numpy')
df = lambdify(x, df_simbolica, 'numpy')

xo = 1
tolerancia = 0.001
error = 100.0

while error >= tolerancia:
    x_new = xo - (f(xo) / df(xo))
    x_new = float(x_new)
    
    error = abs((x_new - xo) / x_new) * 100
    print(x_new)
    xo = x_new