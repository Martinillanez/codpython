class reserva:
    def __init__(self, numr, nom, numc, fechahospedaje, canthues, cantdias, imp):
        self.__numresrva = int(numr)
        self.__nombre = nom
        self.__numcabaña = numc
        self.__fechahospedaje = fechahospedaje
        self.__canthuespedes = int(canthues)
        self.__cantdias = int(cantdias)
        self.__importeseña = float(imp)

    def getnumreserva(self):
        return self.__numresrva

    def getnombre(self):
        return self.__nombre

    def getnumcabaña(self):
        return self.__numcabaña

    def getfecha(self):
        return self.__fechahospedaje

    def getcanthuespedes(self):
        return self.__canthuespedes

    def getcantdias(self):
        return self.__cantdias

    def getseña(self):
        return self.__importeseña




