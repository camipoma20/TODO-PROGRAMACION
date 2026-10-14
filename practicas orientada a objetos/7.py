class CalculadoraAreas:
    def area_cuadrado(self, lado):
        return lado * lado

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_triangulo(self, base, altura):
        return base * altura / 2

    def ejecutar(self):
        while True:
            print("\n1. Cuadrado")
            print("2. Rectángulo")
            print("3. Triángulo")
            print("4. Salir")
            opcion = input("Elija una opción: ").strip()

            if opcion == "4":
                print("adios,vuelva cuando lo necesite")
                break
            elif opcion == "1":
                lado = float(input("Ingrese el lado: "))
                print("Área:", self.area_cuadrado(lado))
            elif opcion == "2":
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Área:", self.area_rectangulo(base, altura))
            elif opcion == "3":
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                print("Área:", self.area_triangulo(base, altura))
            else:
                print("Opción no válida")

figuras = CalculadoraAreas()
figuras.ejecutar()