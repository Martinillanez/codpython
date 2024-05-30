from audiolibro import audilibro

class gestoraudiolibro:
    def crear_audiolibro(self):
        print("Creando CD...")
        titulo = input("Titulo: ")
        categoria = input("Categoria: ")
        precio_base = float(input("Precio base: "))
        tiempo = int(input("Tiempo (en minutos): "))
        nombre_narrador = input("Nombre narrador: ")
        return audilibro(titulo, categoria, precio_base, tiempo, nombre_narrador)