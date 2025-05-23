class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
newLinkedList = LinkedList(10)
print(newLinkedList.head.value)
# this is a linked list with a single node that is both the head and tail

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0    
# class for a linked list that is empty be default