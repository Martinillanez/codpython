from empresa import Empresa

class ServicioTransporte(Empresa):
    __preciohora: float
    __pesocarga: int
    __direcciondestino: str
    def __init__(self, nombreemp, nombrecon, direccion, fechaservicio, comision, preciohora, pesocarga, direcciondestino):
        super().__init__(nombreemp, nombrecon, direccion, fechaservicio, comision)
        self.__preciohora = preciohora
        self.__pesocarga = pesocarga
        self.__direcciondestino = direcciondestino
    def get_preciohora(self):
        return self.__preciohora
    def get_pesocarga(self):
        return self.__pesocarga
    def get_direcciondestino(self):
        return self.__direcciondestino
    def gettipo(self):
        return 'Servicio de Transporte'
    def calcular_costo(self):
        costo_base = self.__preciohora * self.__pesocarga
        if self.__pesocarga > 500:
            costo_base *= 1.10
        return self.getcomision() + costo_base
    def __str__(self):
        return (super().__str__() + f", Precio por Hora: {self.__preciohora:.2f}, Peso de la Carga: {self.__pesocarga}, Direccion de Destino: {self.__direcciondestino}")
