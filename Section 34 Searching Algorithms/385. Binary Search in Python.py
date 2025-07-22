def binarySearch(inputArr, target): # time complexity O(logn) space complexity if recursive is O(logn) space complexity if not recursive is O(1)
    left = 0
    right = len(inputArr) -1
    midpoint = left + right // 2
    
    if target == inputArr[midpoint]:
        return midpoint
    elif target > inputArr[midpoint]:
        return binarySearch(inputArr[midpoint+1 :], target)
    elif target < inputArr[midpoint]:
        return binarySearch(inputArr[:midpoint], target)
    else:
        return -1
    
input = [10,21,34,56,75,80,98]
print(binarySearch(input, 10))