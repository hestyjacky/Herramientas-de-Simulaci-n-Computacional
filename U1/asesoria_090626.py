"""
In this example, we will calculate the position and velocity of a ball thrown 
vertically upward in a gravitational field (neglecting drag) as a function of time t. 
The approximate path of the ball is shown in Figure 2.9.
Recall that velocity is the rate of change of distance with respect to time and 
acceleration is the rate of change of velocity with respect to time. For motion in 
the y direction only, with the y-axis pointing upward, the governing equations are
    V(t) = Vo - gt
    y(t) = Vo * t - (1/2)gt^2
where 
    V is the velocity
    Vo is the velocity at t = 0
    y is the position of the ball at time t
    g is the acceleration of gravity
    t is the time

Equations 2.1 and 2.2 are based on the initial conditions V(0) = Vo and y(0) = 0.
The following MATLAB program calculates V and y vs. t, for 0 ≤ t ≤ 5 s in steps 
of 0.5 s. We have taken Vo = 20 m/s and g = 9.81 m/s2

- pedir 3 valores de Vo al usuario
- print a table of values for t, and y1, y2, y3. 
"""
from sympy import symbols, lambdify
import numpy as np
import matplotlib.pyplot as plt

t_simbolico = symbols('t')
t_numerico = np.arange(0, 5, 0.5)
g = 9.81 # m/s^2

graph = 0
valores_y = []

while True:
    print(f'\n\t--------------  Grafica {graph+1}  --------------')
    Vo = float(input("Ingrese el valor de Vo (m/s): "))

    # velocidad Vo
    Velocidad_simbolica = Vo - g * t_simbolico
    calcular_velocidad = lambdify(t_simbolico, Velocidad_simbolica, 'numpy')
    
    # altura y
    y = Vo * t_simbolico - (g * (t_simbolico**2)) /2
    calcular_y = lambdify(t_simbolico, y, 'numpy')

    valores_tiempo = calcular_y(t_numerico)

    plt.plot(t_numerico, valores_tiempo, linestyle='-', color='black', label=f'V{graph+1} = {Vo}')

    # guardar valor de y, en en el rango de t
    valores_y.append(valores_tiempo)

    resp_t_esp = str(input('¿Desea conocer el valor de y en un tiempo en específico? (S/N) '))

    if resp_t_esp.strip().upper().startswith('S'):
        t_especifico = float(input('Ingrese el tiempo: '))
        valor_t = calcular_y(t_especifico)

        print(f'Imprimir valor de y en tiempo {t_especifico}: {valor_t}')

    graph += 1

    if graph > 2:
        break

# imprimir una tabla de     t | y
    # t | y1 | y2 | y3

print("\n--------------  Tabla de valores: --------------")
print("t\t|\ty1\t|\ty2\t|\ty3")
print("-" * 40)
for i in range(len(t_numerico)):
    # float de .2 decimales
    print(f"{t_numerico[i]:.2f}\t|\t{valores_y[0][i]:.2f}\t|\t{valores_y[1][i]:.2f}\t|\t{valores_y[2][i]:.2f}")

plt.title('Grafica de V')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()