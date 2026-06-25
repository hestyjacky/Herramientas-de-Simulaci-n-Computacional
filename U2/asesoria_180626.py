"""
from sympy import symbols, sin, lambdify
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')

letra = str(input('Ingrese la letra R o C: '))

if letra.lower == 'r':
    a = 0.1
    t_num = np.linspace(4,8,20)
else:
    a = 0.5
    t_num = np.linspace(0,4,20)

y = sin(3*t) + 7*t + a
calcular_y = lambdify(t, y, 'numpy')
valores_y = calcular_y(t_num)

plt.plot(t_num, valores_y, linestyle='-', color='blue')
plt.show()

print('\n\n' + '-'*25)
print('t\t|\ty')
print('-'*25)
for i in range(len(t_num)):
    print(f'{t_num[i]:.3f}\t|\t{valores_y[i]:.3f}')
"""

# ------------------------------ EJERCICIO 2
numero = 0
cero = []
positivo = []
negativo = []
while True:

    valor = float(input(f'Numero {numero+1}: '))
    numero += 1

    if valor == 0:
        cero.append(valor)
    elif valor > 0:
        positivo.append(valor)
    elif valor < 0:
        negativo.append(valor)
    else:
        print('idk')

    if numero == 10:
        break

print('\nnegativos: ', negativo, '|\tCantidad: ', len(negativo))
print('ceros: ', cero, '|\tCantidad: ', len(cero))
print('positivos: ', positivo, '|\tCantidad: ', len(positivo))