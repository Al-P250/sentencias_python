from taskManager import remove_task, add_task,show_task, ask_number


val=True
task_list=[]
while val:
    print("Introduce una opción: ")
    print("1. Añadir tarea: ")
    print("2. Eliminar tarea: ")
    print("3. Mostrar lista: ")
    print("4. Salir: ")
    opcion=int(input(">> "))

    if opcion==1:
        try:
            task= ask_number(task_list,opcion)
            add_task(task,task_list)
        except ValueError as e:
            print(e)
    elif opcion==2:
        try:
            task= ask_number(task_list,opcion)
            remove_task(task,task_list)
        except ValueError as e:
            print(e)
    elif opcion==3:
        show_task(task_list)
    elif opcion==4:
        val=False
