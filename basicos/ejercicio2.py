person= {
    "name": "Alba",
    "age": 18,
    "height": 1.59,
    "colors": ["azul", "verde"],
    "animales": [],
    "location": (1,2)
}
print(person)
print()

for i in range(3):
    valor_color= input("Añada un color: ")
    person["colors"].append(valor_color)
print(person)
print()

person["colors"][0]="negro"
print(person)
print()

for i in range(3):
    mascotas={
        input("Introduzca el nombre de una mascota: "):input("Introduzca el tipo de mascota: ")
    }
    person["animales"].append(mascotas)
print(person)

for elemento in person["animales"]:
    for clave, valor in elemento.items():
        print(f"{clave} es un {valor}")