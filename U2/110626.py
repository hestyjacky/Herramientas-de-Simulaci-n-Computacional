
# ---------------- EJERCICIO 1 ----------------
"""
from sympy import symbols, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt 

x = symbols('x')
f = x**3 - x - 1
df = diff(f, x)
xo = 1

# graficar la función
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


for i in range(5):
    xo_new = xo - (f.subs(x, i) / df.subs(x, i))
    xo_new = float(xo_new)
    print(xo_new)

"""
# ---------------- EJERCICIO 2 ----------------
"""
from sympy import symbols, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
f = (x-1)**3 + 0.512
df = diff(f, x)
xo = 5.0

print(" i\t|\tx\t|\tf(x)\t|\tdf(x)\t|\tx_new")
print("-" * 50)

# Método de Newton-Raphson
for i in range(18):
    xo_new = xo - (f.subs(x, xo) / df.subs(x, xo))
    xo_new = float(xo_new)
    print(f"{i+1}\t|\t{xo:.3f}\t|\t{f.subs(x, xo):.1f}\t|\t{df.subs(x, xo):.2f}\t|\t{xo_new:.3f}")
    xo = xo_new

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
# ---------------- EJERCICIO 3 ----------------

from sympy import symbols, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')
f = x**3 - (0.03)*x**2 + (2.4)*10**-6
df = diff(f, x)
xo = 0.01999

# Método de Newton-Raphson
for i in range(9):
    xo_new = xo - (f.subs(x, xo) / df.subs(x, xo))
    xo_new = float(xo_new)
    print(f"{i+1}\t|\t{xo_new:.3f}")
    xo = xo_new

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


# ---------------- EJERCICIO 4 ----------------

