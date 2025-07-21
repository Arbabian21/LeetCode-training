class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word): # time complex O(m) space complex O(m)
        current = self.root
        for i in word:
            char = i
            node = current.children.get(char)
            if node == None:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.endOfString = True
        print("successfully inserted")
    
    def search(self, target): # time complex O(m) spce complex O(n)
        current = self.root
        for i in target:
            char = i
            node = current.children.get(char)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        return False
    
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False
    
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word)-1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index +1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
    
    
newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Apple")
print(newTrie.search(""))
print(newTrie.search("A"))
print(newTrie.search("App"))
print(newTrie.search("Appl"))
print(newTrie.search("Apple"))

deleteString(newTrie.root, "App", 0)
print(newTrie.search("App"))