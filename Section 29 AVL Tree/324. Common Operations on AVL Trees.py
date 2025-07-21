import QueueLinkedList as queue 

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.height = 1

# O(n) time, O(n) space
def preOrderTraversal(rootNode):
    if not rootNode:
        print("The BST is empty")
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# O(n) time, O(n) space
def inOrderTraversal(rootNode):
    if not rootNode:
        print("The BST is empty")
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# O(n) time, O(n) space
def postOrderTraversal(rootNode):
    if not rootNode:
        print("The BST is empty")
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# O(n) time, O(n) space
def levelOrderTraversal(rootNode):
    if not rootNode:
        print("The BST is empty")
        return

    levelOrderQueue = queue.Queue()
    levelOrderQueue.enqueue(rootNode)

    while not levelOrderQueue.isEmpty():
        currentLevelNode = levelOrderQueue.dequeue()
        currentNode = currentLevelNode.value
        print(currentNode.data)

        if currentNode.leftChild:
            levelOrderQueue.enqueue(currentNode.leftChild)
        if currentNode.rightChild:
            levelOrderQueue.enqueue(currentNode.rightChild)

# O(log n) time (average), O(log n) space (recursive stack)
def search(rootNode, target):
    if not rootNode:
        print("The BST is empty")
    elif rootNode.data == target:
        print("The value is found")
    elif target < rootNode.data:
        search(rootNode.leftChild, target)
    elif target > rootNode.data:
        search(rootNode.rightChild, target)

# O(1) time, O(1) space
def getHeight(root):
    if not root:
        return 0
    return root.height

# O(1) time, O(1) space
def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = newRoot.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# O(1) time, O(1) space
def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = newRoot.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# O(1) time, O(1) space
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# O(log n) time (avg), O(log n) space (recursive stack)
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # Left heavy
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)

    # Left-Right case
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)

    # Right heavy
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)

    # Right-Left case
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)

    return rootNode

def getMinValueNode(rootNode): # time complex O(logn) spacecomplex O(logn)
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue): # time complex O(logn) spacecomplex O(logn)
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    
    return rootNode

def deleteAVL(rootNode): # O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "THe avl has been deleted"

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)

levelOrderTraversal(newAVL)

print("\n")
newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)