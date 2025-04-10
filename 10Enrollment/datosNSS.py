
class DatosNSS:
    def __init__(self, clasificacion):
        self.clasificacion = clasificacion
        self.datosNSS = ['AAAA','Número de Seguridad Social:','NSS:','Social es:','tu Número de Seguridad']
        self.datosNSS2 = ['Tarjeta de Número de Seguridad Social','tu Número de Seguridad']
        self.datos_diccionario = {
            'NSS': self.datosNSS,
            'NSS2': self.datosNSS2
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
            #print(txt)
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
                #print(txt)
                boxAux.append(bbox)
                cont += 1
        cont = 0
        if len(valorResultado) == 0:
            for bbox, txt, prob in resultText:
                #print(txt)
                if cont == 2:
                    if resultClasificacionA == 'NSS':
                        txt2 = None
                        if ':' in txt:
                            txt2 = txt.split(':')[1].strip()
                        valorResultado.append(txt2)
                        valorResultado.append(self.redondeo_personalizado(prob * 100, 2))
                        boxAux.append(bbox)
                        texto = f'{resultClasificacionA}:{txt2} con un {self.redondeo_personalizado(prob * 100, 2)} % de precisión'
                        x,y = self.coorTipoDoc.get(resultClasificacionA, [])
                        posicionTextoCoor.append(x)
                        posicionTextoCoor.append(y)
                        cont = 0
                        break
                if txt in self.datos_diccionario.get('NSS2', []):
                    #print(txt)
                    boxAux.append(bbox)
                    cont += 1

        #print(valorResultado)
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        return valorResultado