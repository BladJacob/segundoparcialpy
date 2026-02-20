'''
Crear un programa que calcule las areas de un cuadrado, rectangulo, triangulo, circulo 
y trapecio y una opcion para salir del programa, utilizando funciones para cada area
y un menu para seleccionar la opcion deseada usando funciones con un ciclo while
para mostrar el menu hasta que el usuario quiera salir
'''

import math,os
os.system("cls")

def menu():
    print("------Menu de Areas------")
    print("1. Area del Cuadrado")
    print("2. Area del Rectangulo")
    print("3. Area del Triangulo")
    print("4. Area del Circulo")
    print("5. Area del Trapecio")
    print("6. Salir del programa para ser feliz")
    
def area_cuadrado(lado):
        return lado * lado
    
def area_rectangulo(base, altura):
        return base * altura
    
def area_triangulo(base, altura):
        return (base * altura) / 2
    
def area_circulo(radio):
        return math.pi * radio * radio
    
def area_trapecio(base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2
                
                
                
while True:
        menu()
        opcion = int(input("Selecciona una opcion: "))
        
        if opcion ==1:
            lado = float(input("Ingrese el lado del cuadrado: "))
            resultado = area_cuadrado(lado)
            print("El area del cuadrado es: ", resultado)
            
        elif opcion == 2:
            Base = float(input("Ingrese la base del rectangulo: "))
            Altura = float(input("Ingrese la altura del rectangulo: "))
            resultado = area_rectangulo(Base, Altura)
            print("El area del rectangulo es: ", resultado)
            
        elif opcion == 3:
            Base = float(input("Ingrese la base del triangulo: "))
            Altura = float(input("Ingrese la altura del triangulo: "))
            resultado = area_triangulo(Base, Altura)
            print("El area del triangulo es: ", resultado)
            
        elif opcion == 4:
            Radio = float(input("Ingrese el radio del circulo: "))
            resultado = area_circulo(Radio)
            print("El area del circulo es: ", resultado)
            
        elif opcion == 5:
            Base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            Base_menor = float(input("Ingrese la base menor del trapecio: "))
            Altura = float(input("Ingrese la altura del trapecio: "))
            resultado = area_trapecio(Base_mayor, Base_menor, Altura)
            print("El area del trapecio es: ", resultado)
                
        # Salir del programa
        elif opcion == 6:
            print("Gracias por usar el programa, adios")
            break
            
        else:
            print("Opcion no valida, por favor seleccione una opcion del menu")
            