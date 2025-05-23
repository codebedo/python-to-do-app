import json
import os

file_name = "todo.json"

# check and create file if not exists
def check_the_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

# load tasks
def load_task():
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)

# save tasks
def save_tasks(tasks):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# add new task
def adding_task():
    task = input("Please add new task: ")
    tasks = load_task()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added.")

# list tasks
def list_tasks():
    tasks = load_task()
    if not tasks:
        print("You have no tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "|-|" if task["completed"] else "X"
            print(f"{i}. {task['task']} [{status}]")

# complete a task
def complete_task():
    tasks = load_task()
    list_tasks()
    try:
        choice = int(input("Task number to complete: "))
        tasks[choice - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid choice.")

# menu
def menu():
    print("\n-- TODO LIST --")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Exit")

# main loop
check_the_file()
while True:
    menu()
    choice = input("Your choice: ")
    if choice == "1":
        adding_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
