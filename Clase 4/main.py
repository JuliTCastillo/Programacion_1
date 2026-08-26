import funciones

def main():
    # Programa principal
    productos = funciones.cargar_productos()

    funciones.mostrar_productos(productos)

    codigo_buscado = input("\nIngresá un código para buscar: ")
    resultado = funciones.buscar_producto(productos, codigo_buscado)
    if resultado:
        print(f"Producto encontrado: {resultado}")
    else:
        print("Producto no encontrado.")

    mayor = funciones.producto_mayor_precio(productos)
    if mayor:
        print(f"\nProducto de mayor precio: {mayor}")
    else:
        print("\nNo hay productos para calcular el mayor precio.")

    promedio = funciones.precio_promedio(productos)
    if promedio is not None:
        print(f"Precio promedio: ${promedio:.2f}")
    else:
        print("No hay productos para calcular el promedio.")

main()