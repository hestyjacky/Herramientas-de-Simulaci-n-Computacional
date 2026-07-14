# ------------ Interpolacion --------------
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Tus datos conocidos (Puntos ancla)
x = np.array([7, 9, 11, 12])
y = np.array([49, 57, 71, 75])

# 2. Los valores de X que queremos averiguar (Interpolar)
i = np.array([8, 10])

# 3. La interpolación
r = np.interp(i, x, y)
print(f"Para x={i}, los valores interpolados de y son: {r}")

# 4. Visualización mejorada
# Trazamos los datos conocidos como una línea con puntos
plt.plot(x, y, marker='o', linestyle='-', label='Datos Conocidos')

# Trazamos los valores interpolados como estrellas rojas (u otro marcador destacado)
plt.plot(i, r, marker='*', markersize=12, linestyle='', label='Puntos Interpolados')

plt.title('Ejemplo de Interpolación Lineal')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.legend()
plt.grid(True) # Agregar una cuadrícula ayuda a leer los valores
plt.show()
"""
# ----------- Ejercicio clase 1 --------------
import numpy as np
import matplotlib.pyplot as plt

u = np.array([-2, 10, 5, np.nan, -3, 8, 2, np.nan,6])

print(np.isnan(u))  # Devuelve un array booleano indicando dónde están los NaN
print(np.where(np.isnan(u))[0]) # Devuelve los índices de los elementos que son NaN

promedio = np.nanmean(u)  # Calcula el promedio ignorando los NaN
print(f"El promedio de los valores no NaN es: {promedio:.5f}")

# check if is there any nan values
if np.any(np.isnan(u)):
    v = u[~np.isnan(u)]  # Filtra los valores que no son NaN
    print(f"Valores no NaN: {v}")
    
# hacer uso de ciclos
suma = 0
contador = 0
for valor in u:
    if not np.isnan(valor):
        suma += valor
        contador += 1
promedio_ciclo = suma / contador
print(f"El promedio calculado con ciclos es: {promedio_ciclo:.5f}")


# ----------- Ejercicio 2 --------------
"""
Un cohete recolecta datos de velocidad en diferentes segundos de su lanzamiento. Debido a la vibración y fallas en los sensores, los datos llegaron en orden caótico y con una pérdida de señal al final.Aquí están los registros recuperados:
A los 5 segundos: velocidad de 120 m/s
A los 15 segundos: velocidad de 380 m/s
A los 20 segundos: velocidad de 520 m/s
A los 25 segundos: velocidad de 710 m/s

Debes programar un script para estimar la velocidad del cohete en tres momentos críticos 
(i = [12, 17, 30] segundos)
"""
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 15, 20, 25]) # s
y = np.array([120, 380, 520, 710]) # m/s

i = np.array([12, 17, 30]) # s

# interpolacion lineal
r = np.interp(i, x, y)
print(f"Para i={i}, los valores interpolados de velocidad son: {r}")

# Visualización mejorada
plt.plot(x, y, marker='o', linestyle='-', label='Datos Conocidos')
plt.plot(i, r, marker='*', markersize=12, linestyle='', label='Puntos Interpolados')
plt.title('Interpolación de Velocidad del Cohete')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid(True)
plt.show()
"""
# ----------- Ejercicio 3 --------------
"""
Here are two vectors representing the census years from 1900 to 1990 and the corresponding United States population in millions of people.
t = 1900:10:1990;
p = [75.995  91.972  105.711  123.203  131.669,
     150.697  179.323  203.212  226.505  249.633];
The expression interp1(t,p,1975) interpolates within the census data to estimate the population in 1975. The result is
ans =
    214.8585
"""
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1900, 1990, 10) # years
p = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633]) # population in millions

i = np.array([1975]) # year to interpolate

# interpolation
r = np.interp(i, t, p)
print(f"Estimated population in {i[0]}: {r[0]} million")

# Visualización mejorada
plt.plot(t, p, marker='o', linestyle='-', label='Census Data')
plt.plot(i, r, marker='*', markersize=12, linestyle='', label='Interpolated Point')
plt.title('US Population Interpolation')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.legend()
plt.grid(True)
plt.show()
"""


# ------------ Ejercicios Lagrange EXTRA --------------
"""
  Find  the  Lagrange’s  interpolating  polynomial  approximating  the function y = log x defined by the following table of values. Hence determine the value of log 2.7 
  x         2        2.5      3.0 
  log x     0.69315  0.91629  1.09861 
"""

"""
The function sin y = x is tabulated below:
x: 0, π/4, π/2
y: 0, 0.70711, 1.0
Using Lagrange’s interpolation formula, find the value of sin(π/6)
"""

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, np.pi/4, np.pi/2])
y = np.array([0, 0.70711, 1.0])

# using Lagrange's interpolation formula to find sin(π/6)
i = np.array([np.pi/6])

r = np.interp(i, x, y)
# result of interpolation based on the book: 0.51743
print(r)

# why is not the same result as the book? because the book uses Lagrange's interpolation formula, while np.interp uses linear interpolation. The result of the book is more accurate than the result of np.interp.

# use of larange's interpolation formula to find sin(π/6)
def lagrange_interpolation(x, y, x0):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x0 - x[j]) / (x[i] - x[j])
        result += term
    return result

# using the Lagrange interpolation function
r_lagrange = lagrange_interpolation(x, y, np.pi/6)
print(r_lagrange)
"""