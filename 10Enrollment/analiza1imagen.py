import fitz  # PyMuPDF
import easyocr
import cv2

# Ruta al archivo PDF
ruta_pdf = r"C:\Users\ccaballerob\Downloads\00001-HACA0001-CONTR.pdf"

# Crear un lector de EasyOCR
reader = easyocr.Reader(lang_list=['en','es'], gpu=False)  # Cambia 'es' por tu idioma

# Abrir el PDF
documento = fitz.open(ruta_pdf)

# Procesar cada página del PDF
for num_pagina in range(len(documento)):
    pagina = documento[num_pagina]
    # Extraer imagen de la página como Pixmap
    pixmap = pagina.get_pixmap(dpi=300)
    imagen_bytes = pixmap.tobytes()  # Obtener los datos de imagen

    # Guardar la imagen temporalmente (opcional)
    ruta_imagen = f"pagina_{num_pagina + 1}.png"
    pixmap.save(ruta_imagen)
    #***********nuevo
    
    image = cv2.imread(ruta_imagen)
    cv2.imshow("Original",image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gris",gray)
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    #enhanced = clahe.apply(gray)
    #cv2.imshow("enhanced",enhanced)
    denoised = cv2.medianBlur(gray, 3)  # o cv2.GaussianBlur(gray, (5,5), 0)
    cv2.imshow("sin ruido",denoised)
    thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("Tresh",thresh)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    cv2.imshow("Kernel",kernel)
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imshow("dilated",dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #****************
    # Usar EasyOCR para analizar el texto de la imagen
    #resultados = reader.readtext(ruta_imagen)
    #resultados = reader.readtext(dilated)
    resultados = reader.readtext(thresh)

    # Mostrar los resultados
    for (bbox, texto, confianza) in resultados:
        print(f"Texto detectado: {texto} (Confianza: {confianza:.2f})")