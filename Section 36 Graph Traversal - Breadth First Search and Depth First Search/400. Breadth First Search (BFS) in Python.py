class Graph:
    def __init__(self, gdict=None):
        if gdict is None: gdict = {}
        self.gdict = gdict
        
    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False
        
    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for i in self.gdict[vertex]:
                self.gdict[i].removeEdge(vertex, i)
            self.gdict.pop(vertex)
            
    def bfs(self, vertex): # time complex O(n)
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        
        while queue:
            currVertex = queue.pop(0)
            print(currVertex)
            for i in self.gdict[vertex]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

                