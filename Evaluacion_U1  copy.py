import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, sin, cos, sqrt, lambdify

# 1. DEFINICIÓN DE SÍMBOLOS (Solo para cálculo matemático con SymPy)
t_sym, r_sym = symbols('t_sym r_sym')
a_val = 44000.0  # mm
omega = 1.0      # Asumimos una velocidad angular constante para relacionar theta y tiempo
theta_sym = omega * t_sym

# Fórmula de velocidad simbólica en función del tiempo (t_sym) y el radio (r_sym)
v_sym = ((-a_val * sin(theta_sym) + (-a_val**2 * sin(theta_sym) * cos(theta_sym))) / 
         sqrt(r_sym**2 - a_val**2 * (sin(theta_sym)**2)))

# Derivamos la velocidad respecto al tiempo para obtener la aceleración simbólica
acc_sym = diff(v_sym, t_sym)

# Convertimos las expresiones simbólicas a funciones numéricas de NumPy
# Ambas funciones recibirán (tiempo, radio)
funcion_velocidad = lambdify((t_sym, r_sym), v_sym, 'numpy')
funcion_aceleracion = lambdify((t_sym, r_sym), acc_sym, 'numpy')

# 2. CONFIGURACIÓN DE VARIABLES NUMÉRICAS
m = 1000.0      # Factor para metros a mm
plg = 25.4      # Factor para pulgadas a mm
tiempo_array = np.linspace(0, 10, 500)  # Un rango de tiempo para graficar
graficas_contadas = 0

plt.figure(figsize=(10, 6)) # Una sola ventana para todas las gráficas

# 3. CICLO PRINCIPAL (Para 5 gráficas)
while graficas_contadas < 5:
    print(f"\n--- Configuración de la gráfica {graficas_contadas + 1} de 5 ---")
    r_str = input('Ingrese el valor de r (ej. "50000 mm", "2000 plg", "60 m"): ').strip().lower()

    # Procesamiento y conversión de unidades
    if r_str.endswith('plg'):
        r = float(r_str.replace('plg', '').strip()) * plg
        print(f'-> Conversión a mm: {r} mm')
    elif r_str.endswith('m'):
        r = float(r_str.replace('m', '').strip()) * m
        print(f'-> Conversión a mm: {r} mm')
    elif r_str.endswith('mm'):
        r = float(r_str.replace('mm', '').strip())
        print(f'-> Valor en mm: {r} mm')
    else:
        # Si solo ingresa el número, asumimos mm
        r = float(r_str)
        print(f'-> Asumiendo mm: {r} mm')

    # Validación física: r debe ser mayor que 'a' para que la raíz cuadrada no sea imaginaria
    if r <= a_val:
        print(f"❌ Error: El valor de r debe ser mayor que 'a' ({a_val} mm) para evitar errores matemáticos.")
        continue

    # Preguntar el color
    color_linea = input('Asigne un color para la línea (ej. red, blue, green, hex): ').strip()

    # Calcular la aceleración numéricamente para el vector de tiempo
    aceleracion_numerica = funcion_aceleracion(tiempo_array, r)

    # Graficar en la misma ventana
    plt.plot(tiempo_array, aceleracion_numerica, linestyle='-', color=color_linea, label=f'r = {r:.1f} mm')

    # Preguntar por un valor específico de theta
    resp = input('¿Desea conocer la velocidad en un valor específico de theta? (si/no): ').strip().lower()
    if resp == 'si':
        theta_especifico = float(input('Ingrese el valor de theta (en radianes): '))
        # Como theta = omega * t, entonces t = theta / omega
        t_especifico = theta_especifico / omega
        vel_especifica = funcion_velocidad(t_especifico, r)
        print(f'➔ La velocidad en theta = {theta_especifico} rad es de: {vel_especifica:.2f} mm/s')

    graficas_contadas += 1

# 4. MOSTRAR LA VENTANA ÚNICA
plt.title('Gráficas de Aceleración variando r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración ($mm/s^2$)')
plt.grid(True)
plt.legend()
plt.show()