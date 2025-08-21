# CADENAS DE CARACTERES
# Métodos para verificar contenido

# CADENAS DE CARACTERES
# Métodos para verificar contenido

print("=== Métodos para verificar contenido ===")

cadena = "Python3"
print("\nMétodo isalnum() - ¿Es alfanumérico?")
print(cadena, "→", cadena.isalnum())

cadena = "+++"
print(cadena, "→", cadena.isalnum())

cadena = "Python"
print("\nMétodo isalpha() - ¿Solo tiene letras?")
print(cadena, "→", cadena.isalpha())

cadena = "1234"
print(cadena, "→", cadena.isalpha())

cadena = "12345"
print("\nMétodo isnumeric() - ¿Solo tiene números?")
print(cadena, "→", cadena.isnumeric())

cadena = "Hola32"
print(cadena, "→", cadena.isnumeric())

cadena = "   "
print("\nMétodo isspace() - ¿Solo tiene espacios en blanco?")
print(cadena, "→", cadena.isspace())

cadena = "  _  "
print(cadena, "→", cadena.isspace())

cadena = "12345"
print("\nMétodo isdigit() - ¿Solo tiene dígitos?")
print(cadena, "→", cadena.isdigit())

cadena = "-12345"
print(cadena, "→", cadena.isdigit())

cadena = "12345"
print("\nMétodo isdecimal() - ¿Solo tiene caracteres decimales?")
print(cadena, "→", cadena.isdecimal())

cadena = "123.45"
print(cadena, "→", cadena.isdecimal())

print("\nMétodo islower() - ¿Está toda en minúsculas?")
cadena = "python"
print(cadena, "→", cadena.islower())

cadena = "Python"
print(cadena, "→", cadena.islower())

print("\nMétodo isupper() - ¿Está toda en mayúsculas?")
cadena = "PYTHON"
print(cadena, "→", cadena.isupper())

cadena = "Python"
print(cadena, "→", cadena.isupper())

print("\nMétodo istitle() - ¿Cada palabra empieza con mayúscula?")
cadena = "Python Es Interesante"
print(cadena, "→", cadena.istitle())

cadena = "Python es interesante"
print(cadena, "→", cadena.istitle())
