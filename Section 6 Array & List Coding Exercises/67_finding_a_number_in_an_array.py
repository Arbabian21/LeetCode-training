import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def linearSearch(inputArray, target):
    for i in range(len(inputArray)):
        if target == inputArray[i]:
            print(i)
    

linearSearch(myArray, 12)