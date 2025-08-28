# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Elevar al cuadrado
# ---------------------------------------------------------------------
"""
Declara una función lambda llamada cuadrado que reciba un número y devuelva ese número al cuadrado.
Prueba tu función con los valores 2, 5 y 10.
"""
cuadrado = lambda x: x**2

num = 5
print(f"El cuadrado de {num} es: {cuadrado(num)}")

# ---------------------------------------------------------------------
# Ejercicio 2 – Obtener el mayor de dos números
# ---------------------------------------------------------------------
"""
Declara una función lambda llamada mayor que reciba dos números y devuelva el mayor de los dos.
Prueba con los pares: (7, 3), (10, 15) y (20, 20).

Clue: usar el operador ternario 
val1 if condicion else val2
"""

mayor = lambda num1, num2: num1 if num1 > num2 else num2

num1 = 7
num2 = 3
print(f"El mayor entre {num1} y {num2} es {mayor(num1, num2)}")
