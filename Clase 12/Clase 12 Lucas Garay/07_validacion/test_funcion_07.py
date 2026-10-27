from funcion_07 import *

# Pruebas de longitud y presencia de al menos un dígito.
def test_clave_valida():
    assert clave_valida("clave123") is True

def test_clave_corta():
    assert clave_valida("abc123") is False

def test_sin_numeros():
    assert clave_valida("abcdefgh") is False

def test_limite_ocho():
    assert clave_valida("abcdefg1") is True
