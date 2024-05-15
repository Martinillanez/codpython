import csv
import numpy as np
from clasemovimiento import movimiento

class gestormovimiento:
    __movimientos: np.ndarray

    def __init__(self):
        self.__movimientos = np.array([], dtype=movimiento)

    def cargar(self):
        archivo = open('MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nuevomovimiento = movimiento(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.__movimientos = np.append(self.__movimientos, nuevomovimiento)
    def buscarmovimiento(self, num):
        acum=0
        print("movimientos\n   fecha    descripcion     importe      tipo de movimiento")
        for i in range(len(self.__movimientos)):
            if self.__movimientos[i].getnum()== num:
                print(f"{self.__movimientos[i].getfecha()}  {self.__movimientos[i].getdescripcion()}    {self.__movimientos[i].getimporte()}    {self.__movimientos[i].gettipo()}")
                if self.__movimientos[i].gettipo == 'P':
                    acum = acum - self.__movimientos[i].getimporte()
                elif self.__movimientos[i].gettipo == 'C':
                    acum = acum + self.__movimientos[i].getimporte()
        return float(acum)
    def buscarnumero(self, num):
        cont=0
        for i in range (len(self.__movimientos)):
            if self.__movimientos[i].getnum()== num:
                cont += 1
        return cont
    def ordenar(self):
        self.__movimientos.sort()
        print("se ordeno con exito los movimientos")
        for i in range(len(self.__movimientos)):
            self.__movimientos[i].mostrar()