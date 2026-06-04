"""
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito 
Vin = 5     # 5V
R = 1000    # 1000 Ohms
L = 10e-3   # 10mH
t = np.linspace(0, 0.0001, 500) # Reduje el tiempo para ver la curva de carga, 
# 0.05s era demasiado para una L tan chica

# Usamos np.arange para permitir pasos decimales
# range(inicio, fin, paso)
for c in np.arange(0, 5, 1):
    # Fórmula de la corriente
    IL = (Vin/R) + c * np.exp(-R/L * t)
    
    # Graficamos dentro del bucle (se van acumulando las líneas)
    plt.plot(t, IL, label=f"c = {c:.1f}")

# Configuramos la gráfica FUERA del bucle
plt.title("Respuesta del Circuito RL para diferentes valores de C")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Corriente (A)") # Corregido a Corriente
plt.grid(True)
plt.legend() # Muestra qué línea corresponde a cada valor de 'c'
plt.show()   # Se llama una sola vez al final

"""

from sympy import symbols, diff, exp, lambdify
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')
m = 68.1
c = 12.5
g = 9.81

v = ((g * m) /c) * (1 - exp(-(c / m) * t))

a_simbolica = diff(v, t)  # Esto calcula la aceleración

# 2. Convertir la expresión de SymPy a una función de NumPy
# lambdify(variable_origen, expresion_simbolica, 'numpy')
a_num = lambdify(t, a_simbolica, "numpy")

# 3. Crear el vector de tiempo para la gráfica
t_vals = np.linspace(0, 10, 500)

# 4. Evaluar la función con los valores de tiempo
a_vals = a_num(t_vals)

# 5. Graficar
plt.plot(t_vals, a_vals, "-", color="r")
plt.xlabel("Tiempo (segundos)")
# Nota: La derivada de la velocidad respecto al tiempo es la aceleración
plt.ylabel("Aceleración (m/s²)")
plt.title("Aceleración en función del tiempo")
plt.grid(True)
plt.show()