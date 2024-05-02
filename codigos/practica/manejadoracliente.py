from clientes import cliente
import csv
class ManejadoraCliente:
    def __init__(self):
        self.lista_clientes = []
    def cargar_datos(self):
        archivo = open("cliente.csv",'r')
        reader=csv.reader(archivo,delimiter=',')
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                uncliente=cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.lista_clientes.append(uncliente)
    def buscar(self, dni):
        dni_encontrado= []
        for uncliente in self.lista_clientes:
            if uncliente.dni == dni:
                dni_encontrado.append(uncliente)
        return dni_encontrado
    def informe_reparacion(self, dni):
        dni_encontrado=self.buscar(dni)
        if dni_encontrado:
            for uncliente in dni_encontrado:
                print(f"dni: {uncliente.dni} apellido: {uncliente.apellido} nombre: {uncliente.nombre} telefono: {uncliente.telefono}")
                total_a_pagar = 0
                for vehiculo in cliente.vehiculos:
                    print(f"\nPatente: {vehiculo.patente} Vehículo: {vehiculo.modelo}")
                    print("Reparación precio repuesto mano de obra subtotal")
                    subtotal_vehiculo = 0
                    for reparacion in vehiculo.reparaciones:
                        subtotal = reparacion.precio_repuesto + reparacion.precio_manobra
                        subtotal_vehiculo += subtotal
                        print(f" ${reparacion.precio_repuesto:.2f} ${reparacion.precio_mano_obra:.2f} ${subtotal:.2f}")
                    total_a_pagar += subtotal_vehiculo
                    print(f"\nTOTAL A PAGAR ${subtotal_vehiculo:.2f}")
                print(f"\nTOTAL A PAGAR POR TODAS LAS REPARACIONES: ${total_a_pagar:.2f}")
        else:
            print("Cliente no encontrado.")
    
    def buscar_patente(self, patente):
         patente_encontrada= []
         for unareaparacion in self.lista_reparaciones:
             if unareaparacion.patente == patente:
                 patente_encontrada.append(unareaparacion)
                 return patente_encontrada
    def estado(self, patente):
        patente_encontrada = self.buscar_patente(patente)
        for uncliente in  patente_encontrada:
                    print("nombre : {}".format(uncliente.nombre))
                    print("apellido : {}".format(uncliente.apellido))
                    print("telefono : {}".format(uncliente.telefono))
                    print("vehiculo : {}".format(uncliente.vehiculo))
                    print("total a pagar : {}".format(uncliente.total_a_pagar))
                    for reparacion in patente_encontrada:
                       print("- Descripción: {}, Estado: {}".format(reparacion.descripcion, "Terminada" if reparacion.terminada else "Pendiente"))
                       