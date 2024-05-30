from lista import Lista
from gestortransporte import GestorTransporte
from gestorembalaje import GestorEmbalaje
from datetime import datetime

def agregar_servicio(lista, tipo_servicio):
    if tipo_servicio.lower() == "transporte":
        gestor_transporte = GestorTransporte()
        lista.agregar_servicio(gestor_transporte.crear_servico_transporte())
    elif tipo_servicio.lower() == "embalaje":
        gestor_embalaje = GestorEmbalaje()
        lista.agregar_servicio(gestor_embalaje.crear_embalaje())

if __name__ == '__main__':
    lista = Lista()
    lista.cargar_servicios()
    while True:
        opcion = int(input("""Ingrese una opcion:
                      [1] Agregar servicio
                      [2] Mostrar costo y contratado en servicio de transporte
                      [3] Mostrar cantidad de servicios de embalaje con peso mayor a 50kg
                      [4] Mostrar servicio con mas contrataciones en una fecha
                      [0] Salir
                      """))
        if opcion == 0:
            break
        elif opcion == 1:
            tipo_servicio = input("Ingrese el tipo de servicio (transporte o embalaje): ")
            agregar_servicio(lista, tipo_servicio)
        elif opcion == 2:
            lista.mostrar_servicio_transporte()
        elif opcion == 3:
            lista.cantidad_embalajes_pesados()
        elif opcion == 4:
            fecha_str = input("Ingrese la fecha (DD/MM/YYYY): ")
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            lista.servicio_mas_contrataciones(fecha)

             
