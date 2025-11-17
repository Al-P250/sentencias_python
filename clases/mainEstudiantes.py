import random

class Student:
    def __init__(self,nombre):
        try:
            if not nombre:
                raise ValueError("No hay nombre")
            elif nombre.isnumeric():
                raise ValueError("No se puede llamar por un número")
            else:
                self.__name=nombre
                self.__grades=[]
                self.add_grade()
                self.__id=self.generar_id()
        except ValueError as e:
            print(e)

    @staticmethod
    def generar_id():
        return random.randint(100000,999999)

    def add_grade(self):
        grade=0
        while grade>=0:
            grade= float(input("Introduzca una nota (-1 para salir): "))
            if grade>=0:
                self.__grades.append(grade)

    @property
    def media(self):
        if len(self.__grades)==0:
            return 0
        return sum(self.__grades)/len(self.__grades)

    def __str__(self):
        return f"[ID: {self.__id}] {self.__name} -> Grades: {self.__grades} Media: {self.media}"



estudiantes=[]

salir=False
while not salir:
    nombre=input("s -> Salir | Introduce un nombre ")
    if nombre!="s":
        estudiante=Student(nombre)
        estudiantes.append(estudiante)
    else:
        salir=True
    print("................")

for estudiante in estudiantes:
    print(estudiante)