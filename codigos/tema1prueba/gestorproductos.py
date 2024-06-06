from congelado import congelado
from refrigerado import refrigerado
import csv

class gestorproducto:
    def __init__(self):
        self.__productos = []
    
    def cargar(self, archivo='productos.csv'):
        with open(archivo, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for fila in reader:
                if fila[0] == 'C':
                    unproducto = congelado(
                        fila[1], fila[2], fila[3], float(fila[4]), fila[5], fila[6], float(fila[7]),
                        int(fila[8]), int(fila[9]), int(fila[10]), int(fila[11]), fila[12]
                    )
                else:
                    unproducto = refrigerado(
                        fila[1], fila[2], fila[3], float(fila[4]), fila[5], fila[6], float(fila[7]), fila[8]
                    )
                self.__productos.append(unproducto)
    def agregar_producto(self):
        producto_tipo = input("Ingrese el tipo de producto (refrigerado 'R' o congelado 'C'):")
        if producto_tipo == 'R':
            nombre = input("Ingrese el nombre del producto: ")
            fechaenvasado = input("Ingrese fecha de envasado (dd/mm/yyyy): ")
            fechavencimiento = input("Ingrese fecha de vencimiento (dd/mm/yyyy): ")
            temperatura = float(input("Ingrese la temperatura de mantenimiento recomendada: "))
            pais = input("Ingrese el país de origen: ")
            numerolote = input("Ingrese el número de lote: ")
            costo = float(input("Ingrese el costo base del producto: "))
            codigosupervision = input("Ingrese el código del organismo de supervisión alimentaria: ")
            unproducto = refrigerado(nombre, fechaenvasado, fechavencimiento, temperatura, pais, numerolote, costo, codigosupervision)
        elif producto_tipo == 'C':
            nombre = input("Ingrese el nombre del producto: ")
            fechaenvasado = input("Ingrese fecha de envasado (dd/mm/yyyy): ")
            fechavencimiento = input("Ingrese fecha de vencimiento (dd/mm/yyyy): ")
            temperatura = float(input("Ingrese la temperatura de mantenimiento recomendada: "))
            pais = input("Ingrese el país de origen: ")
            numerolote = input("Ingrese el número de lote: ")
            costo = float(input("Ingrese el costo base del producto: "))
            nitrogeno = int(input("Ingrese porcentaje de nitrógeno: "))
            oxigeno = int(input("Ingrese porcentaje de oxígeno: "))
            dioxido_de_carbono = int(input("Ingrese porcentaje de dióxido de carbono: "))
            vapordeagua = int(input("Ingrese porcentaje de vapor de agua: "))
            metodo_de_congelacion = input("Ingrese el método de congelación (frío mecánico o frío criogénico): ")
            unproducto = congelado(nombre, fechaenvasado, fechavencimiento, temperatura, pais, numerolote, costo, nitrogeno, oxigeno, dioxido_de_carbono, vapordeagua, metodo_de_congelacion)
        self.__productos.append(unproducto)
    def mostrar_tipoproductos(self):
        posicion = int(input("Ingrese la posición del producto: "))
        if 0 <= posicion < len(self.__productos):
            producto = self.__productos[posicion]
            if isinstance(producto, congelado):
                print("El producto es de tipo congelado")
            elif isinstance(producto, refrigerado):
                print("El producto es de tipo refrigerado")
        else:
            print("El producto no existe")
    def cantidad(self):
        contC = sum(isinstance(p, congelado) for p in self.__productos)
        contR = sum(isinstance(p, refrigerado) for p in self.__productos)
        print(f"La cantidad de productos congelados: {contC}\nCantidad de productos refrigerados: {contR}")
    def mostrar_producto(self):
        for producto in self.__productos:
            producto.mostrarproducto()
    

                        
