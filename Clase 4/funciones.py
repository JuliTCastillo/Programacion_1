def cargar_productos():
    productos = []
    codigos_usados = []

    while True:
        codigo = input("Código del producto (o 'FIN' para terminar): ")
        if codigo == "FIN":
            break

        if codigo in codigos_usados:
            print("Ese código ya existe. Ingresá uno distinto.")
            continue

        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))

        producto = (codigo, descripcion, precio)
        productos.append(producto)
        codigos_usados.append(codigo)

    return productos


def mostrar_productos(productos):
    if not productos:
        print("No hay productos cargados.")
        return

    print("\n--- Catálogo de productos ---")
    for codigo, descripcion, precio in productos:
        print(f"Código: {codigo} | Descripción: {descripcion} | Precio: ${precio:.2f}")


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto[0] == codigo:
            return producto
    return None


def producto_mayor_precio(productos):
    if not productos:
        return None

    mayor = productos[0]
    for producto in productos:
        if producto[2] > mayor[2]:
            mayor = producto
    return mayor


def precio_promedio(productos):
    if not productos:
        return None

    total = sum(producto[2] for producto in productos)
    return total / len(productos)