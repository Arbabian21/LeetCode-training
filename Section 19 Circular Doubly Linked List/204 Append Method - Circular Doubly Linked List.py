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
        
    def append(self,value): # time complex O(1)
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        
        elif self.head == self.tail:
            self.head.next = newNode
            newNode.next = self.head
            newNode.prev = self.head
            self.tail = newNode
            self.head.prev = self.tail

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail = newNode
            self.head.prev = self.tail
            
        self.length += 1
