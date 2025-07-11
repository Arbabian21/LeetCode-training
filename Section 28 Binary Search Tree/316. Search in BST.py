import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data): # time complex O(1) space complex O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insertNode(rootNode, nodeValue): # time complex O(logn) space complex O(logn)
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if not rootNode.leftChild:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if not rootNode.rightChild:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

def preOrderTraversal(rootNode): # time complex O(n) space compelx O(n)
    if not rootNode:
        return "The BST is empty"
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode): # time complex O(n) space compelx O(n)
    if not rootNode:
        return "The BST is empty"
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode): # time complex O(n) space compelx O(n)
    if not rootNode:
        return "The BST is empty"
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
def levelOrderTraversal(rootNode): # time complex O(n) space complex O(n)
    if not rootNode:
        return "The BST is empty"
    levelOrderQueue = queue.Queue()
    levelOrderQueue.enqueue(rootNode)
    while not levelOrderQueue.isEmpty():
        currentLevelNode = levelOrderQueue.dequeue()
        print(currentLevelNode.value.data)
        if currentLevelNode.value.leftChild:
            levelOrderQueue.enqueue(currentLevelNode.value.leftChild)
        if currentLevelNode.value.rightChild:
            levelOrderQueue.enqueue(currentLevelNode.value.rightChild)

def search(rootNode, target): # time complex O(logn) space complexity O(logn)
    if not rootNode:
        print( "The BST is empty")
    
    elif rootNode.data == target:
        print("The value is found")
    
    elif target < rootNode.data:
        if rootNode.leftChild:
            search(rootNode.leftChild, target)
    elif target > rootNode.data:
        if rootNode.rightChild:
            search(rootNode.rightChild, target)

newBST = BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,50))
print(insertNode(newBST,90))
print(insertNode(newBST,30))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,100))
print(insertNode(newBST,20))
print(insertNode(newBST,40))

print(newBST.data)
print(newBST.leftChild.data)

print('\n')
preOrderTraversal(newBST)
print('\n')
inOrderTraversal(newBST)
print('\n')
postOrderTraversal(newBST)
print('\n')
levelOrderTraversal(newBST)
print('\n')
search(newBST, 40)