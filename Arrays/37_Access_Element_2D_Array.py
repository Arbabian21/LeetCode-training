import numpy as np

twoDArray = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])


def accessTwoDArray(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

print(twoDArray)
accessTwoDArray(twoDArray,0,1)