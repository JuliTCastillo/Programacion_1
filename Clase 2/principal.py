#import ModFunc
import videojuegos

# Lista inicial de diez videojuegos
juegos =  ["Minecraft", "Valorant", "Fortnite", "FIFA", "Rocket League", "Roblox", "LOL", "Among Us"]

def probar_funciones():
    # --- Prueba de mostrar_juegos() ---
    print("Catálogo completo:")
    videojuegos.mostrar_juegos(juegos)

    # --- Prueba de buscar_juego() ---
    print("\nBuscar título existente (Fortnite):")
    resultado = videojuegos.buscar_juego(juegos, "Fortnite")
    print(f"Posición encontrada: {resultado}")

    print("\nBuscar título inexistente (Zelda):")
    resultado = videojuegos.buscar_juego(juegos, "Zelda")
    print(f"Posición encontrada: {resultado}")

    # --- Prueba de agregar_juego() ---
    print("\nLista antes de agregar:")
    print(juegos)

    print("\nAgregar título nuevo (Zelda):")
    agregado = videojuegos.agregar_juego(juegos, "Zelda")
    print(f"¿Se agregó?: {agregado}")
    print("Lista después de agregar:")
    print(juegos)

    print("\nIntentar agregar título repetido (Fortnite):")
    agregado = videojuegos.agregar_juego(juegos, "Fortnite")
    print(f"¿Se agregó?: {agregado}")
    print("Lista después del intento:")
    print(juegos)

    # --- Prueba de cantidad_juegos() ---
    print("\n Cantidad total de juegos:")
    print(videojuegos.cantidad_juegos(juegos))

def slicing(juegos):
    print("Los tres primeros elementos:",juegos[:3])
    print("Los cuatro últimos elementos:",juegos[-4:])
    print("Los elementos ubicados desde la posición 1 hasta la 4 inclusive:",juegos[1:5])
    print("Los elementos de posiciones pares:",juegos[::2])
    print("Los elementos de posiciones impares:",juegos[1::2])
    print("La lista invertida:",juegos[::-1])
    print("Todos los elementos excepto el primero:",juegos[1:])
    print("Todos los elementos excepto el ultimo:",juegos[:-1])

numeros = [2, 4, 6, 8, 10, 12, 14]

def modif_slicing(lista):
    copia_a = lista.copy()
    copia_a[2:4] = [60, 80]
    print(copia_a)
    
    copia_b = lista.copy()
    copia_b[4:6] = []
    print(copia_b)

    copia_c = lista.copy()
    copia_c[2:2] = [100, 200]
    print(copia_c)

    copia_d = lista.copy()
    copia_d[:0] = [1, 2, 3]
    print(copia_d)

    copia_e = lista.copy()
    copia_e[:] = []
    print(copia_e)


def duplicar_valores_lista(lista):
    listaNueva = [i*2 for i in lista]
    return listaNueva

def puntajes_aprob(lista):
    listaNueva = [i for i in lista if i >= 60]
    return listaNueva

def cuadrado_pares(lista):
    listaNueva = [i**2 for i in lista if (i % 2) == 0]
    return listaNueva

def nota_final(calificaciones):
    listaNueva = ["Aprobado" if nota >= 60 else "Revisar" for nota in calificaciones]
    return listaNueva


cuadrado = lambda x: x**2

es_par = lambda x: x % 2 == 0

mayor = lambda a, b: a if a > b else b

aplicar_descuento = lambda precio, descuento: (precio/100)*(100 - descuento)


