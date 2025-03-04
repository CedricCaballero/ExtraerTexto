import easyocr
from PIL import Image, ImageDraw
import pytesseract
import cv2
import numpy as np
import time
import re
import torch
from dateutil.parser import parse
import sys
import json
import logging
import warnings
import os
import glob
from decimal import Decimal, getcontext
import fitz  # PyMuPDF
import pandas as pd


#************Ruta Ruta *******************
ruta = r'C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos'
rutaSalida = ruta+r'\imagenS'
#************Arrays de tipos de documentos con sus arrays que lo identifican **************
arrayTipoDoc = ['Aviso','NSS','CURP','Domicilio','Identifiacion']
arrayIdentificacion = ['INSTITUTO NACIONAL ELECTORAL','ELECTORAL','VOTAR','CREDENCIAL','INE']
arrayDomicilio = ['CFE','Suministrador','Servicios Básicos','Electricidad','Comisión Federal']
arrayCurp = ['SEGOB','ESTADOS UNIDOS MEXICANOS','CONSTANCIA','CLAVE','ÚNICA','Clave:']
arrayNSS = ['Instiluto Mexicano del Seguro Sucial','Seguro','Sucial','Social','IMSS','Curp']
arrayAvisoEnrrollment = ['AVISO','PRIVACIDAD','COMUNICACIONES  DIGITALES','IV.','Consentimiento','Posesión','Huellas']
#************Array de cada uno de los elementos para identificar y extraer el dato*********************
datosNSS = ['AAAA','Número de Seguridad Social:']
datosCURP = ['Clave:','REGISTRO NACIONAL DE POBLACIÓN']
datosDomicilio = ['TOTAL A PAGAR:','Comisión Federal de Electricidad']
datosIdentifiacion = ['NOMBRE','FECHA DE NACIMIENTO']
datosAviso1 = ['Huellas','Yo;']
datosAviso2 = ['VI. Medios y procedimiento para revocar el consentimiento y ejercer','Nombre:']



#************Coordenadas para mostrar ******************
coorTipoDoc = {
    'Aviso':[0,0],
    'NSS':[200,20],
    'CURP':[0,90],
    'Domicilio':[0,60],
    'Identifiacion':[-120,-120]    
}
datos_diccionario = {
    'NSS': datosNSS,
    'CURP': datosCURP,
    'Domicilio': datosDomicilio,
    'Identifiacion': datosIdentifiacion,
    'Aviso':datosAviso1,
    'Aviso2':datosAviso2
}

diccionario_Prueba = {
    'NSS': '01139309726',
    'CURP': 'CABC930627HOCBTDO7',
    'Domicilio': 'Privada Malva Oriente Mz9 Lt6, Tizara Town, C.P. 43816, Tizayuca, Hidalgo.',
    'Identifiacion': 'Cedric Omar Caballero Bautista',
    'Aviso':'Cedric Omar Caballero Bautista',
    'Aviso2':'03/03/2025'
}
#************OCR ************************
pytesseract.pytesseract.tesseract_cmd = r'C:\tesseract\tesseract.exe'
custom_config = r'--oem 3 --psm 12 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
# Crea un lector especificando el idioma
reader = easyocr.Reader(['es'],gpu=True)

#************ Funciones de OCR ***********
#Analiza la imagen
def readImage(image):
     results = reader.readtext(image)
     #printResults(results)
     #exit()
     return results;
def readImageTesseract(image):
     return  pytesseract.image_to_string(image,lang='spa',config=custom_config)
def printResults(results):
    for bbox,text,prob in results:
        print(f'{text}:{prob}')
#*************Convierte a escala de grises ************
def imagen_gris(imagen):
    if imagen.mode == 'RGB':
        image_np = np.array(imagen)
        imagen_gris = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    else:
        imagen_gris = imagen
    return imagen_gris

#**************Lista los archivos de la ruta *****************
def listar_archivos(ruta):
    # Patrones para archivos PDF e imágenes
    patrones = ["*.pdf", "*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tiff"]
    archivos = []
    for patron in patrones:
        archivos2 = glob.glob(os.path.join(ruta, patron))
        for archivo in archivos2:
            extension = os.path.splitext(archivo)[1].lower()
            nombre = os.path.splitext(os.path.basename(archivo))[0]
            if extension == ".pdf":
                tipo = "PDF"
            elif extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
                tipo = "Imagen"
            archivos.append((archivo, tipo,nombre))
    return archivos

#****************Cuenta coincidencias *******************
def buscaCoincidencias(result,array):
    conteo = {elemento: 0 for elemento in array}
    for bbox, texto, prob in result:
        #print(f'{texto} : {prob}')
        for elemento in array:
            if elemento in texto:
                conteo[elemento] += 1
                #print(f'{texto} : {prob}')
    suma = 0
    for elemento, cantidad in conteo.items():
        suma += cantidad
        #print(f"{elemento}: {cantidad}")
    return suma
#**************Calcular porcentajes ********************
def redondeo_personalizado(valor, decimales):
    factor = 10 ** decimales
    return int(valor * factor) / factor

#****************Muestra la imagen *************************
def mostrarImagen(img,boxAux,texto,px,py):
    imagen_np = np.array(img)
    imagen_np = cv2.cvtColor(imagen_np, cv2.COLOR_RGB2BGR)
    rect_x0 = None
    rect_y0 = None
    rect_x1 = None
    rect_y1 = None
    for box in boxAux:
        rect_coords = [(int(coord[0]), int(coord[1])) for coord in box]
        incremento = 5
        # Definir el rectángulo utilizando las coordenadas
        rect_x0 = min(coord[0] for coord in rect_coords) - incremento
        rect_y0 = min(coord[1] for coord in rect_coords) - incremento
        rect_x1 = max(coord[0] for coord in rect_coords) + incremento
        rect_y1 = max(coord[1] for coord in rect_coords) + incremento
        #draw = ImageDraw.Draw(img)
        #draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], outline="red", width=5)
        #img.show()
        cv2.rectangle(imagen_np, (rect_x0, rect_y0), (rect_x1, rect_y1), (0, 0, 255), 5)
        cv2.imshow("Imagen con Rectángulo", imagen_np)
        cv2.waitKey(0)
    posicion_texto = (rect_x0+px, rect_y0+py)  # Coordenadas (x, y) para la posición del texto
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(imagen_np, texto, posicion_texto, font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Imagen con Rectángulo", imagen_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#****************Extra informacion solicitada **************
def datoRequerido(resultClasificacion,resultText,img):
    valorResultado = []
    boxAux = []
    texto = ''
    posicionTextoCoor = []
    cont = 0
    cont2 = 0
    valorConcat = ''
    banImpar = 1
    #print(resultClasificacion[0])
    for bbox, txt, prob in resultText:
        #print(f"'{txt}'")
        #print(f'{txt in datosNSS}')
        #print('cont:',cont)
        if cont == 2:
            #print('Sigue 2')
            if resultClasificacion[0] == 'Domicilio':
                #print('ban:',banImpar)
                if banImpar % 2 != 0 or banImpar == 6:
                    boxAux.append(bbox)
                    valorConcat += txt + ','
                if(banImpar == 6):
                    valorResultado.append(valorConcat.rstrip(','))
                    valorResultado.append(redondeo_personalizado(prob * 100, 2))
                    texto = f'{resultClasificacion[0]}:{valorConcat} con un {redondeo_personalizado(prob * 100, 2)} % de precisión'
                    x,y = coorTipoDoc.get(resultClasificacion[0], [])
                    posicionTextoCoor.append(x)
                    posicionTextoCoor.append(y)
                    cont = 0
                    break
                banImpar += 1
            else:
                if resultClasificacion[0] == 'Identifiacion':
                    #print('ban:',banImpar)
                    if ((banImpar % 2 != 0 or banImpar == 6) and banImpar != 5):
                        boxAux.append(bbox)
                        valorConcat += txt + ','
                    if(banImpar == 6):
                        valorResultado.append(valorConcat.rstrip(','))
                        valorResultado.append(redondeo_personalizado(prob * 100, 2))
                        texto = f'{resultClasificacion[0]}:{valorConcat} con un {redondeo_personalizado(prob * 100, 2)} % de precisión'
                        x,y = coorTipoDoc.get(resultClasificacion[0], [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        cont = 0
                        break
                    banImpar += 1
                else:
                    if resultClasificacion[0] == 'Aviso':
                        #print('ban:',banImpar)
                        if(banImpar == 1):
                            boxAux.append(bbox)
                            valorConcat += txt 
                            valorResultado.append([valorConcat,redondeo_personalizado(prob * 100, 2)])
                            #valorResultado.append(redondeo_personalizado(prob * 100, 2))
                            texto = f'{resultClasificacion[0]}:{valorConcat} con un {redondeo_personalizado(prob * 100, 2)} % de precisión'
                            x,y = coorTipoDoc.get(resultClasificacion[0], [])
                            posicionTextoCoor.append(x)
                            posicionTextoCoor.append(y)
                            #****************************
                        banImpar += 1
                        if cont2 >= 8:
                            cont = 0
                            break
                        if cont2 >= 2 and cont2 != 3 and cont2 != 4:
                            ##print(txt)
                            valorResultado.append([txt,redondeo_personalizado(prob * 100, 2)])
                            #valorResultado.append(redondeo_personalizado(prob * 100, 2))
                            cont2 += 1
                        else:
                            if cont2 >= 2:
                                cont2 += 1
                        
                        if txt in datos_diccionario.get('Aviso2'):
                            boxAux.append(bbox)
                            cont2 += 1
                        
                    else:
                        valorResultado.append(txt)
                        valorResultado.append(redondeo_personalizado(prob * 100, 2))
                        boxAux.append(bbox)
                        texto = f'{resultClasificacion[0]}:{txt} con un {redondeo_personalizado(prob * 100, 2)} % de precisión'
                        x,y = coorTipoDoc.get(resultClasificacion[0], [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        cont = 0
                        break
        if txt in datos_diccionario.get(resultClasificacion[0], []):
            boxAux.append(bbox)
            cont += 1
    #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
    return valorResultado
    
#****************Clasifica el documento *****************
def clasificar_documento(result):
    tipoDoc = {elemento: 0 for elemento in arrayTipoDoc}
    tipoDoc['Aviso'] = buscaCoincidencias(result=result,array=arrayAvisoEnrrollment)
    tipoDoc['NSS'] = buscaCoincidencias(result=result,array=arrayNSS)
    tipoDoc['CURP'] = buscaCoincidencias(result=result,array=arrayCurp)
    tipoDoc['Domicilio'] = buscaCoincidencias(result=result,array=arrayDomicilio)
    tipoDoc['Identifiacion'] = buscaCoincidencias(result=result,array=arrayIdentificacion)
    #print(tipoDoc)
    resSuma = None
    classDoc = []
    for element, suma in tipoDoc.items():
        if resSuma is None or suma >= resSuma:
            resSuma = suma
            classDoc = [element,resSuma]
    return classDoc

#**************PDF a imagen - analiza ****************
def pdf_to_images(pdf_path,nombre,output_folder):
    # Abre el archivo PDF
    pdf_document = fitz.open(pdf_path)
    
    datosReturn = []
    # Itera por todas las páginas
    for page_number in range(len(pdf_document)):
        if page_number == 0:
            page = pdf_document.load_page(page_number)
            mat = fitz.Matrix(3, 3)
            pix = page.get_pixmap(matrix=mat)

            # Convierte la página a una imagen
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            resIma = imagen_gris(img)
            resultText = readImage(resIma)
            resultClasificacion = clasificar_documento(resultText)
            #print(resultClasificacion)
            datos = datoRequerido(resultClasificacion=resultClasificacion,resultText=resultText,img=img)
            datosReturn.append(resultClasificacion[0])
            datosReturn.append(datos)

            # Guarda la imagen
            #img.save(f"{output_folder}\\{nombre}_page_{page_number + 1}.png")
    return datosReturn
    
#*****************Comparar extraccion con referencia***********
def actualizar_estatus(row):
    if row['Referencia'].strip() == row['Extracción'].strip():
        return 'Aceptado'
    else:
        return 'Rechazado'

#******************Inicia el proceso *******************
archivos = listar_archivos(ruta+r'\documentosE')
# Imprimir la lista de archivos
todosResultados = []
for archivo, tipo, nombre in archivos:
    #print(f'***************{nombre}************')
    if tipo == 'PDF':
        resultado = pdf_to_images(archivo,nombre,rutaSalida)
        todosResultados.append(resultado)
        #print(resultado)
    else:
        image = Image.open(archivo)
        resIma = imagen_gris(image)
        resultText = readImage(resIma)
        resultClasificacion = clasificar_documento(resultText)
        #print(resultClasificacion)

doc = []
referencia = []
extraccion = []
presicion = []
estatus = []
fecha = ''
proba = 0
for res in todosResultados:
    if (res[0] == 'Aviso'):
        index = 0
        for val in res[1]:
            if index > 1:
                fecha += val[0] +'/'
                proba += val[1]
            else:
                doc.append(res[0])
                referencia.append(diccionario_Prueba.get(res[0],[]))
                extraccion.append(val[0])
                presicion.append(val[1])
                if val[1]> 95.0:
                    estatus.append('Aprovado')
                else:
                    estatus.append('Rechazado')
                #print(val)
            if index == 4:
                doc.append(res[0])
                referencia.append(diccionario_Prueba.get('Aviso2'))
                extraccion.append(fecha.rstrip('/'))
                presicion.append(proba/3)
                if val[1]> 95.0:
                    estatus.append('Aprovado')
                else:
                    estatus.append('Rechazado')
            index += 1
    else:
        doc.append(res[0])
        referencia.append(diccionario_Prueba.get(res[0],[]))
        aux = res[1]
        extraccion.append(aux[0])
        presicion.append(aux[1])
        if aux[1]> 95.0:
            estatus.append('Aprovado')
        else:
            estatus.append('Rechazado')

conjuntoDatos = {
    'Documento':doc,
    'Referencia':referencia,
    'Extracción':extraccion,
    'Presición %':presicion,
    'Estatus':estatus
}
df = pd.DataFrame(conjuntoDatos)
#print(df)
df['Estatus'] = df.apply(actualizar_estatus, axis=1)

print(df)
    