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
                
                
newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
print(newLinkedList)
