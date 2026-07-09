"""
--------------------------------------- EJERCICIO 1

Instrucciones: utilizando los comandos de cálculo simbolico, determinar la distancia total recorrida por un mecanismo cuya velocidad esta dada por la ecuación 

    v(t) = cos(2t) + 3,        evaluada en el intervalo de 0 a pi segundos

Metodología y ecuaciones: la fisica establece que la distancia es la integral de la velocidad respecto al timepo, por lo tanto, el problema consiste en resolver la integral definidad de v(t)
"""
from sympy import symbols, cos, integrate, lambdify
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')
t_num = np.linspace(0,np.pi,100)

v = cos(2*t) + 3

distancia = integrate(v, (t, 0, np.pi))

"""
--------------------------------------- EJERCICIO 2 - regla del rectangulo

Instrucciones: Un actuador aplica una fuerza mecánica dada por F(x) = (2x**2) + 5 (en Newtons)
sobre un riel. Calcule el trabajo total realizado al desplazar un objeto desde x = 1 hasta x = 3 metros, usando la regla del rectángulo izquierdo con 4 subintervalos.

Metodología y ecuaciones: el trabajo mecánico es la integral de la fuerza respecto a la distancia.

Se usara la suma de Riemann izquierda para aproximar el área, utilice la formula h para calcular el ancho del paso.

    h = (b - a) / n
"""
from sympy import symbols, cos, integrate, lambdify
import numpy as np
import matplotlib.pyplot as plt

a = 1 # inicio
b = 3 # fin
n = 4 # segmentos

h = (b - a) / n # tamaño del segmento

x = symbols('x')
f = (2*x**2) + 5
calcular_f = lambdify(x, f, 'numpy')

for i in range(1,5):
    valores_f = calcular_f(a + i*h) 
    print(valores_f)

"""
--------------------------------------- EJERCICIO 3 - regla del trapecio

Instrucciones: se analizo la potencia electrica (watts) disipada por una resistencia en un circuito. como no hay un modelo matemático perfecto, solo se tienen registros del sensor cada 0.2s

los tiempos son: 
    t = [0, 0.2, ... , 1]
y las potencias son:
    P = [10, 8.1, 6.7, 5.4, 4.4, 3.6]

Estime la energía total disipada en Joules

Metodología y ecuaciones: la energía w es el área debajo de la curva de la potencia en el tiempo. Al tener vectores de datos experimentales de la misma dimensión, el  comando trapz y la regla del trapecio compuesta son la solución ideal.
"""
from sympy import symbols, cos, integrate, lambdify
import numpy as np
import matplotlib.pyplot as plt

h = 0.2

suma = 8.1 + 6.7 + 5.4 + 4.4 # el inicio y el fin no se pone en la suma, por ser los extremos

I = (h/2) * (10 + 2*(suma) + 3.6)
# print(I)

"""
--------------------------------------- EJERCICIO 4 - regla de simpson

Intrucciones: para una viga simplemente apoyada sujeta a ciertas cargas, el momento flector está modelado por la función M(x) = 15x**2 - 3x**3

Para calcular un coeficiente estructural, es necesario integrar esta ecuación desde x = 0, hasta x = 4 metros, utilizando la regla de simpson 1/3, con 4 sub intervalos (número par requerido)

Metodología y ecuaciones: se utilizara el ajuste parabólico de la regla de simpson 1/3, agrupando correctamente las evaluaciones pares e impares de los nodos a lo largo de la viga.
"""

from sympy import symbols, cos, integrate, lambdify
import numpy as np
import matplotlib.pyplot as plt

h = 1

Mx0 = 0
Mx1 = 15*(1)**2 - 3*(1)**3
Mx2 = 15*(2)**2 - 3*(2)**3
Mx3 = 15*(3)**2 - 3*(3)**3
Mx4 = 15*(4)**2 - 3*(4)**3


impar = Mx1 + Mx3
par = Mx2 

funcion = h/3 * (Mx0 + 4*(impar) + 2*(par) + Mx4)
print(funcion)