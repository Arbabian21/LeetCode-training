# a singly linked list node is made up of two parts, value, and next.

# example:
#     {
#         "value": 10,
#         "next": None
#     }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
newNode = Node(10)
print(newNode) # will show mem location not value bc we have not setup print method
# time complexity O(1) space complexity O(1)
