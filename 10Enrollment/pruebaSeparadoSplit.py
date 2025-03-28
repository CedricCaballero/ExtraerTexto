import pandas as pd

diccionario_Prueba = {
    'NSS': '01139309726',
    'CURP': 'CABC930627HOCBTDO7',
    'Domicilio': 'Privada Malva Oriente Mz9 Lt6, Tizara Town, C.P. 43816, Tizayuca, Hidalgo.',
    'Identifiacion': 'Cedric Omar Caballero Bautista',
    'Aviso':'Cedric Omar Caballero Bautista',
    'Aviso2':'25/03/2025'
}

abreviaturas = {
    'PRIVADA': 'PRIV',
    'HIDALGO': 'HGO',
    'TIZAYUCA': 'TIZAYUCAC',
    'FRACCIONAMIENTO': 'FRACC',
}

aceptacionDomicilio = 70.0
doc = []
referencia = []
extraccion = []
presicion = []
estatus = []
res = ['Identifiacion', ['CABALLERO,BAUTISTA,CEDRIC OMAR', 97.54]]

#****************************************************
#****************************************************
def estandarizar(lista, diccionario):
    lista_estandarizada = []
    for palabra in lista:
        # Verificar si la palabra tiene una equivalencia en el diccionario
        estandarizada = [key for key, value in diccionario.items() if palabra == value]
        lista_estandarizada.append(estandarizada[0] if estandarizada else palabra)
    return lista_estandarizada

doc.append(res[0])
reemplazos = str.maketrans({',': ' ', '.': ' '})
domicilio_ref = diccionario_Prueba.get(res[0],[]).translate(reemplazos).strip()
domicilio_ref = domicilio_ref.upper()
domicilio_ref = [elemento for elemento in domicilio_ref.split(' ') if elemento]
referencia.append(diccionario_Prueba.get(res[0],[]))
domicilio_Ext = res[1][0].translate(reemplazos).strip()
domicilio_Ext = domicilio_Ext.upper()
domicilio_Ext = [elemento for elemento in domicilio_Ext.split(' ') if elemento]

# Estandarizar ambos arrays
domicilio_ref_estandarizado = set(estandarizar(domicilio_ref, abreviaturas))
domicilio_Ext_estandarizado = set(estandarizar(domicilio_Ext, abreviaturas))

# Contar elementos iguales
iguales = domicilio_ref_estandarizado.intersection(domicilio_Ext_estandarizado)
cantidad_iguales = len(iguales)

# Calcular porcentaje de similitud
total_elementos = len(domicilio_ref_estandarizado.union(domicilio_Ext_estandarizado))
porcentaje_similitud = (cantidad_iguales / total_elementos) * 100
extraccion.append(res[1][0])
presicion.append(f"{porcentaje_similitud:.2f}")
if porcentaje_similitud> aceptacionDomicilio:
    estatus.append('Aprovado')
else:
    estatus.append('Rechazado')


#****************************************************
#****************************************************
conjuntoDatos = {
    'Documento':doc,
    'Referencia':referencia,
    'Extracción':extraccion,
    'Presición %':presicion,
    'Estatus':estatus
}

df = pd.DataFrame(conjuntoDatos)
print(df)