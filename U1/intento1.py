"""
The motion of a piston in an internal combustion engine is shown in 
Figure 2.10. The piston's position, s, as seen from the crankshaft center is 
determined to be

s(t) = r * cos(2 * pi * w * t) + sqrt((b**2) - (r**2) * (sin(2*pi*w*t) * sin(2*pi*w*t)))

  where
   b is the length of the piston rod
   r is the radius of the crankshaft
   ω is rotational speed of the crankshaft in revolutions per second

Develop a MATLAB program that determines s vs. t for 0 ≤ t ≤ 0.01 s. Use 20 subdivisions on the t domain. Take r = 9 cm, ω = 100 revolutions per sec ond, and b = 14 cm. Create a table of s vs. t and print the results to both the screen and to a file.
"""

from sympy import symbols, cos, sqrt, sin, lambdify
import numpy as np
import matplotlib.pyplot as plt

t_sim = symbols('t')
t_num = np.linspace(0, 0.01, 21) # 20 subdivisions en el intervalo de 0 a 0.01 s

r = 9 #cm
w = 100 #revoluciones x s
b = 14 #cm
p = np.pi
valores_arreglo_s_t = []

s_t_simb = r * cos(2 * p * w * t_sim) + sqrt((b**2) - (r**2) * (sin(2*p*w*t_sim) * sin(2*p*w*t_sim)))

calcular_s_t = lambdify(t_sim, s_t_simb, 'numpy')

valores_s_t = calcular_s_t(t_num)

# graficar s vs t
plt.plot(t_num, valores_s_t, marker='o')
plt.title('Gráfica de s(t) vs t')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (cm)')
plt.grid()
plt.show()

# imprimir una tabla con los resultados de la funcion s respecto a t
print("\n Tabla de valores: ")
print("t\t|\ts(t)")
print("-" * 20)
for i in range(len(t_num)):
    print(f"{t_num[i]:.2f}\t|\t{valores_s_t[i]:.2f}")

