import re



def validar_menu_opcion(opcion):
    if opcion == "":
        raise ValueError("Opción en blanco")
    # Patrón que acepta solo los números del 1 al 6
    patron = r"^[1-6]$"
    if not re.match(patron, opcion):
        raise ValueError("Debe ingresar un número entre 1 y 6")
    return True
