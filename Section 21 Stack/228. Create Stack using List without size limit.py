class Stack:
    def __init__(self): # time complex O(1)
        self.list = []
    
    def __str__(self): # time complex O(n)
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)