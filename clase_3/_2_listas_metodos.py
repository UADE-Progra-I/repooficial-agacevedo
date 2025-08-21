# ***********************************************************
# Parte 1: Métodos
# ***********************************************************

print("Listas Avanzadas")

# append() → agrega un solo elemento al final de la lista
lst = [1, 2, 3]
lst.append(4)
print(f"append(): {lst}")  # Resultado: [1, 2, 3, 4]

# extend() → agrega varios elementos de otra lista al final
lst = [1, 2]
lst.extend([3, 4])
print(f"extend(): {lst}")  # Resultado: [1, 2, 3, 4]

# insert() → inserta un elemento en una posición específica (índice)
lst = [1, 2, 3]
lst.insert(1, 1.5)  # en la posición 1 (segunda) agrega 1.5
print(f"insert(): {lst}")  # Resultado: [1, 1.5, 2, 3]

# remove() → elimina la primera ocurrencia de un valor específico
lst = [1, 2, 2, 3]
lst.remove(2)  # elimina el primer "2" que encuentra
print(f"remove(): {lst}")  # Resultado: [1, 2, 3]

# pop() → elimina y devuelve el último elemento (o el índice indicado)
lst = [1, 2, 3]
popped_element = lst.pop()  # saca el último elemento
print(f"pop(): (Elemento: {popped_element}, Lista: {lst})")  # Resultado: (3, [1, 2])

# index() → devuelve la posición (índice) de la primera aparición de un valor
lst = [1, 2, 3]
index_of_element = lst.index(2)  # busca el índice del "2"
print(f"index(): {index_of_element}")  # Resultado: 1

# count() → cuenta cuántas veces aparece un valor en la lista
lst = [1, 2, 2, 3]
count_of_element = lst.count(2)  # cuenta los "2"
print(f"count(): {count_of_element}")  # Resultado: 2

# sort() → ordena la lista en orden ascendente (modifica la lista original)
lst = [3, 1, 2]
lst.sort()
print(f"sort(): {lst}")  # Resultado: [1, 2, 3]

# reverse() → invierte el orden de los elementos en la lista
lst = [1, 2, 3]
lst.reverse()
print(f"reverse(): {lst}")  # Resultado: [3, 2, 1]


# ***********************************************************
# Parte 2: Funciones
# ***********************************************************

# len()
print(f"len([1, 2, 3]): {len([1, 2, 3])}")  # Resultado: 3

# sum()
print(f"sum([1, 2, 3]): {sum([1, 2, 3])}")  # Resultado: 6

# min()
print(f"min([1, 2, 3]): {min([1, 2, 3])}")  # Resultado: 1

# max()
print(f"max([1, 2, 3]): {max([1, 2, 3])}")  # Resultado: 3

# list()
print(f"list((1, 2, 3)): {list((1, 2, 3))}")  # Resultado: [1, 2, 3]


# ***********************************************************
# Parte 3: Acceso y Operaciones
# ***********************************************************

print("\nAcceso y Operaciones")

# Acceso por índice
lst = [1, 2, 3]
print(f"lst[1]: {lst[1]}")  # Resultado: 2

# Slicing
lst = [1, 2, 3, 4]
print(f"lst[1:3]: {lst[1:3]}")  # Resultado: [2, 3]

# Concatenación de listas
lst1 = [1, 2]
lst2 = [3, 4]
print(f"lst1 + lst2: {lst1 + lst2}")  # Resultado: [1, 2, 3, 4]

# Copia de lista
lst = [1, 2]
lst_copy = lst.copy()
print(f"lst.copy(): {lst_copy}")  # Resultado: [1, 2]

# Desempaquetado
a, b, c = [1, 2, 3]
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}")  # Resultado: a = 1, b = 2, c = 3

print("\nFunciones Comunes")
