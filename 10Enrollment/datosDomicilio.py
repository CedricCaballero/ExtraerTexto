

class DatosDomicilio:
    def __init__(self,clasificacion):
        self.clasificacion = clasificacion
        self.datosDomicilio = ['TOTAL A PAGAR:','Comisión Federal de Electricidad']
        self.datos_diccionario = {
            'Domicilio': self.datosDomicilio
        }
        self.coorTipoDoc = {
            'Domicilio':[0,60]  
        }
    #**************Calcular porcentajes ********************
    def redondeo_personalizado(self,valor, decimales):
        factor = 10 ** decimales
        return int(valor * factor) / factor
    
    def datoRequerido(self):
        valorResultado = []
        boxAux = []
        texto = ''
        posicionTextoCoor = []
        cont = 0
        cont2 = 0
        valorConcat = ''
        banImpar = 1
        resultClasificacionA = self.clasificacion[0][0][0]
        resultText = self.clasificacion[0][1]
        #print(resultClasificacionA)
        for bbox, txt, prob in resultText:
            if cont == 2:
                if resultClasificacionA == 'Domicilio':
                    if banImpar % 2 != 0 or banImpar == 6:
                        boxAux.append(bbox)
                        valorConcat += txt + ','
                    if(banImpar == 6):
                        valorResultado.append(valorConcat.rstrip(','))
                        valorResultado.append(self.redondeo_personalizado(prob * 100, 2))
                        texto = f'{resultClasificacionA}:{valorConcat} con un {self.redondeo_personalizado(prob * 100, 2)} % de precisión'
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