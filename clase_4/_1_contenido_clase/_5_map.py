# Usamos la función Map

# Dada una lista con las calificaciones de los estudiantes,
# se requiere redondear sus notas.

calificaciones = [8, 8.5, 9, 9.75]
# calificaciones_rounded = round(calificaciones) <<< ERROR

# Usamos un método tradicional
calificaciones_rounded = []
for calificacion in calificaciones:
    calificaciones_rounded.append(round(calificacion))

print(calificaciones_rounded)

# Usamos map
# map (funcion, iterable)
calificaciones_rounded = list(map(lambda x:round(x), calificaciones))
print(calificaciones_rounded)