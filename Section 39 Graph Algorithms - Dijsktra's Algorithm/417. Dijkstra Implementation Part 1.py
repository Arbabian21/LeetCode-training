class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parentNode = None
        self.neighbors = []
        self.minDistance = float("inf")
        
    def __lt__(self, otherNode):
        return self.minDistance < otherNode.minDistance