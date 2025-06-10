class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self): # time complex O(n)
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.list == []:
            return True
        return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    
    def push(self, value): # time complex O(n)
        if self.isFull():
            return "Stack is full"
        self.list.append(value)
        return "Element Successfully added"
    
    def pop(self): # time complex O(1)
        if self.isEmpty():
            return "The stack has no elements"
        return self.list.pop()
            
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "Stack has no elements"
        return self.list[len(self.list)]
    
    def delete(self): # time complex O(1)
        self.list = None
