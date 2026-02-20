
import math

class figuras:
    
    def cuadrado(self, lado):
        return lado * lado
    
    def rectangulo(self, base, altura):
        return base * altura
    
    def triangulo(self, base, altura):
        return (base * altura) / 2
    
    def circulo(self, radio):
        return math.pi * radio * radio
    
    def trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2

obj = figuras()

# Cuadrado
lado = int(input("Ingrese el lado del cuadrado: "))
print("Area del cuadrado:", obj.cuadrado(lado))

# Rectangulo
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
print("Area del rectangulo:", obj.rectangulo(base, altura))

# Triangulo
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))
print("Area del triangulo:", obj.triangulo(base, altura))

# Circulo
radio = int(input("Ingrese el radio del circulo: "))
print("Area del circulo:", obj.circulo(radio))

# Trapecio
base_mayor = int(input("Ingrese la base mayor del trapecio: "))
base_menor = int(input("Ingrese la base menor del trapecio: "))
altura = int(input("Ingrese la altura del trapecio: "))
print("Area del trapecio:", obj.trapecio(base_mayor, base_menor, altura))

