from gestorvehiculo import gestorvehiculo

if __name__ == '__main__':
    gestor = gestorvehiculo()
    gestor.cargar()
    while True:
        print("""
                    MENU DE OPCIONES
              [1] Agregar vehículo
              [2] Mostrar vehículo según su posición
              [3] Mostrar cantidad de vehículos
              [4] Mostrar todos los vehículos
              [0] Salir
              """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            gestor.agregarvehiculo()
        elif opcion == 2:
            gestor.mostrara_tipovehiculo()
        elif opcion == 3:
            gestor.cantidad()
        elif opcion == 4:
            gestor.mostrar_vehiculos()
        elif opcion == 0:
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
