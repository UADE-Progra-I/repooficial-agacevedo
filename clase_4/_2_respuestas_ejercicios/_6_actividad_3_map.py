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

celsius = [0, 12, 20, 25, 30]

farenheit = list(map(lambda temp: round((temp * 9 / 5) + 32), celsius))
print(f"Las temperaturas a F son: ", farenheit)

# ---------------------------------------------------------------------
#  Ejercicio 2 - Promedio ponderado de notas
# ---------------------------------------------------------------------
"""
Dados dos listados paralelos con notas de parcial y final, 
calculá el promedio ponderado 0.4*parcial + 0.6*final para cada alumno. 
Redondeá a 1 decimal.
"""

parciales = [5, 7, 4, 9]
finales = [6, 8, 10, 7]

promedio = list(map(lambda n_parcial, n_final: round(0.4 * n_parcial + 0.6 * n_final, 1), parciales, finales))
print(promedio)

# ---------------------------------------------------------------------
#  Ejercicio 3 - Normalizar los nombres y apellidos de los estudiantes
# ---------------------------------------------------------------------
"""
Se solicita normalizar los nombre y apellidos de los estudiantes, de manera
que todos sus caracteres sean en minúscula, salvo la primer letra.
"""

nombres   = [" ana  ", "LUIS", "  sOfía "]
apellidos = [" pérez", "GÓMEZ  ", "lópez"]

nombres_normalizados = list(map(lambda nombre : nombre.strip().title(), nombres))
apellidos_normalizados = list(map(lambda apellido: apellido.strip().title(), apellidos))

print(nombres_normalizados)
print(apellidos_normalizados)