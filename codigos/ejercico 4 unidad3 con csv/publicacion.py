class Publicaciones:
    def __init__(self, titulo, categoria, preciobase):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__preciobase = preciobase
    def get_titulo(self):
        return self.__titulo   
    def get_categoria(self):
        return self.__categoria   
    def get_preciobase(self):
        return self.__preciobase   
    def set_preciobase(self, preciobase):
        self.__preciobase = preciobase  
    def __str__(self):
        return f"Titulo: {self.__titulo}, Categoria: {self.__categoria}, Precio Base: {self.__preciobase:.2f}"