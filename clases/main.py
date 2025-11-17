import random


class Persona:

    def __init__(self, nombre):
        self.__id=self.__generate_id()
        self.__nombre=nombre

    @staticmethod
    def __generate_id():
        return random.randint(100000, 999999)

    @property
    def nombre_completo(self):
        return self.__nombre

    def get_nombre(self):
        return self.__nombre
    def get_id(self):
        return self.__id

    def __str__(self):
        return f"{self.__nombre} y el id es {self.__id}"

persona=Persona("Yo")

print(persona.get_nombre())
print(persona.get_id())


print("\n\n\n")

class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.__nombre=nombre
        self.__cantidad=cantidad
        self.__precio=precio

    def get_total(self):
        return self.__cantidad*self.__precio

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre=nombre

    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad=cantidad

    def get_precio(self):
        return self.__precio
    def set_precio(self,precio):
        self.__precio=precio

    def descuento(self, descuento):
        self.__precio-=descuento

    def __str__(self):
        return f"[Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: {self.__precio}]"


presupuesto=2200
cont=0
productos=[]
p1=Producto("TV",3,350)
p2=Producto("PC", 1, 1500)

productos.append(p1)
productos.append(p2)

for producto in productos:
    if presupuesto - producto.get_total()>=0:
        presupuesto-=producto.get_total()
        print("Hemos comprado", producto)
    else:
        print("No se puede comprar este producto", producto)

print(p1)
p1.descuento(100)
print(p1)