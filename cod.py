import tkinter as tk
from PIL import Image, ImageTk
import random


class PerfilPersonal:

    # Constructor de la clase
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi perfil personal - Camila Poma")
        self.ventana.iconbitmap("icono.ico.ico")
        self.ventana.geometry("500x450")
        self.ventana.configure(bg="#FFFFFF")

        self.simbolos = ["✦", "✧", "✶", "⋆", "✩", "✴"]
        self.estrellas = []

        self.crear_estrellas()
        self.crear_foto()
        self.crear_titulo()
        self.crear_presentacion()
        self.crear_hobbies()
        self.crear_boton()

        self.ventana.after(300, self.distribuir_estrellas)
        self.ventana.bind("<Configure>", self.actualizar_estrellas)

    # Crear las estrellas decorativas
    def crear_estrellas(self):
        for i in range(60):
            estrella = tk.Label(
                self.ventana,
                text=random.choice(self.simbolos),
                font=("Arial", random.randint(12, 25)),
                bg="#FFFFFF",
                fg="#000000"
            )
            self.estrellas.append(estrella)

    # Distribuir las estrellas en la ventana
    def distribuir_estrellas(self, event=None):
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        if ancho <= 1 or alto <= 1:
            return

        for estrella in self.estrellas:
            x = random.randint(10, max(11, ancho - 35))
            y = random.randint(10, max(11, alto - 35))
            estrella.place(x=x, y=y)

    # Actualizar las estrellas al cambiar el tamaño
    def actualizar_estrellas(self, event=None):
        if event is not None and event.widget != self.ventana:
            return

        self.ventana.after(300, self.distribuir_estrellas)

    # Mostrar la foto del gatito
    def crear_foto(self):
        foto = Image.open("gato.png.jpeg").convert("RGBA")
        foto.thumbnail((180, 220))

        self.foto_tk = ImageTk.PhotoImage(foto)

        self.etiqueta_foto = tk.Label(
            self.ventana,
            image=self.foto_tk,
            bg="#FCE4EC",
            bd=0
        )
        self.etiqueta_foto.pack(pady=10)

    # Crear el título
    def crear_titulo(self):
        self.titulo = tk.Label(
            self.ventana,
            text="¡Hola, soy Camila Poma!",
            font=("Arial", 20, "bold"),
            bg="#FCE4EC",
            fg="#AD1457"
        )
        self.titulo.pack(pady=20)

    # Crear la presentación
    def crear_presentacion(self):
        self.presentacion = tk.Label(
            self.ventana,
            text="Bienvenidos a mi perfil personal",
            font=("Arial", 12),
            bg="#FCE4EC",
            fg="#444444"
        )
        self.presentacion.pack(pady=5)

    # Mostrar los hobbies
    def crear_hobbies(self):
        self.hobbies = tk.Label(
            self.ventana,
            text=(
                "MIS HOBBIES\n"
                "🎧 Escuchar música\n"
                "🍗 Comer\n"
                "🌿 Caminar en la naturaleza\n"
                "🍿 Ver series"
            ),
            font=("Arial", 14),
            bg="#FCE4EC",
            fg="#6A1B9A",
            justify="left"
        )
        self.hobbies.pack(pady=5)

    # Crear el botón
    def crear_boton(self):
        self.boton = tk.Button(
            self.ventana,
            text="¡Gracias por visitar mi perfil!",
            font=("Arial", 10),
            bg="#F8BBD0",
            fg="#880E4F"
        )
        self.boton.pack(pady=10)


# Programa principal
if __name__ == "__main__":
    ventana = tk.Tk()
    app = PerfilPersonal(ventana)
    ventana.mainloop()