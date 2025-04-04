#import analizaFile
import pandas as pd
import os
from obtenerDocumentos import Documentos
from clasificarDocumento import ClasificarDocumentos
from datosIdentificacion import DatosIdentificacion
from datosDomicilio import DatosDomicilio
from datosNSS import DatosNSS
from datosCurp import DatosCurp
from datosAviso import DatosAviso
from conexionDB import ConexionBaseDatos
#************Ruta Ruta *******************
ruta = r'C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosE'
rutaSalida = ruta+r'\imagenS'
todosResultados = []
dfCompleto = pd.DataFrame()

if __name__ == "__main__":

    '''#Creamos la conexion de base de datos
    db = ConexionBaseDatos()
    conec = db.conectar()
    #print(conec)
    if conec:
        tabla = "APPENROLLMENT.PERSON"
        query = "SELECT p.ID , (p.NAME||' '||p.FIRST_LAST_NAME||' '||p.SECOND_LAST_NAME) AS FULLNAME, p.CURP,p.NOSS, a.COUNTRY,a.NEIGHBORHOOD,a.MUNICIPALITY,a.NO_EXT,a.NO_INT,a.POSTAL_CODE,a.STATE,a.STREET, p.ADDRESS_ID "+"FROM APPENROLLMENT.PERSON p "+"INNER JOIN APPENROLLMENT.ADDRESS a " +"on a.ID = p.ADDRESS_ID " +"WHERE P.PENDING_OPERATION = :PENDING"
        parametros = {'PENDING':'CREATE'}
        column_names, resultado = db.ejecutar_query(query=query,tabla=tabla,parametros=parametros)
        df = pd.DataFrame(resultado, columns=column_names)
        #print(df)
        
        for index, row in df.iterrows():
            #if index == 0:
            if 'A' == 'A':
                #print(row['ID'])
                query = "SELECT CREATED_DATE,DIRECTORY,FILE_NAME ,EXTENSION, DOCUMENT_TYPE_ID FROM APPENROLLMENT.UPLOADED_DOCUMENT ud WHERE ud.PERSON_ID = :PERSON_ID"
                parametros = {'PERSON_ID':row['ID']}
                column_namesDoc, resultadoDoc = db.ejecutar_query(query=query,tabla=tabla,parametros=parametros)
                dfDoc = pd.DataFrame(resultadoDoc, columns=column_namesDoc)
                #print(dfDoc)
                for indexj, row2 in dfDoc.iterrows():
                    #print(row2['DOCUMENT_TYPE_ID'])
                    nueva_fila = pd.DataFrame(row).T
                    nueva_fila2 = pd.DataFrame(row2).T
                    nueva_fila2['ID'] = row['ID']
                    if row2['DOCUMENT_TYPE_ID'] == 4:
                        nueva_fila2['Tipo Documento'] = 'OFICIAL_ID'
                    if row2['DOCUMENT_TYPE_ID'] == 5:
                        nueva_fila2['Tipo Documento'] = 'CURP'
                    if row2['DOCUMENT_TYPE_ID'] == 6:
                        nueva_fila2['Tipo Documento'] = 'NSS'
                    if row2['DOCUMENT_TYPE_ID'] == 7:
                        nueva_fila2['Tipo Documento'] = 'PROOF_OF_ADDRESS'
                    if row2['DOCUMENT_TYPE_ID'] == 8:
                        nueva_fila2['Tipo Documento'] = 'PRIVACY_NOTICE'
                    dfCompletoAux = pd.merge(nueva_fila,nueva_fila2, on='ID', how='outer')
                    dfCompleto = pd.concat([dfCompleto,dfCompletoAux],ignore_index=True)
        
        db.cerrar_conexion()
        print(dfCompleto)
        for index, rowR in dfCompleto.iterrows():
            if rowR['EXTENSION'] == 'pdf':
                #rutaFull = ruta + '\\' + rowR['DIRECTORY'] + '\\' + rowR['FILE_NAME'] + '.'+rowR['EXTENSION']
                rutaFull = ruta + '\\' + rowR['DIRECTORY']

    #exit()'''

    Docs = Documentos(pathFile=ruta)
    list_Docs = Docs.listar_archivos()
    clasificados = ClasificarDocumentos(list_docs=list_Docs,ruta_salida=rutaSalida)
    clasificadosRes = clasificados.ClasificarDocs()
    #print(clasificadosRes)
    #print(len(clasificadosRes))
    datosReturn = []
    ##*************************Ontener los datos de cada documento dependiendo la clasificación********
    for clasificacion in clasificadosRes:
        #print(clasificacion[0][0][0])
        resultIdentificacion = None
        if (clasificacion[0][0][0] == 'Identificacion'):
            #print('entro')
            Identificacion = DatosIdentificacion(clasificacion=clasificacion)
            Identificacion.recorteNombre()
            res2 = Identificacion.datoRequerido()
            #print(res2)
            #exit()
            resultIdentificacion = Identificacion.datoRequerido()
            datosReturn.append([clasificacion[0][0][0],resultIdentificacion])
        if (clasificacion[0][0][0] == 'Domicilio'):
            Domicilio = DatosDomicilio(clasificacion=clasificacion)
            resultDomicilio = Domicilio.datoRequerido()
            datosReturn.append([clasificacion[0][0][0],resultDomicilio])
        if (clasificacion[0][0][0] == 'NSS'):
            NSS = DatosNSS(clasificacion=clasificacion)
            resultNSS = NSS.datoRequerido()
            datosReturn.append([clasificacion[0][0][0],resultNSS])
        if (clasificacion[0][0][0] == 'CURP'):
            Curp = DatosCurp(clasificacion=clasificacion)
            resultCurp = Curp.datoRequerido()
            datosReturn.append([clasificacion[0][0][0],resultCurp])
        if (clasificacion[0][0][0] == 'Aviso'):
            Aviso = DatosAviso(clasificacion=clasificacion)
            resultAviso = Aviso.datoRequerido()
            datosReturn.append([clasificacion[0][0][0],resultAviso])
    print(datosReturn)
    #****************INE***************************
    #print(dfCompleto['NOSS'][0])
    