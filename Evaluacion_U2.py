from sympy import symbols, lambdify, E, cos
import numpy as np

x = symbols('x')
a = 0
b = 2*np.pi
n = 500

h = (b-a)/ n

f_simb = E**(3*x) * cos(4*x)

f = lambdify(x, f_simb, 'numpy')

# sacar por metodo del rectangulo en punto medio
suma = 0
for i in range(n):
    suma += f(a + (i + 0.5) * h) ## UNICO ERROR YA MODIFICADO
total = suma * h
print(f"Integral approximation: {total}")







# VERSION DEL EXAMEN - SIN CORREGIR

from sympy import symbols, lambdify, E, cos
import numpy as np

x = symbols('x')
a = 0
b = 2*np.pi
n = 500

h = (b-a)/ n

f_simb = E**(3*x) * cos(4*x)

f = lambdify(x, f_simb, 'numpy')

suma = 0
for i in range(1,n+1):
    suma += f(a + i * h * 0.5)
total =  h *suma
print(f"Area total: {total}")