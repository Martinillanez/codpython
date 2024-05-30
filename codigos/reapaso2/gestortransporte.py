from serviciotransporte import ServicioTransporte
from datetime import datetime

class GestorTransporte:
    def crear_servico_transporte(self):
        print("Creando servicio de transporte...")
        nomemp = input("Ingrese el nombre de la empresa: ")
        nombrecont = input("Ingrese el nombre de la persona contratada: ")
        direccion = input("Ingrese direccion del contratado: ")       
        while True:
            try:
                fechaservicio = datetime.strptime(input("Fecha de servicio (DD/MM/YYYY): "), "%d/%m/%Y")
                break
            except ValueError:
                print("Por favor, ingrese una fecha válida en el formato DD/MM/YYYY.")
        while True:
            try:
                comision = float(input("Comision: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la comisión.")
        while True:
            try:
                preciohora = float(input("Precio por hora: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio por hora.")
        while True:
            try:
                pesocarga = int(input("Peso de la carga: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el peso de la carga.")
        direcciondestino = input("Ingrese la direccion de destino: ")
        
        return ServicioTransporte(nomemp, nombrecont, direccion, fechaservicio, comision, preciohora, pesocarga, direcciondestino)
