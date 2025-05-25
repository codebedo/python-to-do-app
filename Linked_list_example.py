class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #  sonraki node'a işaretçi

class LinkedList:
    def __init__(self):
        self.head = None # Listenin başlangıcı

    def append(self, data):
        new_node = Node(data) # eğer liste boşsa
        if not self.head:
            self.head = new_node
            return

        # değilse sona kadar git
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end= " -> ")
            current = current.next

        print("None")



# kulllanım şekli

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(50)


ll.print_list()