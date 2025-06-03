class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
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
        
csll = CLinkedList()
csll.append(10)
print(csll.head.value)
print(csll.head.next.value)
csll.append(20)
print(csll.head.next.value)
print(csll.head.next.next.value)
