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
    
    def get(self, index): # time complex O(n)
        if 0 > index > self.length or not self.head:
            return None
        
        midpoint = self.length // 2
        if index < midpoint:
            curr = self.head
            
            for _ in range(index):
                curr = curr.next
            
            return curr.value
        
        else:
            curr = self.length -1
            
            for _ in range(self.length -1, index, -1):
                curr = curr.prev
            
            return curr.value
        
    def set(self, index, value): # time complex O(n)
        node = self.get(index)

        if not node:
            return False
        
        node.value = value
        return True
    
    def insert(self, index, value): # time complex O(n)
        newNode = Node(value)
        if 0 > index or index > self.length:
            print("index out of bounds")
            return
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length -1:
            self.append(value)
            return
        else:    
            tempNode = self.get(index-1)
            newNode.next = tempNode.next
            tempNode.next = newNode
            newNode.prev = tempNode
            newNode.next.prev = newNode
            self.length += 1
 
    def popFirst(self): # time complex O(1)
        if self.head == None:
            return None
        
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped.value
        
        self.head = popped.next
        popped.next = None
        self.length -= 1
        return popped.value
        
    def pop(self): # time complex O(1)
        poppedNode = self.tail
        
        if poppedNode == None:
            return None
        
        if self.tail == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
            return poppedNode
            
        newTail = poppedNode.prev
        self.tail = newTail
        newTail.next = None
        poppedNode.prev = None
        self.length -= 1
        
        return poppedNode
        
newNode = Node(11)
print(newNode)

dll = DoublyLinkedList()
dll.append(10)
print(dll.tail)

dll.reverseTraverse()
print(dll.search(10))