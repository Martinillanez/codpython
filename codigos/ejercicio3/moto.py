class moto:
    def __init__(self, patente, marca, nombre, apellido, kilometraje):
        self.patente = patente
        self.marca = marca
        self.nombre = nombre
        self.apellido = apellido
        self.kilometraje = kilometraje
    def __str__(self):
        return("Patente:{}--Marca:{}--Nombre:{}--Apellido:{}--Kilometraje:{}".format(self.patente,self.marca,self.nombre,self.apellido,self.kilometraje))
    
    def getpatente(self):
        return self.patente
    
    def getNombre(self):
        return self.nombre
    
    def getapellido(self):
        return self.apellido            
    