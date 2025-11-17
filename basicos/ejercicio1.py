nombre: str="Alba"
userEdad: int = 18
otraEdad: int= int(input("Introduzca tu edad: "))
altura: float= 1.59
colores=["Azul", "Verde"]

if otraEdad>userEdad:
    print(f"Eres mayor que {nombre}")
elif otraEdad==userEdad:
    print(f"Tienes la misma edad que {nombre}")
else:
    print(f"Eres más joven que {nombre}")
