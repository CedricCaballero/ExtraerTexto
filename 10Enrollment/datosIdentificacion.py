
class DatosIdentificacion:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.datosIdentificacion = ['NOMBRE','FECHA DE NACIMIENTO']
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

    #****************Extra informacion solicitada **************
    def datoRequerido(self):
        valorResultado = []
        boxAux = []
        posicionTextoCoor = []
        cont = 0
        valorConcat = ''
        banImpar = 1
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        for bbox, txt, prob in resultText:
            if cont == 2:
                if resultClasificacionA == 'Identificacion':
                    if ((banImpar % 2 != 0 or banImpar == 6) and banImpar != 5):
                        boxAux.append(bbox)
                        valorConcat += txt + ','
                    if(banImpar == 6):
                        valorResultado.append(valorConcat.rstrip(','))
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