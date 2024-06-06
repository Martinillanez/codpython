from vehiculos import vehiculo

class vanes(vehiculo):
    __tipoC:str
    def __init__(self,marca, modelo, anio, capacidad, num, distancia, tarifa, tipoC):
        super().__init__(marca, modelo, anio, capacidad, num, distancia, tarifa)
        self.__tipoC = tipoC
    def gettipo(self):
        return self.__tipoC
    def tarifa_de_servicio(self):
        tarifa= float(self.gettarifa())
        if self.__tipoC == "minivan":
            imp= tarifa*0.90
        else:
            imp=tarifa*1.025
        return imp
    def mostrarvehiculos(self):
        print(super().__str__(), f"tarifa de servico vanes: {self.tarifa_de_servicio():.2f}")
    
       
        