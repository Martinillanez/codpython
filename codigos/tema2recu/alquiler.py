class alquiler:
    __nombre: str
    __idcancha: str
    __hora: int
    __minutos: int
    __duracion: int
    def __init__(self, nom, id, hora, minuto, duracion):
        self.__nombre = nom
        self.__idcancha = id
        self.__hora= hora
        self.__minutos = minuto
        self.__duracion = duracion
    def getnombre(self):
        return self.__nombre
    def getidcancha(self):
        return self.__idcancha
    def gethora(self):
        return self.__hora
    def getminutos(self):
        return self.__minutos
    def getduracion(self):
        return self.__duracion
    def __gt__(self, other):
        if self.gethora() > other.gethora():
            return True
        if self.gethora() == other.gethora() and self.getminutos() > other.getminutos():
            return True
        return False

    