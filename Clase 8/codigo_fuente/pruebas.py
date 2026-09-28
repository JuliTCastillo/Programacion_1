import re

print("=" * 60)
print("match, search y fullmatch")
print("=" * 60)

patron = r"[A-Za-z][0-9]{3}"
codigo = "A123XYZ"
print(f"re.match(patron, '{codigo}')     = {re.match(patron, codigo)}")
print(f"re.fullmatch(patron, '{codigo}') = {re.fullmatch(patron, codigo)}")

frase = "Tengo 5 gatos y 12 peces"
busqueda = re.search(r"[0-9]+", frase)
print(f"\nre.search(r'[0-9]+', '{frase}') = {busqueda}")
if busqueda:
    print(f"group(): {busqueda.group()}  start(): {busqueda.start()}  "
          f"end(): {busqueda.end()}  span(): {busqueda.span()}")

texto_ci = "Morty, a veces la Ciencia es más arte que ciencia..."
match_ci = re.search(r"ciencia", texto_ci, re.IGNORECASE)
print(f"\nre.search(r'ciencia', texto, re.IGNORECASE) = {match_ci}")


print("\n" + "=" * 60)
print("findall y finditer")
print("=" * 60)

texto5 = ("Game Hub- Correo: gamehub@gmail.com - Tel: 1234-5678 - Código: GH2026. "
          "Lucas Garay - Correo: lgaray@uade.edu.ar - Tel: 8765-4321 - Código: LG6202.")

numeros = re.findall(r"[0-9]+", texto5)
print(f"findall(r'[0-9]+', texto): {numeros}")

print("\nfinditer(r'[0-9]+', texto):")
for m in re.finditer(r"[0-9]+", texto5):
    print(f"   '{m.group()}' | inicio: {m.start()} | fin: {m.end()}")

patron_grupos = r"([A-Z]{2})([0-9]{4})"
coincidencias_grupos = re.findall(patron_grupos, texto5)
print(f"\nfindall con grupos de captura ([A-Z]{{2}})([0-9]{{4}}): {coincidencias_grupos}")


print("\n" + "=" * 60)
print("sub, split y compile")
print("=" * 60)

texto_telefonos = "Contacto 1: 123-456-7890, Contacto 2: 987-654-3210"
texto_ofuscado = re.sub(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", "XXX-XXX-XXXX", texto_telefonos)
print(f"sub -> original:  {texto_telefonos}")
print(f"sub -> resultado: {texto_ofuscado}")

texto_variado = "Hola, cómo estás? Espero que bien. Chau."
partes = [p for p in re.split(r"[.,?\s]+", texto_variado) if p]
print(f"\nsplit(r'[.,?\\s]+', texto): {partes}")

patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"
print(f"\ncompile + findall: {patron_anio.findall(fechas)}")


print("\n" + "=" * 60)
print("Funciones de validación (punto 7)")
print("=" * 60)


def validar_legajo(legajo):
    return re.fullmatch(r"[0-9]{5}", legajo) is not None


def validar_codigo(codigo):
    return re.fullmatch(r"[A-Z]{2}[0-9]{4}", codigo) is not None


def validar_telefono(telefono):
    return re.fullmatch(r"[0-9]{4}-[0-9]{4}", telefono) is not None


def validar_correo(correo):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", correo) is not None


def validar_importe(importe):
    return re.fullmatch(r"\$[0-9]+", importe) is not None


def validar_patente(patente):
    return re.fullmatch(r"([A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2})", patente) is not None


casos = {
    "validar_legajo": (validar_legajo, ["12345", "00001", "99999"], ["1234", "123456", "12a45"]),
    "validar_codigo": (validar_codigo, ["AB1234", "GH2026", "LG6202"], ["AB12", "1234AB", "ab1234"]),
    "validar_telefono": (validar_telefono, ["1234-5678", "4321-8765", "1111-0000"], ["123-45678", "12345678", "abcd-efgh"]),
    "validar_correo": (validar_correo, ["usuario@dominio.com", "gamehub@mail.org", "ejemplo@domain.ar"], ["usuario@", "usuario@dominio", "@dominio.com"]),
    "validar_importe": (validar_importe, ["$100", "$50", "$12500"], ["100", "$", "$12.50"]),
    "validar_patente": (validar_patente, ["ABC123", "AB123CD", "ZZ000UI"], ["AB123", "123ABCD", "A123BCD"]),
}

for nombre_funcion, (funcion, validos, invalidos) in casos.items():
    print(f"\n{nombre_funcion}:")
    for v in validos:
        print(f"   '{v}' (válido esperado)   -> {funcion(v)}")
    for v in invalidos:
        print(f"   '{v}' (inválido esperado) -> {funcion(v)}")
    print(f"   ''  (vacío)              -> {funcion('')}")


print("\n" + "=" * 60)
print("Extracción de información de un texto")
print("=" * 60)

texto_prueba = """
Registro de contactos:
- UADE: correo uade@empresa.com, tel 1234-5678, código UA1234.
- GAMEHUB: correo gamehub@sitio.org, tel 8765-4321, código GH5678.
- Datos incompletos: correo_invalido@, tel 123-45, código X12.
"""

patron_correo = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
patron_telefono = r"[0-9]{4}-[0-9]{4}"
patron_codigo = r"[A-Z]{2}[0-9]{4}"

correos = re.findall(patron_correo, texto_prueba)
telefonos = re.findall(patron_telefono, texto_prueba)
codigos = re.findall(patron_codigo, texto_prueba)

print(f"Correos encontrados ({len(correos)}): {correos}")
print(f"Teléfonos encontrados ({len(telefonos)}): {telefonos}")
print(f"Códigos encontrados ({len(codigos)}): {codigos}")

print("\nfinditer sobre correos:")
for m in re.finditer(patron_correo, texto_prueba):
    print(f"   '{m.group()}' en rango [{m.start()}, {m.end()})")