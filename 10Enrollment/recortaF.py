import cv2

class RecortadorFirma:
    def __init__(self):
        pass

    def recortar_firma(self, imagen_gris):
        """
        Recorta la firma de una imagen en escala de grises.

        Args:
            imagen_gris: La imagen en escala de grises donde buscar la firma.

        Returns:
            firma_recortada: Imagen recortada que contiene la firma.
        """
        h1 = imagen_gris.shape[0]
        w1 = imagen_gris.shape[1]
        margen_w = 0.1
        margen_h = 0.1
        margen_hsuperior = 0.16
        
        '''cv2.imshow("Imagen con Rectángulo", imagen_gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
        # Aplicar un umbral para resaltar los bordes
        _, umbral = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY_INV)

        # Encontrar contornos
        contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Identificar el contorno más grande
        contorno_mayor = max(contornos, key=cv2.contourArea)

        # Obtener el rectángulo delimitador del contorno
        x, y, w, h = cv2.boundingRect(contorno_mayor)

        margen_x = int(w * margen_w)
        margen_y = int(h * margen_h)
        margen_y_superior = int(h*margen_hsuperior)

        x_nuevo = max(0, x - margen_x)
        y_nuevo = max(0, y-margen_y_superior)
        w_nuevo = min(w1 - x_nuevo, w + 2 * margen_x)
        h_nuevo = min(h1-y_nuevo, h + margen_y_superior + margen_y)
        #h_nuevo = h1

        '''x = x - 5
        y = y - int(h/4) + 10
        w = w + 15
        h = h + int(h/4)
        print(w, h)'''
        #
        #  Recortar el área de la firma
        #firma_recortada = imagen_gris[y:y+h, x:x+w]
        firma_recortada = imagen_gris[y_nuevo:y_nuevo+h_nuevo, x_nuevo:x_nuevo+w_nuevo]

        return firma_recortada