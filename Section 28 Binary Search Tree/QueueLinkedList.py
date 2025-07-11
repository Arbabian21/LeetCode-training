class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
            
class Queue:
    def __init__(self): # time complex O(1)
        self.linkedList = LinkedList()
    
    def __str__(self): # tikme complex O(n)
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.linkedList.head == None:
            return True
        return False
    
    def enqueue(self, value): # time complex O(1)
        newNode = Node(value)
        
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
            return
        
        self.linkedList.tail.next = newNode
        self.linkedList.tail = newNode

    def dequeue(self): # time complex O(1)
        if self.isEmpty():
            return "Queue is empty"
        
        rmNode = self.linkedList.head
        self.linkedList.head = rmNode.next
        if rmNode == self.linkedList.tail:
            self.linkedList.tail = None
        rmNode.next = None
        return rmNode
    
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "The Queue is empty"
        return self.linkedList.head
    
    def delete(self): # time complex O(1)
        self.linkedList.head = None
        self.linkedList.tail = None