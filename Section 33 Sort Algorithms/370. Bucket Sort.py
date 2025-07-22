import math
def bucketSort(customList): # time complex N^2 space complex O(n)
    numbersOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    
    for i in range(numbersOfBuckets):
        arr.append([])
        
    for i in customList:
        index = math.ceil(i*numbersOfBuckets/maxValue)
        arr[index-1].append(i)
        
    for i in range(numbersOfBuckets):
        arr[i] = sorted(arr[i])
        
    k = 0
    for i in range(numbersOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

customList = [9,8,7,6,5,4,3,2,1]
print(bucketSort(customList))