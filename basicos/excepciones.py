try:
    #Intenta hacer algo, pero si te encuentras con un error paras completamente y pasas al except
    pass
except:
    #Si hay un error en el try, accedemos aquí
    pass

def error_division(numero, div):
    try:
        print(numero/div)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")


def imprime_valor_numerico(num):
    try:print("El número es: ", int(num))
    except ValueError:
        print("El valor debe de ser numérico")
    finally:
        print("Este es el mensaje de finally")

def set_rating(value):
    try:
        if not (0<=value<=10):
            raise TypeError("Rating debe de estar entre 0 y 10")
        print(value)
    except TypeError:
        print("El valor solo puede ser un número")


try:
    set_rating(11)
except ValueError as e:
    print(e)
error_division(1,0)
error_division(1,2)
imprime_valor_numerico("hola")

"""
Construir un programa que gestione personajes de
Marvel usando funciones y manejo de excepciones.

- Crea un diccionario vacio llamado marvel.
- Implementa las siguientes funciones con manejo
    de excepciones con raise cuando corresponda.

    - si alguien introduce como nombre
    un número arrojamos una excepción (raise)
    porque tiene que ser string.
    - Si el personaje existe arrojamos una excepción de
    KeyError.

- Implementa otra función para buscar un personaje.
    - Si existe, imprime el personaje.
    - Si no existe, arrojamos una excepción de KeyError.

- Implementar otra función para obtener (con return), el
    personaje con rating más alto.

- Hacer un panel de control tipo:
    - 1. Introducir usuario
    - 2. Comprobar si existe
    - 3. Ver personaje con mayor puntuación
    - 4. Salir
"""