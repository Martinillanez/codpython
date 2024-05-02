from reparacion import reaparacion
import csv
class manejadoreparaciones:
    def __init__(self):
        self.lista_reparaciones = []
    def cargar_datos(self):
        archivo = open("reparaciones.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                unareparacion=reaparacion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.lista_reparaciones.append(unareparacion)
    

                 