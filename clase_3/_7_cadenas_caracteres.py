# cadenas_de_caracteres.py

print("Cadenas de Caracteres")

# Acceso y Operaciones Básicas

# Acceso por índice
s = "hello"
print(f"str[1]: {s[1]}")  # Resultado: 'e'

# Slicing
print(f"str[1:4]: {s[1:4]}")  # Resultado: 'ell'

# Concatenación
s1 = "hello"
s2 = "world"
print(f"str + str2: {s1 + s2}")  # Resultado: 'helloworld'

# Repetición
print(f"str * 2: {s1 * 2}")  # Resultado: 'hellohello'

# Longitud
print(f"len(str): {len(s)}")  # Resultado: 5

# Métodos de Cadenas

# upper()
print(f"str.upper(): {s.upper()}")  # Resultado: 'HELLO'

# lower()
s = "HELLO"
print(f"str.lower(): {s.lower()}")  # Resultado: 'hello'

# strip()
s = " hello "
print(f"str.strip(): '{s.strip()}'")  # Resultado: 'hello'

# replace()
s = "hello"
print(f"str.replace('e', 'a'): {s.replace('e', 'a')}")  # Resultado: 'hallo'

# find()
print(f"str.find('e'): {s.find('e')}")  # Resultado: 1

# split()
s = "hello world"
print(f"str.split(): {s.split()}")  # Resultado: ['hello', 'world']

# join()
lst = ["hello", "world"]
print(f"str.join(lst): {' '.join(lst)}")  # Resultado: 'hello world'

print("\nOtros Comandos")

# lstrip()
print(f"cadena.lstrip(): '{' hola '.lstrip()}'")  # Resultado: 'hola '

# rstrip()
print(f"cadena.rstrip(): '{' hola '.rstrip()}'")  # Resultado: ' hola'

# center()
print(f"cadena.center(10, '-'): '{'hola'.center(10, '-')}'")  # Resultado: '---hola----'

# ljust()
print(f"cadena.ljust(10, '-'): '{'hola'.ljust(10, '-')}'")  # Resultado: 'hola------'

# rjust()
print(f"cadena.rjust(10, '-'): '{'hola'.rjust(10, '-')}'")  # Resultado: '------hola'

# zfill()
print(f"cadena.zfill(5): '{'42'.zfill(5)}'")  # Resultado: '00042'

# isalnum()
print(f"cadena.isalnum(): {('hola123'.isalnum())}")  # Resultado: True

# isalpha()
print(f"cadena.isalpha(): {('hola'.isalpha())}")  # Resultado: True

# isnumeric()
print(f"cadena.isnumeric(): {('123'.isnumeric())}")  # Resultado: True

# isspace()
print(f"cadena.isspace(): {(' '.isspace())}")  # Resultado: True

# isdigit()
print(f"cadena.isdigit(): {('123'.isdigit())}")  # Resultado: True

# isdecimal()
print(f"cadena.isdecimal(): {('123'.isdecimal())}")  # Resultado: True

# join()
print(
    f"separador.join(iterable): {', '.join(['manzana', 'banana', 'cereza'])}"
)  # Resultado: 'manzana, banana, cereza'

# Operador in / not in
print(f"'hola' in 'hola mundo': {'hola' in 'hola mundo'}")  # Resultado: True
print(f"'adiós' not in 'hola mundo': {'adiós' not in 'hola mundo'}")  # Resultado: True
