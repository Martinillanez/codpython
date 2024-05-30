from servicioembalaje import ServicioEmbalaje
from datetime import datetime

class GestorEmbalaje:
    def crear_embalaje(self):
        print("Creando embalaje...")
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
                preciouni = float(input("Precio por unidad: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio por unidad.")
        while True:
            try:
                pesouni = int(input("Peso por unidad: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el peso por unidad.")
        while True:
            try:
                cantidad = int(input("Cantidad de unidades: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad de unidades.")

        return ServicioEmbalaje(nomemp, nombrecont, direccion, fechaservicio, comision, preciouni, pesouni, cantidad)
