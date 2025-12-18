

class DatosDomicilio:
    def __init__(self,clasificacion):
        self.clasificacion = clasificacion
        #self.datosDomicilio = ['TOTAL A PAGAR:','Comisión Federal de Electricidad']
        self.datosDomicilio = ['CFE','Comisión Federal de Electricidad','CFE Suministrador de Servicios Básicos','TOTAL A PAGAR:']
        self.datosDescartar = ['(',')','$']
        self.datos_diccionario = {
            'Domicilio': self.datosDomicilio,
            'Descartar': self.datosDescartar
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
        for bbox, txt, prob in resultText:
            cont2 += 1
            #print(txt)
            #print(bbox)
            #print(bbox[0][0])
            if cont == 4:
                if resultClasificacionA == 'Domicilio':
                    #print(banImpar)
                    if (cont2 == 2):
                        continue
                    if any(caracter in txt for caracter in self.datos_diccionario.get('Descartar', [])):
                        continue
                    if banImpar == 5:
                        if bbox[0][0] > 600:
                            banImpar = 6
                    if (banImpar < 6):
                        boxAux.append(bbox)
                        valorConcat += txt + ','
                    
                    if(banImpar == 6):
                        #if bbox > 500:
                            
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
            
        print(valorConcat)
        print(valorResultado)
        #mostrarImagen(img=img,boxAux=boxAux,texto=texto,px=posicionTextoCoor[0],py=posicionTextoCoor[1])
        return valorResultado