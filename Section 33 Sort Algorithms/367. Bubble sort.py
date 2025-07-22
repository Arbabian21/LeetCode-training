def bubbleSort(customList): # time complex n^2 space complex O(1)
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1], customList[j]
    print(customList)
    
cList = [2,1,5,7,4,9]
bubbleSort(cList)