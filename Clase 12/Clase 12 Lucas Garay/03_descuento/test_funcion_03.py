from funcion_03 import *

# Pruebas para descuentos habituales y entradas inválidas.
def test_descuento_normal():
    assert precio_final(1000, 20) == 800

def test_sin_descuento():
    assert precio_final(250, 0) == 250

def test_descuento_total():
    assert precio_final(250, 100) == 0

def test_descuento_invalido():
    assert precio_final(100, 120) == -1
    assert precio_final(-1, 10) == -1
