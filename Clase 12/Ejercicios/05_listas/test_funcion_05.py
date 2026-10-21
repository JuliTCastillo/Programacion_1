from funcion_05 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: varios mayores, ninguno, lista vacia, igual no cuenta.

def test_varios_mayores():
    assert contar_mayores([5,3,4], 2) == 3

def test_ninguno():
    assert contar_mayores([0,1,2], 2) == 0

def test_lista_vacia():
    assert contar_mayores([0,1,-1], 2) == 0

def test_igual_no_cuenta():
    assert contar_mayores([2], 2) == 0
    pass
