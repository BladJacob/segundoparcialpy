import tkinter as tk

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        
        if opcion.get() == 1:
            resultado = num1 + num2
        elif opcion.get() == 2:
            resultado = num1 - num2
        elif opcion.get() == 3:
            resultado = num1 * num2
        elif opcion.get() == 4:
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        else:
            resultado = "Selecciona una operación"
            
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de radiobotones")
ventana.geometry("350x300")

# Entradas - CORREGIDO: primero crear el widget, luego aplicar grid
tk.Label(ventana, text="Número 1:").grid(row=0, column=0, padx=10, pady=5)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0, padx=10, pady=5)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1, padx=10, pady=5)

# Variables para los radiobotones
opcion = tk.IntVar()

tk.Label(ventana, text="Selecciona la operación:").grid(row=2, column=0, columnspan=2, pady=10)

tk.Radiobutton(ventana, text="Suma", variable=opcion, value=1).grid(row=3, column=0, sticky="w")
tk.Radiobutton(ventana, text="Resta", variable=opcion, value=2).grid(row=3, column=1, sticky="w")
tk.Radiobutton(ventana, text="Multiplicación", variable=opcion, value=3).grid(row=4, column=0, sticky="w")
tk.Radiobutton(ventana, text="División", variable=opcion, value=4).grid(row=4, column=1, sticky="w")

# Boton de calcular
tk.Button(ventana, text="Calcular", command=calcular).grid(row=5, column=0, columnspan=2, pady=10)

# Resultado - CORREGIDO: primero crear el widget, luego aplicar grid
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=6, column=0, columnspan=2)

# Ejecutar la aplicación
ventana.mainloop()