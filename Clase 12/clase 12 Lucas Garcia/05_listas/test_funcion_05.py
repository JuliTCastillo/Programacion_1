from funcion_05 import *

def test_varios_mayores():
    assert contar_mayores([1, 5, 8, 10, 3], 4) == 3
    assert contar_mayores([20, 30, 40], 10) == 3

def test_ninguno():
    assert contar_mayores([1, 2, 3], 10) == 0

def test_lista_vacia():
    assert contar_mayores([], 5) == 0

def test_igual_no_cuenta():
    assert contar_mayores([5, 5, 5], 5) == 0
    assert contar_mayores([4, 5, 6], 5) == 1
