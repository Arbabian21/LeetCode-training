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
    

drinkBT = TreeNode("Drinks")
hot = TreeNode("hot")
cold = TreeNode("cold")
drinkBT.leftChild = hot
drinkBT.rightChild = cold

preOrderTraversal(drinkBT)
print("\n")
inOrderTraversal(drinkBT)