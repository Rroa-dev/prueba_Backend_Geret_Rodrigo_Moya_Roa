import mysql.connector
import os
import random
import time
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def seed_snmp_logs():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = connection.cursor()

        print("Generando datos simulados para 'snmp_logs'...")

        # Lista de IPs y OIDs simulados para variar los datos
        hosts = ['192.168.1.10', '192.168.1.11', '10.0.0.5', '172.16.0.1']
        oids = ['.1.3.6.1.2.1.1.1', '.1.3.6.1.2.1.1.3', '.1.3.6.1.4.1.9']

        # Insertar 10 registros aleatorios
        for _ in range(10):
            host = random.choice(hosts)
            oid = random.choice(oids)
            value = random.randint(10, 100) # Valor aleatorio entre 10 y 100
            
            query = "INSERT INTO snmp_logs (host, oid, value) VALUES (%s, %s, %s)"
            cursor.execute(query, (host, oid, value))
        
        connection.commit()
        print(f"Se insertaron {cursor.rowcount} registros correctamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    seed_snmp_logs()