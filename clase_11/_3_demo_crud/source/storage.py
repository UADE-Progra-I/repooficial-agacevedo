# Leer y retornar el contenido de un archivo csv
import os
import csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_data(file_name):
    print("")
    """
    parametros:
    file_name: nombre del archivo 
    """
    if not isinstance(file_name, str):
        raise TypeError("file_name debe ser un string")
    if file_name.strip() == "":
        raise ValueError("file_name no puede estar vacío")
    
    DATA_PATH = os.path.join(BASE_DIR, "data", file_name)

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))

    return data


# Función que inserta un registro en el csv
def insert_row(file_name, data):
    """
    parametros:
    file_name: str
    data: lista
    """
    DATA_PATH = os.path.join(BASE_DIR, "data", file_name)

    if not isinstance(file_name, str):
        raise TypeError("file_name debe ser un str")
    if file_name.strip() == "":
        raise ValueError("file_name no puede estar vacío")
    if not isinstance(data, list):
        raise TypeError("data debe ser una lista")
    if len(data) == 0:
        raise ValueError("data no puede estar vacío")

    
    with open(DATA_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    return True


def write_data(file_name, data):
    """
    parametros:
    file_name: str
    data: lista
    """
    DATA_PATH = os.path.join(BASE_DIR, "data", file_name)

    if not isinstance(file_name, str):
        raise TypeError("file_name debe ser un str")
    if file_name.strip() == "":
        raise ValueError("file_name no puede estar vacío")
    if not isinstance(data, list):
        raise TypeError("data debe ser una lista")
    if len(data) == 0:
        raise ValueError("data no puede estar vacío")

    
    with open(DATA_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return True