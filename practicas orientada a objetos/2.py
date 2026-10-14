class MayorMenor:
    def ejecutar(self):
        for i in range(10):
            numero = int(input(f"Ingrese el número {i + 1}: 
            if i == 0:
                mayor = numero
                menor = numero
            else:
                if numero > mayor:
                    mayor = numero
                if numero < menor:
                    menor = numero
        print("El mayor es:", mayor)
        print("El menor es:", menor)
analizador = MayorMenor()
analizador.ejecutar()