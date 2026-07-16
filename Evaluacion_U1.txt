from sympy import symbols, exp, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')
R = float(input('Ingrese valor de R: '))
C = float(input('Ingrese valor de C: '))
Vin = float(input('Ingrese valor de Vin: '))

Vc_simb = Vin * (1 - exp(-t /(R*C)))
Ic_simb = C * diff(Vc_simb, t)
Pc_simb = Vc_simb * Ic_simb

t_num_grafica = np.arange(0,5,0.01)
t_num_tabla = np.arange(0,5,1)

calcular_Vc = lambdify(t, Vc_simb, 'numpy')
calcular_Ic = lambdify(t, Ic_simb, 'numpy')
calcular_Pc = lambdify(t, Pc_simb, 'numpy')

valores_Vc  = calcular_Vc(t_num_grafica)
valores_Ic  = calcular_Ic(t_num_grafica)
valores_Pc  = calcular_Pc(t_num_grafica)

plt.plot(t_num_grafica, valores_Vc, linestyle='-', color='red', label='Vc')
plt.plot(t_num_grafica, valores_Ic, linestyle='-.', color='blue', label='Ic')
plt.plot(t_num_grafica, valores_Pc, linestyle='--', color='black', label='black')

plt.grid(True)
plt.legend()
plt.show()

for i in range(len(t_num_tabla)):
    print(f'{t_num_tabla[i]} \t|\t {valores_Vc[i]}')