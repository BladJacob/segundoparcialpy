
import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera aplicación")

#Tamaño de la ventana
ventana.geometry("400x300")

#Creamos una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Mundo!", font=("Arial", 16, "bold"))

etiqueta.pack(pady=20) 
#mostrar la etiqueta en la ventana
ventana.mainloop()
