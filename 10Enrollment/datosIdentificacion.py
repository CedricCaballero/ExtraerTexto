import cv2
from readImage import readImage
class DatosIdentificacion:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.datosIdentificacion = ['NOMBRE']
        self.datos_diccionario = {
            'Identificacion': self.datosIdentificacion
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
                        incrementoy = 130
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
                        boxAux.append(bbox)
                        valorConcat += txt + ' '
                    if(banImpar == len(resultText) - 1):
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
        return valorResultado