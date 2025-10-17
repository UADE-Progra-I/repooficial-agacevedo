"""
Test Unitarios con Pytest

Crear un archivo test_productos.py y escribir pruebas unitarias para las funciones:

- read_productos()
- write_productos()
- insert_productos()
- inicializar_productos()

Recomendaciones:
 Utilizar un archivo temporal (por ejemplo test_productos.csv).
 Verificar que se escriben las líneas correctas.
 Verificar que insert_productos() agrega una línea al final.
 Asegurarse de que read_productos() maneje correctamente el caso de archivo inexistente.

Ejemplo:

def test_insert_productos():
    producto = [4, "Buzo Negro", "Indumentaria", 21000.0]
    insert_productos("test_productos.csv", producto)
    data = read_productos("test_productos.csv")
    assert any(row[1] == "Buzo Negro" for row in data)
"""
import os
import pytest
from actividad import read_productos, write_productos, insert_productos, inicializar_productos

@pytest.fixture
def productos_path_func():
    productos_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ),"data","test_productos.csv"))
    inicializar_productos(productos_path,[])
    
    try:
        yield str(productos_path)
    finally:
        try:
            os.remove(productos_path)
        except FileNotFoundError:
            pass
    
@pytest.fixture
def producto_func():
    return [4, "Buzo Negro", "Indumentaria", 21000.0]

@pytest.fixture
def productos_func():
    productos = [
        [1, "Buzo Blanco", "Indumentaria", 20000.0],
        [2, "Prueba", "Prueba", 6000.5],
        [3, "Prueba1", "Prueba1", 5000.0],
        [4, "Buzo Negro", "Indumentaria", 21000.0]
    ]
    return productos

def test_insert_productos(productos_path_func, producto_func):
    insert_productos(productos_path_func, producto_func)
    data = read_productos(productos_path_func)
    assert any(row[1] == "Buzo Negro" for row in data)

# def test_read_productos():
    
#     pass

def test_write_productos(productos_path_func,productos_func):
    write_productos(productos_path_func,productos_func)
    data = read_productos(productos_path_func)
    assert any(row[1] == "Buzo Negro" for row in data)
    assert len(data) == 4


# def test_inicializar_productos():
#     pass