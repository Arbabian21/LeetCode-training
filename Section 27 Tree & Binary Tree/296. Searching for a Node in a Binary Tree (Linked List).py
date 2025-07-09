class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
            
class Queue:
    def __init__(self): # time complex O(1)
        self.linkedList = LinkedList()
    
    def __str__(self): # tikme complex O(n)
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def isEmpty(self): # time complex O(1)
        if self.linkedList.head == None:
            return True
        return False
    
    def enqueue(self, value): # time complex O(1)
        newNode = Node(value)
        
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
            return
        
        self.linkedList.tail.next = newNode
        self.linkedList.tail = newNode

    def dequeue(self): # time complex O(1)
        if self.isEmpty():
            return "Queue is empty"
        
        rmNode = self.linkedList.head
        self.linkedList.head = rmNode.next
        if rmNode == self.linkedList.tail:
            self.linkedList.tail = None
        rmNode.next = None
        return rmNode
    
    def peek(self): # time complex O(1)
        if self.isEmpty():
            return "The Queue is empty"
        return self.linkedList.head
    
    def delete(self): # time complex O(1)
        self.linkedList.head = None
        self.linkedList.tail = None

class TreeNode:
    def __init__(self, data): # time complex O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def preOrderTraversal(root): # time complex O(n) space complex O(N)
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)
    
def inOrderTraversal(root): # time complex O(n) space complex O(n)
    if not root:
        return
    inOrderTraversal(root.leftChild)
    print(root.data)
    inOrderTraversal(root.rightChild)
    
def postOrderTraversal(root):  # time complex O(n) space complex O(n)
    if not root:
        return
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)

def levelOrderTraversal(root): # time complex O(n) space complex O(n)
    if not root:
        return
    customQueue = Queue()
    customQueue.enqueue(root)
    while not customQueue.isEmpty():
        queueEntry = customQueue.dequeue()
        print(queueEntry.value.data)
        if queueEntry.value.leftChild is not None:
            customQueue.enqueue(queueEntry.value.leftChild)
            
        if queueEntry.value.rightChild is not None:
            customQueue.enqueue(queueEntry.value.rightChild)
    
def searchBT(root, targetVal): # time complex O(n) space complex O(n  )
    if not root:
        return "The BT does not Exist"
    
    customQueue = Queue()
    customQueue.enqueue(root)
    while not customQueue.isEmpty():
        queueEntry = customQueue.dequeue()
        if queueEntry.value.data == targetVal:
            return "Success"
        else:
            if queueEntry.value.leftChild is not None:
                customQueue.enqueue(queueEntry.value.leftChild)
                
            if queueEntry.value.rightChild is not None:
                customQueue.enqueue(queueEntry.value.rightChild)
    return "Unsuccessful"
    

drinkBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
coffee = TreeNode("Coffee")
tea = TreeNode("Tea")
soda = TreeNode("Soda")
juice = TreeNode("Juice")

drinkBT.leftChild = hot
drinkBT.rightChild = cold

hot.leftChild = tea
hot.rightChild = coffee

cold.leftChild = soda
cold.rightChild = juice

print("PreOrder Traversal")
preOrderTraversal(drinkBT)
print("\n")
print("InOrder Traversal")
inOrderTraversal(drinkBT)
print("\n")
print("PostOrder Traversal")
postOrderTraversal(drinkBT)
print("\n")
print("LevelOrder Traversal")
levelOrderTraversal(drinkBT)
print("\n")
print("Search function")
print(searchBT(drinkBT, "j"))
print(searchBT(drinkBT, "Juice"))
