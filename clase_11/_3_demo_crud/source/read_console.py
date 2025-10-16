import utilities

def get_menu_opcion():
    while True:
        try:
            opcion = input("Ingrese su opción: ").strip()
            if utilities.validar_menu_opcion(opcion):
                return opcion
        except Exception as e:
            print(f"ERROR: {e}")
        
def input_nombre_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    # TO DO: agregar validación al nombre
    return nombre

def input_apellido_estudiante():
    apellido = input("Ingrese el apellido del estudiante: ")
    # TO DO: agregar validación al apellido
    return apellido

def input_edad_estudiante():
    edad = input("Ingrese la edad del estudiante: ")
    # TO DO: agregar validación a la edad
    return edad

def input_id_estudiante():
    id = input("Ingrese el id del estudiante: ")
    # TO DO: agregar validación al ID
    return id

def input_confirma_eliminar_estudiante():
    confirma = input("Confirma que desea eliminar el estudiante: s/n?")
    return confirma.strip().lower()
