import pytest
from source.metodos import *


def test_sumar():
    resultado = sumar(2, 4)
    assert resultado == 6, "sumar(2,4) debe retornar 6"

def test_dividir():
    resultado = dividir(4, 2)
    assert resultado == 2, "dividir(4,2) debe retornar 2"

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(4, 0)

def test_dividir_str():
    with pytest.raises(TypeError):
        dividir("2","4")

