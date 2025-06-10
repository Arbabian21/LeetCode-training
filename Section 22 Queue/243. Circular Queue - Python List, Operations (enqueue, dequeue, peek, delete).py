class Queue:
    def __init__(self, maxSize): # time complex O(1) space complex O(n)
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        if self.isEmpty():
            return "None"
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self): # time complex O(1)
        if self.top + 1 == self.start:
            return True
        if self.start == 0 and self.top +1 == self.maxSize:
            return True
        return False
    
    def isEmpty(self): # time complex O(1)
        if self.start == -1:
            return True
        return False
    
    def enqueue(self, value): # time complex O(1)
        if self.isFull():
            return "The Queue is full"
        
        if self.top +1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "The element is inserted at the end of the queue"
    
    def dequeue(self): # time complex O(1)
        if self.isEmpty():
            return "The Queue is empty"
        
        firstElement = self.items[self.start]
        start = self.start
        
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start +1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return firstElement
        
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "There is not any element in the Queue"
        return self.items[self.start]
    
    def delete(self): # time complex O(1)
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
        
customQueue = Queue(3)
print(customQueue)

print("\n")
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.isFull())

print("\n")
print(customQueue.dequeue())
print(customQueue)

print("\n")
print(customQueue.peek())

print("\n")
customQueue.delete()
print(customQueue)