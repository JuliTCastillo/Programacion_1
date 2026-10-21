from funcion_01 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: suma positivos, suma negativos, suma cero.

def test_suma_positivos():
    assert sumar(11, 22) == 33

def test_suma_negativos():
    assert sumar(-14, -6) == -20

def test_suma_cero():
    assert sumar(10, 0) == 10
