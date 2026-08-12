def mostrar_juegos(juegos):
    for juego in juegos:
        print(juego)

def buscar_juego(juegos, titulo):
    posicion = -1
    i = 0
    while posicion == -1 and i < len(juegos):
        if juegos[i] == titulo:
            posicion = i
        i += 1
    return posicion

def agregar_juego(juegos, titulo):
    noExiste = True
    if buscar_juego(juegos, titulo) == -1:
        juegos.append(titulo)
    else:
        noExiste = False
    return noExiste

def cantidad_juegos(juegos):
    return len(juegos)