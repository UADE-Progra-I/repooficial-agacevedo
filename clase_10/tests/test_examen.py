import pytest
from source.examen import *

def test_ejercicio_4():
    resultado = ejercicio_4()
    assert resultado == [1, 4, 9, 16, 25]


def test_ejericio_5():
    resultado = ejercicio_5()
    assert resultado == [3, 7, 10]

def test_ejercicio_6():
    resultado = ejercicio_6()
    assert resultado ==  [2, 3, 5, 10, 15, 20]


def test_ejercicio_8():
    letras, cadena = ejercicio_8()
    assert letras == ['a', 'b', 'c']
    assert cadena == "versi"


def test_ejercicio_9():
    patente = "AB629CZ"
    resultado = ejercicio_9(patente)
    assert resultado == True