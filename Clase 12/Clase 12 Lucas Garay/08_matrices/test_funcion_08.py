from funcion_08 import *

# Pruebas para matrices de diferentes tamaños y valores.
def test_matriz_dos_filas():
    assert sumar_matriz([[1, 2], [3, 4]]) == 10

def test_matriz_vacia():
    assert sumar_matriz([]) == 0

def test_valores_negativos():
    assert sumar_matriz([[-1, -2], [3]]) == 0

def test_una_fila():
    assert sumar_matriz([[2, 4, 6]]) == 12
