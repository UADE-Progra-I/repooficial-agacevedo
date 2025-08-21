# CADENAS DE CARACTERES
# Métodos de búsqueda

print("=== Métodos de búsqueda ===")

# Método find() y rfind()
print("\nMétodos find() y rfind() - Posición de la subcadena dentro de la cadena")

cadena = "Hola, mundo"
print("Cadena:", cadena)
indice = cadena.find("mundo")
print("find('mundo') →", indice)  # 6

cadena = "Hola, mundo, mundo"
print("\nCadena:", cadena)
indice = cadena.rfind("mundo")
print("rfind('mundo') →", indice)  # 13

# Método startswith() y endswith()
print("\nMétodos startswith() y endswith() - Verifica si comienza o termina con una subcadena")

cadena = "Hola, mundo"
print("Cadena:", cadena)
resultado = cadena.startswith("Hola")
print("startswith('Hola') →", resultado)  # True

resultado = cadena.endswith("mundo")
print("endswith('mundo') →", resultado)  # True
