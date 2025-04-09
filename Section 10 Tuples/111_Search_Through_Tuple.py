newTuple = ("a", "b", "c", "d", "e")

print('a' in newTuple) # O(n)

def traverse(newTuple, target):
    for i in newTuple:
        if i == target:
            return True
        else:
            return False
        
def otherTraverse(newTuple, target):
    for i in range(len(newTuple)):
        return True if newTuple[i] == target else False