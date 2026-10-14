class ClasificadorNumeros:
    def ejecutar(self):
        cantidad = int(input("¿Cuántos números va a ingresar? "))
        positivos = 0
        negativos = 0
        ceros = 0

        for i in range(cantidad):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
            else:
                ceros += 1

        print("Positivos:", positivos)
        print("Negativos:", negativos)
        print("Ceros:", ceros)


clasificador = ClasificadorNumeros()
clasificador.ejecutar()