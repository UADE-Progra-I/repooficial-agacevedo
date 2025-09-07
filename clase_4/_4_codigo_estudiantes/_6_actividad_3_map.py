# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Convertir temperaturas
# ---------------------------------------------------------------------
"""
Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""

temperatures = [100, 72, 41, 32, 67, 80, 0, 96]

temperatures_farenheit = list(map(lambda c: round(c * 9 / 5 + 32, 1), temperatures))
print(temperatures_farenheit)

# ---------------------------------------------------------------------
#  Ejercicio 2 - Promedio ponderado de notas
# ---------------------------------------------------------------------
"""
Dados dos listados paralelos con notas de parcial y final, 
calculá el promedio ponderado 0.4*parcial + 0.6*final para cada alumno. 
Redondeá a 1 decimal.
"""

notas_parcial = [7, 9, 2, 3, 5]
notas_final = [3, 6, 7, 3, 10]

notas_promedio = list(
    map(lambda x, y: round(0.4 * int(x) + 0.6 * int(y), 1), notas_parcial, notas_final)
)
print(notas_promedio)

# ---------------------------------------------------------------------
#  Ejercicio 3 - Normalizar los nombres y apellidos de los estudiantes
# ---------------------------------------------------------------------
"""
Se solicita normalizar los nombre y apellidos de los estudiantes, de manera
que todos sus caracteres sean en minúscula, salvo la primer letra.
"""

# Lista de datos (matriz de alumnos)
estudiantes = [
    [1, "Thiago", "Almada", 19],
    [2, "Agostina", "Hein", 25],
    [3, "Leandro", "Bolmaro", 22],
    [4, "Valentina", "Raposo", 24],
]

nombres_normalizados = list(
    map(
        lambda a: str(a[1][0]).upper()
        + str(a[1][1:]).lower()
        + " "
        + str(a[2][0]).upper()
        + str(a[2][1:]).lower(),
        estudiantes,
    )
)
print(nombres_normalizados)
