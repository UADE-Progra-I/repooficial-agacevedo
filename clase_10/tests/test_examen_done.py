import pytest
from source.examen_done import *

def test_ejercicio_2():
    M = [[1, 2], [4, 5]]
    A = 2   
    resultado = ejercicio_2(M,A)
    assert resultado == [[2, 4], [8, 10]]

def test_ejercicio_4():
    resultado = ejercicio_4()
    assert resultado == [1, 4, 9, 16, 25], "Debe retornar [1, 4, 9, 16, 25]"  #1,2,3,4,5 => 1,4,9,16,25

def test_ejercicio_5():
    resultado = ejercicio_5()
    assert resultado == [3, 7, 10], "Debe retornar [3, 7, 10]" # [3, -1, 0, 7, -5, 10, -2] => [3, 0, 7, 10]

def test_ejercicio_6():
    resultado = ejercicio_6()
    assert resultado == [2, 3, 5, 10, 15, 20]  # [10, 3, 7, 2, 15] => [10, 3, 5, 2, 15, 20] => [2, 3, 5, 10, 15, 20]

def test_ejercicio_7():
    cadena = "Programación en Python"
    resultado = ejercicio_7(cadena)
    assert resultado["minusculas"]=="programación en python" 
    assert resultado["cantidad_o"]==2
    assert resultado["termina_python"]==True
    assert resultado["reemplazo"]=="Programación en Java"

def test_ejercicio_8():
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    cadena = "Universidad"
    resultado1, resultado2 = ejercicio_8(letras, cadena)
    assert resultado1 == ["a", "b", "c"]
    assert resultado2 == "versi"

def test_ejercicio_9():
    patente = "AB629CZ"
    resultado = ejercicio_9(patente)
    assert resultado == True

def test_ejercicio_10():
    resultado = ejercicio_10()
    assert resultado[0]["nombre"] == "Ana"
    assert resultado[1]["legajo"] == 102
    assert resultado[2]["apellido"] == "Fernández"