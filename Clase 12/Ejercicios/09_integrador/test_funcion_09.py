from funcion_09 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: dos productos, producto repetido, sin ventas, venta cero.

def test_dos_productos():
    ventas = [("arroz", 3, 1500), ("fideos", 2, 1000),]
    assert resumen_ventas(ventas) == {"arroz": 4500, "fideos": 2000}

def test_producto_repetido():
    ventas = [("arroz", 3, 1500), ("arroz", 2, 1000),]
    assert resumen_ventas(ventas) == {"arroz": 6500}

def test_sin_ventas():
    assert resumen_ventas([]) == {}

def test_venta_cero():
    ventas = [("arroz", 0, 1500), ("fideos", 0, 1000),]
    assert resumen_ventas(ventas) == {"arroz": 0, "fideos": 0}
