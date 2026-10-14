class MenuNumerico:
    def factorial(self, numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    def mostrar_tabla(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    def ejecutar(self):
        while True:
            print("\n1. Factorial")
            print("2. Tabla de multiplicar")
            print("3. Paridad")
            print("4. Cuadrado")
            print("5. Salir")
            opcion = input("Elija una opción: ").strip()

            if opcion == "5":
                print("Un gusto atenderlo")
                break
            if opcion not in ("1", "2", "3", "4"):
                print("Opción no válida")
                continue

            numero = int(input("Ingrese un número: "))
            if opcion == "1":
                if numero < 0:
                    print("El factorial no está definido para números negativos.")
                else:
                    print("Factorial:", self.factorial(numero))
            elif opcion == "2":
                self.mostrar_tabla(numero)
            elif opcion == "3":
                print("El número es par" if numero % 2 == 0 else "El número es impar")
            elif opcion == "4":
                print("Cuadrado:", numero * numero)

menu = MenuNumerico()
menu.ejecutar()