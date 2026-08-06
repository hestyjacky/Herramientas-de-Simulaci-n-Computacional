# TERMINAR DE HACER EL EJERCICIO

"""     NOTAS 04.08.26
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    PARTE 1 - ESTE ARCHIVO
abrir archivo de texto
revisar espacios vacios
si en ese caso, hacer interpolacion o extrapolacion
graficar los datos originales y los interpolados
- grafica de scatter? puros puntos
- grafico de barras? para ver la diferencia entre los datos originales y los interpolados
- grafica polar? Opción para datos angulares


    PARTE 2 - ARCHIVO 06.08.26
trabajar con dos variables, dentro del tema de newton-rapson (initial guess)
porque el profe nos dará más de una ecuacion
"""

# cargar datos de excel U3\data_solar.xls
import pandas as pd

data_file = 'U3/data_solar.xls'
df = pd.read_excel(data_file, header=1, skiprows=[2,3])
print(df.head())

# --- interpolacion con los datos que son 0 para mostrar los valores q faltan

# tomar columnas con 0
cols_with_0 = df.columns[(df == 0).any()]
print("Columnas con 0:", cols_with_0)

# reemplazar 0 con NaN
df[cols_with_0] = df[cols_with_0].replace(0, pd.NA)
print("\nDataFrame con 0 reemplazado por NaN:")
print(df.head())

# hacer interpolación lineal para los valores faltantes --- ARREGLAR ESTO
df[cols_with_0] = df[cols_with_0].interpolate()
print("\nDataFrame con valores interpolados:")
print(df.head())