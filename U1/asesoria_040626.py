# ---------------------------------- 1)
"""
y = x**3

graficar esa funcion derivada en un rango de -20 a 20

from sympy import symbols, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x')

y = x**3

y_derivada = diff(y, x)

print(y_derivada)

y_numerica = lambdify(x, y_derivada, 'numpy') # es como crear una funcion que espera un numerico

rango = np.linspace(-20, 20, 100)

plt.plot(rango, y_numerica(rango), color = "red")
plt.show()
"""

# ---------------------------------- 2)

"""
from sympy import symbols, sin, cos, diff, lambdify, pretty, Subs
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')

funcion = (sin(2*t) / 4) + ((cos(4*t))**2 / 2)

derivada = diff(funcion, t)

print(pretty(funcion))

derivada_num = lambdify(t, derivada, 'numpy')

rango = np.linspace(-20, 20, 100)

plt.plot(rango, derivada_num(rango), linestyle='-', color='blue')
plt.show()

# sustituir el valor de t = 5 en la función derivada y mostrar el resultado numérico
resultado = derivada.subs(t, 5) # sustituir la t por un valor numerico

resultado_en_t = lambdify(t, resultado, 'numpy')
print(f"El resultado de la derivada en t=5 es: {resultado_en_t(5)}")
"""

# ---------------------------------- 3)

"""
from sympy import cos
import numpy as np

t = np.linspace(0, 0.5, 10)
x = 0
theta = np.pi / 6
v = 10
print("\n\t" + "-" * 20)
print("\tt\t|\tx(t)")
print("\t" + "-" * 20)


for t_i in t:
    x_t = x + v * cos(theta) * t_i
    print(f"{t_i:.2f}\t|\t{x_t:.2f}")

print("\t" + "-" * 20 + "\n")
"""

# ---------------------------------- 4)
from sympy import symbols, Eq, solve, sqrt
x, y = symbols('x, y')
eq = Eq(y, 3 + x**2)

solucion = solve(eq, x)
print(solucion)



