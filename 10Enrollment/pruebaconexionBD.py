import cx_Oracle

DB_HOST = "10.150.223.171"
DB_PORT = "1521"
DB_USER = "appfalcon"        # Ejemplo: "192.168.1.10"
DB_PASSWORD = "falcon#2022P"           # Puerto estándar de Oracle
DB_SERVICE = "falconcl"  # El nombre del servicio configurado en la base de datos
# Información de conexión
usuario = "appfalcon"
contraseña = "falcon#2022P"
host = "10.150.223.171"  # Ejemplo: "127.0.0.1"
puerto = "1521"   # Puerto predeterminado de Oracle
sid = "falconcl"    # Identificador del sistema (SID)

# Crear una cadena de conexión
dsn_tns = cx_Oracle.makedsn(host, puerto, sid)

try:
    # Establecer la conexión
    conexion = cx_Oracle.connect(user=usuario, password=contraseña, dsn=dsn_tns)
    print("Conexión exitosa a la base de datos!")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta de ejemplo
    cursor.execute("SELECT DISTINCT(STATUS) FROM APPENROLLMENT.PERSON")
    filas = cursor.fetchall()  # Recuperar los resultados
    for fila in filas:
        print(fila)

except cx_Oracle.DatabaseError as e:
    print("Error al conectar con la base de datos:", e)

finally:
    # Cerrar la conexión
    if 'conexion' in locals() and conexion:
        conexion.close()
        print("Conexión cerrada.")