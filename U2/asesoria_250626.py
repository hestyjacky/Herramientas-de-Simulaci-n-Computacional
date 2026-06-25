"""
Newton Raphson Method or Newton's Method is an algorithm to approximate the roots of zeros of the real-valued functions, using 
guess for the first iteration (x_guess) 
and then approximating the next iteration(x_new) which is close to roots, 
using the following formula.

x_new = x_guess ( f(x_guess) / f'(x_guess) )

"""

# ------------------------------------------- EJERCICIO 1

"""
from sympy import symbols, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
f = x**10 - 1
df = diff(f, x)
xo = 0.5

i = 1

# Método de Newton-Raphson
while True:
    xo_new = xo - (f.subs(x, xo) / df.subs(x, xo))
    xo_new = float(xo_new)
    # error = xo - xo_new # cambiar a porcentaje

    error = abs((xo_new - xo) / xo_new) * 100

    print(f"{i}\t|\t{xo_new:.2f}\t|\t{error:.10f} %")

    xo = xo_new
    i += 1

    if error == 0:
        break


# Graficar la función
f_lambdified = lambdify(x, f, 'numpy')
x_vals = np.linspace(-2, 2, 100)
y_vals = f_lambdified(x_vals)
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='red', linestyle='--')
plt.axvline(0, color='red', linestyle='--')
plt.title('Gráfica de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show() 
"""

# ------------------------------------------- REPASO JAKI 1
"""
Given, x0 = 3 and f(x) = x**3 + 3*x + 1
"""

from sympy import symbols, diff, Subs
x = symbols('x')
f = x**3 + 3*x + 1
df = diff(f, x)
xo = 3

i = 1

while True:
    xo_new = xo - (f.subs(x, xo) / df.subs(x, xo))
    xo_new = float(xo_new)

    error = abs((xo_new - xo) / xo_new) * 100

    print(f"{i}\t|\t{xo_new:.2f}\t|\t{error:.10f} %")

    xo = xo_new
    i += 1

    if error < 0.02:
        break


