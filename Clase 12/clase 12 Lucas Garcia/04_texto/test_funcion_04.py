from funcion_04 import *

def test_mayusculas():
    assert normalizar("HOLA") == "hola"
    assert normalizar("PyThOn") == "python"

def test_espacios():
    assert normalizar("   hola   ") == "hola"
    assert normalizar("  Buenos Aires  ") == "buenos aires"

def test_vacio():
    assert normalizar("") == ""
    assert normalizar("     ") == ""
