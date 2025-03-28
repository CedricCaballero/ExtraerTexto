import cx_Oracle
import configDB
class ConexionBaseDatos:
    def __init__(self):
        # Configuración de conexión
        self.dsn = cx_Oracle.makedsn(configDB.DB_HOST,configDB.DB_PORT,configDB.DB_SERVICE)
        self.username = configDB.DB_USER
        self.password = configDB.DB_PASSWORD

    def conectar(self):
        try:
            self.connection = cx_Oracle.connect(user=self.username, password=self.password, dsn=self.dsn)
            self.cursor = self.connection.cursor()
            return True
        except cx_Oracle.Error as error:
            print("Error al conectarse:", error)
            return False

    def ejecutar_query(self, query, parametros=None):
        try:
            if parametros:
                self.cursor.execute(query, parametros)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except cx_Oracle.Error as error:
            print(f"Error al ejecutar el query: {error}")
            return None

    def cerrar_conexion(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Conexión cerrada.")
        except cx_Oracle.Error as error:
            print(f"Error al cerrar la conexión: {error}")

'''if __name__ == "__main__":
    db = ConexionBaseDatos()
    conec = db.conectar()
    print(conec)
    if conec:
        resultado = db.ejecutar_query("SELECT DISTINCT (PENDING_OPERATION) FROM APPENROLLMENT.PERSON p")
        for fila in resultado:
            print(fila)
        db.cerrar_conexion()'''