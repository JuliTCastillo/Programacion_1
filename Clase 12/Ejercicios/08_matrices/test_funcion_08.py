from funcion_08 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: matriz dos filas, matriz vacia, valores negativos, una fila.

def test_matriz_dos_filas():
    assert sumar_matriz([[1,2],[1,2]]) == 6

def test_matriz_vacia():
    assert sumar_matriz([]) == 0

def test_valores_negativos():
    assert sumar_matriz([[-2,-2],[-1,-1]]) == -6

def test_una_fila():
    assert sumar_matriz([[2,2]]) == 4
