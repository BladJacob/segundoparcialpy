import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 +num2
        etiqueta_resultado.config(text=f"Resulatdo: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por faor ingresa numeros validos")
        
#Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de suma")
ventana.geometry("300x200")

#Etiquetas y Entradas
tk.Label(ventana, text="Primer numero:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Segundo numero:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

#Boton de sumar
tk.Button(ventana, text="Sumar", command=sumar).pack(pady = 10)

#Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

#Ejecutar la aplicacion
ventana.mainloop()









        
        