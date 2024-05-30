from publicacion import Publicaciones

class audilibro(Publicaciones):
    def __init__(self, titulo, categoria, preciobase, tiempo, nombrenarrador):
        super().__init__(titulo, categoria, preciobase)
        self.__tiempo = tiempo
        self.__nombrenarrador = nombrenarrador
    
    def get_tiempo(self):
        return self.__tiempo
    
    def get_nombrenarrador(self):
        return self.__nombrenarrador
    
    def __str__(self):
        return super().__str__() + f", Tiempo: {self.__tiempo} mins, Narrador: {self.__nombrenarrador}"
    