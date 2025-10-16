from source.storage import *


def test_write_read_estudiantes():
    FILE_NAME = "test_estudiantes.csv"
    data = [[1, "John", "Doe", 23]]
    write_data(FILE_NAME, data)
    response = read_data(FILE_NAME)
    assert len(response) == 1, "Debe retornar solo 1 registro"
    assert response[0][1] == "John", "El nombre debe ser John"


def test_insert_row():
    FILE_NAME = "test_estudiantes.csv"
    response1 = read_data(FILE_NAME)
    data = [5, "Ana", "Blitz", 35]
    insert_row(FILE_NAME, data)
    response2 = read_data(FILE_NAME)
    assert len(response2)-len(response1) == 1 , "Solo un registro nuevo"
    assert response2[-1][2]=="Blitz"
