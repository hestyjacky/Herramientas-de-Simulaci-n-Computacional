import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito
Vin = 5       # Voltaje de entrada (V)
R = 1000      # Resistencia (Ohms)
C = 10e-6     # Capacitancia (Faradios) -> 10 uF
t = np.linspace(0, 0.05, 500) 

V = Vin * (1 - np.exp(-t / (R * C)))

# Agregar otros 2 valores con otra R
R2 = 500
V2 = Vin * (1 - np.exp(-t / (R2 * C)))

R3 = 2000
V3 = Vin * (1 - np.exp(-t / (R3 * C)))

plt.plot(t, V, color="blue")
plt.plot(t, V2, linestyle="-", color="red")
plt.plot(t, V3, linestyle="--", color="green")

plt.xlabel("Tiempo (segundos)")
plt.ylabel("Voltaje (V)")
plt.show()