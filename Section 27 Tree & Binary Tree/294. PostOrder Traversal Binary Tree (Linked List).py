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
    inOrderTraversal(root.leftChild)
    
def postOrderTraversal(root):  # time complex O(n) space complex O(n)
    if not root:
        return
    postOrderTraversal(root.rightChild)
    print(root.data)
    postOrderTraversal(root.leftChild)
    
drinkBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
drinkBT.leftChild = hot
drinkBT.rightChild = cold

preOrderTraversal(drinkBT)
print("\n")
inOrderTraversal(drinkBT)
print("\n")
postOrderTraversal(drinkBT)