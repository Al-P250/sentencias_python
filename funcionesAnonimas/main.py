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

