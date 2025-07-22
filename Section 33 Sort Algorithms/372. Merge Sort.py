def merge(customList, l, m, r): # time complex O(n) space coplex O(n)
    numElementsFirstSubArr = m - l + 1
    numElementsSecondSubArr = r-m
    
    L = [0] * numElementsFirstSubArr
    R = [0] * numElementsSecondSubArr
    
    for i in range(numElementsFirstSubArr):
        L[i] = customList[l+i]
    
    for i in range(numElementsSecondSubArr):
        R[i] = customList[m+1+i]
        
    i = 0
    j = 0
    k = l
    
    while i < numElementsFirstSubArr and j < numElementsSecondSubArr:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j+= 1
        k += 1
    
    while i < numElementsFirstSubArr:
        customList[k] = L[i]
        i += 1
        k += 1
        
    while j < numElementsSecondSubArr:
        customList[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(customList, l, r): # time complex NlogN space complex O(n)
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList

cList = [2,1,7,6,5,4,3,9,8]
print(mergeSort(cList, 0,8))