import cv2
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import img_to_array
from scipy.spatial.distance import euclidean
import os
from pathlib import Path
#*************

def redimensionar_imagenes(carpeta, ancho, alto):
    # Crear una carpeta para las imágenes redimensionadas
    carpeta_redimensionada = os.path.join(carpeta, 'redimensionadas')
    if not os.path.exists(carpeta_redimensionada):
        os.makedirs(carpeta_redimensionada)

    # Iterar sobre los archivos de la carpeta
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)

        # Verificar que sea un archivo de imagen
        if os.path.isfile(ruta_archivo) and archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Cargar la imagen
            imagen = cv2.imread(ruta_archivo)

            # Redimensionar la imagen
            imagen_redimensionada = cv2.resize(imagen, (ancho, alto))

            # Guardar la imagen redimensionada en la carpeta de imágenes redimensionadas
            ruta_guardado = os.path.join(carpeta_redimensionada, archivo)
            cv2.imwrite(ruta_guardado, imagen_redimensionada)
            #print(f'Imagen {archivo} redimensionada y guardada en {ruta_guardado}')

# Ejemplo de uso
'''carpeta_imagenes = './imagen'
ancho_deseado = 300
alto_deseado = 300
redimensionar_imagenes(carpeta_imagenes, ancho_deseado, alto_deseado)
exit()'''
# Función para convertir imagen en escala de grises a RGB
def convertir_a_rgb(imagen):
    return cv2.cvtColor(imagen,  cv2.COLOR_GRAY2RGB)

def main(firmaAviso, firmaIdentificacion):
    # Cargar las imágenes de las firmas
    #firma1 = cv2.imread(r'.\imagen\redimensionadas\fcf3.jpeg', cv2.IMREAD_GRAYSCALE)
    #firma2 = cv2.imread(r'.\imagen\redimensionadas\fcf2.jpeg', cv2.IMREAD_GRAYSCALE)
    firma1 = firmaAviso
    firma2 = firmaIdentificacion
    # Convertir la imagen a RGB
    firma1_rgb = convertir_a_rgb(firma1)
    firma2_rgb = convertir_a_rgb(firma2)
    # Binarizar las imágenes
    #_, firma1_bin = cv2.threshold(firma1, 127, 255, cv2.THRESH_BINARY)
    #_, firma2_bin = cv2.threshold(firma2, 127, 255, cv2.THRESH_BINARY)



    # Cargar el modelo preentrenado VGG16 sin la capa superior (clasificación)
    modelo = VGG16(include_top=False, input_shape=(224, 224, 3))

    # Redimensionar las imágenes a 224x224 píxeles y convertirlas a un array
    firma1_resized = cv2.resize(firma1_rgb, (224, 224))
    firma2_resized = cv2.resize(firma2_rgb, (224, 224))
    firma1_array = img_to_array(firma1_resized)
    firma2_array = img_to_array(firma2_resized)

    # Añadir una dimensión extra para representar el batch size (1 imagen por batch)
    firma1_array = tf.expand_dims(firma1_array, axis=0)
    firma2_array = tf.expand_dims(firma2_array, axis=0)

    # Extraer las características
    caracteristicas_firma1 = modelo.predict(firma1_array)
    caracteristicas_firma2 = modelo.predict(firma2_array)

    distancia = euclidean(caracteristicas_firma1.flatten(), caracteristicas_firma2.flatten())
    #print(distancia)
    # Normalizar la distancia y calcular el porcentaje de similitud
    max_distancia = 1000  # Define un valor máximo para la distancia
    porcentaje_similitud = max(0, 100 - (distancia / max_distancia) * 100)
    resultado = []
    resultado.append(f'{porcentaje_similitud:.2f}%')
    #print(f"Porcentaje de similitud: {porcentaje_similitud:.2f}%")
    print("Si las valido")
    umbral = 1000  # Umbral de distancia para determinar si las firmas son similares
    resSimilares = ''
    if distancia < umbral:
        resSimilares = 'Valida'
        #print("Las firmas son similares.")
    else:
        resSimilares = 'Invalida'
        #print("Las firmas son diferentes.")
    resultado.append(resSimilares)
    #print(resultado)
    return resultado
    '''cv2.imshow('Firma 1', firma1_rgb)
    cv2.imshow('Firma 2', firma2_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''