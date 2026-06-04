"""
Determinar la ACELERACIÓN de un objeto considerando que la aceleración es el cambio de la velocidad con respecto al tiempo.
Se realizaran 5 graficas de aceleración variando el valor de r 
    (preguntando al usuario y las unidades que puede ingresar pueden ser m o plg, pero reguiere que sean en mm para pasar por la formula)
y sera mostrado en una sola ventana.
El tipo de color de línea se debera preguntar

Finalmente, se debe preguntar al usuario si desea conocer la velocidad de un valor en especifico de theta
"""

from sympy import symbols, diff, sin, cos, sqrt, lambdify
import numpy as np
import matplotlib.pyplot as plt

theta = symbols('theta')
theta_numerico = np.linspace(-4*np.pi, 4*np.pi, 500)
m = 1000 #mm
plg = 25.4 #mm
a = 44000 #mm
graph = 0

while True:
    r_str = ''
    r_str = str(input('Ingrese el valor de r: '))

    if r_str.endswith('plg'):       # TRANSFORMAR PULGADAS
        r = float(r_str.replace('plg', '').strip()) * plg
        print(f'-> Conversión a mm: {r} mm')

    elif r_str.endswith('m'):       # TRANSFORMAR METROS
        r = float(r_str.replace('m', '').strip()) * m
        print(f'-> Conversión a mm: {r} mm')

    elif r_str.endswith('mm'):
        r = float(r_str.replace('mm', '').strip())
        print(f'-> Valor en mm: {r} mm')
    else:
        # Si solo ingresa el número, asumimos mm
        r = float(r_str)
        print(f'-> Asumiendo mm: {r} mm')

    velocidad_simbolica = ((-a * sin(theta) + ((-a**2 * sin(theta) * cos(theta) ))) / sqrt(r**2 - a**2 * (sin(theta) * sin(theta))))

    aceleracion_simbolica = diff(velocidad_simbolica, theta)

    aceleracion = lambdify(theta, aceleracion_simbolica, 'numpy')

    valores_aceleracion = aceleracion(theta_numerico) # Evaluamos la función
    
    rgb = str(input('Asigne un color: '))
    print(rgb, '-- grafica ', graph+1)

    plt.plot(theta_numerico, valores_aceleracion, linestyle = '-', color=rgb)

    respuesta = str(input('¿Desea conocer la velocidad en un valor especifico de theta? '))
    theta2 = float(input('Ingrese el valor de theta: (ej. 0 a 1.5) '))

    if respuesta.endswith('si'):
        velocidad_especifica_simbolica = ((-a * sin(theta2) + ((-a**2 * sin(theta2) * cos(theta2) ))) / sqrt(r**2 - a**2 * (sin(theta2) * sin(theta2))))
        velocidad_especifica = lambdify(theta2, velocidad_especifica_simbolica, 'numpy')
        print('La velocidad en "', theta2, '" es de: ', velocidad_especifica)

    graph += 1

    if graph == 5:
        break

plt.show()