from funcion_02 import *

def test_numero_par():
    assert es_par(4) == True
    assert es_par(100) == True
    assert es_par(-2) == True

def test_numero_impar():
    assert es_par(7) == False
    assert es_par(1) == False
    assert es_par(-3) == False

def test_cero():
    assert es_par(0) == True
