# --------------------          1) Integral de un num
"""
from sympy import symbols, integrate

x = symbols('x')

y = x**2

r = integrate(y,(x, 0, 10)) # integrate(y,x)

print(r)
"""

# --------------------          2) Expandir el proceso de la multiplicación - binomios
"""
from sympy import symbols, expand

x = symbols('x')
y = (x+5)*(x+5)

r = expand(y)
print(r)
"""

# --------------------          3) Comando simplify - no fraccion / identidades trigonometricas
"""
from sympy import symbols, simplify, sin, cos

x = symbols('x')
y = sin(x)**2 + cos(x)**2

r = simplify(y)
print(r)
"""

# --------------------          4) Comando factor - para compactar/simplificar
"""
from sympy import symbols, factor

x = symbols('x')
y = ((x+1)*(x+2) - (x+2)**2)**3

r = factor(y)
print(r)
"""

# --------------------          5) Comando solve - no esta diseñado para problemas complejos
#                                  N - para obtener cualquier numero (complejos, etc.)

"""
from sympy import symbols, solve, N

x = symbols('x')
y = x**5 + 2*x + 1              # y = (x**2 + 5*x +3)

r = solve(y,x)      # (y,x) -> para despejar
number = [N(sol) for sol in r]      # forzar solucionese
print(number)
"""

# --------------------          5) actividad - graficar otra funcion
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/4, np.pi/4, 300)
y = x * np.sin(1/x)

plt.plot(x, y, '-', color='y')
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi/20, 100)

f1 = np.sin(x)
f2 = np.cos(x)

plt.plot(x, f1, '-', color='r')
plt.plot(x, f2, '--', color='b')
plt.show()