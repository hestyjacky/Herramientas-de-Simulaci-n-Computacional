# Repasar con el metodo del rectangulo (izq, der, medio), trapecio, simpson 1/3, simpson 3/8, y newton-raphson

""" 
I = ∫_a^b f(x) dx
a = 0
b = 10
n = 500
f(x) = x**3 + 3.2*x**2 - 3.4*x + 20.2
"""
# Valor real de la integral
from sympy import symbols, integrate

x = symbols('x')
a = 0
b = 10
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
I_real = integrate(f_simb, (x, a, b))

print(f'Real: {I_real}')

# Regla del rectangulo (izq)
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_izq = 0

for i in range(n):
    suma_izq += f(a + i*h)

total_izq = h * suma_izq 
print(f'Izq: {total_izq}')

# ------ Graficar izq
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label = 'f(x)', color='black')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + i*h), f(a + i*h)], color='gray', alpha=0.5)
plt.grid()
plt.show()

# como calculo el error de cada metodo?
error_izq = abs(I_real - total_izq)
print(f'Error Izq: {error_izq}')

# Regla del rectangulo (der)
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_der = 0

for i in range(n):
    suma_der += f(a + (i+1) * h)

total_der = h * suma_der
print(f'Der: {total_der}')
error_der = abs(I_real - total_der)
print(f'Error Der: {error_der}')

# ------ Graficar der
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label = 'f(x)', color='blue')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + (i+1)*h), f(a + (i+1)*h)], color='lightblue', alpha=0.5)
plt.grid()
plt.show()

# Regla del rectangulo (medio)
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_medio = 0
for i in range(n):
    suma_medio += f(a + (i+0.5) * h)

total_medio = h * suma_medio
print(f'Med: {total_medio}')
error_medio = abs(I_real - total_medio)
print(f'Error Med: {error_medio}')

# --- Graficar medio
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label='f(x)', color='orange')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + (i+0.5)*h), f(a + (i+0.5)*h)], color='orange', alpha=0.5)
plt.grid()
plt.show()

# Regla del trapecio
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_trapecio = 0
suma_trapecio += f(a) + f(b) # EXTREMOS

for i in range(1,n): #MEDIOS
    suma_trapecio += 2 * f(a + i*h)

total_trapecio = (h/2) * suma_trapecio
print(f'Trap: {total_trapecio}')
error_trapecio = abs(I_real - total_trapecio)
print(f'Error Trap: {error_trapecio}')

# --- Graficar trapecio
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a, b, 100)
plt.plot(x, f(x), label='f(x)', color='hotpink')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + i*h), f(a + (i+1)*h)], color='hotpink', alpha=0.5)
plt.grid()
plt.show()

# regla simpson 1/3
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_simpson13 = 0
suma_simpson13 += f(a) + f(b) # EXTREMOS

for i in range(1, n):
    if i % 2 == 0: # si es par
        suma_simpson13 += 2*f(a + i*h)
    else:
        suma_simpson13 += 4*f(a + i*h)

total_simpson13 = (h/3) * suma_simpson13
print(f'1/3: {total_simpson13}')
error_simpson13 = abs(I_real - total_simpson13)
print(f'Error 1/3: {error_simpson13}')

# --- Graficar simpson 1/3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a,b,100)
plt.plot(x, f(x), color='green')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + i*h), f(a + (i+1)*h)], color='darkgreen', alpha=0.5)
plt.grid()
plt.show()

# Regla de simpson 3/8
from sympy import symbols, lambdify

x = symbols('x')
a = 0
b = 10
n = 5

h = (b - a) / n
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
f = lambdify(x, f_simb, 'numpy')

suma_simpson38 = 0
suma_simpson38 += f(a) + f(b) # EXTREMOS

for i in range(1, n):
    if i % 3 == 0: # si es multiplo de 3
        suma_simpson38 += 2*f(a + i*h)
    else:
        suma_simpson38 += 3*f(a + i*h)

total_simpson38 = (3*h/8) * suma_simpson38
print(f'3/8: {total_simpson38}')
error_simpson38 = abs(I_real - total_simpson38)
print(f'Error 3/8: {error_simpson38}')

# --- Graficar simpson 3/8
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(a,b,100)
plt.plot(x, f(x), color='purple')
for i in range(n):
    plt.fill_between([a + i*h, a + (i+1)*h], [f(a + i*h), f(a + (i+1)*h)], color='darkmagenta', alpha=0.5)
plt.grid()
plt.show()

# Newton-raphson
from sympy import symbols, diff, lambdify

x = symbols('x')
f_simb = x**3 + 3.2*x**2 - 3.4*x + 20.2
df_simb = diff(f_simb, x)

f = lambdify(x, f_simb, 'numpy')
df = lambdify(x, df_simb, 'numpy')

xo = 0
tolerancia = 0.001
error = 100.0
# print('\nIteración\tError')

while error >= tolerancia:
    x_new = xo - (f(xo) / df(xo))
    x_new = float(x_new)
    
    error = abs((x_new - xo) / x_new) * 100
    # print(f"{x_new:.6f}\t{error:.6f}%")
    xo = x_new

# graficar la funcion y la raiz
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, f(x), color='blue', label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(x_new, color='red', linestyle='--', label=f'Raíz: {x_new:.6f}')
plt.grid()
plt.legend()
plt.show()