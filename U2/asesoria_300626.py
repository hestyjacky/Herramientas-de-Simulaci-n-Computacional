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
n = 4

h = (b - a) / n

x = symbols('x')
f = x**2
calcular_f = lambdify(x, f, 'numpy')

for i in range(n):
    valores_f = calcular_f(i*h)
    area_total += valores_f
    print(f'V1: {valores_f}  |  Sum: {area_total}')