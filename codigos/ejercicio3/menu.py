from gestormoto import gestormoto
from gestorpedido import gestorpedido
class Menu:
    def __init__(self):
        self.motos = gestormoto()
        self.pedidos = gestorpedido()

    def menu(self):
        print("""
                        MENU DE OPCIONES
                      [1] Leer datos de moto
                      [2] Leer datos de pedido
                      [3] Cargar nuevo pedido
                      [4] Modificar tiempo de entrega
                      [5] Modificar tiempo promedio
                      [0] Salir
                      ->""")
        return int(input("Seleccione una opción: "))

    def ejecutar(self):
        opcion = self.menu()
        while opcion != 0:
            if opcion == 1:
                self.motos.cargarmotos()
                self.motos.patente_registrada()
            elif opcion == 2:
                self.pedidos.cargarpedido()
                self.pedidos.ordenar()
            elif opcion == 3:
                patente = input("Ingrese patente de la moto asignada al pedido: ")
                self.pedidos.nuevopedido(patente)
                self.pedidos.ordenar()
            elif opcion == 4:
                patente = input("Ingrese patente: ")
                ID = int(input("Ingrese ID del pedido: "))
                tiempo_real = input("Ingrese tiempo real de la entrega: ")
                self.pedidos.modificar(patente, ID, tiempo_real)
            elif opcion == 5:
                patente = input("Ingrese patente: ")
                self.motos.mostrardato_conductor(patente)
                self.pedidos.tiempo_promedio_entrega(patente)
            elif opcion == 6:
                self.pedidos.calcularcomision()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            opcion = self.menu()

if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()

