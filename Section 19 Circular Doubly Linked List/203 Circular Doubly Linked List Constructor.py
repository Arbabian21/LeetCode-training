class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class CDLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None