# prueba_Backend_Geret_Rodrigo_Moya_Roa
Prueba en Python con interacción a Mysql

Este proyecto consiste en una aplicación de línea de comandos (CLI) desarrollado en Python para la interacción y gestion con una base de datos en MySQL.
Ademas incluye un módulo extra, con un codigo en PHP y Datatables para la visualizacion de logs SNMP simulados.

## Requisitos Previos

- Python 3.x
- Virtualenv 
- MySQL Server
- PHP / XAMPP

## Instalación y Configuración

1. ## Configuración del Entorno

Es obligatorio utilizar un entorno virtual llamado `env`. 

```bash
# 1. Instalar virtualenv (si no lo tiene)
pip install virtualenv

# 2. Crear el entorno virtual apuntando a Python 3
virtualenv -p python3 env

# 3. Activar el entorno virtual
# En Linux/macOS:
source env/bin/activate
# En Windows:
.\env\Scripts\activate

```
## 2. Instalación de Dependencias

```bash
# Instalar las librerias añadidad en requeriments.txt 
pip install -r requirements.txt

```

### 3. Configuración de Base de Datos
```bash
CREATE DATABASE IF NOT EXISTS prueba_tecnica_db;
USE prueba_tecnica_db;
```

-- 1. Tabla obligatoria para la CLI
```bash
CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    value INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

-- 2. Tabla adicional (Logs SNMP)
```bash
CREATE TABLE IF NOT EXISTS snmp_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    host VARCHAR(50),
    oid VARCHAR(100),
    value INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


### 4. Variables de entorno
  - Renombra el archivo `.env.example` a `.env`.
  - Edita el archivo `.env` con tus credenciales de MySQL.

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=contraseña_acá
DB_NAME=prueba_tecnica_db


## 5. Ejecución

La aplicación se ejecuta desde la terminal mediante el archivo main.py y acepta argumentos para las distintas operaciones.

## 1 Insertar un nuevo registro 
```bash
python main.py add --name "Sensor A" --value 45
```
## 2 Listar todos los registros

```bash
python main.py list
```
## 3 Consultar un registro por ID

```bash
python main.py get --id 2
```
## 4 Actualizar un registro existente

```bash
python main.py update --id 2 --value 99
```

### Extra: DataTables con PHP y Simulación de Datos

## Generación de datos
## Se ha incluido un script en Python para poblar la tabla snmp_logs con datos simulados automáticamente.

```bash
python seed_data.py
```
#1.  **Clonar el repositorio:**
#    ```bash
#    git clone (https://github.com/Rroa-dev/prueba_RPA_geret_Rodrigo_Moya_Roa.git)
#    cd prueba_RPA_geret_Rodrigo_Moya_Roa
#    ```