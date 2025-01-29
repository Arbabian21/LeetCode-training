import array

arr1 = array.array("i", [1, 2, 3, 4, 5, 6])
arr2 = array.array("d", [1.3, 1.5, 1.6])


def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr2)
