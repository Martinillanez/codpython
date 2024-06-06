from abc import ABC, abstractmethod

class producto(ABC):
    def __init__(self, nom, fechae, fechav, tempa, pais, numlote, costo):
        self.__nombre = nom
        self.__fechaenvasado = fechae
        self.__fechavencimiento = fechav
        self.__temperatura = tempa
        self.__pais = pais
        self.__numerolote = numlote
        self.__costo = costo
    def getnombre(self):
        return self.__nombre  
    def getfechaenvasado(self):
        return self.__fechaenvasado   
    def getfechavencimiento(self):
        return self.__fechavencimiento   
    def gettemperatura(self):
        return self.__temperatura   
    def getpais(self):
        return self.__pais   
    def getnumerolote(self):
        return self.__numerolote    
    def getcosto(self):
        return self.__costo    
    def __str__(self):
        return f"{self.__nombre}, {self.__fechaenvasado}, {self.__fechavencimiento}, {self.__temperatura}, {self.__pais}, {self.__numerolote}, {self.__costo}"   
    @abstractmethod
    def mostrarproducto(self):
        pass
