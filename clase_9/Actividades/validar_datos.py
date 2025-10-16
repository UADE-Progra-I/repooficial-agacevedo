# --------------------------------------------------------
# Actividad manejo de excepciones
# --------------------------------------------------------
"""
La función validar, recibe dos argumentos:
1. campo: indica el dato que se quiere validar, "Nombre", "Edad", etc.
2. valor: el valor correspondiente a ese dato

Analizar:
1. Qué sucede si al invocar la función validar, recibe como argumento, un campo que la función no conocer?
2. Cómo se podría mejorar?
3. Cómo se podrían generar (raise) exceptions y como manejarlas desde la función que las invoca para no interrumpir el flujo del programa?
"""


# Importar librerías
import re

def main():
    campo = "Name"
    valor = "JUan"

    print(validar(campo, valor))

# Función de validación   
def validar(campo, valor): # Valida un valor según el tipo de campo.
    
    if campo == "Nombre":
        if valor is None or valor.strip() == "":
            return False
        if not all(parte.isalpha() for parte in valor.split()):
            return False
        return True
    
    if campo == "DNI":
        return valor.isdigit() and len(valor) in (7, 8)
    
    if campo == "Edad":
        if not valor.isdigit():
            return False
        edad = int(valor)
        return 0 < edad < 120

    if campo == "Telefono":
        return valor.isdigit() and len(valor) == 10 and valor.startswith("11")

    if campo == "Email":
        pattern= r'\w+@\w+\.\w+'   #valida caracteres seguido de un @ seguido de caracteres con un punto y seguido de caracteres
        validacion= "Email valido" if re.match(pattern,valor) else "Email invalido"
        return validacion 

    return True



if __name__ == "__main__":
    main()