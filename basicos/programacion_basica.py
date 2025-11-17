#Comentario
x: str = "hola"
n: int =12
n_m: float=12.2
val: bool=True
val_not: bool=False

arr_1=[1,2,3]
tpl=(1,2,3)
dict_1={}
dict_2=dict
dict_3={
    "a":"Valor 1",
    "b": "Valor 2",
    "c": [1,2,3],
    "d": True,
    "e": False,
    "f":{
        "g": "Valor 3",
        "h": "Valor 4"
    }
}
dict_4='{"a":"Valor 1", "b": "Valor 2", "c": [1,2,3], "d": True, "e": False, "f":{ "g": "Valor 3", "h": "Valor 4"}}' #JSON


print(arr_1[1])
print()

print(tpl[0])
print()

print(dict_3["d"])
print()

if n>6:
    if 2 in arr_1:
        print("Sí está 2")
    else:
        print("No está 2")
else:
    print("No es 12")

if n ==6:
    print("es 6")
elif n==12:
    print("Es 12")
else:
    print("No es ninguno de los anteriores [6, 12]")

valor_consola =input("Introduce el valor de la consola: ")
print(valor_consola)

edad_1=int(input("Introduce la edad: "))
print(edad_1)








"""
def main():
    print("Hello World")
if __name__=='__main__':
    main()
    
"""