# ******************************************
# Actividad 1
# Listas y Metodos
# ******************************************

"""
Sugerencia:
dentro de la carpeta "codigo_estudiantes" crear un archivo python,
copiar y pegar alli estas consignas y trabajar en ese archivo
"""

# Datos para comenzar
estudiantes_header = ["id_estudiante", "nombre", "apellido", "email"]

estudiantes_datos = [
    ["Thiago", "Almada"],
    ["Agostina", "Hein"],
    ["Leandro", "Bolmaro"],
    ["Valentina", "Raposo"],
]

emails = [
    e[0][0].lower() + e[1].lower() + "gmail.com".lower() for e in estudiantes_datos
]
for _ in emails:
    print(f"mail = {_}")


# 1
# Agregar emails ficticios usando append()
# Ejemplo: para Thiago Almada → [1, "Thiago", "Almada", "talmada@mail.com"].
print("### Actividad 1 ### Agrego mails faltnates en la lista usando append()")
for enum, a in enumerate(estudiantes_datos):
    a.append(emails[enum])


# 2
# Agregar los ids faltantes usando insert()
print("### Actividad 2 ### Agrego ids faltnates en la lista usando insert()")
for count, a in enumerate(estudiantes_datos):
    a.insert(0, count)


# 3
# Agregar un nuevo estudiante al final con append()
# Hacer que el apellido de este estudiante se repita
# Ejemplo: [5, "Diego", "Almada", "dalmada@gmail.com"]

estudiantes_datos.append([5, "Diego", "Almada", "dalmada@gmail.com"])
print("### Actividad 3 ### Agrego a: ", [5, "Diego", "Almada", "dalmada@gmail.com"])

estudiantes_datos_copia = estudiantes_datos.copy()

# 4
# Eliminar un estudiante por apellido usando remove()
delete_surname = "Hein"

for _ in estudiantes_datos:
    if _[2] == delete_surname:
        estudiantes_datos.remove(_)
        print(f"### Actividad 4 ### Borre a {delete_surname}: {_}")


# 5
# Quitar el último estudiante usando pop() y mostrar qué estudiante fue eliminado.

student_delete = estudiantes_datos.pop(-1)
print("### Actividad 5### Borro ultimo estudiante:", student_delete)

# 6
# Buscar la posición (índice) de un apellido con index().
search_surname = "Raposo"
for _ in estudiantes_datos:
    if _[2] == search_surname:
        almada_data = _

        Almada_index = estudiantes_datos.index(almada_data)
        print(f"### Actividad 6 ### Indice de {search_surname}: {Almada_index}")

# 7
# Contar cuántos estudiantes tienen el mismo apellido con count() (simular apellidos repetidos agregando uno igual).
# Clue 1: generar una lista solo con apellidos
# Clue 2: investigar como implementarlo con listas por comprension


# 8
# Ordenar alfabéticamente los estudiantes por nombre
# Clue 1: Pueden usar sort pero deben combinarlo con funcion lambda
# Clue 2: Pueden usar el método "Bubble Sort"

# NOTA:
# Si usan IA, debe ser con "pensamiento crítico"

for _ in estudiantes_datos:
    print(_)
