

class operabasic:
    n1 = 0
    n2 = 0
    res = 0
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def division(self, a, b):
        return a / b  
    
    def multiplicacion(self, a, b):
        return a * b
    
obj = operabasic()
a = int(input("n1: "))
b = int(input("n2: ")) 
print("La suma es:",obj.suma(a, b))
print("La resta es:",obj.resta(a, b))
print("La division es:",obj.division(a, b))
print("La multiplicacion es:",obj.multiplicacion(a, b))

