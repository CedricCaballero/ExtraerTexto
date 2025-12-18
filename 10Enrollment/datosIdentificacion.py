import cv2
from readImage import readImage
import copy
from recortaF import RecortadorFirma

class DatosIdentificacion:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.imagenOriginal = copy.deepcopy(clasificacion)
        self.datosIdentificacion = ['NOMBRE']
        self.datosIdentificacionFirma1 = ['NOMBRE','FECHA DE NACIMIENTO','LOCALIDAD','EMISIÓN']
        self.datosIdentificacionFirma2 = ['NOMBRE','SEXO H']
        self.datosFirmaCoor = ['INE','Locales','Loca','IFE','EDMUNDO JACOBO MOLINA']
        self.datos_diccionario = {
            'Identificacion': self.datosIdentificacion,
            'Firma1': self.datosIdentificacionFirma1,
            'Firma2': self.datosIdentificacionFirma2,
            'INE' : self.datosFirmaCoor
        }
        #************Coordenadas para mostrar ******************
        self.coorTipoDoc = {
                'Identificacion':[0,0]    
            }
        
    #**************Calcular porcentajes ********************
    def redondeo_personalizado(self,valor, decimales):
        factor = 10 ** decimales
        return int(valor * factor) / factor
    
    #****************Recortar parte nombre *********************
    def recorteNombre(self):
        valorResultado = []
        #self.imagenOriginal = copy.copy(self.clasificacion)
        #print(self.imagenOriginal[0][1])
        boxAux = []
        cont = 0
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        for bbox, txt, prob in resultText:
            #print(txt)
            if cont == 1:
                if resultClasificacionA == 'Identificacion':
                    #imagen_np = cv2.cvtColor(self.clasificacion[0][2], cv2.COLOR_RGB2BGR)
                    imagen_np = self.clasificacion[0][2]
                    rect_x0 = None
                    rect_y0 = None
                    rect_x1 = None
                    rect_y1 = None
                    for box in boxAux:
                        rect_coords = [(int(coord[0]), int(coord[1])) for coord in box]
                        incremento = 10
                        incrementox = 250
                        incrementoy = 115
                        # Definir el rectángulo utilizando las coordenadas
                        rect_x0 = min(coord[0] for coord in rect_coords) - incremento
                        rect_y0 = min(coord[1] for coord in rect_coords) - incremento
                        rect_x1 = max(coord[0] for coord in rect_coords) + incrementox
                        rect_y1 = max(coord[1] for coord in rect_coords) + incrementoy
                        self.clasificacion[0][2] = imagen_np[rect_y0:rect_y1, rect_x0:rect_x1]
                        '''cv2.rectangle(imagen_np, (rect_x0, rect_y0), (rect_x1, rect_y1), (0, 0, 255), 5)
                        cv2.imshow("Imagen con Rectángulo", imagen_np)
                        cv2.imshow("Imagen con Rectángulo", self.clasificacion[0][2])
                        cv2.waitKey(0)'''
                        self.clasificacion[0][1] = readImage(self.clasificacion[0][2]).read_Image()                       
                        break
                    break
            if txt in self.datos_diccionario.get(resultClasificacionA, []):
                boxAux.append(bbox)
                cont += 1

    #****************Extra informacion solicitada **************
    def datoRequerido(self):
        #print('llega')
        valorResultado = []
        boxAux = []
        posicionTextoCoor = []
        cont = 0
        valorConcat = ''
        banImpar = 1
        #print(self.clasificacion)
        
        
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        
        for bbox, txt, prob in resultText:
            
            if cont == 1:
                if resultClasificacionA == 'Identificacion':
                    if (banImpar < len(resultText)):
                        if txt != 'DOMICILIO':
                            boxAux.append(bbox)
                            valorConcat += txt + ' '
                    if((banImpar == len(resultText) - 1) or (txt == 'DOMICILIO')):
                        valorResultado.append(valorConcat.rstrip(' '))
                        probA = prob * 100
                        valorResultado.append(self.redondeo_personalizado(probA, 2))
                        texto = f'{resultClasificacionA}:{valorConcat} con un {self.redondeo_personalizado(probA, 2)} % de precisión'
                        x,y = self.coorTipoDoc.get(resultClasificacionA, [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        cont = 0
                        break
                    banImpar += 1
            if txt in self.datos_diccionario.get(resultClasificacionA, []):
                boxAux.append(bbox)
                cont += 1
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        #Obtener el tipo de INE que Es

        cont1 = 0
        cont2 = 0
        banIdmex = 0
        valorConcat2 = ''
        bboxFirma1 = None
        tipo = 0
        resultText2 = self.imagenOriginal[0][1]
        imageFirma = copy.deepcopy(self.imagenOriginal[0][2])
        #print(len(resultText2))
        '''cv2.imshow("Imagen con Rectángulo", self.imagenOriginal[0][2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
        for bbox, txt, prob in resultText2:
            #print(txt)
            if txt in self.datos_diccionario.get('Firma1', []):
                boxAux.append(bbox)
                cont1 += 1
            if txt in self.datos_diccionario.get('Firma2', []):
                boxAux.append(bbox)
                cont2 += 1

        
        if cont1 > cont2:
            tipo = 1
        else:
            tipo = 2
        
        #**************  
        for bbox, txt, prob in resultText2:
            if resultClasificacionA == 'Identificacion':
                textoIdmex = txt.replace(' ','')
                if 'CURP' in textoIdmex:
                    if tipo == 2:
                        print("entra tipo 2")
                        bboxFirma1 = bbox
                        #banIdmex = 1
            if cont >= 1:
                #print('Llego')
                if resultClasificacionA == 'Identificacion':
                    if 'IDMEX' in textoIdmex:
                        if tipo == 1:
                            bboxFirma1 = bbox
                        banIdmex = 1
                    if banIdmex != 0:
                        #boxAux.append(bbox)
                        textoIdmex = txt.replace(' ','')
                        valorConcat2 += textoIdmex + '$'
                        banIdmex += 1
                    if banIdmex == 4:
                        valorResultado.append(valorConcat.rstrip(' '))
                        probA = prob * 100
                        valorResultado.append(self.redondeo_personalizado(probA, 2))
                        texto = f'{resultClasificacionA}:{valorConcat} con un {self.redondeo_personalizado(probA, 2)} % de precisión'
                        x,y = self.coorTipoDoc.get(resultClasificacionA, [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        cont = 0
                        break
            if txt in self.datos_diccionario.get('INE', []):
                boxAux.append(bbox)
                cont += 1
        print(tipo)
        if not bboxFirma1:
            print("Esta vacio")
            return valorResultado
            
        '''cv2.imshow("Imagen con Rectángulo", self.imagenOriginal[0][2])
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
        rect_coords = [(int(coord[0]), int(coord[1])) for coord in bboxFirma1]
        '''print(rect_coords)
        pt1 = (979, 459)
        pt2 = (1665, 495)

        # Dibuja el rectángulo sobre la imagen
        imagen_con_rectangulo = self.imagenOriginal[0][2].copy()
        cv2.rectangle(imagen_con_rectangulo, pt1, pt2, color=(0, 255, 0), thickness=2)'''

        # Muestra la imagen con el rectángulo
        '''cv2.imshow("Imagen con Rectángulo", imagen_con_rectangulo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''

        if tipo == 1:
            incrementox0 = 200
            incrementoy0 = 235
            incrementox = 500
            incrementoy = 140
        else:
            incrementox0 = -310
            incrementoy0 = 0
            incrementox = 70
            incrementoy = -110
        # Definir el rectángulo utilizando las coordenadas
        '''rect_x0 = min(coord[0] for coord in rect_coords) + (incrementox0)
        rect_y0 = min(coord[1] for coord in rect_coords) - (incrementoy0)
        rect_x1 = max(coord[0] for coord in rect_coords) - (incrementox)
        rect_y1 = max(coord[1] for coord in rect_coords) - (incrementoy)'''

        rect_x0 = min(coord[0] for coord in rect_coords) + incrementox0
        rect_x1 = max(coord[0] for coord in rect_coords) - incrementox
        if rect_x0 > rect_x1:
            rect_x0, rect_x1 = rect_x1, rect_x0  # intercambia si están invertidos

        rect_y0 = min(coord[1] for coord in rect_coords) - incrementoy0
        rect_y1 = max(coord[1] for coord in rect_coords) - incrementoy
        if rect_y0 > rect_y1:
            rect_y0, rect_y1 = rect_y1, rect_y0


        
        imageFirma = imageFirma[rect_y0:rect_y1, rect_x0:rect_x1]
        '''cv2.imshow("Imagen con Rectángulo", imageFirma)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''

        
        recorte = RecortadorFirma()
        
        recorteFirma = recorte.recortar_firma(imagen_gris=imageFirma)

        valorResultado.append(recorteFirma)
        
        #print(valorConcat2)
        #print(cont2)
        return valorResultado