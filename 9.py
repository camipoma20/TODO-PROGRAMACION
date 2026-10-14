class RegistroEdades:
    def ejecutar(self):
        mayores = 0
        menores = 0

        while True:
            edad = int(input("Ingrese una edad (0 para terminar): "))
            if edad == 0:
                break

            if edad >= 18:
                mayores += 1
            else:
                menores += 1

        print("Mayores de edad:", mayores)
        print("Menores de edad:", menores)

registro = RegistroEdades()
registro.ejecutar()