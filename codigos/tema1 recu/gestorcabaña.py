import csv
import numpy as np
from cabaña import cabaña

class gestorcabaña:
    def __init__(self):
        self.__cabañas = np.array([], dtype=object)
        self.cargar()

    def cargar(self):
        archivo = open('Cabañas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            una_cabaña = cabaña(fila[0], fila[1], fila[2], fila[3], float(fila[4]))
            self.__cabañas = np.append(self.__cabañas, una_cabaña)

    def cantidad(self, r):
        huespedes = int(input("Ingrese la cantidad de huéspedes:"))
        for cabaña in self.__cabañas:
            if cabaña >= huespedes and r.reserva(cabaña.getnumero())== -1:
                print(f"La cabaña {cabaña.getnumero()} está disponible para {huespedes} huéspedes.")
            else:
                print(f"La cabaña {cabaña.getnumero()} no está disponible para {huespedes} huéspedes.")

    def importediario(self, numcabaña):
        for cabaña in self.__cabañas:
            if cabaña.getnumero() == numcabaña:
                return cabaña.getimporte()
        return None
