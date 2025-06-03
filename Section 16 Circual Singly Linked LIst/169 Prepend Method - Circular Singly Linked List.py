class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self): #O(n)
        currNode = self.head
        value = ''
        
        if currNode == None:
            return 'List is Empty'

        else:
            while currNode != None:
                value += f'{currNode.value}'
                if currNode.next == self.head:
                    break
                
                value += ' -> '
                currNode = currNode.next
        return value
    
    def prepend(self,value): #O(n) in this scenario but i could make it O(1)
        newNode = Node(value)
        currNode = self.head
        
        if currNode == None:
            self.tail = newNode
            self.head = newNode
            self.length += 1
            newNode.next = newNode
            return
            
        
        while currNode.next != self.head:
            currNode = currNode.next
            
        currNode.next = newNode
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        
    def append(self, value): # time complex is O(n)
        # I can write this with a time complex of O(1) however the way 
        # linked lists are taught here is weird and has head and tail as 
        # seperate values. In actual interviews linkedlists are just 
        # the ListNode class and you only have access to the head
        # which is usually a dummy value that points to the actual first Node
        
        newNode = Node(value)
        currNode = self.head

        if currNode == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            self.length += 1
            return
            

        while currNode.next != self.head:
            currNode = currNode.next
        
        currNode.next = newNode
        newNode.next = self.head
        self.tail = newNode
        self.length += 1
    
        
cll = CLinkedList()
cll.append(10)
print(cll.head.value)
print(cll.head.next.value)
cll.append(20)
print(cll.head.next.value)
print(cll.head.next.next.value)
print('')
cll.append(30)
print(cll)
emptycll = CLinkedList()
print(emptycll)
print('')
cll.prepend(0)
print(cll)
cll.prepend(-1)
print(cll)
