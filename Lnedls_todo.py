class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        if  not self.head:
            self.head = new_node
            print(f"Added task: {task}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added Task: {task}")

    def view_tasks(self):
        if not self.head:
            print("No tasks found")
            return
        current =self.head
        index = 0
        print("\n --- Task List ---")
        while current:
            print(f"{index}. {current.task}")
            current = current.next
            index += 1
    def delete_task(self, index):
        if not self.head:
            print("No tasks to delete")
            return

        if index == 0:
            print(f"Deleted task: {self.head.task}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if not current:
            print("Invalid ındex")
            return

        print(f"Deleted task: {current.task}")
        prev.next = current.next

def menu():
    print("\n --- Task Manager --- ")
    print("1. Add Task")
    print("2.View Tasks")
    print("3. Delete Task")
    print("4. Exit")

task_list = TaskList()


while True:
    menu()
    choice = input("Enter your choice")

    if choice == "1":
        task = input("Enter your task: ")
        task_list.add_task(task)
    elif choice == "2":
        task_list.view_tasks()
    elif choice == "3":
        task_list.view_tasks()
        index = int(input("Enter index to delete: "))
        task_list.delete_task(index)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid Choice. Try Again.")