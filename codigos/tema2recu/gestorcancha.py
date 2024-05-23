import csv
import numpy as np
from cancha import cancha

class gestorcancha:
    __canchas: np.ndarray
    def __init__(self):
        self.__canchas = np.array([], dtype= object)
        self.cargar()
    def cargar(self):
        archivo = open ('Canchas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unacancha= cancha(fila[0], fila[1], float(fila[2]))
            self.__canchas = np.append(self.__canchas, unacancha)
    def importehora(self, id):
        for cancha in self.__canchas:
            if cancha.getid() == id:
                return cancha.getimportehora()
        return None
    
