class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
    
class Stack:
    def __init__(self): # time complex O(1)
        self.LinkedList = LinkedList()
    
    def __str__(self): # time complex O(n)
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.LinkedList.head is None:
            return True
        return False
    
    def push(self, value): # time complex O(1)
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode
    
    def pop(self): # time complex O(1)
        if self.isEmpty():
            return "There is not any element in the stack"
        popped = self.LinkedList.head
        self.LinkedList.head = popped.next
        popped.next = None
        return popped
    
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "The Stack is Empty"
        return self.LinkedList.head
    
    def delete(self): # time complex O(1)
        self.LinkedList.head = None
    
customStack = Stack()
emptyStack = Stack()
print(customStack.isEmpty())
print('\n')

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print('\n')
print(customStack.pop())

print('\n')
print(customStack)

print('\n')
print(customStack.peek())
print(emptyStack.peek())