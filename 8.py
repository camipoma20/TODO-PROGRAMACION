class RegistroNotas:
    def ejecutar(self):
        suma = 0
        cantidad = 0
        mayor = None
        menor = None

        while True:
            nota = float(input("Ingrese una nota (-1 para finalizar): "))
            if nota == -1:
                break

            suma += nota
            cantidad += 1
            if mayor is None or nota > mayor:
                mayor = nota
            if menor is None or nota < menor:
                menor = nota

        if cantidad > 0:
            print("Promedio:", suma / cantidad)
            print("Nota mayor:", mayor)
            print("Nota menor:", menor)
        else:
            print("No se ingresaron notas")

registro = RegistroNotas()
registro.ejecutar()