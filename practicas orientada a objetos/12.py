class CuentaBancaria:
    def __init__(self, saldo_inicial=1000):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print("Su saldo es:", self.saldo)

    def depositar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            self.saldo += monto
            print("Depósito realizado. Saldo:", self.saldo)

    def retirar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif monto <= self.saldo:
            self.saldo -= monto
            print("Retiro realizado. Saldo:", self.saldo)
        else:
            print("Fondos insuficientes")

    def ejecutar(self):
        while True:
            print("\n1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")
            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                self.consultar_saldo()
            elif opcion == "2":
                monto = float(input("Monto a depositar: "))
                self.depositar(monto)
            elif opcion == "3":
                monto = float(input("Monto a retirar: "))
                self.retirar(monto)
            elif opcion == "4":
                print("Un gusto atenderlo")
                break
            else:
                print("Opción no válida")

cuenta = CuentaBancaria()
cuenta.ejecutar()