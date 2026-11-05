from funcion_01 import *

def test_suma_positivos():
    assert sumar(2, 3) == 5
    assert sumar(10, 15) == 25

def test_suma_negativos():
    assert sumar(-2, -3) == -5
    assert sumar(-10, 4) == -6

def test_suma_cero():
    assert sumar(0, 0) == 0
    assert sumar(7, 0) == 7
    assert sumar(0, -7) == -7
