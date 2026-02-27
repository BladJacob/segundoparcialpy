
import tkinter as tk

#creamos la ventana principal
def saludo():
    label_resultado.config(text="Hola alumnos de Python")
ventana = tk.Tk()

#le damos un titulo a la ventana
ventana.title("Mi primer aplicación")

#tamaño de la ventana
ventana.geometry("400x300")

#creamos un boton
boton_saludo = tk.Button(ventana, text="Saludar", command=saludo)
boton_saludo.pack(pady=20)

#creamos una etiqueta
label_resultado = tk.Label(ventana, text="", font=("Arial", 16, "bold"))

#mostrar la etiqueta en la ventana
label_resultado.pack(pady=20)
ventana.mainloop()
