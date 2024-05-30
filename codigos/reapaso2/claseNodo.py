from empresa import Empresa

class Nodo:
    __empresa: Empresa
    __siguiente: object
    def __init__(self, empresa):
        self.__empresa = empresa
        self.__siguiente = None
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
    def get_siguiente(self):
        return self.__siguiente
    def get_empresa(self):
        return self.__empresa
