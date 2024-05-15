class movimiento:
    __numetarjeta: int
    __fecha: str
    __descripcion: str
    __tipo: str
    __importe: float
    
    def __init__(self, num, fecha, desc, tipo, imp):
        self.__numetarjeta = num
        self.__fecha = fecha
        self.__descripcion = desc
        self.__tipo = tipo
        self.__importe = imp
    def getnum(self):
        return self.__numetarjeta
    def getfecha(self):
        return self.__fecha
    def getdescripcion(self):
        return self.__descripcion
    def gettipo(self):
        return self.__tipo
    def getimporte(self):
        return self.__importe
    def __lt__(self, other):
        return self.__numetarjeta < other.__numetarjeta
    def mostrar(self):
        print(f"numero tarjeta: {self.__numetarjeta}\n fecha: {self.__fecha}\n descripcion: {self.__descripcion}\n tipo: {self.__tipo}\n importe: {self.__importe}")

    


      