# ----- Interpolación - Leer datos desde un archivo y separarlos en columnas
import numpy as np
"""
m = np.loadtxt('U3\data_short.txt')
print(m, '\n')

# esto es para separar las columnas y convertirlas a enteros
x = m[:,0].astype(int)
y = m[:,1]

# otra forma de leer el archivo
m2 = np.genfromtxt('U3\data_short.txt')
print(m2)
"""

# otra forma de leer el archivo y separar las columnas

rows = []

with open('U3\data_short.txt', 'r') as f:
    for line in f:
        values = line.split()
        
        if len(values) == 2:
            rows.append([int(values[0]), float(values[1])])
        elif len(values) == 1:
            rows.append([int(values[0]), 0.0])  # Asignar un valor predeterminado para la segunda columna

# Convertir la lista de filas a un array de NumPy
data = np.array(rows)

# print(data)

# graficar los datos
import matplotlib.pyplot as plt

x = data[:,0]
y = data[:,1]

plt.plot(x, y, 'o-')
plt.grid()
plt.show()

# agregar nueva fila en la linea 9
# data = np.insert(data, 8, [9, 0.0], axis=0) 

# agregar nueva fila en la linea 13
# data = np.insert(data, 13, [13, 0.0], axis=0)  

# si en la columna 2 hay vacio, colocar nan
data[data[:,1] == 0.0, 1] = np.nan



# eliminar fila 9 y fila 13
# data = np.delete(data, np.where(np.isnan(data[:,1]))[0], axis=0)
data = np.delete(data, [8, 12], axis=0)
print(data, '\n')

# hacer interpolación lineal para los valores faltantes
# --- actualizar x e y después de eliminar filas
x = data[:,0]
y = data[:,1]

# i = np.array([9, 13])

# otra forma de encontrar los valores faltantes en la columna 1
i = []
for j in range(1, len(data)):
    if j not in data[:,0]:
        i.append(j)

interpolacion = np.interp(i, x, y)

print(f"para x:{i}\ninterpolados: {interpolacion}")

# hacerlo ahora con pandas
import pandas as pd

rows = []

with open('U3\data_short.txt', 'r') as f:
    for line in f:
        values = line.split()
        
        if len(values) == 2:
            rows.append([int(values[0]), float(values[1])])
        elif len(values) == 1:
            rows.append([int(values[0]), 0.0])  # Asignar un valor predeterminado para la segunda columna

# Convertir la lista de filas a un array de NumPy
data = np.array(rows)

# df desde data
df = pd.DataFrame(data, columns=['X', 'Y'])

# mostrar el DataFrame original
print("\nDataFrame original:")
print(df, '\n')

# hacer la interpolación lineal para los valores faltantes
df['Y'] = df['Y'].replace(0.0, np.nan)
df['Y'] = df['Y'].interpolate()

# mostrar el DataFrame con los valores interpolados
print("DataFrame con valores interpolados:")
print(df, '\n')
