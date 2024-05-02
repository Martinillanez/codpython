from moto import moto
import csv 

class gestormoto:
    def __init__(self):
        self.listamotos = []

    def agregarmoto(self, unamoto):
        self.listamotos.append(unamoto)

    def cargarmotos(self):
        with open('D:/codigos/datosmoto.csv') as f: 
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                print("patente: {0}, marca: {1}, nombre: {2}, apellido: {3},  kilometraje: {4}".format(row[0], row[1], row[2], row[3], row[4]))

    def patente_registrada(self, patente):
        patente_encontrada = []
        for motos in self.listamotos:
            if motos.patente == patente:
                patente_encontrada.append(motos)
        return patente_encontrada

    def mostrardato_conductor(self, patente):
        for moto in self.listamotos:
            if moto.getpatente() == patente:
                return [moto.getnombre(), moto.getapellido(), moto.getmarca(), moto.getkilometraje()]
        print("No se encontró ninguna moto con esa patente")
        return None

if __name__ == "__main__":
    listamotos = gestormoto()
    listamotos.cargarmotos()
   
