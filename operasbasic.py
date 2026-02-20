'''
crear un programa en el que pidamos las opciones con un menu(), y cada operacion sera una funcion:
suma, resta, dividir, multipicar
Antes de limpiar pantalla mostrar resultado de la operacion
Utilizando funciones con un siclo while para mostrar el menu hasta 
que el usuario quiera salir
'''

def menu():
    print("Menu de operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
    
while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "5":
        print("Saliendo del programa...")
        break
    
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    
    if opcion == "1":
        resultado = suma(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = resta(num1, num2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == "4":
        resultado = division(num1, num2)
        print(f"El resultado de la division es: {resultado}")
    else:
        print("Opcion no valida. Por favor seleccione una opcion del 1 al 5.")
    input("Presione Enter para continuar...")
    