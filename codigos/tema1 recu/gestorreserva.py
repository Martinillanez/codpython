import csv
from reserva import reserva

class gestoreserva:
    def __init__(self):
        self.__reservas = []
        self.cargar()

    def cargar(self):
        archivo = open('Reservas.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            unareserva = reserva(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], float(fila[6]))
            self.__reservas.append(unareserva)

    def reserva(self, num):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__reservas):
            if self.__reservas[i].getnumreserva() == num:
                encontrado = True
                return i
            i += 1
        return -1

    def listareserva(self, x):
        fecha = input("Ingrese una fecha de inicio de hospedaje: ")
        print(f"Reservas para la fecha: {fecha}\nNº cabaña    importe diario    cantidad de días    seña    importe a cobrar")
        for i in range(len(self.__reservas)):
            if self.__reservas[i].getfecha() == fecha:
                imp_diario = x.importediario(self.__reservas[i].getnumcabaña())
                if imp_diario is not None:
                    importe_a_cobrar = self.__reservas[i].getcantdias() * imp_diario - self.__reservas[i].getseña()
                    print(f"{self.__reservas[i].getnumcabaña()}     {imp_diario:.2f}   {self.__reservas[i].getcantdias()}      {self.__reservas[i].getseña():.2f}   {importe_a_cobrar:.2f}")
                else:
                    print(f"Error: No importe diario found for cabin {self.__reservas[i].getnumcabaña()}")
