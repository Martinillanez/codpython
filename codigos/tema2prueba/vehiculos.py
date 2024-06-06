from abc import  ABC, abstractmethod
class vehiculo(ABC):
    __marca:str
    __modelo:str
    __aniofabricacion:int
    __capacidadpasajero:int
    __numplazas:int
    __distanciarecorrida:int
    __tarifa:float
    def __init__(self, marca, modelo, anio, capacidad, num, distancia, tarifa):
        self.__marca = marca
        self.__modelo = modelo
        self.__aniofabricacion = anio
        self.__capacidadpasajero = capacidad
        self.__numplazas = num
        self.__distanciarecorrida = distancia
        self.__tarifa = tarifa
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getanio(self):
        return self.__aniofabricacion
    def getcapacidad(self):
        return self.__capacidadpasajero
    def getnum(self):
        return self.__numplazas
    def getdistancia(self):
        return self.__distanciarecorrida
    def gettarifa(self):
        return self.__tarifa
    def __str__(self):
        return  f"{self.__marca}, {self.__modelo}, {self.__aniofabricacion}, {self.__capacidadpasajero}, {self.__numplazas}, {self.__distanciarecorrida}, {self.__tarifa}"
    @abstractmethod
    def mostrarvehiculos(self):
        pass
