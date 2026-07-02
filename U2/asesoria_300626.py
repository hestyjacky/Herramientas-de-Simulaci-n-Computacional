"""
S0_4 x**2 dx

h = (b - a) / n
"""
from sympy import symbols, lambdify
import numpy as np
import matplotlib.pyplot as plt
area_total = 0
 
a = 0
b = 4
n = 1000

h = (b - a) / n

x = symbols('x')
f = x**2
calcular_f = lambdify(x, f, 'numpy')

# ---------por la izq
for i in range(n):
    valores_f = calcular_f(i*h)
    area_total += valores_f
    # print(f'V1: {valores_f}')

areaTotal = area_total * h
print('\nIzquierda: ',areaTotal)

# ---------por la der
area_total_der = 0
for i in range(1, n+1):
    valores_f_der = calcular_f(i*h)
    area_total_der += valores_f_der
    # print(f'V1: {valores_f_der}')

areaTotal_der = area_total_der * h
print('Derecha: ',areaTotal_der)

# ---------por metodo del trapecio              -- SIN CORREGIR !!!
suma = 0

suma += calcular_f(a) # EXTREMO A
print(f'f({a}) = {calcular_f(a)}   ---- {suma}')

for i in range(a+1,n): # ENTRE MEDIAS
    suma += 2*calcular_f(i)
    print(f'f({i}) = {calcular_f(i)} * 2  ---- {suma}')

suma += calcular_f(b) # EXTREMO B
print(f'f({b}) = {calcular_f(b)}   ---- {suma}')
    
    
print('SUMA: ',suma)
total = h/2 * suma
print('total',total)