#import analizaFile
from obtenerDocumentos import Documentos
from clasificarDocumento import ClasificarDocumentos
from datosIdentificacion import DatosIdentificacion
from datosDomicilio import DatosDomicilio
from datosNSS import DatosNSS
from datosCurp import DatosCurp
from datosAviso import DatosAviso
#************Ruta Ruta *******************
ruta = r'C:\Users\ccaballerob\Documents\Proyectos\10-validacion enrollment\documentos\documentosE'
rutaSalida = ruta+r'\imagenS'
todosResultados = []



if __name__ == "__main__":
    Docs = Documentos(pathFile=ruta)
    list_Docs = Docs.listar_archivos()
    clasificados = ClasificarDocumentos(list_docs=list_Docs,ruta_salida=rutaSalida)
    clasificadosRes = clasificados.ClasificarDocs()
    #print(clasificadosRes)
    print(len(clasificadosRes))
    datosReturn = []
    ##*************************Ontener los datos de cada documento dependiendo la clasificación********
    for clasificacion in clasificadosRes:
        print(clasificacion[0][0][0])
        resultIdentificacion = None
        if (clasificacion[0][0][0] == 'Identificacion'):
            Identificacion = DatosIdentificacion(clasificacion=clasificacion)
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
    
    