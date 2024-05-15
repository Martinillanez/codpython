import csv
from clasecliente import cliente
class gestorcliente:
    __clientes: list
    def __init__(self):
        self.__clientes = []
    def cargar(self):
        archivo = open('ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nuevocliente = cliente(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__clientes.append(nuevocliente)
    def mostrar(self, xi):
        print(f"cliente: {self.__clientes[xi].getapellido(), self.__clientes[xi].getnombre()} numero de cuenta:{self.__clientes[xi].getnumero()} \n saldo anterior:{self.__clientes[xi].getsaldoanterior()}")
    def buscardni(self, dni):
        encontrado= False
        i=0
        while encontrado == False and i< len(self.__clientes):
            if self.__clientes[i].getdni()== dni:
                encontrado = True
                return i
            else:
                i= i+1
        i=-1
        return i
    def actualizar(self, dni, x):
        i= self.buscardni(dni)
        if i != -1:
            num= self.__clientes[i].getnumero()
            self.mostrar(i)
            acum=float(x.buscarmovimiento(num))
            saldo_actual= float(self.__clientes[i].getsaldoanterior())
            self.__clientes[i].setsaldo(str(saldo_actual+ acum))
            print(f" saldo actualizado: {self.__clientes[i].getsaldoanterior()}")
        else:
            print("no se encontro el cliente")
    def movimiento(self, a):
        dni = input("ingrese el DNI:")
        i =self.buscardni(dni)
        if i != -1:
            num=self.__clientes[i].getnumero()
            x=a.buscarmovimiento(num)
            if x==0:
                print(f"el cliente {self.__clientes[i].getapellido(), self.__clientes[i].getnombre()}  realizo movimientos en el mes de abril")
            else:
                print(f"el cliente {self.__clientes[i].getapellido(), self.__clientes[i].getnombre()}  no realizó movimientos en el mes de abril")
        else:
            print("no se encontro el cliente")