import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread(r'C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\imagenS\ine_page_1.png')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB para Matplotlib

# Mostrar la imagen con Matplotlib
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la ventana
plt.imshow(imagen)
plt.axis('off')  # Ocultar los ejes
plt.show()