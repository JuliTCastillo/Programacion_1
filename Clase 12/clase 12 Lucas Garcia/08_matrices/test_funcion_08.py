from funcion_08 import *

def test_matriz_dos_filas():
    assert sumar_matriz([[1, 2, 3], [4, 5, 6]]) == 21

def test_matriz_vacia():
    assert sumar_matriz([]) == 0

def test_valores_negativos():
    assert sumar_matriz([[-1, -2], [-3, -4]]) == -10
    assert sumar_matriz([[5, -5], [10, -3]]) == 7

def test_una_fila():
    assert sumar_matriz([[7, 8, 9]]) == 24
