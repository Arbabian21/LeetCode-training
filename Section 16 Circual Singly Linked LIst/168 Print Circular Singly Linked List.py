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
    
    def append(self, value): # time complex is O(n)
        # I can write this with a time complex of O(1) however the way 
        # linked lists are taught here is weird and has head and tail as 
        # seperate values. In actual interviews linkedlists are just 
        # the ListNode class and you only have access to the head
        # which is usually a dummy value that points to the actual first Node
        
        newNode = Node(value)
        currNode = self.head

        if currNode == None:
            currNode = newNode
            self.head = newNode
            

        else:
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
