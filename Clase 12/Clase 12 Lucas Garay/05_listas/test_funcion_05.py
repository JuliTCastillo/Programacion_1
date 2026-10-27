from funcion_05 import *

# Pruebas para distintos contenidos de una lista.
def test_varios_mayores():
    assert contar_mayores([1, 5, 8, 3], 3) == 2

def test_ninguno():
    assert contar_mayores([1, 2, 3], 5) == 0

def test_lista_vacia():
    assert contar_mayores([], 0) == 0

def test_igual_no_cuenta():
    assert contar_mayores([3, 4, 3], 3) == 1
