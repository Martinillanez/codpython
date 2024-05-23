class cancha:
    __id: str
    __tipo: str
    __importehora: float
    def __init__(self, id, tipo, imph):
        self.__id = id
        self.__tipo = tipo
        self.__importehora = imph
    def getid(self):
        return self.__id
    def gettipo(self):
        return self.__tipo
    def getimportehora(self):
        return self.__importehora
