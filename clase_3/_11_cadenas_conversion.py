# CADENAS DE CARACTERES
# Conversión
# - de cadenas de caracteres a lista
# - de cadenas de caracteres a tupla
# - de lista o tupla a cadena de caracteres

print("split y rsplit:")
# cadena.split(separador, maxsplit), cadena.rsplit(separador, maxsplit)
cadena = "uno,dos,tres,cuatro,cinco"
lista_split = cadena.split(",")
print("split:", lista_split)  # ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista_split2 = cadena.split(",", 2)
print("split:", lista_split2)  # ['uno', 'dos', 'tres,cuatro,cinco']
lista_rsplit = cadena.rsplit(",", 2)
print("rsplit:", lista_rsplit)  # ['uno,dos,tres', 'cuatro', 'cinco']

print("\nsplitlines:")
# cadena.splitlines(keeplinebreaks)
cadena_multilinea = "Hola mundo\nEsto es una prueba\nCon varias líneas"
lista_splitlines = cadena_multilinea.splitlines()
print("splitlines:", lista_splitlines)  # ['Hola mundo', 'Esto es una prueba', 'Con varias líneas']

# cadena.partition(separador), cadena.rpartition(separador)
print("\npartition y rpartition:")
cadena = "manzana pera manzana uva manzana"
tupla_partition = cadena.partition("manzana")
print("partition:", tupla_partition)  # partition: ('', 'manzana', ' pera manzana uva manzana')
tupla_rpartition = cadena.rpartition("manzana")
print("rpartition:", tupla_rpartition)  # rpartition: ('manzana pera manzana uva ', 'manzana', '')

# separador.join(iterable)
print("\njoin:")
palabras = ["Hola", "mundo", "esto", "es", "un", "ejemplo"]
resultado = " ".join(palabras)
print(resultado)  #    "Hola mundo esto es un ejemplo"
