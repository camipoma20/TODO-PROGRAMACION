import tkinter as tk
from PIL import Image, ImageTk
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi perfil personal - Camila Poma")
ventana.geometry("500x450")
ventana.configure(bg="#FFFFFF")
# Decoraciones de estrellas adaptables
import random

simbolos = ["✦", "✧", "✶", "⋆", "✩", "✴"]
estrellas = []

for i in range(60):
    estrella = tk.Label(
        ventana,
        text=random.choice(simbolos),
        font=("Arial", random.randint(12, 25)),
        bg="#FFFFFF",
        fg="#000000"
    )
    estrellas.append(estrella)

def distribuir_estrellas(event=None):
    if event is not None and event.widget != ventana:
        return

    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()

    if ancho <= 1 or alto <= 1:
        return

    for estrella in estrellas:
        x = random.randint(10, max(11, ancho - 35))
        y = random.randint(10, max(11, alto - 35))
        estrella.place(x=x, y=y)

# Esperar a que la ventana tenga su tamaño definitivo
ventana.after(300, distribuir_estrellas)

# Redistribuir al cambiar el tamaño, con una pequeña pausa
def actualizar_estrellas(event=None):
    if event is not None and event.widget != ventana:
        return

    ventana.after(300, distribuir_estrellas)

ventana.bind("<Configure>", actualizar_estrellas)

# Mi gatito
foto = Image.open("gato.png.jpeg").convert("RGBA")
foto.thumbnail((180, 220))

foto_tk = ImageTk.PhotoImage(foto)

etiqueta_foto = tk.Label(
    ventana,
    image=foto_tk,

    bg="#FCE4EC",
    bd=0
)
etiqueta_foto.pack(pady=10)
# Titulo
titulo = tk.Label(
    ventana,
    text="¡Hola, soy Camila Poma!",
    font=("Arial", 20, "bold"),
    bg="#FCE4EC",
    fg="#AD1457"
)
titulo.pack(pady=20)

# Presentacion
presentacion = tk.Label(
    ventana,
    text="Bienvenidos a mi perfil personal",
    font=("Arial", 12),
    bg="#FCE4EC",
    fg="#444444"
)
presentacion.pack(pady=5)

# Mis Hobbies
hobbies = tk.Label(
    ventana,
    text="MIS HOBBIES\n"
         "🎧 Escuchar música\n"
         "🍗 Comer\n"
         "🌿 Caminar en la naturaleza\n"
         "🍿 Ver series",
    font=("Arial", 14),
    bg="#FCE4EC",
    fg="#6A1B9A",
    justify="left"
)

hobbies.pack(pady=5)

# Botón

boton = tk.Button(
    ventana,
    text="¡Gracias por visitar mi perfil!",
    font=("Arial", 10),
    bg="#F8BBD0",
    fg="#880E4F"
)
boton.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()