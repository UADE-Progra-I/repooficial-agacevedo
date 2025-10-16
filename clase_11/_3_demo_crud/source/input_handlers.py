import read_console


def input_estudiante():
    """
    return: lista
    """
    nombre = read_console.input_nombre_estudiante()
    apellido = read_console.input_apellido_estudiante()
    edad = read_console.input_edad_estudiante()
    return [nombre, apellido, edad]

def input_id_estudiante():
    """
    return str numerico
    """
    id = read_console.input_id_estudiante()
    return id

def input_confirma_eliminar_estudiante():
    """
    return True/False
    """
    confirma = read_console.input_confirma_eliminar_estudiante()
    return True if confirma == "s" else False