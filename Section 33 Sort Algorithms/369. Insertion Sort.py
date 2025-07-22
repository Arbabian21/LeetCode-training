
def insertionSort(customList): # time complex N^2 space complex O(1)
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)
    
customList = [8, 4, 1, 5]
insertionSort(customList)