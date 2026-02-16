




alumno ={
    "nombre": "Ana",
    "edad": 21,
    "carrera": "Ingenieria"
}
print(type(alumno))
print(alumno)

print("print(alumno['nombre']) = ",alumno['nombre'])
print("print(alumno.get('edad')) = ",alumno.get('edad'))

#agregar o modificar valores
alumno["promedio"] = 8
print(alumno)
alumno["edad"] = 22
print(alumno)

#eliminar un par clave-valor
del alumno["carrera"]
print(alumno)



#funciones utiles para diccionarios
print("cantidad de pares clave-valor: ",len(alumno))
print("claves del diccionario: ",alumno.keys())
print("valores del diccionario: ",alumno.values())
print("pares clave-valor del diccionario: ",alumno.items())
