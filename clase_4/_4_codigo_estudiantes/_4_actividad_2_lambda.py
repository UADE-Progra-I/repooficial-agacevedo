# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  Ejercicio 1 - Ordenar una lista de listas
# ---------------------------------------------------------------------
"""
Declarar una lista de listas con una matriz de tu proyecto.
Luego generar una función que retorne la lista ordenada por alguna variable numérica.

Clue: usar función sorted combinada con lambda para ordenar ese arreglo
"""

# Lista de datos (matriz de alumnos)
estudiantes = [
    [1, "Thiago", "Almada", 19],
    [2, "Agostina", "Hein", 25],
    [3, "Leandro", "Bolmaro", 22],
    [4, "Valentina", "Raposo", 24],
]

estudiantes_ordenado = sorted(estudiantes, key=lambda x: x[2])
# print(estudiantes_ordenado)


# ---------------------------------------------------------------------
#  Ejercicio 2 - Invertir el orden
# ---------------------------------------------------------------------
"""
Generar una función complementaria, que además de ordenar, 
lo haga de forma ascendente o descendente, según indique el usuario 
"""


def ordenado(lista, asc):
    if asc:
        return sorted(lista, key=lambda x: x[2], reverse=True)
    else:
        return sorted(lista, key=lambda x: x[2])


variable = int(
    input(
        "Ingrese si quiere ordenar de forma ascendente o descendente:\n[1] Ascendente\n[2] Descendente\n"
    )
)
if variable == 1:
    asc = True
else:
    asc = False

print(ordenado(estudiantes, asc))
