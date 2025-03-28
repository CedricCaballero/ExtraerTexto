
class DatosNSS:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.datosNSS = ['AAAA','Número de Seguridad Social:']
        self.datos_diccionario = {
            'NSS': self.datosNSS
        }
        self.coorTipoDoc = {
            'NSS':[200,20]
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
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        for bbox, txt, prob in resultText:
            if cont == 2:
                if resultClasificacionA == 'NSS':
                    valorResultado.append(txt)
                    valorResultado.append(self.redondeo_personalizado(prob * 100, 2))
                    boxAux.append(bbox)
                    texto = f'{resultClasificacionA}:{txt} con un {self.redondeo_personalizado(prob * 100, 2)} % de precisión'
                    x,y = self.coorTipoDoc.get(resultClasificacionA, [])
                    posicionTextoCoor.append(x)
                    posicionTextoCoor.append(y)
                    cont = 0
                    break
            if txt in self.datos_diccionario.get(resultClasificacionA, []):
                boxAux.append(bbox)
                cont += 1
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        return valorResultado