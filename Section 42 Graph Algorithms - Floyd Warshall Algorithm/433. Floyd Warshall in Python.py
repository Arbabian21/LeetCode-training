INF = 9999

def printSolution(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")
        
def floydWarshall(nv, G): # time complexity O(v^3) space complexity (v^2)
    distance = G
    
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    printSolution(nv, distance)
    
graph = [
    [0,8,INF,1],
    [INF,0,1,INF],
    [4,INF,0,INF],
    [INF,2,9,1],
]

floydWarshall(4,graph)