from empresa import Empresa

class ServicioEmbalaje(Empresa):
    __precioporunidad:float
    __pesounidad:int
    __cantidadunidades:int
    def __init__(self, nombreemp, nombrecon, direccion, fechaservicio, comision, preciouni, pesouni, cantidadunidades):
        super().__init__(nombreemp, nombrecon, direccion, fechaservicio, comision)
        self.__precioporunidad = preciouni
        self.__pesounidad = pesouni
        self.__cantidadunidades = cantidadunidades
    def getpreciounidad(self):
        return self.__precioporunidad
    def getpesounidad(self):
        return self.__pesounidad
    def getcantidadunidades(self):
        return self.__cantidadunidades
    def gettipo(self):
        return 'Servicio de Embalaje'
    def calcular_costo(self):
        costo_base = self.__precioporunidad * self.__cantidadunidades
        if self.__pesounidad > 50:
            costo_base *= 1.10
        return self.getcomision() + costo_base
    def __str__(self):
        return (super().__str__() + f", Precio por Unidad: {self.__precioporunidad:.2f}, Peso por Unidad: {self.__pesounidad}, Cantidad de Unidades: {self.__cantidadunidades}")
