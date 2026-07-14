# Aprender sobre Interpolacion
import numpy as np
import matplotlib.pyplot as plt

x = np.array([7, 9, 11, 12])
y = np.array([49, 57, 71, 75])

i = np.array([8, 10])

r = np.interp(i, x, y) # aqui se interpola, se le pasa el arreglo de los puntos a interpolar, el arreglo de los puntos conocidos y el arreglo de los valores conocidos
print(r)

plt.plot(x, y, 'o', label='Datos')
plt.plot(i, r, label='Interpolacion')
plt.legend()
plt.show()

# ------------ Otro ejercicio de interpolacion --------------
import numpy as np

