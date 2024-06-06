from vehiculos import vehiculo

class autobus(vehiculo):
    __tipo:str
    __turno:str
    def __init__(self,marca, modelo, anio, capacidad, num, distancia, tarifa, tipo, turno):
        super().__init__(marca, modelo, anio, capacidad, num, distancia, tarifa)
        self.__tipo = tipo
        self.__turno = turno
    def gettipo(self):
        return self.__tipo
    def getturno(self):
        return self.__turno
    def tarifa_de_servicio(self):
        tarifa= float(self.gettarifa())
        if self.__turno == 'noche' and self.__tipo == 'turismo':
            imp= tarifa * 1.20
        else:
            imp = tarifa * 1.05
        return imp
    def mostrarvehiculos(self):
       print(super().__str__(), f"tarifa de servico autobus: {self.tarifa_de_servicio():.2f}")


