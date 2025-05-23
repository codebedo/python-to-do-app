import os
file_name= "tasks01.txt"

def menu():
    print("\n -- TODO LISTS --")
    print("1. Add a Task")
    print("2. Listing works.")
    print("3. exit")


def add_task():
    task = input("Please add a task: ").strip()
    if task:
        with open(file_name, "a" , encoding="utf-8") as file:
            file.write(task + "\n")
        print("task succesfully added")
    else:
        print("blank file cannot adding")


def task_list():
    if not os.path.exists(file_name):
        print("you have not anny task yet")
        return


    with open(file_name, "r", encoding="utf-8") as file:
        tasks = [g.strip() for g in file.readline() if g.strip()]


    if not tasks:
        print("you have not any tasks yet")
    else:
        print("\n tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"i.{task}")



while True:
    menu()
    choice = input("Your choice").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        task_list()
    elif choice == "3":
        print("you are exiting the program ")
        break
    else:
        print("invalid selection ")