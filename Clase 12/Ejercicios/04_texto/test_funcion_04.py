from funcion_04 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: mayusculas, espacios, vacio.

def test_mayusculas():
    assert normalizar("JULIETA") == "julieta"

def test_espacios():
    assert normalizar(" Julieta Castillo ") == "julieta castillo"

def test_vacio():
    assert normalizar("") == ""
