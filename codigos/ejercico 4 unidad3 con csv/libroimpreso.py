from publicacion import Publicaciones
from datetime import datetime

class libroimpreso(Publicaciones):
    def __init__(self, titulo, categoria, preciobase, nombreautor, fechaedicion, cantpaginas):
        super().__init__(titulo, categoria, preciobase)
        self.__nombreautor = nombreautor
        self.__fechaedicion = fechaedicion
        self.__cantpaginas = cantpaginas  
    def get_nombreautor(self):
        return self.__nombreautor 
    def get_fechaedicion(self):
        return self.__fechaedicion   
    def get_cantpaginas(self):
        return self.__cantpaginas  
    def __str__(self):
        return super().__str__() + f", Autor: {self.__nombreautor}, Fecha Edicion: {self.__fechaedicion}, Cantidad de Paginas: {self.__cantpaginas}"
    @staticmethod
    def parse_fecha(fecha_str):
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y").year
        except ValueError:
            try:
                return datetime.strptime(fecha_str, "%Y").year
            except ValueError:
                raise ValueError(f"Formato de fecha no válido: {fecha_str}")
