'''
crear un programa que permita ingresar los datos de varios alumnos 
(nombre, edad, materia,calificacion) y almacenarlos en una lista de diccionarios. 
Luego, mostrara cuantos alumnos fueron ingresados y el promedios de sus calificaciones.
''' 
import os
os.system("cls")

alumnos = []
cantidad = int(input("Ingrese la cantidad de alumnos: "))
for i in range(cantidad):
    alumno = {}
    alumno["nombre"] = input("Ingrese el nombre del alumno: ")
    alumno["edad"] = int(input("Ingrese la edad del alumno: "))
    alumno["materia"] = input("Ingrese la materia del alumno: ")
    alumno["calificacion"] = float(input("Ingrese la calificacion del alumno: "))
    alumnos.append(alumno)
print("Cantidad de alumnos ingresados: ",len(alumnos))
suma_calificaciones = 0
for alumno in alumnos:
    suma_calificaciones += alumno["calificacion"]
promedio = suma_calificaciones / len(alumnos)
print("El promedio de las calificaciones es: ",promedio)
