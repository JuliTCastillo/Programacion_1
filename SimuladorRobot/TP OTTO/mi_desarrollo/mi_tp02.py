# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  Lucas Garay.....................................
#  Comision:           1151.....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO, MISIONES


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CODIGO ACA
    comandos_validos = {
        "avanzar": 2,     # necesita velocidad y tiempo
        "girar": 2,       # necesita velocidad y tiempo
        "detenerse": 0,   # sin datos extra
        "saludar": 0,     # sin datos extra
    }

    if len(comando) == 0:
        return False

    nombre = comando[0]

    if nombre not in comandos_validos:
        return False

    datos = comando[1:]
    cantidad_esperada = comandos_validos[nombre]

    if len(datos) != cantidad_esperada:
        return False

    for dato in datos:
        if not isinstance(dato, (int, float)):
            return False

    if cantidad_esperada == 2:
        velocidad, tiempo = datos
        if tiempo < 0:
            return False

    return True
    


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CODIGO ACA
    nombre = comando[0]

    try:
        if nombre == "avanzar":
            _, velocidad, tiempo = comando
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
            return f"Avanzó a {velocidad} m/s durante {tiempo}s"

        elif nombre == "girar":
            _, velocidad, tiempo = comando
            robot.girar(velocidad=velocidad, tiempo=tiempo)
            return f"Giró a {velocidad} rad/s durante {tiempo}s"

        elif nombre == "detenerse":
            robot.detenerse()
            return "Se detuvo"

        elif nombre == "saludar":
            robot.saludar()
            return "Saludó"

    except ErrorDeSeguridad as e:
        return f"Rechazado por el robot (seguridad): {e}"
    


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    # TU CODIGO ACA
    for comando in mision:
        if not comando_es_valido(comando):
            historial.append((comando, False, "Comando con formato inválido"))
            continue

        resultado = ejecutar_comando(robot, comando)
        historial.append((comando, True, resultado))
   


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    # TU CODIGO ACA
    exitosos = [h for h in historial if h[1]]
    rechazados = [h for h in historial if not h[1]]

    print("\n--- Reporte de la misión ---")
    print(f"Comandos ejecutados correctamente: {len(exitosos)}")
    print(f"Comandos rechazados: {len(rechazados)}")

    if rechazados:
        print("\nMotivos de rechazo:")
        for comando, _, motivo in rechazados:
            print(f"- {comando}: {motivo}")
   


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        # Empeza probando con MISION_BASICA.
        # Cuando funcione, proba con MISION_CON_ERRORES: esa tiene
        # comandos invalidos a proposito.
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        


if __name__ == "__main__":
    main()
