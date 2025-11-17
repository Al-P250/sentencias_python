def add_task(task,task_list):
    task_list.append(task)

def remove_task(task, task_list):
    task_list.remove(task)

def show_task(task_list):
    for task in task_list:
        print(task)