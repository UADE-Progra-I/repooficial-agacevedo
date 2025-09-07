# Dada una lista de int, la podemos ordenar con el método sort()
lista = [1, 3, 4, 6]
lista.sort()
print(lista)

# Dada una lista de listas, como estudiantes_datos, podremos ordenarla con sort()
estudiantes_datos = [
    ["Thiago", "Almada", 19],
    ["Agostina", "Hein", 25],
    ["Leandro", "Bolmaro", 22],
    ["Valentina", "Raposo", 24],
]

# estudiantes_datos.sort()
# print(estudiantes_datos)

# Y como hacemos para ordenarla por edad?
estudiantes_datos_ordenados = sorted(estudiantes_datos, key=lambda x: x[0], reverse=True)
print(estudiantes_datos_ordenados)
