from funcion_07 import *

def test_clave_valida():
    assert clave_valida("python2024") == True
    assert clave_valida("12345678") == True

def test_clave_corta():
    assert clave_valida("abc1") == False
    assert clave_valida("") == False

def test_sin_numeros():
    assert clave_valida("contraseña") == False
    assert clave_valida("abcdefghij") == False

def test_limite_ocho():
    assert clave_valida("abcdefg1") == True
    assert clave_valida("abcdef1") == False
