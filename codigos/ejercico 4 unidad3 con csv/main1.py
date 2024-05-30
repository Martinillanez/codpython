from audiolibro import audilibro
from libroimpreso import libroimpreso
from claselista import Lista
from gestoraudiolibro import gestoraudiolibro
from gestorlibroimpreso import Gestorlibroimpreso

def agregar_publicacion(lista, tipo_publicacion):
    if tipo_publicacion.lower() == "cd":
        gestor_audiolibro = gestoraudiolibro()
        lista.agregar_publicacion(gestor_audiolibro.crear_audiolibro())
    elif tipo_publicacion.lower() == "libro":
        gestor_libro = Gestorlibroimpreso()
        lista.agregar_publicacion(gestor_libro.crear_libro())
    else:
        print("La publicacion no existe")

if __name__ == '__main__':
    lista = Lista()
    lista.cargar_publicaciones()  # Cargar publicaciones desde los archivos CSV al inicio
    while True:
        opcion = int(input("""Ingrese una opcion:
                      [1] Agregar publicacion
                      [2] Determinar tipo de publicacion
                      [3] Mostrar cantidad de publicaciones de cada tipo
                      [4] Mostrar publicacion con su precio
                      [0] Salir
                      """))
        if opcion == 0:
            break
        elif opcion == 1:
            tipo_publicacion = input("Ingrese el tipo de publicacion (cd o libro): ")
            agregar_publicacion(lista, tipo_publicacion)
        elif opcion == 2:
            i = 1
            for publicacion in lista:
                print(f"Posicion: {i}\n{publicacion}\n")
                i += 1
            posicion = int(input("Ingrese la posicion de la publicacion que desea ver: "))
            publicacion = lista.buscar(posicion - 1)
            if isinstance(publicacion, audilibro):
                print(f"La publicacion en la posicion {posicion} es de tipo CD\n")
            elif isinstance(publicacion, libroimpreso):
                print(f"La publicacion en la posicion {posicion} es de tipo Libro\n")
            else:
                print("La publicacion no existe en la posicion dada\n")
        elif opcion == 3:
            lista.contar_publicaciones()
        elif opcion == 4:
            lista.precio()
            for publicacion in lista:
                print(f"Titulo: {publicacion.get_titulo()}\nCategoria: {publicacion.get_categoria()}\nPrecio: {publicacion.get_preciobase():.2f}\n")
        else:
            print("La opcion no existe")