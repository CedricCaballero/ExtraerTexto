import cv2
import numpy as np
class ImgenGris:
    def __init__(self, imagen):
        self.imagen = imagen
        self.imagen_grisV = None

    def imagen_gris(self):
        if self.imagen.mode == 'RGB':
            image_np = np.array(self.imagen)
            self.imagen_grisV = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        else:
            self.imagen_grisV = self.imagen
        return self.imagen_grisV