from funcion_06 import *

# Pruebas para actualización de stock y casos rechazados.
def test_producto_existente():
    stock = {"manzana": 10}
    assert actualizar_stock(stock, "manzana", 5) is True
    assert stock["manzana"] == 15

def test_producto_inexistente():
    stock = {"manzana": 10}
    assert actualizar_stock(stock, "pera", 5) is False
    assert stock == {"manzana": 10}

def test_cantidad_negativa():
    stock = {"manzana": 10}
    assert actualizar_stock(stock, "manzana", -2) is False
    assert stock["manzana"] == 10
