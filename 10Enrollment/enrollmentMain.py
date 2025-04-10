#import analizaFile
import pandas as pd
import os
import cv2
from obtenerDocumentos import Documentos
from clasificarDocumento import ClasificarDocumentos
from datosIdentificacion import DatosIdentificacion
from datosDomicilio import DatosDomicilio
from datosNSS import DatosNSS
from datosCurp import DatosCurp
from datosAviso import DatosAviso
from conexionDB import ConexionBaseDatos
from comparacionResultados import comparacionResultados
#************Ruta Ruta *******************
ruta = r'C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosE'
rutaSalida = ruta+r'\imagenS'
todosResultados = []
dfCompleto = pd.DataFrame()
list_Docs = []
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
imga = None
diasDiferencia = 7

if __name__ == "__main__":

    #Creamos la conexion de base de datos
    db = ConexionBaseDatos()
    conec = db.conectar()
    #print(conec)
    if conec:
        tabla = "APPENROLLMENT.PERSON"
        query = "SELECT p.ID , (p.NAME||' '||p.FIRST_LAST_NAME||' '||p.SECOND_LAST_NAME) AS FULLNAME, p.CURP,p.NOSS, a.COUNTRY,a.NEIGHBORHOOD,a.MUNICIPALITY,a.NO_EXT,a.NO_INT,a.POSTAL_CODE,a.STATE,a.STREET, p.ADDRESS_ID "+"FROM APPENROLLMENT.PERSON p "+"INNER JOIN APPENROLLMENT.ADDRESS a " +"on a.ID = p.ADDRESS_ID " +"WHERE P.PENDING_OPERATION = :PENDING"
        parametros = {'PENDING':'CREATE'}
        column_names, resultado = db.ejecutar_query(query=query,tabla=tabla,parametros=parametros)
        df = pd.DataFrame(resultado, columns=column_names)        
         
        for index, row in df.iterrows():
            #print(row['ID'])
            #if index == 0:
            if 'A' == 'A':
                #print(row['ID'])
                query = "SELECT CREATED_DATE,DIRECTORY,FILE_NAME ,EXTENSION, DOCUMENT_TYPE_ID FROM APPENROLLMENT.UPLOADED_DOCUMENT ud WHERE ud.PERSON_ID = :PERSON_ID"
                parametros = {'PERSON_ID':row['ID']}
                column_namesDoc, resultadoDoc = db.ejecutar_query(query=query,tabla=tabla,parametros=parametros)
                dfDoc = pd.DataFrame(resultadoDoc, columns=column_namesDoc)
                if len(dfDoc) > 0:
                    for indexj, row2 in dfDoc.iterrows():
                        #print(row2['DOCUMENT_TYPE_ID'])
                        nueva_fila = pd.DataFrame(row).T
                        nueva_fila2 = pd.DataFrame(row2).T
                        nueva_fila2['ID'] = row['ID']
                        if row2['DOCUMENT_TYPE_ID'] == 4:
                            nueva_fila2['Tipo Documento'] = 'Identificacion'
                        if row2['DOCUMENT_TYPE_ID'] == 5:
                            nueva_fila2['Tipo Documento'] = 'CURP'
                        if row2['DOCUMENT_TYPE_ID'] == 6:
                            nueva_fila2['Tipo Documento'] = 'NSS'
                        if row2['DOCUMENT_TYPE_ID'] == 7:
                            nueva_fila2['Tipo Documento'] = 'Domicilio'
                        if row2['DOCUMENT_TYPE_ID'] == 8:
                            nueva_fila2['Tipo Documento'] = 'Aviso'
                        dfCompletoAux = pd.merge(nueva_fila,nueva_fila2, on='ID', how='outer')
                        dfCompleto = pd.concat([dfCompleto,dfCompletoAux],ignore_index=True)
            
            
                    for indexi, rowR in dfCompleto.iterrows():
                        if rowR['EXTENSION'] == 'pdf':
                            rutaFull = ruta + '\\' + rowR['DIRECTORY'] + '\\' + rowR['FILE_NAME'] + '.'+rowR['EXTENSION']
                            if os.path.isfile(rutaFull):
                                rutaFull = ruta + '\\' + rowR['DIRECTORY'] + '\\' + rowR['FILE_NAME'] + '.'+rowR['EXTENSION']
                                list_Docs.append((rutaFull, 'PDF',rowR['FILE_NAME']))
                                #rutaFull = ruta + '\\' + rowR['DIRECTORY']
                
                    #Docs = Documentos(pathFile=rutaFull)
                    #list_Docs = Docs.listar_archivos()
                    '''print(dfCompleto.columns)
                    dom = dfCompleto.loc[dfCompleto["Tipo Documento"] == "Domicilio", ["COUNTRY","NEIGHBORHOOD","MUNICIPALITY","NO_EXT","NO_INT","POSTAL_CODE","STATE","STREET"]]
                    domicilio = dom["COUNTRY"]+" "+dom["NEIGHBORHOOD"]+" "+dom["MUNICIPALITY"]+" "+dom["NO_EXT"]+" "+dom["NO_INT"]+" "+dom["POSTAL_CODE"]+" "+dom["STATE"]+" "+dom["STREET"]
                    domicilio.values[0]
                    #print(dom)
                    print(domicilio.values[0])

                    exit()'''
                    clasificados = ClasificarDocumentos(list_docs=list_Docs,ruta_salida=rutaSalida)
                    clasificadosRes = clasificados.ClasificarDocs()
                    #print(clasificadosRes)
                    #exit()
                    #print(len(clasificadosRes))
                    datosReturn = []
                    imgFirmaAviso = None
                    imgFirmaIdentificacion = None
                    resultIdentificacion = None
                    ##*************************Ontener los datos de cada documento dependiendo la clasificación********
                    for clasificacion in clasificadosRes:
                        clasificacionAux = clasificacion[0]
                        if (clasificacionAux[0][0][0] == 'Identificacion'):
                            Identificacion = DatosIdentificacion(clasificacion=clasificacionAux)
                            Identificacion.recorteNombre()
                            #res2 = Identificacion.datoRequerido()
                            resultIdentificacion = Identificacion.datoRequerido()
                            imgFirmaIdentificacion = resultIdentificacion[2]
                            
                            #exit()
                            datosReturn.append([clasificacionAux[0][0][0],resultIdentificacion])
                        if (clasificacionAux[0][0][0] == 'Domicilio'):
                            Domicilio = DatosDomicilio(clasificacion=clasificacionAux)
                            resultDomicilio = Domicilio.datoRequerido()
                            datosReturn.append([clasificacionAux[0][0][0],resultDomicilio])
                        if (clasificacionAux[0][0][0] == 'NSS'):
                            NSS = DatosNSS(clasificacion=clasificacionAux)
                            resultNSS = NSS.datoRequerido()
                            datosReturn.append([clasificacionAux[0][0][0],resultNSS])
                        if (clasificacionAux[0][0][0] == 'CURP'):
                            Curp = DatosCurp(clasificacion=clasificacionAux)
                            resultCurp = Curp.datoRequerido()
                            datosReturn.append([clasificacionAux[0][0][0],resultCurp])
                        if (clasificacionAux[0][0][0] == 'Aviso'):
                            Aviso = DatosAviso(clasificacion=clasificacionAux)
                            resultAviso = Aviso.datoRequerido()
                            imgFirmaAviso = Aviso.getClasificacion()[0][2]
                            datosReturn.append([clasificacionAux[0][0][0],resultAviso])
                    
                    '''cv2.imshow("Imagen con Rectángulo", imgFirmaAviso)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()'''

                    #print(resultIdentificacion)
                    #edad_ana = dfCompleto.loc[dfCompleto["Tipo Documento"] == "Identificacion", ["FULLNAME"]].values[0][0]
                    #print(edad_ana)
                    
                    datos = comparacionResultados(datosResult=datosReturn,dfcompleto=dfCompleto,diasDiferencia = diasDiferencia,firmaAviso=imgFirmaAviso,firmaidentificacion = imgFirmaIdentificacion)
                    dat = datos.compara()
                    print(row['ID'], dat)
        db.cerrar_conexion()
        #print(datosReturn)
        #print(dfCompleto)
        #****************INE***************************
        #print(dfCompleto['NOSS'][0])
    