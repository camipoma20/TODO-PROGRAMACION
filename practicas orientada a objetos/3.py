class CalculadoraPromedio:
    def ejecutar(self):
        cantidad = int(input("¿Cuántos números va a ingresar? "))
        if cantidad <= 0:
            print("Debe ingresar una cantidad mayor que cero.")
            return
        suma = 0
        for i in range(cantidad):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            suma += numero
        print("La suma es:", suma)
        print("El promedio es:", suma / cantidad)
calculadora = CalculadoraPromedio()
calculadora.ejecutar()