from funcion_06 import *

def test_producto_existente():
    stock = {"manzana": 10, "pera": 5}
    assert actualizar_stock(stock, "manzana", 3) == True
    assert stock["manzana"] == 13
    assert stock["pera"] == 5

def test_producto_inexistente():
    stock = {"manzana": 10}
    assert actualizar_stock(stock, "banana", 4) == False
    assert stock == {"manzana": 10}

def test_cantidad_negativa():
    stock = {"manzana": 10}
    assert actualizar_stock(stock, "manzana", -2) == False
    assert stock["manzana"] == 10
