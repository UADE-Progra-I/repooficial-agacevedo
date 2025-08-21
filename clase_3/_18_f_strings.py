# f_strings.py

print("F-Strings en Python")

# Insertar el valor de una variable
name = "Alice"
print(f'f"texto {{variable}}": Hello, {name}!')  # Resultado: 'Hello, Alice!'

# Insertar el resultado de una expresión
a = 5
b = 10
print(f'f"{{expresión}}": The sum is {a + b}')  # Resultado: 'The sum is 15'

# Formatear un número con dos decimales
price = 12.3456
print(f'f"{{variable:.2f}}": Price: {price:.2f}')  # Resultado: 'Price: 12.35'

# Alinear el texto a la derecha en un campo de ancho 10
name = "Bob"
print(f'f"{{variable:10}}": Name: {name:10}')  # Resultado: 'Name: Bob '

# Alinear el texto a la izquierda en un campo de ancho 10
print(f'f"{{variable:<10}}": Name: {name:<10}')  # Resultado: 'Name: Bob '

# Centrar el texto en un campo de ancho 10
print(f'f"{{variable:^10}}": Name: {name:^10}')  # Resultado: 'Name: Bob '

# Rellenar con ceros a la izquierda en un campo de ancho 10
number = 42
print(f'f"{{variable:010}}": Number: {number:010}')  # Resultado: 'Number: 0000000042'

# Usar comas como separadores de miles en números grandes
number = 1000000
print(f'f"{{variable:,}}": Number: {number:,}')  # Resultado: 'Number: 1,000,000'

# Formatear un número como porcentaje con dos decimales
percentage = 0.1234
print(f'f"{{variable:.2%}}": Percentage: {percentage:.2%}')  # Resultado: 'Percentage: 12.34%'

# Alinear el texto a la derecha en un campo de ancho 10, rellenando con espacios
text = "align"
print(f'f"{{variable:>10}}": Text: {text:>10}')  # Resultado: 'Text:      align'
