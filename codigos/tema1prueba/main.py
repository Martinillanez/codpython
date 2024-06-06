from gestorproductos import gestorproducto


if __name__ == '__main__':
    gestor = gestorproducto()
    gestor.cargar()
    while True:
        print("""
                    MENU DE OPCIONES
              [1] Agregar producto
              [2] Mostrar tipo de producto según su posición
              [3] Mostrar cantidad de productos
              [4] Mostrar todos los productos
              [0] Salir
              """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            gestor.agregar_producto()
        elif opcion == 2:
            gestor.mostrar_tipoproductos()
        elif opcion == 3:
            gestor.cantidad()
        elif opcion == 4:
            gestor.mostrar_producto()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
