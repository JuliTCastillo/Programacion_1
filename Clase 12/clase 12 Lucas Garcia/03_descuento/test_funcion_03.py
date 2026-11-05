from funcion_03 import *

def test_descuento_normal():
    assert precio_final(1000, 20) == 800
    assert precio_final(200, 50) == 100

def test_sin_descuento():
    assert precio_final(1000, 0) == 1000
    assert precio_final(350, 0) == 350

def test_descuento_total():
    assert precio_final(1000, 100) == 0
    assert precio_final(0, 100) == 0

def test_descuento_invalido():
    assert precio_final(1000, -10) == -1
    assert precio_final(1000, 150) == -1
    assert precio_final(-500, 20) == -1
