import numpy as np

"""
print("\n10, 20, 30\n")
# pedir un numero
numero = float(input('Ingresa un numero: '))

# -----------------------     1) tomar raiz e imprimir
if numero >= 0 :
    operacion = np.sqrt(numero)

    # si la raiz no es exacta, imprimir "..."
    print(f"El resultado de la raiz cuadrada es: {operacion}\n")
else:
    print("No se le puede sacar la raiz\n")
"""


# -----------------------     2) comparar valores
"""
if numero == 10 or numero == 20 or numero == 30:
    print(numero)
else:
    print("No es ninguno de los valores mencionados anteriormente: ",numero)
"""

# -----------------------     3) comparar texto

"""
genero = str(input("Ingrese genero: M/H   ")).lower
calorias = float(input("Ingrese las calorias:  "))

if genero.startswith("m") and calorias >= 2500:
   print("Algo te va a suceder")
else:
    print("Puede comer pay")

if genero.startswith('h') and calorias >= 2000:
    print("Algo te va a suceder")
else:
    print("Puede comer pay")
"""

# -----------------------     4) usar opcion multiple
calificación = str(input("Ingresa calificacion: A/B/C/D     "))

match calificación:
    case 'a': 
        print("A - Excelente")
    case 'b': 
        print("B - Muy bien")
    case 'c': 
        print("C - Bien")
    case 'd': 
        print("D - Se puede mejorar")
