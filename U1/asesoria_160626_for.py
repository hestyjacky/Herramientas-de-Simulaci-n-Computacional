"""
For example, suppose we had an equation for the x position of a vehicle as a 
function of time, such as
X(t)= Xo - vt 

where
Xo is the initial position of the vehicle
v is the vehicle’s speed

- crear la grafica y la tabla de la X posición del vehículo en diferentes tiempos
"""
"""
import numpy as np
from sympy import symbols, lambdify
import matplotlib.pyplot as plt

t = symbols('t')
Xo = 10
v = 40
t_num = np.linspace(0,0.1, 20)

x = Xo - v*t
calcular_x = lambdify(t, x, 'numpy')
valores_x = calcular_x(t_num)

plt.plot(t_num, valores_x, marker='o')
plt.show()

print('\tt\t|\tx(m)')
print('-' * 30)
for i in range(len(t_num)):
    print(f'\t{t_num[i]:.2f}\t|\t{valores_x[i]:.2f}')

print('-' * 30)
"""

# sumar los numeros naturales, del 1 al 100
"""
sumatoria = 0
for i in range(101):
    #print(sumatoria, '+', i)
    #print('-'*7)
    sumatoria += i
    #print(sumatoria, '\n\n')

print(sumatoria)
"""

# mostrar los caracteres de uno por uno
palabra = 'jackelyn'

for i in (palabra):
    print(i)