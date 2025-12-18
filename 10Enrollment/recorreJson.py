import json
from pathlib import Path
import os

from obtenerDocumentos import Documentos
from clasificarDocumento import ClasificarDocumentos
from datosIdentificacion import DatosIdentificacion
from datosDomicilio import DatosDomicilio
from datosNSS import DatosNSS
from datosCurp import DatosCurp
from datosAviso import DatosAviso
from conexionDB import ConexionBaseDatos
from comparacionResultados import comparacionResultados

# Cargar el archivo JSON
with open('C:\\Users\\ccaballerob\\Documents\\Proyectos\\10-validacion enrollment\\jsonService.json', 'r', encoding='utf-8') as f:
    contenido = json.load(f)

body = contenido.get('responseEntity', {}).get('body', {})

# Extraer datos de paginationInfo
pagination = body.get('paginationInfo', {})
print("📦 Información de paginación:")
print(f"Total de elementos: {pagination.get('totalElements')}")
print(f"Tipo de evento: {pagination.get('typeEvent')}")
print(f"Estatus: {pagination.get('status')}")
print(f"Ruta de almacenamiento: {pagination.get('pathStorage')}")

#pathStorage = pagination.get('pathStorage')
pathStorage = Path("C:\\Users\\ccaballerob\\Documents\\Proyectos\\10-validacion enrollment\\documentos\\documentosEnrollment")


# Extraer y recorrer data

data = body.get('data', None)

if isinstance(data, list):
    for i, item in enumerate(data):
        list_Docs = []
        person = item.get('person', {})
        print(f"\n📄 Registro #{i + 1}")
        
        print(f"ID: {person.get('id')}")
        print(f"Nombre: {person.get('name')}")
        print(f"Apellido 1: {person.get('firstLastName')}")
        print(f"Apellido 2: {person.get('secondLastName')}")
        print(f"CURP: {person.get('curp')}")
        print(f"No. Seguro Social: {person.get('noSS')}")
        print(f"Nacionalidad: {person.get('nationality')}")
        print(f"Email: {person.get('email')}")
        print(f"Teléfono: {person.get('phone')}")
        print(f"Empleo: {person.get('employment')}")
        print(f"Estatus: {person.get('status')}")

        documents = person.get('documents', [])
        for j, doc in enumerate(documents):
            pathStorageAux = ''
            #pathStorageAux = pathStorage +'/'+doc.get('directory')+'/'+doc.get('fileName')
            pathStorageAux = pathStorage / doc.get('directory') / doc.get('fileName')
            doc_type = doc.get('documentType', {})
            
            if pathStorageAux.is_file():
                
                list_Docs.append((pathStorageAux, doc.get('extension'),doc.get('fileName')))
            else:
                print("no entra")
            pathStorageAux = pathStorageAux.with_suffix("."+doc.get('extension'))
            
            #clprint(str(pathStorageAux))
            
            '''print(f"  📎 Documento #{j + 1}")
            print(f"  Directorio: {doc.get('directory')}")
            print(f"  Archivo: {doc.get('fileName')}")
            print(f"  Extensión: {doc.get('extension')}")
            doc_type = doc.get('documentType', {})
            print(f"  Tipo ID: {doc_type.get('id')}")
            print(f"  Tipo Nombre: {doc_type.get('name')}")
            print(f"  Tipo Código: {doc_type.get('code')}")
        
        company = item.get('company', {})
        print(f"Empresa ID: {company.get('id')}")
        print(f"RFC: {company.get('rfc')}")
        print(f"Nombre Empresa: {company.get('name')}")'''
        
        clasificados = ClasificarDocumentos(list_docs=list_Docs,ruta_salida='')
        clasificadosRes = clasificados.ClasificarDocs()
        datosReturn = []
        imgFirmaAviso = None
        imgFirmaIdentificacion = None
        resultIdentificacion = None
        ##*************************Ontener los datos de cada documento dependiendo la clasificación********
        for clasificacion in clasificadosRes:
            clasificacionAux = clasificacion[0]
            
            '''if (clasificacionAux[0][0][0] == 'Identificacion'):
                Identificacion = DatosIdentificacion(clasificacion=clasificacionAux)
                Identificacion.recorteNombre()
                #res2 = Identificacion.datoRequerido()
                resultIdentificacion = Identificacion.datoRequerido()
                if resultIdentificacion:
                    imgFirmaIdentificacion = resultIdentificacion[2]
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
                datosReturn.append([clasificacionAux[0][0][0],resultCurp])'''
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
        print("este es el resultado final")
        print(datosReturn)
        #print(datosReturn[0][1][4])
        
        '''datos = comparacionResultados(datosResult=datosReturn,dfcompleto=dfCompleto,diasDiferencia = diasDiferencia,firmaAviso=imgFirmaAviso,firmaidentificacion = imgFirmaIdentificacion)
        dat = datos.compara()
        print(row['ID'], dat)'''


else:
    print("El campo 'data' no existe o no es una lista.")
