
class persona:
    
    def inicilizar(self, nom):
        self.nombre = nom
        
    def imprimir(self):
        print("Nombre",self.nombre)
            
 #Bloque principal
 
persona1 = persona() #creando un objeto
persona1.inicilizar("Pedro")
persona1.imprimir()  

persona2 = persona()                   
persona2.inicilizar("Carla")
persona2.imprimir()

class operabasic():
    n1 = 0
    n2 = 0
    res = 0
    def sumar(self, a, b):
        return a + b
    
    def pedirnumeros(self):
        self.n1 = int(input("n1: "))
        self.n2 = int(input("n2: "))
        print("La suma es:",self.sumar(self.n1, self.n2))
        
obj = operabasic()

obj.pedirnumeros()