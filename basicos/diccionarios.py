persona={
    "nombre" : "Alba",
    "apellido" : "Pinelas",
    "esEstudiante":True,
    "frutas":["manzana", "pera"],
    "estaDeVacaciones" : True,
    "animales": [{"animal1": "perro"}, {"animal2": "gato"}]
}

print(persona)
print(persona["nombre"]) #Acceder a un valor haciendo uso de su clave
print()

if persona["esEstudiante"]:
    print("Es estudiante")
else:
    print("Es profesor")

print()
for fruta in persona["frutas"]:
    print(fruta)

print()
#print(persona.get("estaDeVacaciones", "No está definido"))
estaDeVacaciones =persona.get("estaDeVacaciones", False) #Obetener un dato de un diccionario
print(estaDeVacaciones)

print()

persona.pop("estaDeVacaciones") #Borra Clave-Valor del diccionario pero deja basura en la memoria
print(persona)

print()
del persona["frutas"] #Borra Clave-Valor pero también de la memoria
print(persona)

print()
'''persona.clear() #Limpia el diccionario. Borra todo de la memoria
print(persona)'''
persona["esEstudiante"]=False #Sobreescribe el valor de una clave
for clave, valor in persona.items(): #Acceder a la Clave-Valor de cada elemento por iteración
    print(f"La clave es {clave} y su valor es {valor}")

print()
for value in persona.values(): # Accede solo a los valores
    print(value)

print()
for clave in persona.keys(): # Accede solo a las claves
    print(clave)

print()

for elemento in persona["animales"]:
    for clave, valor in elemento.items():
        print(f"El {clave} es {valor}")
print()

clave_consola =input("Introduce la clave: ")
valor_consola =bool(input("Introduce el valor: "))
persona[clave_consola]=valor_consola
print()
print(persona)



