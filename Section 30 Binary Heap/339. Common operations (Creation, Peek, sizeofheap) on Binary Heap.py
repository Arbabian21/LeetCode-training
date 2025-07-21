class BinaryHeap:
    def __init__(self, size): # time complex O(1) space complex O(n)
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        
def peek(rootNode): # time and space O(1)
    if not rootNode:
        return
    return rootNode.customList[1]
    
def sizeOf(rootNode): # time and space O(1)
    if not rootNode:
        return 
    return rootNode.heapSize

def levelOrderTraversal(rootNode): # time complex O(n) space complex O(1)
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize+1):
        print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType): # time complex O(logn) space complex O(logn)
    parentIndex = index//2
    if index <= 1:
        return
    if heapType == "Min":
        if not rootNode.cusrootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
        
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
        
def insertNode(rootNode, nodeValue, heapType): # time complex O(logn) space complex O(logn)
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize +1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyExtract(rootNode, index, heapType): # time and space O(logn)
    leftIndex = index*2
    rightIndex = index*2 +1
    swapChild = 0
    
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customLIst[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customLIst[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customLIst[index] > rootNode.customList[swapChild]:
                temp = rootNode.customLIst[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyExtract(rootNode, swapChild, heapType)
        
def extract(rootNode, heapType): # time and space O(logn)
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType)
        return extractedNode
    
def deleteBP(rootNode): # time and space O(1)
    rootNode.customList = None
    
    
newBinaryHeap = BinaryHeap(5)
levelOrderTraversal(newBinaryHeap) 
print("\n")
insertNode(newBinaryHeap, 4, "Max")
levelOrderTraversal(newBinaryHeap)
print("\n")
insertNode(newBinaryHeap, 5, "Max")
levelOrderTraversal(newBinaryHeap)
print("\n")
insertNode(newBinaryHeap, 2, "Max")
levelOrderTraversal(newBinaryHeap)
print("\n")
insertNode(newBinaryHeap, 1, "Max")
levelOrderTraversal(newBinaryHeap)
print("\n")
print(extract(newBinaryHeap,"Max"))