import comparaFirma
import pandas as pd
from datetime import datetime

class comparacionResultados:
    def __init__(self, dfcompleto,datosResult,diasDiferencia,firmaAviso,firmaidentificacion):
        self.firmaidentificacion = firmaidentificacion
        self.firmaAviso = firmaAviso
        self.diasDiferencia = diasDiferencia
        self.dfcompleto = dfcompleto
        self.datosresult = datosResult
        self.aceptacionDomicilio = 70.0
        self.aceptacionidentificacion = 70.0
        self.abreviaturas = {
                'PRIVADA': 'PRIV',
                'HIDALGO': 'HGO',
                'TIZAYUCA': 'TIZAYUCAC',
                'FRACCIONAMIENTO': 'FRACC',
            }
        self.diccionario_Prueba = {
                'NSS': '01139309726',
                'CURP': 'CABC930627HOCBTDO7',
                'Domicilio': 'Privada Malva Oriente Mz9 Lt6, Tizara Town, C.P. 43816, Tizayuca, Hidalgo.',
                'Identificacion': 'Cedric Omar Caballero Bautista',
                'Aviso':'Cedric Omar Caballero Bautista',
                'Aviso2':'25/03/2025'
            }
    def calcular_dias_diferencia(self,fecha1, fecha2):
        formatos = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"]  # Formatos comunes
        for formato in formatos:
            try:
                fecha1_obj = datetime.strptime(fecha1, formato)
                fecha2_obj = datetime.strptime(fecha2, formato)
                diferencia = abs((fecha2_obj - fecha1_obj).days)  # Diferencia en días
                return diferencia
            except ValueError:
                continue
        raise ValueError("No se pudieron interpretar las fechas con los formatos comunes.")


    def es_fecha_valida(self,cadena):
        formatos = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"]
        for formato in formatos:
            try:
                datetime.strptime(cadena,formato)
                return True
            except ValueError:
                pass
        return False

    #*****************Comparar extraccion con referencia***********
    def actualizar_estatus(self,row):
        if row['Referencia'].strip() == 'FIRMA':
            return row['Estatus'].strip()
        else:
            if row['Documento'].strip() == 'Domicilio':
                return row['Estatus'].strip()
            else:
                if row['Documento'].strip() == 'Identificacion':
                    return row['Estatus'].strip()
                else:
                    if row['Documento'].strip() == 'Aviso':
                        if self.es_fecha_valida(row['Referencia'].strip()):
                            if self.es_fecha_valida(row['Extracción'].strip()):
                                try:
                                    dias_diferencia = self.calcular_dias_diferencia(row['Referencia'].strip(), row['Extracción'].strip())
                                    if(dias_diferencia <= self.diasDiferencia):
                                        return 'Aceptado'
                                    else:
                                        return 'Rechazado'
                                except ValueError as e:
                                        print(f"Error: {e}")
                        else:
                            if row['Referencia'].strip() == row['Extracción'].strip():
                                return 'Aceptado'
                            else:
                                return 'Rechazado'
                        return row['Estatus'].strip()
                    else:
                        if row['Referencia'].strip() == row['Extracción'].strip():
                            return 'Aceptado'
                        else:
                            return 'Rechazado'

    #*****************Funciones, diccionarios y vareiables para domicilio ********************
    def estandarizar(self,lista, diccionario):
        lista_estandarizada = []
        for palabra in lista:
            # Verificar si la palabra tiene una equivalencia en el diccionario
            estandarizada = [key for key, value in diccionario.items() if palabra == value]
            lista_estandarizada.append(estandarizada[0] if estandarizada else palabra)
        return lista_estandarizada

    def compara(self):
        doc = []
        referencia = []
        extraccion = []
        presicion = []
        estatus = []
        fecha = ''
        proba = 0
        for res in self.datosresult:
            #print(res)
            if (res[0] == 'Aviso'):
                index = 0
                #print(res[1])
                for val in res[1]:
                    #print(val)
                    if index >= 1:
                        fecha += val[0] +'/'
                        proba += val[1]
                    if index == 0:
                        doc.append(res[0])
                        referencia.append(self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "Aviso", ["FULLNAME"]].values[0][0])
                        extraccion.append(val[0])
                        presicion.append(val[1])
                        if val[1]> 95.0:
                            estatus.append('Aceptado')
                        else:
                            estatus.append('Rechazado')
                        #print(val)
                    if index == 3:
                        doc.append(res[0])
                        fecha_hoy = datetime.now()
                        referencia.append(fecha_hoy.strftime("%d/%m/%Y"))
                        extraccion.append(fecha.rstrip('/'))
                        presicion.append(f"{proba/3:.2f}")
                        if val[1]> 95.0:
                            estatus.append('Aceptado')
                        else:
                            estatus.append('Rechazado')
                    index += 1
            else:
                if (res[0] == "Domicilio"):
                    doc.append(res[0])
                    reemplazos = str.maketrans({',': ' ', '.': ' '})
                    dom = self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "Domicilio", ["COUNTRY","NEIGHBORHOOD","MUNICIPALITY","NO_EXT","NO_INT","POSTAL_CODE","STATE","STREET"]]
                    domicilio = dom["COUNTRY"]+" "+dom["NEIGHBORHOOD"]+" "+dom["MUNICIPALITY"]+" "+dom["NO_EXT"]+" "+dom["NO_INT"]+" "+dom["POSTAL_CODE"]+" "+dom["STATE"]+" "+dom["STREET"]
                    
                    domicilio_ref = domicilio.values[0].translate(reemplazos).strip()
                    domicilio_ref = domicilio_ref.upper()
                    domicilio_ref = [elemento for elemento in domicilio_ref.split(' ') if elemento]
                    referencia.append(domicilio.values[0])
                    domicilio_Ext = res[1][0].translate(reemplazos).strip()
                    domicilio_Ext = domicilio_Ext.upper()
                    domicilio_Ext = [elemento for elemento in domicilio_Ext.split(' ') if elemento]

                    # Estandarizar ambos arrays
                    domicilio_ref_estandarizado = set(self.estandarizar(domicilio_ref, self.abreviaturas))
                    domicilio_Ext_estandarizado = set(self.estandarizar(domicilio_Ext, self.abreviaturas))

                    # Contar elementos iguales
                    iguales = domicilio_ref_estandarizado.intersection(domicilio_Ext_estandarizado)
                    cantidad_iguales = len(iguales)

                    # Calcular porcentaje de similitud
                    total_elementos = len(domicilio_ref_estandarizado.union(domicilio_Ext_estandarizado))
                    porcentaje_similitud = (cantidad_iguales / total_elementos) * 100
                    extraccion.append(res[1][0])
                    presicion.append(f"{porcentaje_similitud:.2f}")
                    if porcentaje_similitud> self.aceptacionDomicilio:
                        estatus.append('Aceptado')
                    else:
                        estatus.append('Rechazado')
                else:
                    if (res[0] == "Identificacion"):
                        doc.append(res[0])
                        reemplazos = str.maketrans({',': ' ', '.': ' '})
                        identificacion_ref = self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "Identificacion", ["FULLNAME"]].values[0][0].translate(reemplazos).strip()
                        identificacion_ref = identificacion_ref.upper()
                        identificacion_ref = [elemento for elemento in identificacion_ref.split(' ') if elemento]
                        referencia.append(self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "Identificacion", ["FULLNAME"]].values[0][0])
                        identificacion_Ext = res[1][0].translate(reemplazos).strip()
                        identificacion_Ext = identificacion_Ext.upper()
                        identificacion_Ext = [elemento for elemento in identificacion_Ext.split(' ') if elemento]
                        # Contar elementos iguales
                        iguales = list(set(identificacion_ref) & set(identificacion_Ext))
                        cantidad_iguales = len(iguales)

                        # Calcular porcentaje de similitud
                        total_elementos = len(set(identificacion_ref) | set(identificacion_Ext))
                        porcentaje_similitud = (cantidad_iguales / total_elementos) * 100
                        extraccion.append(res[1][0])
                        presicion.append(f"{porcentaje_similitud:.2f}")
                        if porcentaje_similitud> self.aceptacionidentificacion:
                            estatus.append('Aceptado')
                        else:
                            estatus.append('Rechazado')
                    else:
                        if (res[0] == "CURP"):
                            doc.append(res[0])
                            referencia.append(self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "CURP", ["CURP"]].values[0][0])
                            aux = res[1]
                            #if (len(aux) > 0):
                            extraccion.append(aux[0])
                            presicion.append(aux[1])
                            if aux[1]> 95.0:
                                estatus.append('Aceptado')
                            else:
                                estatus.append('Rechazado')
                        else:
                            if (res[0] == "NSS"):
                                doc.append(res[0])
                                referencia.append(self.dfcompleto.loc[self.dfcompleto["Tipo Documento"] == "NSS", ["NOSS"]].values[0][0])
                                aux = res[1]
                                #if (len(aux) > 0):
                                extraccion.append(aux[0])
                                presicion.append(aux[1])
                                if aux[1]> 95.0:
                                    estatus.append('Aceptado')
                                else:
                                    estatus.append('Rechazado')
                            else:
                                doc.append(res[0])
                                referencia.append(self.diccionario_Prueba.get(res[0],[]))
                                aux = res[1]
                                #if (len(aux) > 0):
                                extraccion.append(aux[0])
                                presicion.append(aux[1])
                                if aux[1]> 95.0:
                                    estatus.append('Aceptado')
                                else:
                                    estatus.append('Rechazado')
                                
        if ('Aviso' in doc) & ('Identificacion' in doc):
            resultFirma = comparaFirma.main(firmaIdentificacion=self.firmaidentificacion,firmaAviso=self.firmaAviso)
            doc.append('Aviso')
            referencia.append('FIRMA')
            extraccion.append(resultFirma[1])
            presicion.append(resultFirma[0])
            if resultFirma[1] == 'Valida':
                estatus.append('Aceptado')
            else:
                estatus.append('Rechazado')

        conjuntoDatos = {
            'Documento':doc,
            'Referencia':referencia,
            'Extracción':extraccion,
            'Presición %':presicion,
            'Estatus':estatus
        }
        df = pd.DataFrame(conjuntoDatos)
        #print(df)
        df['Estatus'] = df.apply(self.actualizar_estatus, axis=1)
        return df
        #print(df)