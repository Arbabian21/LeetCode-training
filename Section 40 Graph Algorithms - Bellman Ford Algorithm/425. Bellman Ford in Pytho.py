class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        
    def addEdge(self, s, d, w):
        self.graph.append([s,d,w])
    
    def addNode(self,value):
        self.nodes.append(value)
        
    def printSolution(self,dist):
        print("vertex Distance from Source")
        for key, value in dist.items():
            print(' ' + key, ' :    ', value)
            
    def bellmanFord(self, src): # time complex O(n) space complex O(n)
        dist = {i : float("inf") for i in self.nodes}
        dist[src] = 0
        
        for _ in range(self.V-1):
            for s,d,w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("graph contains negative cycle")
                return
        
        self.printSolution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)
g.bellmanFord("E")