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
estudiantes_datos = [
    ["Thiago", "Almada", 19],
    ["Agostina", "Hein", 25],
    ["Leandro", "Bolmaro", 22],
    ["Valentina", "Raposo", 24],
]

def ordenar_arreglo(lista):
    return sorted(lista, key=lambda x: x[2])

print(f"Mi lista ordenada es:", ordenar_arreglo(estudiantes_datos))

# ---------------------------------------------------------------------
#  Ejercicio 2 - Invertir el orden
# ---------------------------------------------------------------------
"""
Generar una función complementaria, que además de ordenar, 
lo haga de forma ascendente o descendente, según indique el usuario 
"""

def ordenar_arreglo(lista, orden):
    if orden == 1:
        return sorted(lista, key=lambda x: x[2])
    else:
        return sorted(lista, key=lambda x: x[2], reverse=True)

print(f"Mi lista ordenada es:", ordenar_arreglo(estudiantes_datos,1))
print(f"Mi lista ordenada es:", ordenar_arreglo(estudiantes_datos,0))
