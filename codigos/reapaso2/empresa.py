class Empresa:
    __nombreempresa:str
    __nombrecontratante:str
    __direccion:str
    __fechaservicio:int
    __comision:float
    def __init__(self, nombreemp, nombrecon, direccion, fechaservicio, comision):
        self.__nombreempresa = nombreemp
        self.__nombrecontratante = nombrecon
        self.__direccion = direccion
        self.__fechaservicio = fechaservicio
        self.__comision = comision
    def getnombreempresa(self):
        return self.__nombreempresa
    def getnombrecontratante(self):
        return self.__nombrecontratante
    def getdireccion(self):
        return self.__direccion
    def getfechaservicio(self):
        return self.__fechaservicio
    def getcomision(self):
        return self.__comision
    def setcomision(self, comision):
        self.__comision = comision
    def __str__(self):
        return (f"Nombre Empresa: {self.__nombreempresa}, Nombre Contratante: {self.__nombrecontratante}, "
                f"Direccion: {self.__direccion}, Fecha Servicio: {self.__fechaservicio}, Comision: {self.__comision:.2f}")
