class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
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
    
    def insert(self, value, index): # time complex O(n)
        # Negative indices are invalid
        if index < 0:
            print('index out of bounds bucko')
            return

        newNode = Node(value)

        # Empty list case: only index == 0 is allowed
        if self.head is None:
            if index != 0:
                print('index out of bounds bucko')
                return
            # Create a one-node circle
            self.head = newNode
            newNode.next = newNode
            self.length += 1
            return

        # Insert at head (index == 0) into non-empty list
        if index == 0:
            # Find the old tail by looping once
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next
            tail.next = newNode
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return

        # Walk exactly (index - 1) steps, but detect if we wrap back to head early
        curr = self.head
        count = 0
        while count < index - 1:
            curr = curr.next
            count += 1
            if curr is self.head:
                # We looped all the way around before reaching (index - 1)
                print('index too large')
                return

        # At this point, curr points to the node at position (index - 1),
        # unless index == size, in which case curr is the old tail.
        # If curr.next is head, we are inserting at the end (index == size).
        if curr.next is self.head:
            curr.next = newNode
            newNode.next = self.head
            self.tail = newNode
            self.length += 1
            return

        # Otherwise, insert in the middle
        nextNode = curr.next
        curr.next = newNode
        newNode.next = nextNode
        self.length += 1
        return

    def traverse(self): # time complex O(n)
        currNode = self.head
        
        while currNode != None:
            print(currNode.value)
            currNode = currNode.next
            if currNode == self.head:
                break
    
    def search(self, target): # time complex O(n)
        curNode = self.head
        while curNode != None:
            if curNode.value == target:
                return True
            curNode = curNode.next
            if curNode == self.head:
                break
            
        return False
    
    def get(self, index): # time comples O(n)
        currNode = self.head
        if index < 0 or self.head == None:
            return None
            
        for _ in range(index):
            currNode = currNode.next
            if currNode == self.head:
                return None
        
        return currNode
    
    def set(self, index, value): # time complex O(n)
        if index < 0 or self.head == None:
            return None
            
        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
            if currNode == self.head:
                return None
        
        if currNode:
            currNode.value = value
            return True
        
        return False
        
        
        
        
        
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

cll.insert(-2,0)
print(cll)
cll.insert(5,3)
print(cll)
cll.insert(35,6)
print(cll)
cll.insert(5,300)
print(cll)

cll.insert(1000,-10)
print(cll)

print('')
emptycll.insert(100,0)
print(emptycll)
print('\n\n')



cll1 = CLinkedList()
cll1.append(10)
cll1.append(20)
cll1.append(30)
print(cll1)                # → 10 -> 20 -> 30
print("head:", cll1.head.value)  # → 10
print("tail:", cll1.tail.value)  # → 30

cll1.insert(25, 3)         # size is 3, so index 3 means “append”
print(cll1)                # → 10 -> 20 -> 30 -> 25
print("head:", cll1.head.value)  # → 10
print("tail:", cll1.tail.value)  # → STILL 30  ← should have become 25

