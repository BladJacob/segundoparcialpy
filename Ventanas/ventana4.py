import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    texto = entrada.get()
    label_resultado.config(text=f"Escribiste: {texto}")
    
    ventana = tk.Tk()
ventana.title("Entrada de texto")
ventana.geometry("400x300")

#creamos una entrada de texto
entrada = ttk.Entry(ventana, font=("Arial", 14))
