biblioteca={}
num=int(input("¿Cuántos libros quieres añadir?(mínimo 3): "))
while num<3:
    num=int(input("Mínimo 3, imbécil: "))
for i in range(num):
    titulo=input("Introduzca el título: ")
    autor=input("Introduzca el autor: ")
    pregunta=input("¿Está disponible? (s/n): ")
    if pregunta.upper()=="S":
        disp=True
    else:
        disp=False
    biblioteca[titulo] ={"Autor": autor, "Disponible": disp}

existe=0
nombre=input("Introduzca un título para ver si el libro existe: ")
for clave in biblioteca.keys():
    if clave==nombre:
        existe=1

if existe==1:
    if biblioteca[nombre]["Disponible"]:
      print("El libro existe y está disponible")
    else:
        print("El libro existe pero no está disponible")
else:
    print("No existe en la biblioteca")

for clave1,val1 in biblioteca.items():
    print(f"\nEl libro {clave1} escrito por {val1["Autor"]} está {val1["Disponible"]}")

