def normalizar_nombre(nombre):
    return nombre.title()


def nombre_mayusculas(nombre):
    return nombre.upper()


def cantidad_caracteres(nombre):
    return len(nombre)


def generar_sigla(nombre):
    palabras = nombre.split()
    sigla = ""

    for palabra in palabras:
        sigla += palabra[0].upper()

    return sigla


def contiene_digitos(texto):
    val = False

    for caracter in texto:
        if caracter.isdigit():
            val = True

    return val