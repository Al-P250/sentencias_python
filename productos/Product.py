# Ejercicio de Productos

"""Vamos a crear una tienda online. Vamos a crear una clase llamada Product, que representará un producto en una tienda.

Cada producto tendrá la siguiente estructura:
- name
- price
- stock (Número aleatorio entre 0 y 1) -> Se genera automáticamente usando random
- code (Identificador único) -> Se genera automáticamente con secrets

El programa debe de almacenar varios productos en una lista (Como si un usuario estuviera creando un carrito).

Crea una property que se llame isActive que será True si el stock es mayor a 0 y False en caso contrario.

Comprobaciones (Comprobaciones con control de errores de tipo ValueError):
1. Comprobar si el nombre no está vacío. También si este nombre tiene más de 3 caracteres.
2. El precio debe de ser mayor a 0.

[Punto 1 de comprobaciones] Crea un método estático llamado is_valid_text(value) que usaremos para la comprobación de errores del nombre.

Cuando imprima mi objeto quiero que se vea de esta forma:
[code] Nombre producto -> Precio € (stock: [value])

Quiero mi menú para añadir productos y también para verlos. """
import random
import secrets


class Product:
    def __init__(self, name,price):
        self.__is_valid_text(name)
        self.__is_valid_price(price)
        self.__name=name
        self.__price=price
        self.__stock=random.randint(0,1)
        self.__code=secrets.token_hex(16)

    @property
    def isActive(self):
        return self.__stock>0


    @staticmethod
    def __is_valid_text(name):
        if name =="":
            raise ValueError("El nombre no puede estar vacío")
        if len(name)<3:
            raise ValueError("El nombre tiene que tener más de 3 caracteres")
        if name.isnumeric():
            raise ValueError("El nombre no puede ser un número")

    @staticmethod
    def __is_valid_price(price):
        if price<0:
            raise ValueError("El precio no puede ser menor que 0")


    def __str__(self):
        return f"[{self.__code}] {self.__name} -> {self.__price}€ (stock: {self.__stock})"

