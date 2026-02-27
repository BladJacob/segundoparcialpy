'''
Generar una ventana con un botón que al hacer click que muestre etiqueta numero1 y numero 2 
para ingresar 2 valores, y agregar 2 botones uno debajo de numero 2 que diga calcular
y otro un mas abajo pero a la derecha que diga resultado, sin tener funcionalidad por ahora
'''

import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

#Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

#Etiquetas y Entradas
tk.Label(ventana, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

#Boton de calcular
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

#Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

#cerrar la ventana
ventana.mainloop()








