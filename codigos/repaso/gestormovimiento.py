import numpy as np
import csv
from movimiento import movimiento

class gestormovimiento:
    __movimiento: np.ndarray
    def __init__(self):
        self.__movimiento = np.array([],dtype=movimiento)
    def cargar(self):
        archi = open('MovimientosAbril2024.csv')
        reader = csv.reader(archi, delimiter=';')
        next(reader)
        for fila in reader:
            mov = movimiento(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.__movimiento = np.append(self.__movimiento, mov)
    def buscarmovimiento(self, num):
        acum = 0
        print("movimiento\n fecha       descripcion      importe        tipo de movimiento")
        for i in  range(len(self.__movimiento)):
            if self.__movimiento[i].getnum() == num:
                print(f"{self.__movimiento[i].getfecha()}   {self.__movimiento[i].getdescripcion()}    {self.__movimiento[i].getimporte()}   {self.__movimiento[i].gettipo()}")
                if self.__movimiento[i].gettipo() == 'P':
                    acum = acum - self.__movimiento[i].getimporte()
                elif self.__movimiento[i].gettipo() == 'C':
                    acum = acum + self.__movimiento[i].getimporte()
        return float(acum)
    def ordenar(self):
        self.__movimiento.sort()
        print("se ordeno  la lista")
        for i in range(len(self.__movimiento)):
            self.__movimiento[i].mostrar()  
