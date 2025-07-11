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

newBST = BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,60))
print(newBST.data)
print(newBST.leftChild.data)