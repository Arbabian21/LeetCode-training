
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

    def get(self, index): # time complexity is O(n) space complex O(1)
        if index < 0 or index >= self.length:
            return None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        
    def set(self, index, value): #time complexity is O(n) space complexity is O(1)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self): # spce complexity is O(1) time complexity O(1)
        if self.length > 0:
            poppedNode = self.head
            if self.length == 1:
                self.tail = None
            self.head = self.head.next
            poppedNode.next = None
            self.length -= 1
            return poppedNode
        return None
    
    def pop(self): # time complex O(n) space complex O(1) 
        if self.length > 0:
            popped = self.tail
            
            if self.length == 1:
                self.tail = None
                self.head = None
            else:
                tempNode = self.head
                while tempNode is not self.tail:
                    tempNode = tempNode.next
                self.tail = tempNode
                tempNode.next = None
            
            self.length -= 1
            return popped
        
        return None

    def remove(self, index): # time complex O(n) space complex O(1)
        
        if index > self.length-1 or self.length <= 0:
            return None
        
        if index == 0:
            self.pop_first
            
        if index == self.length-1:
            self.pop
            
        prevNode = self.get(index-1)
        rmNode = prevNode.next
        prevNode.next = rmNode.next
        rmNode.next = None
        
        self.length -= 1
        return rmNode
    
    def deleteAll(self): # time and space O(1)
        self.head = None
        self.tail = None
        self.length = 0

                
                
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
print(newLinkedList.get(1))
print(newLinkedList.get(-1))


print(newLinkedList.pop_first().value)
print(newLinkedList)

oneElement = LinkedList()
oneElement.append(10)
print(oneElement)
print(oneElement.pop_first().value)
print(oneElement)

emptyList = LinkedList()
print(emptyList.pop_first())

print(newLinkedList)

print(emptyList.pop())
oneElement.append(10)
print(oneElement.pop().value)
 