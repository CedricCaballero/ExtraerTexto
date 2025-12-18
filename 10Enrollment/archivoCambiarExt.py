import PyPDF2
# Abrir archivo original
with open(r"C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosEnrollment\77c813c7-edc5-46f1-b12f-7d5ccc66bb20\0d760f8c-f746-4951-8447-63904a4e47d3.pdf", "rb") as original:
    contenido = original.read()

# Guardar el contenido en un archivo sin extensión
with open(r"C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosEnrollment\77c813c7-edc5-46f1-b12f-7d5ccc66bb20\0d760f8c-f746-4951-8447-63904a4e47d3", "wb") as archivo_salida:
    archivo_salida.write(contenido)
