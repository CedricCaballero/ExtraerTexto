import cv2

class DatosAviso:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.datosAviso1 = ['Consentimiento','fotografia','Huellas','Yo;']
        self.datosAviso2 = ['Firma:','Fecha:']
        self.coorTipoDoc = {
            'Aviso':[0,0]   
        }
        self.datos_diccionario = {
            'Aviso':self.datosAviso1,
            'Aviso2':self.datosAviso2
        }
    #**************Calcular porcentajes ********************
    def redondeo_personalizado(self,valor, decimales):
        factor = 10 ** decimales
        return int(valor * factor) / factor
    
    def getClasificacion(self):
        return self.clasificacion
    #****************Extra informacion solicitada **************
    def datoRequerido(self):
        valorResultado = []
        boxAux = []
        posicionTextoCoor = []
        cont = 0
        cont2 = 0
        valorConcat = ''
        banImpar = 1
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        for bbox, txt, prob in resultText:
            if cont == 2:
                if resultClasificacionA == 'Aviso':
                    if(banImpar == 1):
                        boxAux.append(bbox)
                        valorConcat += txt 
                        valorResultado.append([valorConcat,self.redondeo_personalizado(prob * 100, 2)])
                        texto = f'{resultClasificacionA}:{valorConcat} con un {self.redondeo_personalizado(prob * 100, 2)} % de precisión'
                        x,y = self.coorTipoDoc.get(resultClasificacionA, [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        #****************************
                    banImpar += 1
                    if cont2 >= 5:
                        cont = 0
                        break
                    #if cont2 >= 2 and cont2 != 3 and cont2 != 4:
                    if cont2 >= 2:
                        valorResultado.append([txt,self.redondeo_personalizado(prob * 100, 2)])
                        cont2 += 1
                    else:
                        if cont2 >= 2:
                            cont2 += 1
                    if txt in self.datos_diccionario.get('Aviso2'):
                        if txt == 'Firma:':
                            imagen_np = self.clasificacion[0][2]
                            rect_x0 = None
                            rect_y0 = None
                            rect_x1 = None
                            rect_y1 = None
                            
                            rect_coords = [(int(coord[0]), int(coord[1])) for coord in bbox]
                            incrementox0 = 40
                            incrementoy0 = 90
                            incrementox = 550
                            incrementoy = 50
                            # Definir el rectángulo utilizando las coordenadas
                            rect_x0 = min(coord[0] for coord in rect_coords) + incrementox0
                            rect_y0 = min(coord[1] for coord in rect_coords) - incrementoy0
                            rect_x1 = max(coord[0] for coord in rect_coords) + incrementox
                            rect_y1 = max(coord[1] for coord in rect_coords) + incrementoy
                            self.clasificacion[0][2] = imagen_np[rect_y0:rect_y1, rect_x0:rect_x1]
                            '''cv2.rectangle(imagen_np, (rect_x0, rect_y0), (rect_x1, rect_y1), (0, 0, 255), 5)
                            cv2.imshow("Imagen con Rectángulo", imagen_np)
                            cv2.imshow("Imagen con Rectángulo", self.clasificacion[0][2])
                            cv2.waitKey(0)'''
                            
                        boxAux.append(bbox)
                        cont2 += 1
            if txt in self.datos_diccionario.get(resultClasificacionA, []):
                boxAux.append(bbox)
                cont += 1
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        return valorResultado