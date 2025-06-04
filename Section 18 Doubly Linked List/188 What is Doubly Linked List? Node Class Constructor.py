class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return f'{self.value}'
        
newNode = Node(11)
print(newNode)