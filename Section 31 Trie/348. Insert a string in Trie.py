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

newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Apple")
