from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
        
    def addEdge(self,vertex, edge):
        self.graph[vertex].append(edge)
        
    def topologicalSortUtil(self,vertex, visited, stack):
        visited.append(vertex)
        
        for i in self.graph[vertex]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
                
        stack.insert(0,vertex)
        
    def topologicalSort(self): # time complex O(n) space complex O(n)
        visited = []
        stack = []
        
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        
        print(stack)
        
customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("B", "C")
customGraph.addEdge("B", "D")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "F")
customGraph.addEdge("E", "H")
customGraph.addEdge("D", "F")
customGraph.addEdge("F", "G")
customGraph.topologicalSort()