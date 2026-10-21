from funcion_03 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: descuento normal, sin descuento, descuento total, descuento invalido.

def test_descuento_normal():
    assert precio_final(100, 20) == 80

def test_sin_descuento():
    assert precio_final(100, 0) == 100

def test_descuento_total():
    assert precio_final(2800, 50) == 1400

def test_descuento_invalido():
    assert precio_final(2800, -50) == -1
