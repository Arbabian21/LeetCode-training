import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])


def traverseArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])


print(array)
traverseArray(array)
