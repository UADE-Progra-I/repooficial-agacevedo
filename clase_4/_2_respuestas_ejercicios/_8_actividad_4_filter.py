# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Limpiar inscripciones: quedarse solo con e-mails válidos
# ---------------------------------------------------------------------
"""
A partir de una lista de emails, se solicita filtrar aquellos que tengan un formato válido,
y con ellos retornar una nueva lista.

Finalmente, se sugiere normalizar la lista resultante, de manera que no tengan espacios en blanco
y todos sus caracteres se encuentren en minúcula.

Criterio simple: es str, contiene @ y .

Clue: correr el siguiente 
nombre = "ana"
cell = 1156568585
print(f"Es nombre una instancia de str?: ", isinstance(nombre, str))
print(f"Es cell una instancia de str?: ", isinstance(cell, str))

"""
emails_registrados = ["  ana@uni.edu ", None, "sin-email", "luis@gmail.com", "  ", "sofia@dominio"]

emails_validos = list(filter(
    lambda email: isinstance(email, str) and "@" in email and "." in email and email.strip() != "",
    emails_registrados
))

# Normalizamos (trim + minúsculas) con map encadenado
emails_normalizados = list(map(lambda email: email.strip().lower(), emails_validos))

print(f"Emails normalizados: ", emails_normalizados)  # ['ana@uni.edu', 'luis@gmail.com']
