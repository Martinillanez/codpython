import csv
from vanes import vanes
from autobus import autobus

class gestorvehiculo:
    __vehiculos:list
    def __init__(self):
        self.__vehiculos = []
    def cargar(self, archivo='vehiculos.csv'):
        with open(archivo, newline='')as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for fila in reader:
                if fila[0]=='A':
                    unvehiuclo= autobus(
                        fila[1],fila[2],fila[3],fila[4],fila[5], fila[6],fila[7],fila[8], fila[9]
                    )
                else:
                    unvehiuclo=vanes(
                        fila[1],fila[2],fila[3],fila[4],fila[5], fila[6],fila[7],fila[8]
                    )
                self.__vehiculos.append(unvehiuclo)
    def agregarvehiculo(self):
        vehiculo_tipo= input("ingrse el tipo de vehiculo(autobus'A' o vanes'V'):")
        if vehiculo_tipo=='A':
            marca=input("ingrese la marca del vehiculo:")
            modelo=input("ingrese el modelo del vehiculo:")
            aniofabricacion=int(input("ingrse el anio de fabricacion del vehiculo:"))
            capacidad=int(input("ingrese el capacidad de pasajeros:"))
            numplazas=int(input("ingrese el numero de plazas:"))
            distanciarecorrida=int(input("ingrese la distancia recorrida por el vheiculo:"))
            tarifa=float(input("ingrese la tarifa base:"))
            tipo=input("ingrese el tipo de servicio(interurbano o turismo):")
            turno=input("ingre el turno en el que brindo servicio(mañana, tarde o noche):")
            unvehiuclo= autobus(marca,modelo,aniofabricacion,capacidad,numplazas,distanciarecorrida,tarifa,tipo,turno)
        elif vehiculo_tipo == 'V':
            marca=input("ingrese la marca del vehiculo:")
            modelo=input("ingrese el modelo del vehiculo:")
            aniofabricacion=int(input("ingrese el anio de fabricacion del vehiculo:"))
            capacidad=int(input("ingrese el capacidad de pasajeros:"))
            numplazas=int(input("ingrese el numero de plazas:"))
            distanciarecorrida=int(input("ingrese la distancia recorrida por el vheiculo:"))
            tarifa=float(input("ingrese la tarifa base:"))
            tipoC=input("ingrese el tipo de carroceria(minivan o van):")
            unvehiuclo=vanes(marca,modelo,aniofabricacion, capacidad, numplazas, distanciarecorrida, tarifa, tipoC)
        self.__vehiculos.append(unvehiuclo)
    def mostrara_tipovehiculo(self):
        posicion= int(input("ingrese una posicion del vehiculo:"))
        if 0 <= posicion < len(self.__vehiculos):
            vehiculo= self.__vehiculos[posicion]
            if isinstance(vehiculo, autobus):
                print("El vehiculo es de tipo autobus")
            elif isinstance(vehiculo, vanes):
                print("El vehiculo es de tipo vanes")
        else:
            print("El vehiculo no existe")
    def cantidad(self):
        cantA=0
        cantV=0
        for i in self.__vehiculos:
            if isinstance(i, autobus):
                cantA+=1
            elif isinstance(i, vanes):
                cantV+=1
        print(f"cantidad de autobuses: {cantA}")
        print(f"cantidad de vanes: {cantV}")
    def mostrar_vehiculos(self):
        for vehiculo in self.__vehiculos:
            vehiculo.mostrarvehiculos()
            


               