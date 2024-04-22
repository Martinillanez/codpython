class CajaDeAhorro:
    def __init__(self, nrocuenta, cuil, apellido, nombre, saldo):
        self.nrocuenta = nrocuenta
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.saldo = saldo

    def mostrar_datos(self):
        print("Número de cuenta:", self.nrocuenta)
        print("CUIL:", self.cuil)
        print("Apellido:", self.apellido)
        print("Nombre:", self.nombre)
        print("Saldo:", self.saldo)

    def extraer(self, importe):
        if self.saldo >= importe:
            self.saldo -= importe
            print("Extracción exitosa. Nuevo saldo:", self.saldo)
        else:
            print("Error: saldo insuficiente.")
            return -1

    def depositar(self, importe):
        if importe > 0:
            self.saldo += importe
            print("Depósito exitoso. Nuevo saldo:", self.saldo)
        else:
            print("Error: el importe debe ser positivo")

    def validar_cuil(self):
        if len(self.cuil) != 13 or self.cuil[2] != "-" or self.cuil[11] != "-":
            return False

        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        cuil_sin_guiones = self.cuil.replace("-", "")

        aux = 0
        for i in range(10):
            aux += int(cuil_sin_guiones[i]) * base[i]

        aux = 11 - (aux - (int(aux / 11) * 11))

        if aux == 11:
            aux = 0
        if aux == 10:
            aux = 9

        return aux == int(cuil_sin_guiones[10])


def test():
    cuentas = []
    for _ in range(3):
        cuil = input("Ingrese CUIL: ")
        cuenta = CajaDeAhorro("", cuil, "", "", 0)  # Número de cuenta se solicita después de validar CUIL
        if cuenta.validar_cuil():
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            numero_cuenta = input("Ingrese número de cuenta: ")
            saldo = float(input("Ingrese saldo inicial: "))
            cuenta = CajaDeAhorro(numero_cuenta, cuil, apellido, nombre, saldo)
            cuentas.append(cuenta)
        else:
            print("CUIL inválido. Ingrese nuevamente.")

    # Ejemplo de uso de métodos de la clase
    for cuenta in cuentas:
        print("\nCuenta:")
        cuenta.mostrar_datos()
        deposito = float(input("Ingrese monto a depositar: "))
        cuenta.depositar(deposito)
        extraccion = float(input("Ingrese monto a extraer: "))
        cuenta.extraer(extraccion)
