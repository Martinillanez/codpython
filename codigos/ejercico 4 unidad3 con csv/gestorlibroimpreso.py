from libroimpreso import libroimpreso
from datetime import datetime

class Gestorlibroimpreso:
    def crear_libro(self):
        print("Creando libro...")
        titulo = input("Titulo: ")
        categoria = input("Categoria: ")
        while True:
            try:
                precio_base = float(input("Precio base: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio base.")
        nombre_autor = input("Nombre autor: ")
        while True:
            try:
                fechaedicion = datetime.strptime(input("Fecha de edicion: "), "%d/%m/%Y")

                break
            except ValueError:
                print("Por favor, ingrese una fecha válida.")
        while True:
            try:
                cantpaginas = int(input("Cantidad de paginas: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad de páginas.")
        
        return libroimpreso(titulo, categoria, precio_base, nombre_autor, fechaedicion, cantpaginas)