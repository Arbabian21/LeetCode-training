def selectionSort(customList): # time complex n^2 space complex O(1) 
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)
    
Clist = [10,9,1,2,8,3,4,5,7,6,0]
selectionSort(Clist)