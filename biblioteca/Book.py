## Biblioteca
"""Creemos un programa que gestione una pequeña colección de libros en una biblioteca usando una clase llamada Book (Intentemos crear códigos en archivos diferentes).

- Cada libro debe de tener los siguientes atributos privados:
  - __title: Título del libro (No puede estar vacío ni numérico además, el tamaño del título debe de ser de más de 5 caracteres).
  - __author: Nombre del autor que escribió el libro (No puede estar vacío ni numérico).
  - __price: Precio en euros (solo números positivos).
  - __isbn: Código de identificación único (Igual que el ID que creamos en el anterior, pero la cantidad de caracteres aquí serán de 25).

- El programa debe de validar con ValueError los errores mencionados anteriormente.
- Implementa una propiedad de descuento. Será True si vale más de 25.00/False si no lo hace. Además, antes de retornar, descontará al precio original 10€ en caso de ser True.
- Implementa el método __str__ para mostrar:
  - [ISBN: numero] "Nombre del libro" de "Nombre de autor" -> Precio€"""
import secrets


class Book:
    def __init__(self, title, author, price):
        self.__comprobar_title(title)
        self.__comprobar_author(author)
        self.__comprobar_price(price)
        self.__title=title
        self.__author=author
        self.__price=price
        self.__isbn=self.__create_isbn()

    @property
    def descuento(self):
        if self.__price>25:
            self.__price-=10
        return self.__price


    @staticmethod
    def __comprobar_title(title):
        if len(title)<5:
            raise ValueError("El título debe de tener una longitud a 5 caracteres")
        if title=="":
            raise ValueError("El título no puede estar vacío")
        if title.isnumeric():
            raise ValueError("El título no puede ser un número")
    @staticmethod
    def __comprobar_author(author):
        if author=="":
            raise ValueError("El autor no puede estar vacío")
        if author.isnumeric():
            raise ValueError("El autor no puede ser un número")

    @staticmethod
    def __comprobar_price(price):
        if price<0:
            raise ValueError("El precio debe ser mayor que 0")

    @staticmethod
    def __create_isbn():
        return secrets.token_hex(16)

    def __str__(self):
        return f"[ISBN: {self.__isbn}] '{self.__title}' de '{self.__author}' -> '{self.descuento}€"