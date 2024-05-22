from gestorcabaña import gestorcabaña
from gestorreserva import gestoreserva

if __name__ == '__main__':
    cabaña = gestorcabaña()
    reserva = gestoreserva()
    while True:
        print("""
                        MENU DE OPCIONES
              [1] Capacidad de las cabañas
              [2] Fecha de hospedaje
              [0] Salir
              """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cabaña.cantidad(reserva)
        elif opcion == 2:
            reserva.listareserva(cabaña)
        elif opcion == 0:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

