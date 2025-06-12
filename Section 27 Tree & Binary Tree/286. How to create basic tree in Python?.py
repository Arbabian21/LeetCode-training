class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        
tree = TreeNode("Drinks", [])
cold = TreeNode("cold", [])
hot = TreeNode("hot", [])
print(tree)
print(cold)
print(hot)

print("\n")
tree.addChild(cold)
tree.addChild(hot)
print(tree)

print("\n")
tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])
fanta = TreeNode("fanta", [])
cola = TreeNode("cola", [])

hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(fanta)
cold.addChild(cola)
print(tree)