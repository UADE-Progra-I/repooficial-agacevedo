# ***********************************************************
# ACTIVIDAD PRUEBAS UNITARIAS
# ***********************************************************

"""
Se propone usar las consignas del examen, para desarrollar las funciones de cada ejercicio
y su correspondiente función de validación / prueba unitaria usando Pytest

"""

# ------------------------------------------------------------------------------------
# Ejercicio 1 (0.5 puntos)
"""
Crear una rama secundaria llamada "desarrollo"
Desarrollar todo el examen en esa rama "desarrollo"
A medida que avanzas hace commits parciales
Cuando finalices hace un pull request de manera de hacer un merge
de la rama "desarrollo" con la rama principal "main.
"""


# ------------------------------------------------------------------------------------
# Ejercicio 2 (1 puntos)
""" 
Se solicita calcular el producto de una matriz de n* m dimensiones por un escalar. 
Analizar el código de la siguiente función matriz_por_escalar y en caso de ser necesario,
refactoriza para que cumpla con la consigna """


def matriz_por_escalar(matriz, escalar):
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    resultado = [[0] * nColumnas for _ in range(nFilas)]
    for i in range(nFilas):
        for j in range(nColumnas):
            resultado[i][j] = matriz[i][j] * escalar
    return resultado


# Escribí aquí tu respuesta o el código de la función refactorizada:


# ------------------------------------------------------------------------------------
#  Ejercicio 3 (0.5 puntos)
"""
Dada una matriz M de dimensiones 2 x 2 y un escalar A, 
escriba el código de la invocación a la función matriz_por_escalar 
pasando los argumentos correspondientes e indique la matriz que retorna.
"""
M = [[1, 2], [4, 5]]
A = 2

# Tu respuesta aquí:


# ------------------------------------------------------------------------------------
# Ejercicio 4 (1 punto)
"""¿Cuál de las siguientes expresiones en Python 
genera una lista con los cuadrados de los números del 1 al 5 utilizando lista por comprensión?"""

# a) [x * x for x in range(1, 6)]
# b) [x ** 2 for x in range(6)]
# c) [x ^ 2 for x in range(1, 6)]
# d) [x ** 2 for x in (1, 2, 3, 4)]

# Tu respuesta aquí:
list(range(6))  # 0,1,2,4,3,5
list(range(1, 6))  # 1,2,4,3,5

# ------------------------------------------------------------------------------------
# Ejercicio 5 (1 punto)
"""
Usando filter y lambda, 
escriba el código necesario para obtener una nueva lista 
que contenga únicamente los números positivos de la siguiente lista:
"""
numeros = [3, -1, 0, 7, -5, 10, -2]

# Tu respuesta aquí:

list(filter(lambda x: x > 0, numeros))

# ------------------------------------------------------------------------------------
# Ejercicio 6 (1 puntos)
"""
Método de listas

Dada la lista numeros = [10, 3, 7, 2, 15], aplicá los métodos de lista necesarios para:
1. Agregar el número 20 al final.
2. Insertar el número 5 en la posición 2.
3. Eliminar el número 7.
4. Ordenar la lista de menor a mayor.
Implementar en modificar_lista(numeros).
"""
numeros = [10 ,3, 7, 2, 15]

# Respuesta item 1:

# Respuesta item 2:

# Respuesta item 3:
numeros.pop(3) # indice 3 - remueve el  valor 2
# Respuesta item 4:


# Ejercicio 7 (2 puntos)
"""
Dada la siguiente función procesar_texto(cadena), 
indique cuál será la salida al invocarla con la cadena "Programación en Python".
"""


def procesar_texto(cadena):
    return {
        "minusculas": cadena.lower(),  # convierte a minúsculas
        "cantidad_o": cadena.count("o"),  # cuenta cuántas 'o' hay
        "termina_python": cadena.endswith("Python"),  # verifica si termina en "Python"
        "reemplazo": cadena.replace("Python", "Java"),  # reemplaza la palabra "Python" por "Java"
    }


print(f"Ejercicio 7: {procesar_texto("Programación en Python")}")

cadena_procesada = procesar_texto("Programación en Python")

print(cadena_procesada["minusculas"])
# Respuesta:

print(cadena_procesada["cantidad_o"])
# Respuesta:

print(cadena_procesada["termina_python"])
# Respuesta:

print(cadena_procesada["reemplazo"])
# Respuesta:


# ------------------------------------------------------------------------------------
# Ejercicio 8 (1 punto)
"""
Slicing en listas y cadenas

Dada una lista de letras de la 'a' a la 'i', devolvé los tres primeros elementos usando slicing.  
Dada la cadena "Universidad", devolvé "versi" usando slicing.
"""
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# Tu respuesta aquí
letras[ 0 : 3 ]
letras[  : 3 ]

cadena = "Universidad"
# Tu respuesta aquí:
cadena[3:8]

# ------------------------------------------------------------------------------------
# Ejercicio 9 (1 punto)
"""
Expresiones regulares (Regex)

Patentes argentinas formato 2016 en adelante: LL NNN LL
(2 letras, 3 dígitos, 2 letras, sin separadores).
Ejemplo: "AB629CZ"

Usando el módulo `re`, seleccioná la expresión regular que valida
correctamente este formato (solo una opción es correcta).
"""
import re

patente = "AB629CZ"

# a) r'^[A-Z]{2}\d{3}[A-Z]{2}'
# b) r'^[A-Z]{3}\d{2}[A-Z]{2}'
# c) r'^[A-Za-z]{2}[0-9]{4}[A-Za-z]{1}'
# d) r'^[A-Z]{2}\d{3}[A-Z]'

pattern = r"^[A-Z]{2}\d{3}[A-Z]$"
if re.match(pattern, patente):
    print(f"Ejercicio 9: coincide")
else:
    print("Ejercicio 9: No coincide")

# ------------------------------------------------------------------------------------
# Ejercicio 10 (1 punto)
"""
Construí una lista que contenga 3 diccionarios, cada uno con la información de un estudiante.  
Cada diccionario debe tener las claves:
- "legajo"
- "nombre"
- "apellido"

Usá los siguientes datos ficticios:

1) legajo: 101, nombre: Ana, apellido: López  
2) legajo: 102, nombre: Bruno, apellido: García  
3) legajo: 103, nombre: Carla, apellido: Fernández
"""

# Tu respuesta aquí:
# Lista de diccionarios
Ana = "Ana"
estudiantes = [
    {"legajo" : 101, "nombre": "Ana"},
    {},
    {}
]
