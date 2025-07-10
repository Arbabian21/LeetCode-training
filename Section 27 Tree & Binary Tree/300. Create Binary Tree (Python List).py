class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
newBT = BinaryTree(8) # time complex O(1) space complex O(n)