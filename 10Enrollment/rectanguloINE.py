import cv2
import matplotlib.pyplot as plt
# Cargar la imagen

class RecortarINE:
    def __init__(self, pathINE):
        self.pathINE = pathINE
    
    def Recorta(self):
        recortes = []
        imagen = cv2.imread(self.pathINE)
        # Convertir a escala de grises
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Aplicar detección de bordes
        umbral_inferior = 10  # Puedes disminuir o aumentar este valor
        umbral_superior = 100  # Ajusta este valor también para cambiar la sensibilidad
        desenfoque = cv2.GaussianBlur(gris, (5, 11), 0)
        # Aplicar detección de bordes con Canny
        bordes = cv2.Canny(desenfoque, umbral_inferior, umbral_superior)
        # Encontrar contornos
        contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # Umbral mínimo para área del rectángulo
        area_minima = 500  # Ajusta según lo necesites
        rectangulosEncontrados= 0
        # Dibujar solo rectángulos grandes
        for contorno in contornos:
            # Aproximar la forma del contorno
            epsilon = 0.02 * cv2.arcLength(contorno, True)
            aproximacion = cv2.approxPolyDP(contorno, epsilon, True)

            # Verificar si tiene 4 lados (es un rectángulo)
            if len(aproximacion) == 4:
                # Calcular el área del contorno
                area = cv2.contourArea(contorno)
                # Filtrar por área mínima
                if area >= area_minima:
                    rectangulosEncontrados += 1
                    # Obtener las coordenadas del rectángulo
                    x, y, ancho, alto = cv2.boundingRect(aproximacion)
                    # Dibujar el rectángulo en la imagen
                    ###cv2.rectangle(imagen, (x-10, y-10), (x+ancho+20, y+alto+20), (0, 255, 0), 4)  # Verde y grosor 2 px
                    # **Recortar el rectángulo de la imagen**
                    recorte = imagen[y-10:y + alto+20, x-10:x + ancho+20]  # Recorte usando slicing
                    recortes.append(recorte)
                    # Guardar o mostrar el recorte
                    '''cv2.imshow(f'Recorte {rectangulosEncontrados}', recorte)
                    #cv2.imwrite(f'recorte_{rectangulosEncontrados}.jpg', recorte)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()'''

        '''print(rectangulosEncontrados)
        # Mostrar la imagen con los rectángulos dibujados

        plt.figure(figsize=(100, 60))  # Ajustar el tamaño de la ventana
        plt.imshow(imagen)
        plt.axis('off')  # Ocultar los ejes
        plt.show()'''
        return recortes