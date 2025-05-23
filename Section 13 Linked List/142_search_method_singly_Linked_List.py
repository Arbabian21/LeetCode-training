class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value): # time complexity is O(1) Space complexity is O(1)
        newNode = Node(value)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1
        
    def prepend(self, value): # time is O(1) space is O(1)
        newNode = Node(value)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        self.length += 1
        
    def insert(self, index, value): #time complexity is O(n) space complexity O(1)
        newNode = Node(value)
        # currIndex = 0
        # currNode = self.head
        # while currIndex <= index and currNode:
        #     if currIndex == index:
        #         newNode.next = currNode.next
        #         currNode.next = newNode
        #         self.length += 1
        #     else:
        #         currNode = currNode.next
        #         currIndex += 1
        if index >= self.length or index < 0:
            
            if self.head == None and self.tail == None:
                self.head = newNode
                self.tail = newNode
            elif index == 0:
                newNode.next = self.head
                self.head == newNode
            else:    
                tempNode = self.head
                for _ in range(index-1):
                    tempNode = tempNode.next
                
                if tempNode == self.tail:
                    self.tail = newNode
                newNode.next = tempNode.next
                tempNode.next = newNode
                
            self.length += 1
        else:
            print("Index out of bounds")
        
        
    def __str__(self): # time is O(n) space is O(1)
        tempNode = self.head
        result = ""
        if not tempNode:
            result += "List is empty"
        else:
            while tempNode:
                result += f"{tempNode.value}"
                if tempNode.next:
                    result += " -> "
                tempNode = tempNode.next
        return result
    
    def traverse(self): # time complexity is O(n) space complexity is O(1)
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
            
    def search(self, target): # time complexity O(n) space complexity is O(1)
        curr = self.head
        while curr:
            if curr.value == target:
                return True
            curr = curr.next
        return False
                
newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
print(newLinkedList)
newLinkedList.prepend(0)
print(newLinkedList)
newLinkedList.insert(1,5)
print(newLinkedList)
newLinkedList.insert(3,30)
print(newLinkedList)

anotherNewLinkedList = LinkedList()
anotherNewLinkedList.insert(0,10)
print(anotherNewLinkedList)

newLinkedList.traverse()

print(newLinkedList.search(20))
print(newLinkedList.search(40))
