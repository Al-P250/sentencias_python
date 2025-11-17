from functools import reduce
from traceback import print_tb


def sumar(a,b):
    return a+b

suma_anonima=lambda a,b: a+b

suma_total=sumar(1,2)
print(suma_total)

5+suma_anonima(4,5)
print(5+suma_anonima(4,5))

textos=lambda txt1, txt2: txt1 + txt2
print(textos("hola", "mundo"))

otra_suma=lambda a,b: a if a>5 else a+b
print(otra_suma(1,2))
print(otra_suma(10,2))

print("\n###########################")
print("###########################")
print("###########################\n")

array=[("Juan", 0), ("Camilo", 5), ("Pepe", 2)]
arr_1_ordenado=sorted(array, key=lambda n:n[1])
arr_1_ordenado_nombre=sorted(array, key=lambda n:n[0], reverse=True)
print(arr_1_ordenado)
print(arr_1_ordenado_nombre)

print("\n###########################")
print("###########################")
print("###########################\n")

empleados=[
    {"nombre": "Admin", "nota": 5,"salario": 50000},
    {"nombre": "John", "nota": 3,"salario": 60000},
    {"nombre": "Pepe", "nota": 0,"salario": 10000}
]
ord_salario=sorted(empleados, key=lambda emp:emp["salario"])
ord_nota=sorted(empleados, key=lambda emp:emp["nota"])
print(ord_salario)
print(ord_nota)


reviews = [
    {"nombre": "Película 1", "valoración": 3.4},
    {"nombre": "Película 2", "valoración": 4.2},
    {"nombre": "Película 3", "valoración": 4.4},
    {"nombre": "Película 4", "valoración": 3.7},
]

def ordenar(resenias):
    valoraciones=[]
    for i in range(len(resenias)):
        aux=0
        for diccionario in resenias:
            if diccionario["valoración"]>aux and diccionario not in valoraciones:
                aux=diccionario["valoración"]
                aniadir=diccionario
        valoraciones.append(aniadir)
    print(valoraciones)

ordenar(reviews)

suma_dos_primeras=lambda a,b: a+b

print(suma_dos_primeras(reviews[0]["valoración"], reviews[1]["valoración"]))
print(sorted(reviews,key=lambda rev:rev["valoración"], reverse=True))

print("\n###########################")
print("########## MAP ############")
print("###########################\n")

empleados=[
    {"nombre": "Admin", "nota": 5,"salario": 50000, "departamento": "IT"},
    {"nombre": "John", "nota": 3,"salario": 60000, "departamento": "RRHH"},
    {"nombre": "Pepe", "nota": 0,"salario": 10000, "departamento": "IT"}
]
empleados_salario_x2=list(map(lambda emp: emp["salario"]*2, empleados))
print(empleados_salario_x2)

print("\n###########################")
print("######### FILTER ##########")
print("###########################\n")

empleados_salario_50000=list(filter(lambda emp: emp["salario"]>=50000, empleados))
print(empleados_salario_50000)

solo_IT=list(filter(lambda emp:emp["departamento"]=="IT", empleados))
print(solo_IT)

print("\n###########################")
print("######### REDUCE ##########")
print("###########################\n")

def suma_todo_salarios():
    cont=0
    for emp in empleados:
        cont+=emp["salario"]
    return cont

suma_salarios=reduce(lambda cont, emp: cont +emp["salario"], empleados, 0)
suma_salarios=reduce(lambda cont, emp: cont +emp["salario"] if emp["departamento"]=="IT" else cont, empleados, 0)
print(suma_salarios)

"""
Ejercicios

- Análisis de películas:
    Tienes una lista de películas con su nombre, valoración y duración.
        - Ordena las películas de mayor a menor en valoración. Luego ordénalas también alfabéticamente.
        - Obtener solo las películas que duren más de 120 minutos.
        - Crea una lista solo con los nombres de las películas.
"""
peliculas = [
    {"nombre": "El padrino", "valoracion": 9.2, "duracion": 175},
    {"nombre": "Toy Story", "valoracion": 8.9, "duracion": 154},
    {"nombre": "El señor de los anillos", "valoracion": 8.3, "duracion": 81},
    {"nombre": "Forrest Gump", "valoracion": 8.8, "duracion": 142},
]

print(sorted(peliculas,key=lambda peli:peli["valoracion"], reverse=True))
print(sorted(peliculas,key=lambda peli:peli["nombre"]))

print(list(filter(lambda peli:peli["duracion"]>120,peliculas)))



"""
- Procesamiento de ventas
    Dada una lista de ventas, calcula el total de ventas y también obten las ventas mayores a 1000.
"""
ventas = [1500, 800, 2200, 600, 3500, 950, 1200, 450]

print(reduce(lambda cont, venta:cont+venta,ventas,0))

print(list(filter(lambda venta: venta>1000,ventas)))

"""
- Procesamiento de texto
    Dada una lista de frases:
        - Convertir todas las frases a mayúsculas
        - Obtener solo las frases con más de 3 palabras
        - ¿Cuántas palabras tienen todas mis frases en total?
"""
frases = [
    "Python es genial",
    "Me gusta programar",
    "Hola mundo",
    "La programación funcional es interesante",
    "Hola"
]

