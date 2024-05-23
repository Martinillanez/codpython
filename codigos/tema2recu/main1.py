from gestoralquiler import gestoralqulier
from gestorcancha import gestorcancha

if __name__ == '__main__':
    gestor_cancha = gestorcancha()
    gestor_alquiler = gestoralqulier()
    while True:
        print("""
                    MENU DE OPCIONES
              [1] Listado de alquileres por hora
              [2] cantidad de minutos  alquilada la cancha
              [0] Salir
              """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            gestor_alquiler.listado(gestor_cancha)
        elif opcion == 2:
            gestor_alquiler.cantidad()
        elif opcion == 0:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    