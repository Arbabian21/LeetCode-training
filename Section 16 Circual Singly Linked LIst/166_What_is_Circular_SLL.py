class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0