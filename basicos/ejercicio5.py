"""
Crea un programa en Python que permita gestionar una lista de tareas pendientes utilizando
funciones y manejo de excepciones. El programa debe almacenar las tareas en una lista llamada
tasks, donde cada elemento será una cadena de texto. Se deben crear funciones para añadir,
eliminar y mostrar tareas. La función add_task(task: str, task_list: list[str]) debe añadir una
tarea a la lista, pero antes debe comprobar que el texto no esté vacío y que no sea numérico; en
caso de incumplir estas condiciones, deberá lanzar una excepción ValueError con un mensaje adecuado.
La función remove_task(task: str, task_list: list[str]) debe eliminar la tarea indicada si existe,
y lanzar un ValueError si el elemento no se encuentra en la lista. La función show_tasks(task_list: list[str])
debe mostrar todas las tareas numeradas, y si la lista está vacía, debe lanzar un ValueError indicando
que no hay tareas registradas.

En el programa principal debe implementarse un menú en bucle que permita al usuario elegir entre cuatro opciones:
    - 1. Añadir una nueva tarea,
    - 2. Eliminar una tarea existente.
    - 3. Mostrar la lista completa de tareas.
    - 4. Salir del programa.

Cada opción debe ejecutarse dentro de un bloque try/except (Si se requiere) para capturar y mostrar
los mensajes de error sin que el programa se detenga. Los mensajes deben ser claros, mostrando
confirmaciones cuando una acción se realice correctamente y avisos cuando ocurra algún error
(por ejemplo, si el usuario intenta eliminar una tarea inexistente o introduce un valor no válido).
El programa debe continuar ejecutándose hasta que el usuario elija la opción de salir.
"""

lista=[]
def menu():
    opcion=""
    while type(opcion)==str or opcion <1 or opcion>4:
        try:
            opcion=input("Introduzca una de las cuatro opciones: \n1. Añadir una nueva tarea \n2. Eliminar una tarea existente \n3. Mostrar la lista completa de tareas \n4. Salir del programa\n")
            if opcion.isnumeric():
                opcion=int(opcion)
                if opcion <1 or opcion>4:
                    raise ValueError("La opción tiene que ser entre 1 y 4")
            else:
                raise TypeError("La opción tiene que ser numérica ")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
    return opcion

def aniadir(lista):
    addible="1"
    while addible.isnumeric() or addible =="":
        try:
            addible=input("Introduzca la tarea que quiera añadir: ")
            if addible.isnumeric():
                raise ValueError("La tarea no puede ser un número")
            elif addible=="":
                raise ValueError("Pon algo cabrón")
        except ValueError as e:
            print(e)
    lista.append(addible)

def remove(lista):
    try:
        existe=0
        quitar=input("Introduzca la tarea que quieres eliminar: ")
        for i in range(len(lista)-1):
            if quitar==lista[i]:
                lista.pop(i)
                existe=1
        if existe==0:
            raise ValueError("La tarea no existe")
    except ValueError as e:
        print(e)

def mostrar(lista):
    try:
        if len(lista)==0:
            raise ValueError("La lista está vacía")
        else:
            for i in range(len(lista) - 1):
                print(f"{i+1}. {lista[i]}")
    except ValueError as e:
        print(e)



continuar=True

while continuar:
    opcion=menu()
    if opcion==1:
        aniadir(lista)
    elif opcion==2:
        remove(lista)
    elif opcion==3:
        mostrar(lista)
    else:
        continuar=False



