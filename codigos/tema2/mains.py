from gestorcliente import gestorcliente
from gestormovimiento import gestormovimiento

if __name__ == '__main__':
    clientes = gestorcliente()
    clientes.cargar()
    movimientos = gestormovimiento()
    movimientos.cargar()
    while True:
        print(""" 
                    MENU DE OPCIONES
              [1] actualizar saldo
              [2] mostrar movimientos
              [3] ordenar lista de movimientos
              [4] salir
              """)
        opcion= int(input("ingrese una opcion:"))
        if (opcion == 1):
            dni = input("ingrese DNI:")
            clientes.actualizar(dni, movimientos)
        elif (opcion == 2):
            clientes.movimiento(movimientos)
        elif (opcion== 3):
            movimientos.ordenar()
        elif (opcion == 4):
            print("saliendo del programa")
            break
        else:
            print("opcion no valida. por favor, seleccione una opcion valida")