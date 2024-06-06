from producto import producto

class congelado(producto):
    def __init__(self, nom, fechae, fechav, tempa, pais, numlote, costo, nitrogeno, oxigeno, dioxido_de_carbono, vapordeagua, metodo):
        super().__init__(nom, fechae, fechav, tempa, pais, numlote, costo)
        self.__nitrogeno = nitrogeno
        self.__oxigeno = oxigeno
        self.__dioxido_de_carbono = dioxido_de_carbono
        self.__vapordeagua = vapordeagua
        self.__metodo_de_congelacion = metodo
    def get_nitrogeno(self):
        return self.__nitrogeno   
    def get_oxigeno(self):
        return self.__oxigeno  
    def get_dioxido_de_carbono(self):
        return self.__dioxido_de_carbono  
    def get_vapordeagua(self):
        return self.__vapordeagua    
    def get_metodo(self):
        return self.__metodo_de_congelacion   
    def importeventa(self):
        return self.getcosto() * 1.15  
    def mostrarproducto(self):
        print(super().__str__(), f"Importe de venta: {self.importeventa():.2f}")