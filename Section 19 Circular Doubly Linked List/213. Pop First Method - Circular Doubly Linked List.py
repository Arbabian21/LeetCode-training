class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.value)
        
class CDLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        
    def __str__(self):
        curr = self.head
        result = ''
        
        while curr:
            result += str(curr.value)
            curr = curr.next
            if curr == self.head:
                break
            result += ' <-> '
        
        return result
    
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
        
    def prepend(self, value): # time complex O(1)
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
            
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = self.tail
            self.head = newNode
            self.tail.next = newNode
            
        self.length += 1

    def traverse(self): # time complex O(n)
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
            if curr == self.head:
                break
            
    def reverseTraverse(self): # time complex O(n)
        curr = self.tail
        while curr:
            print(curr)
            curr = curr.prev
            if curr == self.tail:
                break
    
    def search(self, targetVal): # time complex O(n)
        left = self.head
        right = self.tail
        
        while left or right:
            if left.value == targetVal:
                return True
            elif right.value == targetVal:
                return True
            if left == right:
                break
            left = left.next
            right = right.next
            
            if left == self.head:
                break
            if right == self.tail:
                break
            
        return False
    
    def get(self, index): # time complex O(n)
        curr = None
        if 0 > index or index >= self.length:
            return None
        elif index < self.length//2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length -1, index, -1):
                curr = curr.prev
                
        return curr
    
    def set(self, index, value): # time complex O(n)
        curr = self.get(index)
        if curr:
            curr.value = value
            return True
        return False
    
    def insert(self, index, value): # time complex O(n)
        if 0 > index or index > self.length:
            return Exception("index out of bounds")
        newNode = Node(value)
        
        if index == 0:
            self.prepend(value)
            return
        
        if index == self.length:
            self.append(value)
            return
        

        prev = self.get(index-1)
        prev.next.prev = newNode
        newNode.next = prev.next
        newNode.prev = prev
        prev.next = newNode
        self.length += 1
            
    def popFirst (self): # time complex O(1)
        popped = self.head
        
        if not popped:
            return None
        
        if self.length == 1:
            popped.next = None
            popped.prev = None
            self.head = None
            self.tail = None
            self.length -= 1
            return popped
        
        self.head = popped.next
        self.tail.next = popped.next
        popped.next.prev = self.tail
        popped.next = None
        popped.prev = None
        self.length -= 1
        return popped
    
cdll = CDLinkedList()
emptycdll = CDLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)

print(cdll)

cdll.prepend(0)
print(cdll)

# emptycdll.prepend(0)
# print(emptycdll)

print(cdll.search(-1))

print(cdll.get(1))

