# ==============================================================================
# PASO 1: IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
# Importamos las herramientas de SymPy para trabajar con matemáticas simbólicas (fórmulas)
from sympy import symbols, diff, sin, cos, sqrt, lambdify
# Importamos NumPy para manejar vectores numéricos y operaciones de arreglos
import numpy as np
# Importamos Matplotlib para generar los gráficos en pantalla
import matplotlib.pyplot as plt

# ==============================================================================
# PASO 2: CONFIGURACIÓN DE VARIABLES Y ENTORNO
# ==============================================================================
# Definimos 'theta' como un SÍMBOLO matemático puro. No tiene valor numérico aún.
theta = symbols('theta')

# Creamos un vector numérico de 500 puntos entre 0 y 2*pi para el eje X de la gráfica.
# Usamos radianes porque las funciones matemáticas de Python trabajan en radianes.
theta_num = np.linspace(0, 2 * np.pi, 500) 

# Factores de conversión para las unidades de longitud a milímetros (mm)
m = 1000       # 1 metro = 1000 mm
plg = 25.4     # 1 pulgada = 25.4 mm
a = 44000      # Valor constante 'a' en milímetros

# Inicializamos el contador de gráficas en 0 (debe llegar a 5)
graph = 0

# ==============================================================================
# PASO 3: BUCLE PRINCIPAL PARA CAPTURAR 5 GRÁFICAS
# ==============================================================================
while True:
    # Solicitamos al usuario el valor de 'r' junto con su unidad (ej. "2 m", "45 plg", "50000")
    r_str = str(input('Ingrese el valor de r (ej. 50000, 2 m, 80 plg): '))

    # --- BLOQUE DE CONVERSIÓN DE UNIDADES ---
    if r_str.endswith('plg'):       
        # Si termina en 'plg', removemos el texto, limpiamos espacios, pasamos a flotante y multiplicamos por 25.4
        r = float(r_str.replace('plg', '').strip()) * plg
        print(f'-> Conversión a mm: {r} mm')

    elif r_str.endswith('m'):       
        # Si termina en 'm', removemos la unidad, limpiamos espacios, pasamos a flotante y multiplicamos por 1000
        r = float(r_str.replace('m', '').strip()) * m
        print(f'-> Conversión a mm: {r} mm')

    elif r_str.endswith('mm'):
        # Si ya termina en 'mm', solo removemos el texto y lo convertimos a número flotante
        r = float(r_str.replace('mm', '').strip())
        print(f'-> Valor en mm: {r} mm')
        
    else:
        # Si el usuario solo escribió el número, asumimos que ya está en milímetros
        r = float(r_str)
        print(f'-> Asumiendo mm: {r} mm')

    # ==============================================================================
    # PASO 4: CÁLCULO SIMBÓLICO (MATEMÁTICAS PURAS CON SYMPY)
    # ==============================================================================
    # Escribimos la fórmula de la velocidad usando el símbolo 'theta'. 
    # Python guarda esto como una ecuación algebraica abierta, no como un resultado numérico.
    velocidad_simbolica = ((-a * sin(theta) + ((-a**2 * sin(theta) * cos(theta)))) / sqrt(r**2 - a**2 * (sin(theta) * sin(theta))))

    # Derivamos la velocidad respecto a 'theta' usando SymPy para obtener la fórmula de la aceleración.
    aceleracion_simbolica = diff(velocidad_simbolica, theta)

    # ==============================================================================
    # PASO 5: TRADUCCIÓN A NUMERÍTICO (CONVERSIÓN CON LAMBDIFY)
    # ==============================================================================
    # Convertimos la ecuación de aceleración en una función de Python que acepta arreglos de NumPy.
    # El primer argumento SIEMPRE debe ser el símbolo original ('theta').
    calcular_aceleracion = lambdify(theta, aceleracion_simbolica, 'numpy')
    
    # También convertimos la ecuación de velocidad a función numérica por si el usuario la consulta al final.
    calcular_velocidad = lambdify(theta, velocidad_simbolica, 'numpy')
    
    # ==============================================================================
    # PASO 6: EVALUACIÓN Y GRÁFICA
    # ==============================================================================
    # Solicitamos el color de la línea como texto limpio (ej: red, blue, green)
    rgb = str(input('Asigne un color para esta línea: '))
    print(rgb, '-- grafica ', graph+1)

    # Evaluamos la función de la aceleración pasándole TODO el vector numérico 'theta_num'
    # Esto nos devuelve una lista con 500 resultados de aceleración calculados.
    valores_aceleracion = calcular_aceleracion(theta_num)

    # Graficamos: Eje X = los ángulos (theta_num), Eje Y = los resultados medidos (valores_aceleracion)
    # Al estar dentro del 'while', Matplotlib acumulará las 5 líneas en la misma ventana.
    plt.plot(theta_num, valores_aceleracion, linestyle='-', color=rgb, label=f'r = {r} mm')

    # ==============================================================================
    # PASO 7: EVALUACIÓN DE UN PUNTO ESPECÍFICO DE VELOCIDAD
    # ==============================================================================
    # Preguntamos al usuario si desea calcular un dato exacto
    respuesta = str(input('¿Desea conocer la velocidad en un valor especifico de theta? (si/no): '))
    
    # Pasamos la respuesta a minúsculas (.lower()) para evitar fallas si escriben "SI" o "Si"
    if respuesta.lower().endswith('si'):
        # Solicitamos el valor numérico en el que se quiere evaluar (ej. 1.5)
        theta2 = float(input('Ingrese el valor numérico de theta en radianes (ej. 0 a 6.28): '))
        
        # Evaluamos el número ingresado directamente en nuestra función numérica 'calcular_velocidad'
        # ¡Ya no hay peligro de mezclar símbolos con números reales!
        velocidad_final = calcular_velocidad(theta2)
        
        # Imprimimos el resultado exacto en la consola
        print(f'La velocidad en {theta2} rad es de: {velocidad_final} mm/s\n')
    else:
        print("Continuando al siguiente ciclo...\n")

    # Incrementamos en 1 el contador de gráficos realizados
    graph += 1

    # Si ya se recolectaron los datos para las 5 gráficas, rompemos el bucle infinito
    if graph == 5:
        break

# ==============================================================================
# PASO 8: DESPLIEGUE VISUAL DE LA VENTANA
# ==============================================================================
# Configuramos los títulos decorativos del gráfico final
plt.title('Evaluación Cinemática: Gráficas de Aceleración vs Theta')
plt.xlabel('Ángulo Theta (Radianes)')
plt.ylabel('Aceleración (mm/s²)')
plt.grid(True)     # Activamos la cuadrícula de fondo para leer mejor los datos
plt.legend()       # Muestra un cuadro indicando qué color pertenece a qué valor de 'r'

# Finalmente, abrimos la ventana interactiva en la pantalla con las 5 curvas impresas
plt.show()