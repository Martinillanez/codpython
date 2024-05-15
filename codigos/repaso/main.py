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
                  [1] Actualizar saldo
                  [2] Mostrar movimientos
                  [3] Ordenar lista de movimientos
                  [4] Salir
                  """)
        opcion = int(input("Seleccione una opción: "))  
        if (opcion == 1): 
            dni= input("ingrese un DNI:")
            clientes.actualizar(dni,movimientos)
        elif (opcion == 2):
                clientes.movimientos()
        elif (opcion == 3):
                movimientos.ordenar()
        elif (opcion == 4):
                print("Saliendo del programa...")
                break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
