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
    
    def search(self, target): # time complex O(n) space complex O(1)
        for i, val in enumerate(self.customList):
            if val == target:
                return f"success, {target} is located at index {i}"
        return "not found"
    
    
newBT = BinaryTree(8) # time complex O(1) space complex O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.search("Tea"))
print(newBT.search("Hot"))