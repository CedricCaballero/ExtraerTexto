
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
                        boxAux.append(bbox)
                        cont2 += 1
            if txt in self.datos_diccionario.get(resultClasificacionA, []):
                boxAux.append(bbox)
                cont += 1
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        return valorResultado