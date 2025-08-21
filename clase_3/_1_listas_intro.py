# ***********************************************************
# Parte 1: Listas estáticas
# ***********************************************************

# lista vacia
listaVacia = []  # También puede usarse list()
lista = list()

# lista estatica con números
listaNumeros1 = [1, 2, 3, 4]
listaNumeros2 = list(range(4))  # longitud 4 / por default: inicia en 1, saltos de 1
listaNumeros3 = list(range(2, 8, 3))  # longitud 8, inicia en 2, saltos de 3
print("listaNumeros1", listaNumeros1)
print("listaNumeros2", listaNumeros2)
print("listaNumeros3", listaNumeros3)

input("\nPresione para continuar...")

# lista estatica con cadenas de caracteres
listaTexto = ["Hola", "Mundo", "!"]

# lista con elementos de diferente tipo
listaDistintosTipos = ["A", True, 123, 123.12]

# lista de listas (ya lo vimos con matrices)
listaDeListas = [[1, 2, 3], [4, 5, 6]]

# uso de índices dentro de una lista
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
print("dias[0]", dias[0])  # Lunes
print("dias[1]", dias[1])  # Martes
print("dias[-1]", dias[-1])  # Viernes
print("dias[-3]", dias[-3])  # Miercoles


# ***********************************************************
# Parte 2: Listas dinámicas
# ***********************************************************

# usamos range para crear una lista
indices = list(range(len(dias)))
print(indices)

input("\nPresione para continuar...")

# usamos los datos de consola para inicializar una lista
lista_personalizada = []
indice = 0
print("Ingrese los elementos para inicializar la lista:")
while True:
    item = input(f"Itema {indice}: ")
    lista_personalizada.append(item)
    continua = input("Presion z para salir o cualquier tecla para continuar: ").strip().lower()
    if continua == "z":
        break
print("lista resultante: ", lista_personalizada)


# ***********************************************************
# Parte 3: Iterar listas
# ***********************************************************

# Iteramos una lista con for in
print("\nLista iterada con for in:")
for item in dias:
    print(item)

input("\nPresione para continuar...")

# Iteramos una lista con range
print("\nLista iterada con range:")
for indice in range(len(dias)):
    print(f"Indice: {indice}: Item: {dias[indice]}")

input("\nPresione para continuar...")

# Enumerate retorna una tupla formada por indice + item
print("\nLista iterada con enumerate:")
for indice, item in enumerate(dias):
    print(f"Indice: {indice}: Item: {item}")
