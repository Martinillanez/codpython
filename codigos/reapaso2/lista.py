import csv
from claseNodo import Nodo
from servicioembalaje import ServicioEmbalaje
from serviciotransporte import ServicioTransporte
from collections import Counter
from datetime import datetime

class Lista:
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_empresa()
            self.__actual = self.__actual.get_siguiente()
            return dato
    def agregar_servicio(self, empresa):
        nodo = Nodo(empresa)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nodo)
        self.__tope += 1
    def cargar_servicios(self):
        with open('transporte.csv', newline='') as archivo1:
            reader1 = csv.reader(archivo1, delimiter=';')
            next(reader1)  # Saltar cabecera
            for fila in reader1:
                fecha = datetime.strptime(fila[3], "%d/%m/%Y")
                untransporte = ServicioTransporte(fila[0], fila[1], fila[2], fecha, float(fila[4]), float(fila[5]), int(fila[6]), fila[7])
                self.agregar_servicio(untransporte)
        with open('embalaje.csv', newline='') as archivo2:
            reader2 = csv.reader(archivo2, delimiter=';')
            next(reader2)  # Saltar cabecera
            for fila in reader2:
                fecha = datetime.strptime(fila[3], "%d/%m/%Y")
                unembalaje = ServicioEmbalaje(fila[0], fila[1], fila[2], fecha, float(fila[4]), float(fila[5]), int(fila[6]), int(fila[7]))
                self.agregar_servicio(unembalaje)
    def mostrar_servicio_transporte(self):
        servicio_transporte = []
        actual = self.__comienzo
        while actual is not None:
            empresa = actual.get_empresa()
            if empresa.gettipo() == 'Servicio de Transporte':
                servicio_transporte.append(empresa)
            actual = actual.get_siguiente()

        servicio_transporte.sort(key=lambda x: x.calcular_costo())
        total_recaudado = 0
        print("Nombre contratante      Costo total")
        for servicio in servicio_transporte:
            costo = servicio.calcular_costo()
            print(f"{servicio.getnombrecontratante()}       {costo:.2f}")
            total_recaudado += costo
        print(f"Total recaudado: {total_recaudado:.2f}")
    def cantidad_embalajes_pesados(self):
        actual = self.__comienzo
        embalajes_pesados = 0
        while actual is not None:
            empresa = actual.get_empresa()
            if empresa.gettipo() == 'Servicio de Embalaje' and empresa.getpesounidad() > 50:
                embalajes_pesados += 1
            actual = actual.get_siguiente()
        print(f"Cantidad de embalajes que superaron los 50 kg: {embalajes_pesados}")
    def servicio_mas_contrataciones(self, fecha):
        if isinstance(fecha, datetime):  # Verifica si ya es un objeto datetime
            fecha_dada = fecha
        else:
            fecha_dada = datetime.strptime(fecha, "%d/%m/%Y") 

        contrataciones_por_tipo = Counter()
        actual = self.__comienzo
        while actual is not None:
            empresa = actual.get_empresa()
            if empresa.getfechaservicio().date() == fecha_dada.date():
                tipo_servicio = empresa.gettipo()
                contrataciones_por_tipo[tipo_servicio] += 1
            actual = actual.get_siguiente()

        if contrataciones_por_tipo:
            servicio_mas_contratado = contrataciones_por_tipo.most_common(1)[0]
            print(f"El servicio con más contrataciones el {fecha_dada.strftime('%d/%m/%Y')} es '{servicio_mas_contratado[0]}' con {servicio_mas_contratado[1]} contrataciones.")
        else:
            print(f"No hay contrataciones registradas para la fecha {fecha_dada.strftime('%d/%m/%Y')}.")
