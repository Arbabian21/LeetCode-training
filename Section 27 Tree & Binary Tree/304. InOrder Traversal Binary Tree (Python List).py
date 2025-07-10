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
    
    def preOrderTraversal(self, index): # time complex O(n) space complex O(n)
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
        
    def inOrderTraversal(self, index): # time complex O(n) space complex O(n)
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)
    
newBT = BinaryTree(8) # time complex O(1) space complex O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.search("Tea"))
print(newBT.search("Hot"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))

print('\n')
print("Preorder Traversal:")
newBT.preOrderTraversal(1)
print('\n')
print("Inorder traversal:")
newBT.inOrderTraversal(1)