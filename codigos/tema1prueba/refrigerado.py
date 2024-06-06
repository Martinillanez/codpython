from producto import producto
from datetime import datetime

class refrigerado(producto):
    def __init__(self, nom, fechae, fechav, tempa, pais, numlote, costo, codsup):
        super().__init__(nom, fechae, fechav, tempa, pais, numlote, costo)
        self.__codigosupervison = codsup
    def getcodigosupervison(self):
        return self.__codigosupervison   
    def importeventa(self):
        fecha_vencimiento = datetime.strptime(self.getfechavencimiento(), '%d/%m/%Y')
        dias_para_vencer = (fecha_vencimiento - datetime.now()).days
        if dias_para_vencer <= 60:
            imp = self.getcosto() * 0.9
        else:
            imp = self.getcosto() * 1.01
        return imp 
    def mostrarproducto(self):
        print(super().__str__(), f"Importe de venta: {self.importeventa():.2f}")

    