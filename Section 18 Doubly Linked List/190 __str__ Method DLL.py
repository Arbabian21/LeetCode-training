class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return f'{self.value}'
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        result = ''
        curr = self.head
        
        while curr:
            result += f'{curr.value}'
            if curr.next:
                result += ' <-> '
            curr = curr.next
        return result
    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.length += 1
        
        
newNode = Node(11)
print(newNode)

dll = DoublyLinkedList()
dll.append(10)
print(dll.tail)