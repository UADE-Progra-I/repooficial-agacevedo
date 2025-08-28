# Dada una lista de calificaciones, queremos obtener solo aquellos valores
# que sean mayores o iguales a 7

calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75]
calificaciones_filtradas = list(filter(lambda x: x>=7 , calificaciones))
print(f"Listado de calificaciones mayores o iguales a 7: ", calificaciones_filtradas)


# Dada una lista de listas, como estudiantes_datos, filtrar aquellos estudiantes
# con calificación mayor o iguala a 7 

estudiantes_datos = [
    ["Thiago", "Almada", 19, 8],
    ["Agostina", "Hein", 25, 7],
    ["Leandro", "Bolmaro", 22, 6.5],
    ["Valentina", "Raposo", 24, 8.5],
]

estudiantes_aprobados = list(filter(lambda estudiante: estudiante[3]>=7 , estudiantes_datos))
print(f"Listado de estudiantes aprobados: ", estudiantes_aprobados)