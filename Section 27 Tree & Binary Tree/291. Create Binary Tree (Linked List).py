class TreeNode:
    def __init__(self, data): # time complex O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    # def __str__(self, level = 0): # time complex (2^n)
    #     ret = " " * level + str(self.data) + "\n"
    #     while self.leftChild or self.rightChild:
    #         if self.leftChild:
    #             ret += self.leftChild.__str__(level + 1)
    #         else:
    #             ret += self.rightChild.__str__(level + 1)
    #     return ret
    
drinkBT = TreeNode("Drinks")


