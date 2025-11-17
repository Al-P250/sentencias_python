arr_1: list =[10,20,30]
frutas: list[str]=["manzana", "pera", "uva"]

for item in arr_1:
    print(item)
print()

for fruta in frutas:
    print(fruta)

frutas.append("mango") #Añade un elemento al final de la lista
print()
for fruta in frutas:
    print(fruta)
print()

frutas.pop(0) #Elimina el último elemento de la lista. Si le ponemos un índex/posición, borramos el elemento de esa posición.
for fruta in frutas:
    print(fruta)

frutas.insert(0,"banana")  # Inserta un elemento en la posición indicada
frutas.insert(2,"sandía")
print()
for fruta in frutas:
    print(fruta)
print()

print(frutas[1])

frutas.remove("uva") #Borra un elemento con un valor específico. Si el valor no existe, da un error de tipo ValueError
print()
for fruta in frutas:
    print(fruta)
print()

frutas.sort() #Ordena el arrayList de forma alfabética
print()
for fruta in frutas:
    print(fruta)
print()

frutas.append("banana")
print(frutas.count("banana")) #Cuenta cuantos elementos con ese valor hay en el array

print(f"Hay {frutas.count("banana")} banana dentro de frutas")