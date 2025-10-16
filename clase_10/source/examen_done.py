"""
--------------------------------------------------------------------------------------
Ejercicio 2 / 3
Se solicita calcular el producto de una matriz de n * m dimensiones por un escalar.
Analizar el código de la siguiente función ejercicio_2 y en caso de ser necesario,
refactoriza para que cumpla con la consigna

Arma además su test asociado.

Validar con
M = [[1, 2], [4, 5]]
A = 2
"""


# def ejercicio_2(matriz, escalar):
#     nFilas = len(matriz)
#     nColumnas = len(matriz[0])
#     resultado = [[0]*nColumnas for _ in range(nFilas)]
#     for i in range(nFilas):
#         for j in range(nColumnas):
#             resultado[i][j] = matriz[i][j] * escalar
#     return resultado

def ejercicio_2(matriz, escalar):
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    resultado = []
    for i in range(nFilas):
        columnas = []
        for j in range(nColumnas):
            columnas.append(matriz[i][j] * escalar)
        resultado.append(columnas)
    return resultado


"""
--------------------------------------------------------------------------------------
Ejercicio 4:
¿Cuál de las siguientes expresiones en Python
genera una lista con los cuadrados de los números del 1 al 5 utilizando lista por comprensión?

# a) [x * x for x in range(1, 6)]
# b) [x ** 2 for x in range(6)]
# c) [x ^ 2 for x in range(1, 6)]
# d) [x ** 2 for x in (1, 2, 3, 4)]

Arma la función y su test asociado
"""


def ejercicio_4():
    return [x * x for x in range(1, 6)]


"""
--------------------------------------------------------------------------------------
Ejercicio 5:
Usando filter y lambda, escribi el código necesario para obtener una nueva lista 
que contenga únicamente los números positivos de la siguiente lista:

numeros = [3, -1, 0, 7, -5, 10, -2]

Arma la función y su test asociado
"""


def ejercicio_5():
    numeros = [3, -1, 0, 7, -5, 10, -2]
    positivos = list(filter(lambda x: x > 0, numeros))
    return positivos


"""
--------------------------------------------------------------------------------------
Ejercicio 6:
Método de listas

Dada la lista numeros = [10, 3, 7, 2, 15], aplicá los métodos de lista necesarios para:
1. Agregar el número 20 al final.
2. Insertar el número 5 en la posición 2.
3. Eliminar el número 7.
4. Ordenar la lista de menor a mayor.

Arma la función y su test asociado
"""


def ejercicio_6():
    numeros = [10, 3, 7, 2, 15]
    numeros.append(20)
    numeros.insert(2, 5)
    numeros.remove(7)
    numeros.sort()
    return numeros


"""
--------------------------------------------------------------------------------------
Ejercicio 7:
Dada la siguiente función ejercicio_7(cadena), 
arma la función de testing y valida con
cadena = "Programación con Python"
"""

def ejercicio_7(cadena):
    return {
        "minusculas": cadena.lower(),  # convierte a minúsculas
        "cantidad_o": cadena.count("o"),  # cuenta cuántas 'o' hay
        "termina_python": cadena.endswith("Python"),  # verifica si termina en "Python"
        "reemplazo": cadena.replace("Python", "Java"),  # reemplaza la palabra "Python" por "Java"
    }


"""
--------------------------------------------------------------------------------------
Ejercicio 8:
Slicing en listas y cadenas

Dadas las siguientes variables
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
cadena = "Universidad"

desrrollá la función ejercicio_8(letras, cadena)

que retorna una tupla con:
1. slicing de los 3 primeros elementos de letra
2. slicing de cadena con "versi" 

Generá también su test asociado
"""


def ejercicio_8(letras, cadena):
    return letras[:3], cadena[3:8]


"""
--------------------------------------------------------------------------------------
Ejercicio 9:
Expresiones regulares (Regex)

Patentes argentinas formato 2016 en adelante: LL NNN LL
(2 letras, 3 dígitos, 2 letras, sin separadores).
Ejemplo: "AB629CZ"

Usando el módulo `re` y la expresión
re.match(pattern, patente)

desarrollá la función ejercicio_9(patente)
que recibe la patente que se quiere validar.

probar pattern con las siguientes expresiones regulares

# a) r'^[A-Z]{2}\d{3}[A-Z]{2}$'
# b) r'^[A-Z]{3}\d{2}[A-Z]{2}$'
# c) r'^[A-Za-z]{2}[0-9]{4}[A-Za-z]{1}$'
# d) r'^[A-Z]{2}\d{3}[A-Z]$'s

patente = "AB629CZ"
"""

import re


def ejercicio_9(patente):
    pattern = r"^[A-Z]{2}\d{3}[A-Z]{2}$"
    return bool(re.match(pattern, patente))


"""
--------------------------------------------------------------------------------------
Ejercicio 10
Diccionarios

Desarrolla la función ejercicio_10(), 
de manera que al invocarla, retorne una lista que contenga 3 diccionarios, 
cada uno con la información de un estudiante.  

- "legajo"
- "nombre"
- "apellido"

Usá los siguientes datos ficticios:

1) legajo: 101, nombre: Ana, apellido: López  
2) legajo: 102, nombre: Bruno, apellido: García  
3) legajo: 103, nombre: Carla, apellido: Fernández

Generá además su correspondiente test asociado
"""


def ejercicio_10():
    return [
        {"legajo": 101, "nombre": "Ana", "apellido": "López"},
        {"legajo": 102, "nombre": "Bruno", "apellido": "García"},
        {"legajo": 103, "nombre": "Carla", "apellido": "Fernández"},
    ]
