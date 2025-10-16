import storage


# Leer todos los estudiantes del storage
def get_all_estudiantes():
    """
    parametros: None
    return: data
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.csv"

    # invoco a read_data para recuperar los datos del archivo
    data = storage.read_data(FILE_NAME)
    return data


# Buscar en el storage un estudiante por su id
def get_estudiante_by_id(id_estudiante):
    """
    parametros: id str
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.csv"
    estudiantes = get_all_estudiantes()
    if len(estudiantes) == 0:
        raise Exception("get_all_students retorno 0")

    # Normalizar el id a string
    id_str = str(id_estudiante)

    # Buscar coincidencia
    for e in estudiantes:
        if e[0] == id_str:
            return e

    # Si no se encontró
    return False


def add_estudiante(new_estudiante):
    """
    parametros: estudiante (lista)
    return: True
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.csv"

    estudiantes = get_all_estudiantes()
    if len(estudiantes) == 0:
        new_estudiante.insert(0, 1)
    else:
        last_id = estudiantes[-1][0]
        next_id = int(last_id) + 1
        new_estudiante.insert(0, str(next_id))

    # invoco a write_data para persistir el dato en el archivo
    storage.insert_row(FILE_NAME, new_estudiante)
    return True


def delete_estudiante_by_id(id_estudiante):
    """
    parametros: id str
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.csv"
    estudiantes = get_all_estudiantes()

    # Normalizar el id a string
    id_str = str(id_estudiante)

    # Buscar coincidencia
    flag = False
    for e in estudiantes:
        if e[0] == id_str:
            estudiantes.remove(e)
            flag = True
            break
    if not flag:
        raise Exception("No se ha encontrado el estudiante que se desea eliminar")

    storage.write_data(FILE_NAME, estudiantes)

    return True
