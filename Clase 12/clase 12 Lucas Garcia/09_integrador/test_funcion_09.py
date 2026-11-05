from funcion_09 import *

def test_dos_productos():
    ventas = [("remera", 2, 1000), ("pantalon", 1, 3000)]
    assert resumen_ventas(ventas) == {"remera": 2000, "pantalon": 3000}

def test_producto_repetido():
    ventas = [("remera", 2, 1000), ("remera", 3, 1000)]
    assert resumen_ventas(ventas) == {"remera": 5000}

def test_sin_ventas():
    assert resumen_ventas([]) == {}

def test_venta_cero():
    ventas = [("gorra", 0, 500)]
    assert resumen_ventas(ventas) == {"gorra": 0}
