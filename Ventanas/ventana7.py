import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("cerrar con confirmacion")
root.geometry("500x400")

def cerrar():
    respuesta = messagebox.askyesno("salir","deseas cerrar el programa?")
    if respuesta:
        root.destroy()

imagen = Image.open("books-5937823_1280.jpg")
fondo = ImageTk.PhotoImage(imagen)

label_fondo = tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

frame_acciones = tk.LabelFrame(root, text="acciones", bg="red", fg="white", padx=10, pady=10)
frame_acciones.place(x=200, y=200, width=200, height=100)

tk.Button(frame_acciones, text="salir", command=cerrar).pack(pady=20)

root.mainloop()