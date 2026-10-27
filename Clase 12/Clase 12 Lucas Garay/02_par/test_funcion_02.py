from funcion_02 import *

# Pruebas para pares, impares y cero.
def test_numero_par():
    assert es_par(4) is True

def test_numero_impar():
    assert es_par(7) is False

def test_cero():
    assert es_par(0) is True
