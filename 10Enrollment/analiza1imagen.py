import fitz  # PyMuPDF
import easyocr

# Ruta al archivo PDF
ruta_pdf = r"C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosE\a409bd41-d632-4100-9411-5f091e75b0a6\3af6e6df-df7e-4a09-bc9c-f90d95af0bd7.pdf"

# Crear un lector de EasyOCR
reader = easyocr.Reader(lang_list=['es'], gpu=False)  # Cambia 'es' por tu idioma

# Abrir el PDF
documento = fitz.open(ruta_pdf)

# Procesar cada página del PDF
for num_pagina in range(len(documento)):
    pagina = documento[num_pagina]
    # Extraer imagen de la página como Pixmap
    pixmap = pagina.get_pixmap()
    imagen_bytes = pixmap.tobytes()  # Obtener los datos de imagen

    # Guardar la imagen temporalmente (opcional)
    ruta_imagen = f"pagina_{num_pagina + 1}.png"
    pixmap.save(ruta_imagen)

    # Usar EasyOCR para analizar el texto de la imagen
    resultados = reader.readtext(ruta_imagen)

    # Mostrar los resultados
    for (bbox, texto, confianza) in resultados:
        print(f"Texto detectado: {texto} (Confianza: {confianza:.2f})")