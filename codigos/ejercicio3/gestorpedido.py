import csv
from pedido import pedido

class gestorpedido:
    def __init__(self):
        self.listapedidos = []

    def agregarpedido(self, unpedido):
        self.listapedidos.append(unpedido)

    def cargarpedido(self):
        with open('D:\codigos\datospedido.csv') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                print("patente: {0}, id: {1}, comida: {2}, tiempo estimado: {3}, tiempo real: {4}, precio: {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    def nuevopedido(self, patente):
        for moto in self.listamotos:
            if moto.patente == patente:
                ID = moto.getID()   
                comida= input("Comida: ")
                tiempo_estimado = input("Tiempo estimado: ")
                tiempo_real = input("Tiempo real: ")
                precio = float(input("Precio: "))
                nuevo_pedido = pedido(ID, comida, tiempo_estimado, tiempo_real, precio)
                moto.agregarpedido(nuevo_pedido)
                print("Pedido cargado correctamente")
                return
        print("No se encontró ninguna moto con esa patente")

    def modificar_tiempo_real(self, ID):
        for pedido in self.listapedidos:
            if pedido.ID == ID:
                tiempo_real = int(input("Ingrese nuevo tiempo real: "))
                pedido.settiemporeal(tiempo_real)
                return pedido
        print("El pedido no se ha encontrado")
        return None

    def tiempo_promedio_entrega(self):
        acum = 0
        cont = 0
        for pedido in self.listapedidos:
            if pedido.tiempo_real is not None:
                acum += pedido.tiempo_real
                cont += 1
        if cont > 0:
            prom = acum / cont  
            print("El tiempo promedio de entrega es:", prom, "minutos")
        else:
            print("No hay pedidos cargados")

    def calcular_comision(self):
        comision_total = 0
        for pedido in self.listapedidos:
            if pedido.tiempo_real is not None:
                if pedido.tiempo_estimado > pedido.tiempo_real:
                    comision = (pedido.tiempo_estimado - pedido.tiempo_real) * pedido.precio
                    print("El precio de la comisión para el pedido", pedido.identificador, "es:", comision)
                    comision_total += comision
            else:
                print("No hay comisión para el pedido", pedido.identificador)
        if comision_total > 0:
            print("El precio total de las comisiones es:", comision_total)
        else:
            print("No hay comisiones calculadas")

    def ordenar(self):
        self.listapedidos.sort()
        for pedido in self.listapedidos:
            print(pedido)