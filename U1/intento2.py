"""
Determinar la ACELERACIÓN de un objeto considerando que la aceleración es el cambio de la velocidad con respecto al tiempo.
Se realizaran 5 graficas de aceleración variando el valor de r (preguntando al usuario y las unidades que puede ingresar pueden ser m o plg, pero reguiere que sean en mm para pasar por la formula) y sera mostrado en una sola ventana.
El tipo de color de línea se debera preguntar

Finalmente, se debe preguntar al usuario si desea conocer la velocidad de un valor en especifico de theta

- Intentar r con: 45m, 50m, 60m, 2000plg, 70000mm

"""
# LIBRERIAS
from sympy import symbols, sin, cos, sqrt, diff, lambdify
import numpy as np
import matplotlib.pyplot as plt

# VARIABLES
theta = symbols('theta')
theta_numerico = np.linspace(-4*np.pi, 4*np.pi, 500)
m = 1000 #mm
plg = 25.4 #mm
a = 44000 #mm
graph = 0

# CONVERSION DE UNIDADES
def conversion_de_unidades(r_str):
    print(f'--- Conversion de Unidades: {r_str}')

    if r_str.lower().strip().endswith('plg'): # pulgadas a mm
        r = float(r_str.replace('plg',''))
        r = r * plg
        print(f'\t-- Equivalencia: {r} mm')
        return r
    elif r_str.lower().strip().endswith('m'):
        r = float(r_str.replace('m',''))
        r = r * m
        print(f'\t-- Equivalencia: {r} mm')

        return r
    else:
        r = float(r_str)
        print(f'\t-- Equivalencia: {r} mm')
        return r
    

# CICLO PARA 5 GRAFICAS
while True:
    print(f'\n\n\t-----------------------  GRAFICA {graph+1}  -----------------------')
    # PREGUNTAR EL VALOR DE r
    r_str = str(input('Introduzca el valor de r: (ej. 45m, 50m, 60m, 2000plg, 70000)  '))
    
    r = conversion_de_unidades(r_str)

    # FORMULA EJERCICIO - VELOCIDAD
    velocidad_simbolica = ((-a * sin(theta) + ((-a**2 * sin(theta) * cos(theta) ))) / sqrt(r**2 - a**2 * (sin(theta) * sin(theta))))
    
    # FORMULA - ACELERACIÓN
    aceleracion_simbolica = diff(velocidad_simbolica, theta)

    # CAMBIO A NUMERICO
    calculo_velocidad = lambdify(theta, velocidad_simbolica, 'numpy')
    calculo_aceleracion = lambdify(theta, aceleracion_simbolica, 'numpy')

    # ASIGNARLE VALORES NUMERICOS A LA ACELERACIÓN
    valores_theta_num = calculo_aceleracion(theta_numerico)

    # PREGUNTAR EL COLOR
    rgb = str(input('Introduzca el color de la grafica: (ej. red, green, blue, orange, black)  '))

    # GRAFICAR
    plt.plot(theta_numerico, valores_theta_num, linestyle='-', color=rgb, label=f'r: {r}mm')

    # PREGUNTAR SI DESEA CONOCER LA VELOCIDAD EN THETA ESP
    respuesta = str(input('¿Desea conocer la velocidad de un valor en especifico de theta? (si/no) '))

    if respuesta.lower().strip().endswith('si'):
        # PREGUNTAR EL VALOR ESP DE THETA
        theta_usuario = float(input('Introduzca un valor de theta: (ej. 0 a 6.28)  '))

        # CALCULAR LA VELOCIDAD ESP
        resultado = calculo_velocidad(theta_usuario)
        print(f'-- La velocidad es de {resultado} en theta {theta_usuario}. ')

    graph += 1

    if graph == 5:
        break

plt.title('Aceleración')
plt.xlabel('Theta')
plt.ylabel('Aceleración')
plt.grid(True)
plt.legend()
plt.show()