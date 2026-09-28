from validaciones import *


def pedir_dato(pregunta, validador, mensaje_error):
    while True:
        valor = input(pregunta).strip()
        if validador(valor):
            return valor
        print(mensaje_error)


def pedir_datos():
    nombre = pedir_dato(
        "Nombre completo: ",
        validar_nombre,
        "Solo letras, palabras separadas por un espacio. Ej: Agustina Fernandez",
    )
    legajo = pedir_dato(
        "Legajo: ",
        validar_legajo,
        "Deben ser exactamente 5 dígitos. Ej: 12345",
    )
    correo = pedir_dato(
        "Correo electrónico: ",
        validar_correo,
        "Formato usuario@dominio.ext. Ej: agustina@uade.edu.ar",
    )
    telefono = pedir_dato(
        "Teléfono (formato 1234-5678): ",
        validar_telefono,
        "Deben ser 4 dígitos, guion y 4 dígitos. Ej: 1234-5678",
    )
    comision = pedir_dato(
        "Código de comisión (6 dígitos): ",
        validar_comision,
        "Deben ser exactamente 6 dígitos. Ej: 123456",
    )
    return nombre, legajo, correo, telefono, comision



def mostrar_resultados(nombre, legajo, correo, telefono, comision):
    print("\n=== Datos registrados ===")
    print(f"Nombre: {nombre}")
    print(f"Legajo: {legajo}")
    print(f"Correo electrónico: {correo}")
    print(f"Teléfono: {telefono}")
    print(f"Código de comisión: {comision}")



def main():
    print("=== Formulario de registro ===")
    nombre, legajo, correo, telefono, comision = pedir_datos()
    mostrar_resultados(nombre, legajo, correo, telefono, comision)
main()