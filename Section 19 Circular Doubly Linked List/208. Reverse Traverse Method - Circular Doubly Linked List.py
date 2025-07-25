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
