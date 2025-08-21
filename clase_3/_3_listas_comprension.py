# listas_por_comprension.py

import math

# Ejemplo 1: Crear una Lista con Listas por Comprensión
numeros = [0, 1, 2, 3, 4, 5]  # arreglo o iterable numeros
cuadrados = [num**2 for num in numeros]
print("Cuadrados:", cuadrados)  # [0, 1, 4, 9, 16, 25]

# Ejemplo 2: Filtrar Elementos
# [ exp1  for item in iterable if condicion]
lista = [1, -2, 5, 0, 3, 4]
listaCuadradosParesPorComp = [num**2 for num in lista if num % 2 == 0]
print("Cuadrados de pares:", listaCuadradosParesPorComp)  # [4, 0, 16]

# Ejemplo 3: Filtro con Condición if-else
# [ exp1 if condicion else exp2  for item in iterable]
lista = [1, -2, 5, 0, 3, 4]
listaPorComp = [num**2 if num % 2 == 0 else num for num in lista]
print("Cuadrados de pares, impares sin cambios:", listaPorComp)  # [1, 4, 5, 0, 3, 16]

# Ejemplo 4: Aplicación de Funciones
numeros = [1, 4, 9, 16]
raices = [math.sqrt(x) for x in numeros]
print("Raíces cuadradas:", raices)  # [1.0, 2.0, 3.0, 4.0]

# Ejemplo 5: Uso de Función Lambda (Lo vemos en más detalle en clase 4)
numeros = [1, 2, 3, 4, 5]
dobles = [(lambda x: x * 2)(x) for x in numeros]
print("Dobles de los números:", dobles)  # [2, 4, 6, 8, 10]
