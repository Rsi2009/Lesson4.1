class Task():
    def __init__(self, description, deadline):  # Исправлено имя метода на __init__
        self.description = description
        self.deadline = deadline
        self.status = False  # Невыполнено

tasks_list = []

def add_task(description, deadline):  # Исправлена индентация
    tasks_list.append(Task(description, deadline))

def mark_task_as_done(description):  # Исправлена индентация
    for task in tasks_list:
        if task.description == description:
            task.status = True
            print(f"Задача '{description}' отмечена как выполненная.")
            break
    else:
        print(f"Задача с описанием '{description}' не найдена.")

def show_current_tasks():  # Исправлена индентация
    print("Текущие задачи:")
    for task in tasks_list:
        if not task.status:
            print(f"{task.description} - срок: {task.deadline}")

def remove_task(description):  # Исправлена индентация
    for i, task in enumerate(tasks_list):
        if task.description == description:
            del tasks_list[i]
            print(f"Задача '{description}' была удалена.")
            break
    else:
        print(f"Задача с описанием '{description}' не найдена.")

def show_completed_tasks():  # Исправлена индентация
    print("Выполненные задачи:")
    for task in tasks_list:
        if task.status:
            print(f"{task.description} - срок: {task.deadline}")

add_task("Изучить Python", "01.06.2023")
add_task("Сделать уборку", "05.05.2023")
add_task("Пройти курс по медитации", "20.05.2023")

mark_task_as_done("Изучить Python")

show_current_tasks()

remove_task("Сделать уборку")

show_completed_tasks()




