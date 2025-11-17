def ask_number(task_list, opt):
    task=input("Introduce una tarea: ")
    if opt==1:
        if task in task_list:
            raise ValueError("La tarea ya existe")
    elif opt==2:
        if task not in task_list:
            raise ValueError("La tarea no existe")
    if not task:
        raise ValueError("No se ha introducido nada")
    return task