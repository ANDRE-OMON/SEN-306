from stack import Stack
from queue import Queue
from linkedlist import SinglyLinkedList


student_records = SinglyLinkedList()

student_records.add_student("Andre")
student_records.add_student("Tolu")
student_records.add_student("Aisha")

print("Registered Students:")
print(student_records.display_students())


support_queue = Queue()

support_queue.enqueue("Andre Complaint")
support_queue.enqueue("Tolu Complaint")
support_queue.enqueue("Aisha Complaint")

print("\nSupport Requests:")
print(support_queue.display())


undo_stack = Stack()

processed_request = support_queue.dequeue()

undo_stack.push(processed_request)

print("\nProcessed Request:")
print(processed_request)

print("\nRemaining Queue:")
print(support_queue.display())


restored_request = undo_stack.pop()

support_queue.enqueue(restored_request)

print("\nUndo Operation Completed")

print("\nUpdated Queue:")
print(support_queue.display())