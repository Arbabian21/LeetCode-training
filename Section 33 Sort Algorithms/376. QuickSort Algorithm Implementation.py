def swap(inputList, index1, index2):
    inputList[index1], inputList[index2] = inputList[index2], inputList[index1]
    
def pivot(inputList, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if inputList[i] < inputList[pivotIndex]:
            swapIndex += 1
            swap(inputList, swapIndex, i)
    swap(inputList, pivotIndex, swapIndex)
    return swapIndex

def quickSort(inputList, left, right):
    if left < right:

        pivotIndex = pivot(inputList, left, right)
        quickSort(inputList, left, pivotIndex-1)
        quickSort(inputList, pivotIndex+1, right)
    return inputList

lis = [3,5,0,6,2,1,4]
print(quickSort(lis, 0, 6))

