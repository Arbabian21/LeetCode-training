class Stack:
    def __init__(self): # time complex O(1)
        self.list = []
    
    def __str__(self): # time complex O(n)
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.list == []:
            return True
        return False
    
    def push(self, value): # time complex O(n)
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self): # time complex O(1)
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            self.list.pop()
            
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "There is not any element in the stack"
        return self.list[len(self.list) -1]
    
    def delete(self): # time complex O(1)
        self.list = None
    
customStack = Stack()
print(customStack.isEmpty())