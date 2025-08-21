# LISTAS
# Slicing

numeros = [2, 34, 25, 1, 19, 23, 48, 19, 38, 9]

# Extraer una subsección de la lista
print("Extraer una subsección de la lista:")
print(numeros[2:5])  # [25, 1, 19]

# Omitir 'inicio' o 'fin'
print("Omitir 'inicio' o 'fin':")
print(numeros[:4])  # [2, 34, 25, 1]
print(numeros[5:])  # [23, 48, 19, 38, 9]

# Superar índice
print("Superar índice:")
print(numeros[1:100])  # [34, 25, 1, 19, 23, 48, 19, 38, 9]

# Índices Negativos
print("Índices Negativos:")
print(numeros[-5:-2])  # [23, 48, 19]

# Incremento e incremento negativo
print("Incremento e incremento negativo:")
print(numeros[2:7:2])  # [25, 19, 48]
print(numeros[7:1:-2])  # [19, 23, 1]

# Invertir una lista
print("Invertir una lista:")
print(numeros[::-1])  # [9, 38, 19, 48, 23, 19, 1, 25, 34, 2]

# Reemplazar elementos
print("Reemplazar elementos:")
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [80, 85]
print(lista)  # [19, 23, 80, 85, 38, 9]

# Eliminar elementos
print("Eliminar elementos:")
lista[2:4] = []
print(lista)  # [19, 23, 38, 9]

# Reemplazar e insertar elementos
print("Reemplazar e insertar elementos:")
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [80, 85, 101]
print(lista)  # [19, 23, 80, 85, 101, 38, 9]
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [99]
print(lista)  # [19, 23, 99, 38, 9]

# Rebanadas nulas – insertar elementos
print("Rebanadas nulas - insertar elementos:")
lista = [19, 23, 48, 19, 38, 9]
lista[2:2] = [110, 115, 118]
print(lista)  # [19, 23, 110, 115, 118, 48, 19, 38, 9]

# Rebanadas para realizar copias
print("Rebanadas para realizar copias:")
listaOriginal = [2, 34, 25]
listaCopia = listaOriginal[:]
listaCopia.append(18)
print(listaOriginal)  # [2, 34, 25]
print(listaCopia)  # [2, 34, 25, 18]

# Recorrer parcialmente una lista utilizando rebanadas
print("Recorrer parcialmente una lista utilizando rebanadas:")
lista = [19, 23, 48, 19, 38, 9]
for i in lista:
    print(i, end=" ")  # 19 23 48 19 38 9
print()
for i in lista[2:5]:
    print(i, end=" ")  # 48 19 38
print()

"""
# ¿Cuál es la salida?
lista = [19, 23, 48, 19, 38, 9]
for i in lista[::2]:
    print(i, end=" ")
print()
"""


# Desafío
def partirLista(lista):
    # .....
    mitad = int(len(lista) / 2)
    listaPrimeraParte = lista[:mitad]
    listaSegundaParte = lista[mitad:]
    return listaPrimeraParte, listaSegundaParte
