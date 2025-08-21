# CADENAS DE CARACTERES
# Manipulación

# str()
print("str():")
mensaje = "El resultado es: "
numero = 42
resultado = mensaje + str(numero)
print(resultado)  # El resultado es: 42
print()

# cadena.capitalize(), cadena.title(), cadena.lower(), cadena.upper(), cadena.swapcase()
texto = "hOLA, mUnDo. eSTO eS uN eJeMpLo."
texto_capitalize = texto.capitalize()
print("capitalize:", texto_capitalize)  # capitalize: Hola, mundo. esto es un ejemplo.
texto_title = texto.title()
print("title:", texto_title)  # title: Hola, Mundo. Esto Es Un Ejemplo.
texto_lower = texto.lower()
print("lower:", texto_lower)  # lower: hola, mundo. esto es un ejemplo.
texto_upper = texto.upper()
print("upper:", texto_upper)  # upper: HOLA, MUNDO. ESTO ES UN EJEMPLO.
texto_swapcase = texto.swapcase()
print("swapcase:", texto_swapcase)  # swapcase: Hola, MuNdO. Esto Es Un EjEmPlO.
