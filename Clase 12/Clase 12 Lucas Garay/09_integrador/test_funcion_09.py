from funcion_09 import *

# Pruebas para resumir importes agrupados por producto.
def test_dos_productos():
    ventas = [("pan", 2, 100), ("leche", 1, 250)]
    assert resumen_ventas(ventas) == {"pan": 200, "leche": 250}

def test_producto_repetido():
    ventas = [("pan", 2, 100), ("pan", 3, 100)]
    assert resumen_ventas(ventas) == {"pan": 500}

def test_sin_ventas():
    assert resumen_ventas([]) == {}

def test_venta_cero():
    assert resumen_ventas([("pan", 0, 100)]) == {"pan": 0}
