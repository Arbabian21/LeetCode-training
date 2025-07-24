class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            gdict={}
        self.gdict = gdict
        
    def bfs(self,start,end): # time complex O(n) space complex O(m)
        queue =[]
        queue.append([start])
        
        while queue:
            path = queue.pop()
            node = path(-1)
            if node == end:
                return path

            for adjacent in self.gdict.get(node, []):
                newPath = list(path)
                newPath.append(adjacent)
                queue.append(newPath)