class cliente:
   __nombre: str
   __apellido: str
   __dni: int
   __numtarjeta: int
   __saldoanterior: float
   def __init__(self, nom, ape, dni , num, saldo):
      self.__nombre = nom
      self.__apellido = ape
      self.__dni = dni
      self.__numtarjeta = num
      self.__saldoanterior = saldo
   def getnombre(self):
      return self.__nombre
   def getapellido(self):
      return self.__apellido
   def getdni(self):
       return self.__dni
   def getnumero(self):
       return self.__numtarjeta
   def getsaldo(self):
       return self.__saldoanterior
   def setsaldo(self, saldo):
       self.__saldoanterior = saldo
   def mostrar(self):
      print(f"nombre: {self.__nombre}\n apellido: {self.__apellido}\n DNI: {self.__dni}\n numero tarjeta: {self.__numtarjeta}\n saldo anteriror: {self.__saldoanterior}")