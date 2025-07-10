class BinaryTree:
    def __init__(self, size): # time complex O(1) space complex O(n)
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
    def insertNode(self, value): # time complex O(1) space complex O(1)
        if self.lastUsedIndex+1 == self.maxSize:
            return "The Binary Tree is full"

        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
newBT = BinaryTree(8) # time complex O(1) space complex O(n)