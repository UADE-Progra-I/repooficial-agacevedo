# --------------------------------------------------------
# Actividad manejo de excepciones
# --------------------------------------------------------
"""
La función origianl validarPass, valida que una contraseña cumpla con ciertos requerimentos
La misma fue refactorizada para que cuando una regla no se cumple genere una excepción.
Asimismo, el llamado a la función maneja las excepciones con try/except.
Es una buena práctica que las funciones generen excepciones cuando no se cumple una regla del negocio,
y que las funciones superiores decidan que hacer.

Analizar como referencia, validarPassException()

Pueden hacer las modificaciones adicionales que consideren.
"""


def main():
    while True:
        password = input("Ingrese su password: ")
        try:
            if validarPassException(password):
                print("Password valida!")
                break
        except:
            print("La password no cumple con los requisitos")
            next = input("Presione 's' intentarnuevamente o cualquier tecla para cancelar: ").strip().lower()
            if next != 's':
                break
        finally:
            print("")


def validarPass(password):
    """
    Verifica si una contraseña cumple con los criterios de seguridad definidos.

    Una contraseña válida debe:
    - Tener entre 8 y 12 caracteres.
    - Incluir al menos una letra.
    - Incluir al menos un número.
    - Incluir al menos un símbolo (carácter no alfanumérico).

    Args:
        password (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    if 8 <= len(password) <= 12:
        tiene_letra = any(c.isalpha() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        tiene_simbolo = any(not c.isalnum() for c in password)
        return tiene_letra and tiene_numero and tiene_simbolo
    return False

def validarPassException(password):
    """
    Verifica si una contraseña cumple con los criterios de seguridad definidos.

    Lanza excepciones con mensajes específicos si no se cumple alguna condición:
    - Entre 8 y 12 caracteres.
    - Al menos una letra.
    - Al menos un número.
    - Al menos un símbolo (no alfanumérico).
    """
    if len(password) < 8 or len(password) > 12:
        raise ValueError("La contraseña debe tener entre 8 y 12 caracteres.")

    if not isinstance(password, str):
        raise TypeError("La contraseña debe ser una cadena de texto.")

    if not any(c.isalpha() for c in password):
        raise ValueError("La contraseña debe contener al menos una letra.")

    if not any(c.isdigit() for c in password):
        raise ValueError("La contraseña debe contener al menos un número.")

    if not any(not c.isalnum() for c in password):
        raise ValueError("La contraseña debe contener al menos un símbolo (no alfanumérico).")

    return response





if __name__ == "__main__":
    main()