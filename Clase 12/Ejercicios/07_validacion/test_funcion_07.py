from funcion_07 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: clave valida, clave corta, sin numeros, limite ocho.

def test_clave_valida():
    assert clave_valida("Prueba!123") == True

def test_clave_corta():
    assert clave_valida("Prueba?") == False

def test_sin_numeros():
    assert clave_valida("contraseña") == False


def test_limite_ocho():
    assert clave_valida("Test1234") == True
