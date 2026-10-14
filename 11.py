class CajaRegistradora:
    def __init__(self):
        self.total = 0

    def agregar_producto(self):
        producto = input("Nombre del producto: ")
        precio = float(input(f"Precio de {producto}: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
        self.total += precio

    def ejecutar(self):
        while True:
            print("\n1. Agregar producto")
            print("2. Finalizar")
            opcion = input("Elija una opción: ").strip()

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                break
            else:
                print("Opción no válida")

        print("El total a pagar es:", self.total)

caja = CajaRegistradora()
caja.ejecutar()