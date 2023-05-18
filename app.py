from pathlib import Path

# -----------------------------
ruta_absoluta = Path("datos.text").resolve()

print(ruta_absoluta)
# -------------------
archivo = Path("datos.txt")
if archivo.exists():
    print("El archivo existe")
else:
    print("El archivo no existe")

# --------------------------------
# ls - l para saber los permisos


ruta = Path("app.py")
if ruta.is_file():
    print("La ruta representa un archivo")
else:
    print("La ruta no representa un archivo")

# --------------------------
directorio = Path("")
if directorio.is_dir():
    print("La ruta representa un directorio")
else:
    print("La ruta no representa un directorio")
# ---------------------------------
ruta_archivo = Path('/datos.txt')
resultado = ruta_archivo.parent
print(resultado)
# ------------------------------------

extension = Path('datos.txt')
extension_ruta = extension.resolve()
extension = ruta.suffix
print(extension_ruta)
print(extension)
# -----------------------------
# crear directorio

# nuevo_dir = Path('nuevo_Directorio')
# nuevo_dir.mkdir()

# ------------------------------
# Eliminar el direcciorio

# nuevo_dir = Path('rnuevo_Directorio')
# nuevo_dir.rmdir()

# ----------------------------------
"""El número 33206 en la representación decimal corresponde al modo de acceso en octal 100644.

En el modo de acceso 100644:

El primer dígito "1" indica que se trata de un archivo regular.
Los siguientes tres dígitos "006" corresponden a los permisos del propietario del archivo. En este caso, el propietario tiene permisos de lectura y escritura (6), pero no tiene permiso de ejecución.
Los siguientes tres dígitos "4" representan los permisos del grupo asociado al archivo. En este caso, el grupo solo tiene permisos de lectura (4).
Los últimos tres dígitos "4" indican los permisos para otros usuarios. Aquí, los otros usuarios también tienen permisos de lectura (4).
"""
ruta = Path('datos.txt')
acceso = ruta.stat().st_mode

print(acceso)
