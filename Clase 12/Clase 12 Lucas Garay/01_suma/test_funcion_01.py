from funcion_01 import *

# Pruebas de suma: positivos, negativos y cero.
def test_suma_positivos():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-2, -3) == -5

def test_suma_cero():
    assert sumar(8, 0) == 8
