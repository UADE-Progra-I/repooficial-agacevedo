import random

# Creamos una matriz estatica de 2 filas por 2 columnas
matriz_estatica = [[1, 2], [3, 4]]


print("\nMostramos la matriz estatica de 2x2")
for fila in matriz_estatica:
    print(fila)  # imprimimos la matriz completa


# Mostramos la primera fila
print("\nMostramos la primera fila")
print(matriz_estatica[0])  # imprimimos la primera fila


# Mostramos el valor de la primera fila y primera columna
print("\nMostramos el valor de la primera fila y primera columna")
print(matriz_estatica[1][0])  # imprimimos el primer elemento de la segunda fila


# Generamos una matriz nula de 3 filas por 3 columnas
matriz_nula = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("\nMostramos la matriz nula de 3x3")
for fila in matriz_nula:
    print(fila)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Alternativa 1 para crear matrices dinámicas
filas = 3
columnas = 4
matriz3x4 = []  # Creamos una lista vacía
for fil in range(filas):
    matriz3x4.append([])  # Agregamos una nueva fila
    for col in range(columnas):
        matriz3x4[fil].append(0)  # Agregamos un nuevo elemento a la fila
print("\nMetodo 1:")
print(matriz3x4)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Alternativa 2 para crear matrices dinámicas
filas = 3
columnas = 4
matriz3x4 = []  # Creamos una lista vacía
for fil in range(filas):
    matriz3x4.append([0] * columnas)  # Agregamos una nueva fila
print("\nMetodo 2:")
print(matriz3x4)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Alternativa 3 para crear matrices dinámicas
filas = 3
columnas = 4
matriz3x4porComp = [[0] * columnas for fil in range(filas)]
print("\nMetodo 3:")
print(matriz3x4porComp)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Alternativa 4 para crear matrices dinámicas con numeron random
filas = 3
columnas = 4
matriz3x4porComp = [[random.randint(1, 10)] * columnas for fil in range(filas)]
print("\nMetodo 4:")
print(matriz3x4porComp)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# jugando en clase
filas = 3
columnas = 4
matrizTest = []
for fila in range(filas):  # for fil in range(filas)
    matrizTest.append([])
    for columna in range(columnas):
        matrizTest[fila].append(columna)  # [0] * columnas

# print claro
print("*" * 10)
for fila in matrizTest:
    print(fila)
