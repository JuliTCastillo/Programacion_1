import funciones

equipo = input("Nombre del equipo: ")
comision = input("Comisión: ")

cantidad_integrantes = int(input("Cantidad de integrantes: "))

integrantes = []

for i in range(cantidad_integrantes):
    nombre = input(f"Nombre del integrante {i + 1}: ")
    rol = input(f"Rol de {nombre}: ")

    nombre = funciones.normalizar_nombre(nombre)
    integrantes.append((nombre, rol))

print("\n--- PERFIL DEL EQUIPO ---")
print(f"Equipo: {funciones.nombre_mayusculas(equipo)}")
print(f"Comisión: {comision}")
print(f"Cantidad de caracteres: {funciones.cantidad_caracteres(equipo)}")
print(f"Sigla: {funciones.generar_sigla(equipo)}")
print(f"¿Contiene dígitos?: {funciones.contiene_digitos(equipo)}")

print("\nIntegrantes:")

for nombre, rol in integrantes:
    print(f"- {nombre} | Rol: {rol}")