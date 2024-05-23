import csv
from alquiler import alquiler

class gestoralqulier:
    __alquiler:list
    def __init__(self):
        self.__alquiler = []
        self.cargar()
    def cargar(self):
        archivo = open('Alquiler.csv')
        reader=csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unalquiler = alquiler(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__alquiler.append(unalquiler)
    def listado(self, x):
        self.__alquiler.sort()
        print("Hora    id de cancha    duracion alquiler    importe por hora    importe alquiler")
        total_recaudado = 0.0
        for i in range(len(self.__alquiler)):
            hora = f"{self.__alquiler[i].gethora():02}:{self.__alquiler[i].getminutos():02}"
            idcancha = self.__alquiler[i].getidcancha()
            duracion = int(self.__alquiler[i].getduracion())
            imphora = float(x.importehora(idcancha))
            impalquiler = (duracion / 60.0) * imphora  
            total_recaudado += impalquiler
            print(f"{hora}   {idcancha}     {duracion}          {imphora:.2f}       {impalquiler:.2f}")
        print(f"Total recaudado: {total_recaudado:.2f}")
    def cantidad(self):
        idcancha= input(" ingrese el identificador de la cancha:")
        acum=0
        for alquiler in self.__alquiler:
            if alquiler.getidcancha() == idcancha:
                acum+= int(alquiler.getduracion())
        print(f"el total de minutos de minutos que estuvo ocupada  la cancha {idcancha} alquilada fue: {acum}")


