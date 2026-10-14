class ClasificadorEdades:
    def ejecutar(self):
        cantidad = int(input("¿Cuántas edades va a ingresar? "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

        ninos = adolescentes = adultos = mayores = 0
        for i in range(cantidad):
            edad = int(input(f"Ingrese la edad {i + 1}: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                return
            if edad <= 12:
                ninos += 1
            elif edad <= 17:
                adolescentes += 1
            elif edad <= 60:
                adultos += 1
            else:
                mayores += 1

        print("Niños:", ninos)
        print("Adolescentes:", adolescentes)
        print("Adultos:", adultos)
        print("Adultos mayores:", mayores)

clasificador = ClasificadorEdades()
clasificador.ejecutar()