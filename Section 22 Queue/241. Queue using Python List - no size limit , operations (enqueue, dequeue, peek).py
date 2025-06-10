class Queue:
    def __init__(self): # time complex O(1)
        self.items = []
        
    def __str__(self): # time complex O(n)
        if self.items == None:
            return "Empty"
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value): # time complex O(n)
        self.items.append(value)
        return "The element has been inserted at the end of the Queue"
    
    def dequeue(self): # time complex O(n)
        if self.isEmpty():
            return "The Queue is empty"
        return self.items.pop(0)
    
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "The Queue is empty"
        return self.items[0]
    
    def delete(self): # time complex O(1)
        self.items = None
        
customQueue = Queue()
print(customQueue)
print(customQueue.isEmpty())

print("\n")
customQueue.enqueue(0)
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)

print("\n")
customQueue.dequeue()
print(customQueue)

print("\n")
print(customQueue.peek())
customQueue.delete()
print(customQueue)