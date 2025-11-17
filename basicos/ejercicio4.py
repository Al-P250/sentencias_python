"""
Construir un programa en Python que gestione un pequeño registro de personajes y equipos de Marvel.
    -   Crea un diccionario llamado marvel donde cada clave sea un nombre de un personaje y su valor sea otro
        diccionario.
    - El valor debe de tener los siguientes elementos:
        - alias -> nombre de superheroe.
        - team -> será un array unidimensional. Valores añadidos por consola. "Avengers", "X-men", ...
        - powers -> lista de poderes (array de strings)
        - isAvailable -> Si está disponible o no (True o False)
        - rating -> valoración del personaje 0.0 al 10.0 (float)

    Incluir al menos 3 personajes. Todos los datos se introducen de forma manual.

    - Mostrar todos los personajes introducidos.
    - Mostrar todos los nombres de los personajes que estén disponibles.
    - Buscar un personaje, comprobar si existe o no. Si existe, decir los poderes de ese personaje.
    - Decir que personaje es el que tiene más rating de todos los introducidos
        (Este ejercicio es complejo, No es obligatorio).
"""
def buscar(marvel):
    nom = input("Introduzca un nombre para buscar: ")
    existe = 0
    for clave in marvel.keys():
        if nom == clave:
            existe = 1
    if existe == 1:
        print(f"{marvel[nom]}")
    else:
        raise KeyError("El personaje no existe")

def masRating(marvel):
    maxm = 0
    for clave, valor in marvel.items():
        if valor["Valoración"] > maxm:
            maxm = valor["Valoración"]
            mejor = clave
    return mejor

marvel= {}

num=int(input("¿Cuántos personajes quieres añadir?(mínimo 3): "))
"""while num<3:
    num=int(input("Mínimo 3, imbécil: "))"""

for i in range(num):
    try:
        nombre=input("Introduzca el nombre: ")
        if nombre.isnumeric():
            raise TypeError("El nombre tiene que ser String")
    except TypeError as e:
        print(e)
    if nombre in marvel:
        raise KeyError("El personaje ya existe")
    alias=input("Introduzca el nombre de superhéroe: ")
    equipos=int(input("¿A cúantos equipos pertenece? "))
    team=[]
    for j in range(equipos):
        team.append(input("Ingrese equipo: "))

    po=int(input("¿Cúantos poderes tiene? "))
    poderes=[]
    for j in range(po):
        poderes.append(input("Ingrese poder: "))

    disp=input("¿Está disponible? (s/n): ")
    if disp.upper()=="S":
        available=True
    else:
        available=False

    rating=float(input("Valoración del personaje (0.0-10.0): "))

    marvel[nombre]={"Alias": alias, "Equipos" : team, "Poderes" : poderes, "Está disponible" : available, "Valoración":rating}

for clave, valor in marvel.items():
    print(f"El personaje {clave} de alias {valor["Alias"]}, perteneciente a los equipos {valor["Equipos"]}, con los poderes {valor["Poderes"]}, está {valor["Está disponible"]} y cuenta con una calificación de {valor["Valoración"]} \n")

print("Los personajes disponibes son: ")
for clave, valor in marvel.items():
    if valor["Está disponible"]:
        print(clave)

buscar(marvel)

print(f"El personaje mejor valorado es {masRating(marvel)}")
