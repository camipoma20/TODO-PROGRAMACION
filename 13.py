class EstadisticasNotas:
    def ejecutar(self):
        aprobadas = 0
        reprobadas = 0
        suma = 0

        for i in range(10):
            nota = float(input(f"Ingrese la nota {i + 1} (0 a 100): "))
            if nota < 0 or nota > 100:
                print("Nota inválida. Ingrese un valor de 0 a 100.")
                return

            suma += nota
            if nota >= 51:
                aprobadas += 1
            else:
                reprobadas += 1

        print("Aprobadas:", aprobadas)
        print("Reprobadas:", reprobadas)
        print("Promedio:", suma / 10)
        print("Porcentaje de aprobadas:", aprobadas * 10, "%")

estadisticas = EstadisticasNotas()
estadisticas.ejecutar()