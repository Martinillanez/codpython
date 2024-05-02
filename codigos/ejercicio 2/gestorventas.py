import numpy as np
class gestorventas:
    __gestorventas: np.ndarray

    def __init__(self) -> None:
        self.__gestorventas = np.empty([5, 7], dtype=float)

    def ingresarfactura(self):
        dia = int(input("ingrese dia del 1 al 7:"))
        sucursal = int(input("ingrese numero sucursal del 1 al 5:"))
        importe = float(input("ingrese importe de factura:"))
        self.__gestorventas[sucursal - 1][dia - 1] += importe

    def calcular_total(self, sucursal):
        total = sum(self.__gestorventas[sucursal - 1])
        print("la factura total es:", total)

    def sucursal_mas_facturo(self, dia):
        max_facturacion = max((self.__gestorventas[i][dia - 1], i + 1) for i in range(5))
        print("la sucursal que mas facturo es:", max_facturacion[1])

    def sucursal_menos_facturo(self):
        min_facturacion = min((sum(self.__gestorventas[i]), i + 1) for i in range(5))
        print("la sucursal que menos facturo es:", min_facturacion[1])

    def total_factura(self):
        total = np.sum(self.__gestorventas)
        print("el total acumulado es:", total)

    def menu(cls):
      
        while True:
            print("\nMenú:")
            print("a) Ingresar factura")
            print("b) Calcular total de facturación para una sucursal")
            print("c) Obtener la sucursal que más facturó en un día")
            print("d) Calcular la sucursal con menos facturación durante toda la semana")
            print("e) Calcular el total facturado por todas las sucursales durante toda la semana")
            print("q) Salir")
            opcion = input("Ingrese la opción deseada: ")
            gestor = cls()
            if opcion == 'a':
                gestor.ingresarfactura()
            elif opcion == 'b':
                sucursal = int(input("Ingrese el número de sucursal (1-5): "))
                gestor.calcular_total(sucursal)
            elif opcion == 'c':
                dia = int(input("Ingrese el día de la semana (1-7): "))
                gestor.sucursal_mas_facturo(dia)
            elif opcion == 'd':
                gestor.sucursal_menos_facturo()
            elif opcion == 'e':
                gestor.total_factura()
            elif opcion == 'q':
                print("Saliendo del programa...")
                break  # Movemos el break aquí dentro del bucle
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

gestorventas.menu()



