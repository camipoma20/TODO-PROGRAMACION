class Calculadora:
    def ejecutar(self):
        while True:
            print("\n1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = input("Elija una opción: ").strip()

            if opcion == "5":
                print("Hasta luego")
                break
            if opcion not in ("1", "2", "3", "4"):
                print("Opción no válida")
                continue

            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print("Resultado:", a + b)
            elif opcion == "2":
                print("Resultado:", a - b)
            elif opcion == "3":
                print("Resultado:", a * b)
            elif opcion == "4":
                if b == 0:
                    print("No se puede dividir entre cero.")
                else:
                    print("Resultado:", a / b)

calculadora = Calculadora()
calculadora.ejecutar()