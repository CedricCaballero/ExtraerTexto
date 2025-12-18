import fitz  # PyMuPDF
from PIL import Image, ImageDraw
from imagenGris import ImgenGris
from readImage import readImage
from rectanguloINE import RecortarINE
import cv2
class ClasificarDocumentos:
    def __init__(self,list_docs,ruta_salida,archivo=None):
        self.rutaSalida = ruta_salida
        self.archivos = list_docs
        self.archivo = archivo
        #self.resultadoClasificacion = []
        self.todosResultados = []
        self.resultText = None
        #************Arrays de tipos de documentos con sus arrays que lo identifican **************
        self.arrayTipoDoc = ['Aviso','NSS','CURP','Domicilio','Identificacion']
        self.arrayIdentificacion = ['INSTITUTO NACIONAL ELECTORAL','ELECTORAL','VOTAR','CREDENCIAL','INE']
        self.arrayDomicilio = ['CFE','Suministrador','Servicios Básicos','Electricidad','Comisión Federal']
        self.arrayCurp = ['SEGOB','ESTADOS UNIDOS MEXICANOS','CONSTANCIA','CLAVE','ÚNICA','Clave:']
        self.arrayNSS = ['Instiluto Mexicano del Seguro Sucial','Seguro','Sucial','Social','IMSS','Curp']
        self.arrayAvisoEnrrollment = ['VISO','AVISO','PRIVACIDAD','COMUNICACIONES  DIGITALES','IV.','Consentimiento','Posesión','Huellas']
    
    def pdf_to_images(self,pdf_path,nombre):
        # Abre el archivo PDF
        pdf_document = fitz.open(pdf_path)
        resultadoClasificacion = []
        datosReturn = []
        # Itera por todas las páginas
        for page_number in range(len(pdf_document)):
            if page_number == 0:
                page = pdf_document.load_page(page_number)
                mat = fitz.Matrix(3, 3)
                pix = page.get_pixmap(matrix=mat)
                # Convierte la página a una imagen
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                resImaA = ImgenGris(img)
                resIma = resImaA.imagen_gris()
                self.resultText = readImage(resIma).read_Image()
                resultClasificacion = self.clasificar_documento()
                #print(len(self.resultText))
                #print(resultClasificacion)
                '''if 'Identificacion' in resultClasificacion:
                    print('es iden')
                    imaINE = RecortarINE(resIma)
                    imaINEA = imaINE.Recorta()
                    resIma = imaINEA[1]
                    self.resultText = readImage(resIma).read_Image()'''
                
                '''cv2.imshow(f'Recorte ', resIma)
                #cv2.imwrite(f'recorte_{rectangulosEncontrados}.jpg', recorte)
                cv2.waitKey(0)
                cv2.destroyAllWindows()'''
                resultadoClasificacion.append([resultClasificacion,self.resultText,resIma])
                #datos = datoRequerido(resultClasificacion=resultClasificacion,resultText=resultText,img=img)
                #datosReturn.append(resultClasificacion[0])
                #datosReturn.append(datos)

                # Guarda la imagen
                #img.save(f"{output_folder}\\{nombre}_page_{page_number + 1}.png")
                #exit()
        return resultadoClasificacion
    #****************Cuenta coincidencias *******************
    def buscaCoincidencias(self,array):
        conteo = {elemento: 0 for elemento in array}
        for bbox, texto, prob in self.resultText:
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
    #****************Clasifica el documento *****************
    def clasificar_documento(self):
        tipoDoc = {elemento: 0 for elemento in self.arrayTipoDoc}
        tipoDoc['Aviso'] = self.buscaCoincidencias(array=self.arrayAvisoEnrrollment)
        tipoDoc['NSS'] = self.buscaCoincidencias(array=self.arrayNSS)
        tipoDoc['CURP'] = self.buscaCoincidencias(array=self.arrayCurp)
        tipoDoc['Domicilio'] = self.buscaCoincidencias(array=self.arrayDomicilio)
        tipoDoc['Identificacion'] = self.buscaCoincidencias(array=self.arrayIdentificacion)
        #print(tipoDoc)
        resSuma = None
        classDoc = []
        for element, suma in tipoDoc.items():
            if resSuma is None or suma >= resSuma:
                resSuma = suma
                classDoc = [element,resSuma]
        return classDoc
    
    def ClasificarDocs(self):
        for archivo, tipo, nombre in self.archivos:
            #print(f'***************{nombre}************')
            if tipo == 'pdf':
                #self.pdf_to_images(archivo,nombre)
                self.todosResultados.append((self.pdf_to_images(archivo,nombre),nombre))
                
            #else:
                #image = Image.open(archivo)
                #resIma = imagen_gris(image)
                #resultText = readImage(resIma)
                #resultClasificacion = clasificar_documento(resultText)
        #print(resultClasificacion)
        return self.todosResultados