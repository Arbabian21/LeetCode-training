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
    
    
drinkBT = TreeNode("Drinks")
hot = TreeNode("hot")
cold = TreeNode("cold")
drinkBT.leftChild = hot
drinkBT.rightChild = cold

preOrderTraversal(drinkBT)