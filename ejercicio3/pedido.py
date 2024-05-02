class pedido:
    def __init__(self, patente, ID, comida, tiempo_estimado, tiempo_real, precio):
        self.patente =  patente
        self.ID = ID
        self.comida = comida
        self.tiempo_estimado = tiempo_estimado
        self.tiempo_real = tiempo_real
        self.precio = precio
    def __str__(self):
        return("pedido id:{}--comida:{}--tiempo estimado{}--tiempo real{}--precio{}".format(self.ID, self.patente,self.comida,self.tiempo_estimado, self.tiempo_real, self.precio))
    
    def __it__(self, other):
        return self.patente<other.getpatente()
    
    def settiemporeal(self, entrega):
        self.tiempo_real=entrega
        print('tiempo real de entrega modificado!')

    def getpatente(self):
        return(self.patente)
    
    def getID(self):
        return(self.ID)
    
    def getcomida(self):
        return(self.comida)
    
    def gettiempo_estimado(self):
        return(self.tiempo_estimado)
    
    def gettiempo_real(self):
        return(self.tiempo_real)
    
    def getprecio(self):
        return(self.precio)
    