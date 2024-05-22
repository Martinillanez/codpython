class cabaña:
    def __init__(self, num, canthabitacion, cantcamagrande, cantcamachica, imp):
        self.__numero = num
        self.__canthabitacion = canthabitacion
        self.__cantcamasgrande = int(cantcamagrande)
        self.__cantcamachica = int(cantcamachica)
        self.__importepordia = float(imp)

    def getnumero(self):
        return self.__numero

    def getcanthabitacion(self):
        return self.__canthabitacion

    def getcantcamasgrande(self):
        return self.__cantcamasgrande

    def getcantcamachica(self):
        return self.__cantcamachica

    def getimporte(self):
        return self.__importepordia

    def __ge__(self, other):
        capacidad_total = self.__cantcamasgrande * 2 + self.__cantcamachica
        return capacidad_total >= other

    
