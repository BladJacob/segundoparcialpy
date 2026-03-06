'''
crear una ventana con un fondo de una imagen y un frame con botones para realizar acciones
de recepcion para un cine con entradas donde pida nombre cantidad de compradores, tarjeta de cine
cantidad de boletos, una categoria de salida con el valor a pagar y una categoria de acciones
con la accion de procesar y una de salir con confirmacion
'''

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def procesar():
    try:
        #obtener datos de las entradas
        nombre = entrada_nombre.get()
        cantidad_compradores = int(entrada_cantidad.get())
        cantidad_boletos = int(entrada_boletos.get())
        tarjeta_cine = tarjeta_var.get()
        
        #Validar datos
        if not nombre:
            messagebox.showerror("Error", "Por favor ingresa un nombre")
            return
        
        #Validar limite de boletos por comprador (7 por persona)
        if cantidad_boletos > cantidad_compradores * 7:
            messagebox.showerror("Error", f"No se pueden comprar más de {cantidad_compradores * 7} boletos")
            return
        
        if cantidad_boletos <= 0:
            messagebox.showerror("Error", "La cantidad de boletos debe ser mayor a cero")
            return
        
        #Precio base por boleto
        precio_unitario = 12
        subtotal = cantidad_boletos * precio_unitario
        
        #Calcular descuento por cantidad de boletos
        descuento = 0
        if cantidad_boletos > 5:
            descuento = subtotal * 0.15 #15% si son mas de 5 boletos
        elif cantidad_boletos >= 3:
            descuento = subtotal * 0.10 #10% si son 3 a 5 boletos
        
        subtotal_con_descuento = subtotal - descuento
    
        #Calcular descuento adicional por tarjeta de cine
        descuento_tarjeta = 0
        if tarjeta_cine:
            descuento_tarjeta = subtotal_con_descuento * 0.10 #10% adicional con tarjeta
            
        #Total a pagar
        total = subtotal_con_descuento - descuento_tarjeta
        
        #Mostrar resultado
        etiqueta_valor_pagar.config(text=f"${total:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos")

def salir():
    if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres salir?"):
        ventana.destroy()
            
#Crear ventana principal
ventana = tk.Tk()
ventana.title("Cine")
ventana.geometry("500x400")

#Cargar imagen de fondo (manejo de error si no existe)
try:
    imagen = Image.open("cinepolis.jpg")
    fondo = ImageTk.PhotoImage(imagen)
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
except:
    ventana.configure(bg='gray')

#Titulo
titulo = tk.Label(ventana, text="Compra de Boletos", font=("Arial", 16, "bold"), bg="black", fg="white")
titulo.pack(pady=10)

#Frame de entradas
frame_entradas = tk.LabelFrame(ventana, text="Datos del comprador", bg="white", fg="black", padx=10, pady=10)
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entrada_nombre = tk.Entry(frame_entradas)
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_entradas, text="Cantidad de compradores:").grid(row=1, column=0, padx=10, pady=5)
entrada_cantidad = tk.Entry(frame_entradas)
entrada_cantidad.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_entradas, text="Cantidad de boletos:").grid(row=2, column=0, padx=10, pady=5)
entrada_boletos = tk.Entry(frame_entradas)
entrada_boletos.grid(row=2, column=1, padx=10, pady=5)

tarjeta_var = tk.BooleanVar()
tk.Checkbutton(frame_entradas, text="Tarjeta de Cine", variable=tarjeta_var).grid(row=3, column=0, columnspan=2, pady=5)

#Frame de resultado
frame_resultado = tk.LabelFrame(ventana, text="Valor a pagar", bg="white", fg="black", padx=10, pady=10)
frame_resultado.pack(pady=10)
etiqueta_valor_pagar = tk.Label(frame_resultado, text="$0.00", font=("Arial", 14, "bold"))
etiqueta_valor_pagar.pack()

#Frame de acciones
frame_acciones = tk.LabelFrame(ventana, text="Acciones", bg="white", fg="black", padx=10, pady=10)
frame_acciones.pack(pady=10)

tk.Button(frame_acciones, text="Procesar", command=procesar).pack(side="left", padx=10)
tk.Button(frame_acciones, text="Salir", command=salir).pack(side="right", padx=10)

ventana.mainloop()