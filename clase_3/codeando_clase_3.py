# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


# print("\nLista iterada con range:")
# for indice in range(len(dias)):
#     print(f"Indice: {indice}: Item: {dias[indice]}")


# numeros = [0, 1, 2, 3, 4, 5]  # arreglo o iterable numeros
# cuadrados = []

# cuadrados = list()
# for num in numeros:
#     if num > 3:
#         cuadrados.append(num**2)
#     else:
#         cuadrados.append(num)

# print(cuadrados)

# numeros = [0, 1, 2, 3, 4, 5]  # arreglo o iterable numeros

# cuadrados_comp_1 = [num**2 for num in numeros]
# cuadrados_comp_2 = [num**2 for num in numeros if num > 3]
# cuadrados_comp_3 = [num**2 if num > 3 else num for num in numeros]
# cuadrados_comp_4 = [num**2 if num**2 > 20 else num for num in numeros]

# print(cuadrados_comp_1)
# print(cuadrados_comp_2)
# print(cuadrados_comp_3)
# print(cuadrados_comp_4)


# lst = [1, 2, 3]
# lst.append(4)
# lst.insert(2, 5) # posicion 2, insertar valor 5
# print(lst)


# estudiantes_datos = [
#     ["Thiago", "Almada"],
#     ["Agostina", "Hein"],
#     ["Leandro", "Bolmaro"],
#     ["Valentina", "Raposo"],
# ]
# for estudiante in estudiantes_datos:
#     inicial_buscar = estudiante[1][0]

#     if inicial_buscar.lower() == "r":
#         print("encontre a Raposo")


lista_1 = [1, 2]
lista_2 = [3, 4]

print(lista_1)
lista_1.append(5)
print(lista_1)
lista_1.append([5, 6])
print(lista_1)
lista_1.extend([7, 8])
print(lista_1)

lista_1 = [1, 2]
lista_2 = [3, 4]

lista_3 = lista_1
lista_4 = lista_1.copy()
print("lista_1", id(lista_1))
print("lista_2", id(lista_2))
print("lista_3", id(lista_3))
print("lista_4", id(lista_4))

num1, num2 = lista_1
print(num1)
print(lista_1[0])
