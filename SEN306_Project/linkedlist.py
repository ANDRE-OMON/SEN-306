class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display_students(self):
        students = []

        current = self.head

        while current:
            students.append(current.data)
            current = current.next

        return students
    