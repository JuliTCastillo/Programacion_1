from funcion_06 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: producto existente, producto inexistente, cantidad negativa.

def test_producto_existente():
    stock = {
        "arroz": 10,
        "fideos": 5
    }
    assert actualizar_stock(stock, "arroz", 10) == True 

def test_producto_inexistente():
    stock = {
        "arroz": 10,
        "fideos": 5
    }
    assert actualizar_stock(stock, "harina", 10) == False 

def test_cantidad_negativa():
    stock = {
        "arroz": 10,
        "fideos": 5
    }
    assert actualizar_stock(stock, "arroz", -7) == False 
