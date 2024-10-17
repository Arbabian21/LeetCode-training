import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def searchArray(arr, searchParam):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] ==  searchParam:
                return "Found in indicies i = " + str(i) + " and j = " +  str(j)
    return "Not Found"


print(array)
print(searchArray(array, 12))
