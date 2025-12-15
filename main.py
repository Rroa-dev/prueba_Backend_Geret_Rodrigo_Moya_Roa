import argparse
import sys
from services.record_services import RecordService

def main():
    parser = argparse.ArgumentParser(description="CLI para gestión de registros MySQL")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando 1: add 
    addParser = subparsers.add_parser("add", help="Agregar un nuevo registro")
    addParser.add_argument("--name", required=True, type=str, help="Nombre del registro")
    addParser.add_argument("--value", required=True, type=int, help="Valor numérico")

    # Comando 2: list 
    subparsers.add_parser("list", help="Listar todos los registros")

    # Comando 3: get 
    getParser = subparsers.add_parser("get", help="Obtener registro por su ID")
    getParser.add_argument("--id", required=True, type=int, help="ID del registro")

    # Comando 4: update 
    updateParser = subparsers.add_parser("update", help="Actualizar valor de un registro")
    updateParser.add_argument("--id", required=True, type=int, help="ID del registro")
    updateParser.add_argument("--value", required=True, type=int, help="Nuevo valor")

    # Parsear argumentos
    args = parser.parse_args()
    service = RecordService()

    # Router de comandos
    if args.command == "add":
        service.addRecord(args.name, args.value)
    elif args.command == "list":
        service.getAllRecords()
    elif args.command == "get":
        service.getRecordById(args.id)
    elif args.command == "update":
        service.updateRecord(args.id, args.value)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()