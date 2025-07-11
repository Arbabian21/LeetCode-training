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
    
    def prepend(self,value): #time complex O(1)
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode

        
        else:
            currHead = self.head
            currHead.prev = newNode
            newNode.next = currHead
            self.head = newNode
        
        self.length += 1
        
    def traverse(self): # time complex O(n)
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next
    
    def reverseTraverse(self): # time complex O(n)
        curr = self.tail
        while curr:
            print(curr)
            curr = curr.prev
            
    def search(self, target): #time complex O(logn)
        head = self.head
        headIndex = 0
        tail = self.tail
        tailIndex = self.length -1
        
        while head or tail:
            if head.value == target:
                return headIndex
            elif tail.value == target:
                return tailIndex
            elif head == tail:
                return -1

            if head:
                head = head.next
                headIndex += 1
            if tail:
                tail = tail.prev
                tailIndex -= 1
        return -1
            
newNode = Node(11)
print(newNode)

dll = DoublyLinkedList()
dll.append(10)
print(dll.tail)

dll.reverseTraverse()
print(dll.search(10))