from clasenodo import Nodo
from audiolibro import audilibro
from libroimpreso import  libroimpreso
from datetime import datetime
import csv

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
            dato = self.__actual.get_publicacion()
            self.__actual = self.__actual.get_siguiente()
            return dato
    def agregar_publicacion(self, publicacion):
        nodo = Nodo(publicacion)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            actual = self.__comienzo
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nodo)
        self.__tope += 1
    
    def cargar_publicaciones(self):
        with open('libroimpreso.csv', newline='') as archivo1:
            reader1 = csv.reader(archivo1, delimiter=';')
            next(reader1)  # Skip header
            for fila in reader1:
                unlibro = libroimpreso(fila[0], fila[1], float(fila[2]), fila[3], fila[4], int(fila[5]))
                self.agregar_publicacion(unlibro)
        
        with open('audiolibro.csv', newline='') as archivo2:
            reader2 = csv.reader(archivo2, delimiter=';')
            next(reader2)  # Skip header
            for fila in reader2:
                uncd = audilibro(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
                self.agregar_publicacion(uncd)
    def buscar(self, posicion):
        if posicion < 0 or posicion >= self.__tope:
            return None
        else:
            indice = 0
            actual = self.__comienzo
            while actual is not None and indice < posicion:
                actual = actual.get_siguiente()
                indice += 1
            return actual.get_publicacion() if actual else None
    def contar_publicaciones(self):
        actual = self.__comienzo
        cont_cd = 0
        cont_libro = 0
        while actual is not None:
            if isinstance(actual.get_publicacion(), audilibro):
                cont_cd += 1
            elif isinstance(actual.get_publicacion(), libroimpreso):
                cont_libro += 1
            actual = actual.get_siguiente()
        print(f"La cantidad de publicaciones del tipo CD es: {cont_cd}")
        print(f"La cantidad de publicaciones del tipo Libro es: {cont_libro}")
    def precio(self):
        actual = self.__comienzo
        while actual is not None:
            publicacion = actual.get_publicacion()
            if isinstance(publicacion, audilibro):
                publicacion.set_preciobase(publicacion.get_preciobase() * 1.1)
            elif isinstance(publicacion, libroimpreso):
                anio_actual = datetime.now().year
                publicacion.set_preciobase(publicacion.get_preciobase() - (anio_actual - int(publicacion.get_fechaedicion().split('/')[-1])))
            actual = actual.get_siguiente()