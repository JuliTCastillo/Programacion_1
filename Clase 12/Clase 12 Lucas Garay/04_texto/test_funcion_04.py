from funcion_04 import *

# Pruebas para minúsculas, espacios y texto vacío.
def test_mayusculas():
    assert normalizar("HOLA") == "hola"

def test_espacios():
    assert normalizar("  Hola Mundo  ") == "hola mundo"

def test_vacio():
    assert normalizar("") == ""
