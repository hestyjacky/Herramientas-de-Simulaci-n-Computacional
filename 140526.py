# --------------------          1) FOR - sacar el factorial de un numero

"""
op = 1
numero = int(input("Ingrese un numero: "))

if (numero >= 0): # numeros positivos

    for i in range(1, numero + 1):
        op = op * i                 # 4! = 4 x 3 x 2 x 1
    print("el factorial es: ",op)

else:
    print("no se puede multiplicar")
    
"""

# --------------------          2) WHILE - imprimir un numero hasta el 16

"""
numero = int(input("Ingresa un numero: "))

while numero <= 16:
    print(numero)
    numero = numero + 1
"""

# --------------------          3) ecuaciones matemáticas

"""
from sympy import symbols

a, b, c, x = symbols('a,b,c,x')
f=a*x**2+b*x+c
r=f.subs(x,3)   

print(r)
"""

# --------------------          4) Personalizar grafica

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 500)

y = np.sin(x)
g = np.cos(x)

plt.plot(x, y, '--', color='red', label='sin(x)')
plt.plot(x, g, color='blue', label='cos(x)')
plt.show()
"""

# --------------------          5) Graficar un seno

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.linspace(-2*np.pi, 2*np.pi, 500)

X,Y = np.meshgrid(x,y)
Z = np.sin(X)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()
"""

# --------------------          6) Graficar un coseno

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.linspace(-2*np.pi, 2*np.pi, 500)

X,Y = np.meshgrid(x,y)
Z = np.cos(X)                                   # cambia para ver la grafica del coseno
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()
"""

# --------------------          7) Derivadas

from sympy import symbols, diff

x = symbols('x')

y = x**3
dy= diff(y,x) # derivada de x = 3x*2
print(dy)