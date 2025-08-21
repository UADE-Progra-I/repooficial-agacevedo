# CADENAS DE CARACTERES
# Formato de cadenas

# Especificadores de conversión
legajo = 11212
nombre = "María"
nota = 10
print(
    "Legajo: %d, Nombre: %s, Nota: %d" % (legajo, nombre, nota)
)  # Legajo: 11212 Nombre: María Nota: 10

# Método format
legajo = 15035
nombre = "Carlos"
nota = 8
print(
    "Legajo: {}, Nombre: {}, Nota: {}".format(legajo, nombre, nota)
)  # Legajo: 15035 Nombre: Carlos Nota: 8

# F-Strings
legajo = 16489
nombre = "Luciana"
nota = 7
print(f"Legajo: {legajo}, Nombre: {nombre}, Nota: {nota}")  # Legajo: 16489 Nombre: Luciana Nota: 7
