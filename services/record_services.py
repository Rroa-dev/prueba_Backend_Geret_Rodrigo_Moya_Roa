from db.connection import getConnection
from db.models import Record
import sys 

class RecordService:

    def addRecord(self, name, value):
        connection = getConnection()
        if not connection:
            return
        
        try:
            cursor = connection.cursor()
            query = "insert into records (name, value) values (%s, %s)"
            cursor.execute(query, (name, value))
            connection.commit()
            print("Registro insertado con éxito, ID:", cursor.lastrowid)
        except Exception as e:
            print("Error al insertar registro", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def getAllRecords(self):
        connection = getConnection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("select * from records")
            rows = cursor.fetchall()
            
            print(f"{'ID':<5} {'Name':<20} {'Value':<10} {'Created At':<20}")
            print("-" * 60)
            
            for row in rows:
                # Mapeo a objeto Record
                record = Record(row[0], row[1], row[2], row[3])
                print(f"{record.id:<5} {record.name:<20} {record.value:<10} {record.createdAt}")
                
        except Exception as e:
            print("Error al obtener registros: ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def getRecordById(self, recordId):
        connection = getConnection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "select * from records where id = %s"
            cursor.execute(query, (recordId,))
            row = cursor.fetchone()

            if row:
                record = Record(row[0], row[1], row[2], row[3])
                print(f"{'ID':<5} {'Name':<20} {'Value':<10} {'Created At':<20}")
                print(f"{record.id:<5} {record.name:<20} {record.value:<10} {record.createdAt}")
            else:
                print("Error: ID inexistente") 
        except Exception as e:
            print("Error al buscar el registro: ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    
    def updateRecord(self, recordId, newValue):
        connection = getConnection()
        if not connection:
            return

        try:
            # Primero verificamos si existe
            cursor = connection.cursor()
            checkQuery = "select id from records where id = %s"
            cursor.execute(checkQuery, (recordId,))
            if not cursor.fetchone():
                print("Error: ID inexistente. No se puede actualizar.")
                return

            updateQuery = "update records set value = %s where id = %s"
            cursor.execute(updateQuery, (newValue, recordId))
            connection.commit()
            print("Registro actualizado correctamente")
        except Exception as e:
            print("Error al actualizar registro: ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

